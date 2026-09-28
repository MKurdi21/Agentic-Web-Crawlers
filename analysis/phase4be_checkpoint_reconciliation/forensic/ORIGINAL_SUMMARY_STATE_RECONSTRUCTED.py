"""Refresh recoverable corpus state without model calls or summary edits."""

import csv
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "analysis"
REQUIRED = [
    "Plain-Language Orientation", "Document Roadmap", "Background and Context",
    "Research Problem and Gap", "Research Questions", "Assumptions / Threat Model",
    "Methodology", "Experiments / Analyses", "Results", "Figure-by-Figure",
    "Table-by-Table", "Diagram / Architecture", "Equations and Mathematical",
    "Interpretation and Discussion", "Contributions and Novelty", "Limitations",
    "Threats to Validity", "Future Work and Open Questions",
    "Terminology and Notation Glossary", "Key Numerical Results", "Evidence Map",
    "Very Simple Explanation",
]


def digest(path):
    if not path.is_file():
        return None
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def relative(path):
    return path.relative_to(ROOT).as_posix()


def resolve(value):
    path = (ROOT / value.replace("\\", "/")).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError(f"Path outside repository: {value}")
    return path


def normalized(value):
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def check_structure(path):
    if not path.is_file():
        return {"passed": False, "missing": [], "characters": 0}
    text = path.read_text(encoding="utf-8-sig")
    headings = re.findall(r"(?m)^#{1,6}\s+(.+)$", text)
    clean = [normalized(h) for h in headings]
    missing = []
    positions = []
    for number, title in enumerate(REQUIRED, 1):
        matches = [i for i, h in enumerate(clean)
                   if re.match(rf"^{number}\s+", h)
                   and normalized(title) in h]
        if matches:
            positions.append(matches[0])
        else:
            missing.append(f"{number}. {title}")
    if not any("stage 0" in h for h in clean):
        missing.append("Stage 0")
    if not any("completeness audit" in h for h in clean):
        missing.append("Completeness Audit")
    ordered = positions == sorted(set(positions))
    return {"passed": not missing and ordered and len(text) >= 20000,
            "missing": missing, "numbered_sections_in_order": ordered,
            "characters": len(text)}


def write_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")
    temporary.replace(path)


def main():
    now = datetime.now(timezone.utc).isoformat()
    with (STATE / "manifest.csv").open(encoding="utf-8-sig", newline="") as stream:
        manifest = list(csv.DictReader(stream))
    reviews = json.loads((STATE / "reviews.json").read_text(encoding="utf-8"))
    prompt_hash = digest(STATE / "PROMPT.md")
    if not prompt_hash:
        raise ValueError("Missing saved prompt")
    issues = []
    all_pdfs = sorted(ROOT.rglob("*.pdf"))
    canonical = [p for p in all_pdfs if "99_Duplicates" not in p.relative_to(ROOT).parts]
    duplicates = [p for p in all_pdfs if p not in canonical]
    mapped = [resolve(row["Pdf"]) for row in manifest]
    for path in set(canonical) - set(mapped):
        issues.append(f"Unmapped PDF: {relative(path)}")
    for key in ("Pdf", "SummaryName", "StageTarget", "FinalTarget"):
        for value, count in Counter(r[key].casefold() for r in manifest).items():
            if count > 1:
                issues.append(f"Manifest collision in {key}: {value}")
    baseline_path = STATE / "baseline.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8")) if baseline_path.exists() else None
    if baseline and baseline["prompt_sha256"] != prompt_hash:
        issues.append("Saved prompt changed since recovery; review generation and approval provenance")
    staged_paths = {resolve(row["StageTarget"]) for row in manifest}
    for path in (ROOT / ".summary_v2").glob("*.md"):
        if path.resolve() not in staged_paths:
            issues.append(f"Unmapped staged draft: {relative(path)}")
    records = []
    for row in manifest:
        source, draft, final = (resolve(row[key]) for key in ("Pdf", "StageTarget", "FinalTarget"))
        source_hash, draft_hash, final_hash = map(digest, (source, draft, final))
        structure = check_structure(draft)
        status = "pending" if draft_hash is None else "structural_pass" if structure["passed"] else "needs_repair"
        if not source_hash:
            issues.append(f"Missing source: {row['Pdf']}")
        review = reviews.get(row["SummaryName"], {})
        reviewed = bool(source_hash and draft_hash and structure["passed"] and
                        review.get("source_sha256") == source_hash and
                        review.get("prompt_sha256") == prompt_hash and
                        review.get("draft_sha256") == draft_hash and
                        review.get("reviewed_at") and review.get("notes_path") and
                        resolve(review["notes_path"]).is_file())
        if reviewed:
            status = "promoted" if final_hash == draft_hash else "source_verified"
        if baseline:
            prior = baseline["papers"].get(row["SummaryName"], {})
            if prior and prior["source_sha256"] != source_hash:
                issues.append(f"Source changed since recovery: {row['SummaryName']}")
        run_file = STATE / "evidence" / Path(row["SummaryName"]).stem / "run.json"
        run = json.loads(run_file.read_text(encoding="utf-8-sig")) if run_file.exists() else None
        records.append({**row, "status": status, "source_sha256": source_hash,
                        "prompt_sha256": prompt_hash, "draft_sha256": draft_hash,
                        "final_sha256": final_hash, "structure": structure,
                        "source_review_valid": reviewed,
                        "last_generation": run,
                        "generation_provenance": "see evidence; hashes observed now do not prove original generation inputs"})
    duplicate_records = []
    source_hashes = {r["source_sha256"] for r in records if r["source_sha256"]}
    for path in duplicates:
        sha = digest(path)
        duplicate_records.append({"path": relative(path), "sha256": sha,
                                  "matches_canonical": sha in source_hashes})
        if sha not in source_hashes:
            issues.append(f"Archived PDF has no canonical hash match: {relative(path)}")
    counts = dict(Counter(r["status"] for r in records))
    snapshot = {"schema_version": 1, "updated_at": now, "prompt_sha256": prompt_hash,
                "usage_plan_remaining": None, "concurrency_default": 1, "batch_size": 2,
                "canonical_pdf_count": len(canonical), "total_pdf_count": len(all_pdfs),
                "counts": counts, "issues": issues, "duplicates": duplicate_records,
                "orphan_candidate_directories": [p.name for p in ROOT.glob(".summary_work_*") if p.is_dir()],
                "papers": records}
    if baseline is None:
        write_json(baseline_path, {"created_at": now, "prompt_sha256": prompt_hash,
                                  "papers": {r["SummaryName"]: {k: r[k] for k in
                                    ("source_sha256", "draft_sha256", "final_sha256")}
                                             for r in records}})
    write_json(STATE / "checkpoint.json", snapshot)
    lines = ["# Analysis Checkpoint", "", f"Updated: {now}", "",
             f"Corpus: {len(canonical)} canonical PDFs; {len(duplicates)} archived duplicates.",
             f"Saved prompt SHA256: `{prompt_hash}`", "",
             "## Progress", "", "| Status | Papers |", "|---|---:|"]
    lines.extend(f"| {status} | {counts.get(status, 0)} |" for status in
                 ("pending", "needs_repair", "structural_pass", "source_verified", "promoted"))
    lines += ["", "Structural passes are unreviewed drafts. No scientific accuracy or complete",
              "visual coverage is implied. Existing older summaries remain in Summaries/.", "",
              "## Recovery", "", "Read [WORKFLOW.md](WORKFLOW.md). Refresh with `python scripts/summary_state.py`.",
              "Usage allowance is unknown. User preference: two papers per batch, run sequentially; checkpoint each paper.",
              "Inspect process command lines before treating scratch directories as abandoned.", "",
              "## Next Pending Papers", ""]
    lines += [f"- `{r['SummaryName']}`: `{r['Pdf']}`" for r in records if r["status"] == "pending"][:5]
    lines += ["", "## Issues", ""] + ([f"- {issue}" for issue in issues] or ["No corpus mapping or duplicate-hash issues detected."])
    runs = [r for r in records if r["last_generation"]]
    lines += ["", "## Recorded Runs", ""]
    lines += [f"- `{r['SummaryName']}`: {r['last_generation']['status']}. "
              "See its evidence directory for the log; running status can be stale after a crash."
              for r in runs] or ["No runs recorded by the durable runner yet."]
    lines += ["", "## All Papers", "", "| Paper / Filename | State |", "|---|---|"]
    lines += [f"| {r['SummaryName']} | {r['status']} |" for r in records]
    temp = STATE / "CHECKPOINT.md.tmp"
    temp.write_text("\n".join(lines) + "\n", encoding="utf-8")
    temp.replace(STATE / "CHECKPOINT.md")
    print(json.dumps({"counts": counts, "issues": issues}, indent=2))


if __name__ == "__main__":
    main()
