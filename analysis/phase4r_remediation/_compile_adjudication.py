"""Independently reconcile all original Phase 4 disagreements with source adjudications."""
import collections
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
LANES = OUT / "adjudication_lanes"


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


original = list(csv.DictReader((ROOT / "analysis/phase4_rehearsal/HOLDOUT_DISAGREEMENTS.csv").open(encoding="utf-8", newline="")))
records = [read(p) for p in sorted((LANES / "h01_h02").glob("H0*_ei*.json"))]
records += read(LANES / "h03_h04/ADJUDICATION_H03_H04.json")["records"]
records += read(LANES / "h05_h06/H05_H06_DISAGREEMENT_ADJUDICATION.json")["records"]
expected = {(x["holdout_id"], x["stable_item_id"]) for x in original}
actual = {(x["holdout_id"], x["evidence_item_id"]) for x in records}
assert len(original) == len(expected) == len(records) == len(actual) == 43
assert expected == actual

for record in records:
    evidence = record["exact_source_evidence"]
    private_path = Path(evidence["private_path"])
    paths = [ROOT / private_path, OUT / private_path, LANES / private_path]
    match = next((p for p in paths if p.is_file()), None)
    assert match is not None, record["evidence_item_id"]
    assert hashlib.sha256(match.read_bytes()).hexdigest() == evidence["sha256"]
    assert match.is_relative_to(OUT)
    record["source_evidence_integrity"] = "HASH_VERIFIED_PRIVATE_NEVER_PACKAGE"
    record["scientific_acceptance"] = "NOT_GRANTED"

records.sort(key=lambda x: (x["holdout_id"], x["evidence_item_id"]))
outcomes = dict(collections.Counter(x["adjudicated_outcome"] for x in records))
roots = dict(collections.Counter(x["root_cause_code"] for x in records))
result = {
    "schema_version": "phase4r-source-adjudication-compiled-v1",
    "evidence_phase": "CONSUMED_VALIDATION_SET_DIAGNOSTIC_AND_REMEDIATION_DATA",
    "original_disagreement_count": len(original),
    "adjudicated_count": len(records),
    "missing_original_ids": [],
    "extra_adjudication_ids": [],
    "outcome_counts": outcomes,
    "primary_root_cause_counts": roots,
    "human_source_review_performed": False,
    "ground_truth_critical_false_accepts": "UNKNOWN",
    "all_private_evidence_hashes_verified": True,
    "records": records,
}
(OUT / "DISAGREEMENT_ADJUDICATION.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

lines = [
    "# Phase 4R source adjudication",
    "",
    "All **43/43** original Phase 4 critical disagreement IDs match a Phase 4R source-adjudication record. Exact source evidence is stored only in private Phase 4R paths and every referenced private file passed SHA-256 verification. No record grants scientific acceptance or qualified human ground truth.",
    "",
    "| Outcome | Count |",
    "|---|---:|",
]
lines += [f"| `{key}` | {value} |" for key, value in sorted(outcomes.items())]
lines += ["", "Primary root-cause counts:", "", "| Root cause | Count |", "|---|---:|"]
lines += [f"| `{key}` | {value} |" for key, value in sorted(roots.items(), key=lambda pair: (-pair[1], pair[0]))]
lines += ["", "Decisive source findings: H03's 16.37% main-table result is narrower than the later 19.78% appendix result; H04 has four zero-vulnerability rows rather than three; H05 sampled 300 tasks rather than observing 300 failures; H06's page-27 locator does not entail its broad qualitative conclusion. These reports are now development evidence, not untouched validation data.", "", "See `DISAGREEMENT_ADJUDICATION.json` for every item, source hash, original and verifier positions, private evidence hash, outcome, severity, and candidate generalized fix."]
(OUT / "DISAGREEMENT_ADJUDICATION.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(json.dumps({"count": len(records), "outcomes": outcomes, "roots": roots}))
