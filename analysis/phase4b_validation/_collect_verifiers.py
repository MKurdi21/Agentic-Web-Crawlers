"""Independently reconcile every dispatched B01 verification item."""
import argparse
import collections
import hashlib
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("holdout_id")
args = parser.parse_args()
report = OUT / "holdout_validation" / args.holdout_id
dispatch = json.loads((report / "VERIFIER_DISPATCH_MANIFEST.json").read_text())
sample = json.loads((report / "VERIFICATION_SAMPLE_MANIFEST.json").read_text())
all_results = []
errors = []
for batch in dispatch["batches"]:
    packet_path = Path(batch["packet_path"])
    packet = json.loads(packet_path.read_text(encoding="utf-8"))
    result_path = packet_path.parent / "VERIFICATION_RESULTS.json"
    if not result_path.is_file():
        errors.append(f"missing_results_batch_{batch['batch']}")
        continue
    result = json.loads(result_path.read_text(encoding="utf-8"))
    if result.get("context_id") != batch["context_id"] or result.get("holdout_id") != args.holdout_id or result.get("source_sha256") != sample["source_sha256"] or result.get("complete") is not True:
        errors.append(f"header_mismatch_batch_{batch['batch']}")
    expected = {x["stable_item_id"] for x in packet["candidate_items"]}
    actual = [x.get("stable_item_id") for x in result.get("results", [])]
    if set(actual) != expected or len(actual) != len(expected):
        errors.append(f"item_coverage_batch_{batch['batch']}")
    for item in result.get("results", []):
        if item.get("stable_item_id") in expected:
            all_results.append(dict(item, verifier_context_id=batch["context_id"], batch=batch["batch"]))
all_ids = [x.get("stable_item_id") for x in all_results]
if len(all_ids) != len(set(all_ids)) or len(all_ids) != sum(x["item_count"] for x in dispatch["batches"]):
    errors.append("global_item_coverage")

payload = {"holdout_id": args.holdout_id, "results": all_results, "errors": errors, "complete": not errors}
(report / "private/COMBINED_VERIFICATION_RESULTS.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
verdicts = collections.Counter(x.get("verdict", "MISSING") for x in all_results)
locators = collections.Counter(x.get("locator_status", "MISSING") for x in all_results)
metrics = {
    "holdout_id": args.holdout_id,
    "dispatched_item_count": sum(x["item_count"] for x in dispatch["batches"]),
    "verified_item_count": len(all_results),
    "critical_item_count": sample["critical_item_count"],
    "sampled_lower_risk_count": sample["required_sample_size"],
    "verifier_context_count": len(dispatch["batches"]),
    "verdict_counts": dict(verdicts),
    "locator_status_counts": dict(locators),
    "verifier_flagged_false_accept_count": sum(bool(x.get("detected_false_accept")) for x in all_results),
    "verifier_flagged_quantitative_error_count": sum(bool(x.get("quantitative_error")) for x in all_results),
    "verifier_flagged_comparative_error_count": sum(bool(x.get("comparative_error")) for x in all_results),
    "coverage_passed": not errors,
    "errors": errors,
}
(report / "VERIFIER_METRICS.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
print(json.dumps(metrics))
if errors:
    raise SystemExit(1)
