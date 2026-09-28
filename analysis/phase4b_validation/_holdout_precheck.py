"""Metadata-only holdout purity and immutable candidate check."""
import csv
import hashlib
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
P4R = ROOT / "analysis/phase4r_remediation"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


manifest = json.loads((OUT / "CANDIDATE_CODE_MANIFEST.json").read_text(encoding="utf-8"))
errors = []
for candidate in ("candidate_frozen", "candidate_v4r"):
    root = OUT / candidate
    expected = {e["relative_path"] for e in manifest["immutable_files"]}
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file() and "shadow" not in p.relative_to(root).parts and "__pycache__" not in p.relative_to(root).parts}
    if actual != expected:
        errors.append(candidate + ":unexpected_file_set")
    for entry in manifest["immutable_files"]:
        path = root / entry["relative_path"]
        if not path.is_file() or path.stat().st_size != entry["size_bytes"] or sha(path) != entry["sha256"]:
            errors.append(candidate + ":hash:" + entry["relative_path"])

with (P4R / "PHASE4B_VALIDATION_HOLDOUT.csv").open(encoding="utf-8-sig", newline="") as f:
    holdout = list(csv.DictReader(f))
identifiers = {r["paper_report_id"] for r in holdout}
metadata_allowed = {
    "PHASE4B_VALIDATION_HOLDOUT.csv", "PHASE4B_HOLDOUT_SELECTION_RECEIPT.json",
    "_select_phase4b_holdout.py", "PHASE4B_HOLDOUT_SELECTION_PROTOCOL.md",
    "PROTECTED_FILE_HASHES_INITIAL.csv", "GIT_STATUS_INITIAL.txt", "GIT_STATUS_FINAL.txt",
}
leakage = []
for path in P4R.iterdir():
    if not path.is_file() or path.name in metadata_allowed or path.suffix.lower() not in {".md", ".json", ".csv", ".py"}:
        continue
    content = path.read_text(encoding="utf-8", errors="replace")
    if any(identifier in content for identifier in identifiers):
        leakage.append(path.name)
if leakage:
    errors.extend("selected_report_in_unexpected_phase4r_file:" + name for name in leakage)

contamination = json.loads((P4R / "PHASE4B_HOLDOUT_CONTAMINATION_LOG.json").read_text(encoding="utf-8"))
if contamination.get("events") or contamination.get("status") != "UNTOUCHED":
    errors.append("phase4r_contamination_log")
result = {
    "candidate_immutable_equal": not any(e.startswith("candidate_") for e in errors),
    "candidate_file_count": len(manifest["immutable_files"]),
    "phase4r_report_identifier_leakage": leakage,
    "phase4r_contamination_events": contamination.get("events"),
    "errors": errors,
    "passed": not errors,
}
(OUT / "HOLDOUT_PREVALIDATION_CHECK.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
if errors:
    raise SystemExit(1)
