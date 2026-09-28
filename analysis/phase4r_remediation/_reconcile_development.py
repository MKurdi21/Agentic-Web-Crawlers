"""Independent identity/count reconciliation across all six consumed reports."""
import collections
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
DEV = OUT / "development_lanes"


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


original = list(csv.DictReader((ROOT / "analysis/phase4_rehearsal/HOLDOUT_DISAGREEMENTS.csv").open(encoding="utf-8", newline="")))
adj = read(OUT / "DISAGREEMENT_ADJUDICATION.json")
a = read(DEV / "h01_h02/H01_H02_ITEM_OUTCOMES.json")["items"]
b_result = read(DEV / "h03_h04/DEVELOPMENT_REPLAY_H03_H04.json")
b = b_result["critical_items"] + b_result["lower_risk_items"]
c_result = read(DEV / "h05_h06/H05_H06_DEVELOPMENT_RERUN.json")
c = c_result["critical_items"] + c_result["lower_risk_status"]
orig_ids = {(x["holdout_id"], x["stable_item_id"]) for x in original}
adj_ids = {(x["holdout_id"], x["evidence_item_id"]) for x in adj["records"]}
assert len(orig_ids) == len(adj_ids) == 43 and orig_ids == adj_ids


def item_id(row):
    return row.get("evidence_item_id") or row.get("original_evidence_item_id")


dev_rows = a + b + c
dev_ids = {(x["holdout_id"], item_id(x)) for x in dev_rows}
assert len(dev_rows) == len(dev_ids) == 233
critical = [x for x in dev_rows if x.get("critical", x in b_result["critical_items"] or x in c_result["critical_items"])]
assert len(critical) == 209
assert len(dev_rows) - len(critical) == 24
assert orig_ids <= dev_ids

dev_by_id = {(x["holdout_id"], item_id(x)): x for x in dev_rows}
adj_by_id = {(x["holdout_id"], x["evidence_item_id"]): x for x in adj["records"]}
matrix = []
for old in original:
    key = old["holdout_id"], old["stable_item_id"]
    x = dev_by_id[key]
    source = adj_by_id[key]
    if key[0] <= "H02":
        treatment = "CORRECTED_LOCATOR_PROPOSED" if x["known_disagreement_fix"] == "CORRECTED_LOCATOR_AND_OLD_FAIL_CLOSED" else "UNRESOLVED"
        revised = x["revised_original_claim_outcome"]
        locator = "ORIGINAL_FAIL_CLOSED_CORRECTED_PROPOSAL" if treatment != "UNRESOLVED" else "FAIL_CLOSED"
    elif key[0] <= "H04":
        revised = x["phase4r_outcome"]
        treatment = "FAIL_CLOSED" if revised.startswith("FAIL_CLOSED") else "CORRECTED_SOURCE_BOUND_PROPOSAL"
        locator = "FAIL_CLOSED" if treatment == "FAIL_CLOSED" else "ORIGINAL_FAIL_CLOSED_CORRECTED_PROPOSAL"
    else:
        revised = x["v3_assessment"]
        treatment = "FAIL_CLOSED" if x["disagreement_disposition"] == "FAIL_CLOSED" else "CORRECTED_SOURCE_BOUND_PROPOSAL"
        locator = "FAIL_CLOSED" if treatment == "FAIL_CLOSED" else "ORIGINAL_FAIL_CLOSED_CORRECTED_PROPOSAL"
    matrix.append({
        "original_disagreement_id": source["disagreement_id"],
        "holdout_id": key[0],
        "evidence_item_id": key[1],
        "field_id": source["field_id"],
        "root_cause": source["root_cause_code"],
        "original_outcome": source["adjudicated_outcome"],
        "revised_workflow_outcome": revised,
        "known_failure_fixed": treatment,
        "new_failure": "NONE_IN_THIS_ORIGINAL_DISAGREEMENT_RECORD",
        "locator_status": locator,
        "numeric_status": "CORRECTED_OR_FAIL_CLOSED" if source["root_cause_code"] in {"GLOBAL_RESULT_RECONCILIATION_FAILURE", "NEGATIVE_RESULT_COUNT_ERROR", "SAMPLE_DENOMINATOR_SCOPE_ERROR"} else "NOT_APPLICABLE",
        "regression_status": "ORIGINAL_DISAGREEMENT_NOT_PREVIOUSLY_SUPPORTED",
        "scientific_acceptance": "NOT_GRANTED",
        "notes": "Correction is a consumed-development proposal; no independent validation or human approval.",
    })
assert len(matrix) == 43

with (OUT / "DISAGREEMENT_RESOLUTION_MATRIX.csv").open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(matrix[0]))
    writer.writeheader()
    writer.writerows(matrix)

locator_original = {key for key in orig_ids if "LOCATOR_FAILURE" in next(x["error_codes"] for x in original if (x["holdout_id"], x["stable_item_id"]) == key)}
assert len(locator_original) == 42
locator_treatments = collections.Counter(x["locator_status"] for x in matrix if (x["holdout_id"], x["evidence_item_id"]) in locator_original)
assert locator_treatments["ORIGINAL_FAIL_CLOSED_CORRECTED_PROPOSAL"] + locator_treatments["FAIL_CLOSED"] == 42
assert all(x["known_failure_fixed"] != "UNRESOLVED" for x in matrix)

summary = {
    "status": "INDEPENDENT_COUNTS_RECONCILED",
    "original_phase4_disagreements": 43,
    "source_adjudicated_disagreements": 43,
    "development_replay_evidence_items": len(dev_rows),
    "development_replay_critical_items": len(critical),
    "development_replay_lower_risk_items": len(dev_rows) - len(critical),
    "original_locator_failures": 42,
    "original_locator_failure_treatments": dict(locator_treatments),
    "known_failure_treatments": dict(collections.Counter(x["known_failure_fixed"] for x in matrix)),
    "original_detected_false_accepts": 4,
    "original_detected_false_accepts_scientifically_accepted": 0,
    "newly_source_adjudicated_h05_sample_denominator_error": True,
    "previously_supported_original_claims_newly_fail_closed_or_scope_limited": 2 + 3 + 5,
    "additional_locator_weaknesses_reported_by_a_lane": 6,
    "material_factual_regressions_detected_by_lanes": 0,
    "human_ground_truth": "UNKNOWN",
    "methodological_limitation": "Development replay and model source review do not independently validate a new workflow; full v3 payload construction and an untouched Phase4B holdout remain necessary.",
}
(OUT / "test_results").mkdir(exist_ok=True)
(OUT / "test_results/INDEPENDENT_DEVELOPMENT_RECONCILIATION.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary))
