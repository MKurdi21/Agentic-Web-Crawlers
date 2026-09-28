"""Record first substantive access without changing another report's state."""
import argparse
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("holdout_id")
args = parser.parse_args()
ledger_path = OUT / "HOLDOUT_ACCESS_LEDGER.json"
ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
report = next(r for r in ledger["reports"] if r["holdout_id"] == args.holdout_id)
receipt_path = OUT / "holdout_validation" / args.holdout_id / "private/FIRST_SUBSTANTIVE_ACCESS.json"
receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
assert receipt["source_sha256"] == report["source_sha256"]
assert receipt["context_id"] == report["primary_context_id"]
assert report["state"] == "VALIDATION_IN_PROGRESS"
observed_at = receipt.get("first_substantive_access_utc") or receipt.get("at") or receipt.get("timestamp")
assert observed_at, "missing first access timestamp"
if not report["substantive_access"]:
    report["substantive_access"] = True
    report["consumed"] = True
    report["first_substantive_access_at"] = observed_at
    ledger["events"].append({"event": "FIRST_SUBSTANTIVE_ACCESS", "holdout_id": args.holdout_id, "context_id": report["primary_context_id"], "at": report["first_substantive_access_at"]})
    ledger_path.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
elif report.get("first_substantive_access_at") is None:
    report["first_substantive_access_at"] = observed_at
    for event in ledger["events"]:
        if event.get("event") == "FIRST_SUBSTANTIVE_ACCESS" and event.get("holdout_id") == args.holdout_id and event.get("at") is None:
            event["at"] = observed_at
    ledger_path.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"holdout_id": args.holdout_id, "consumed": report["consumed"], "state": report["state"], "at": report.get("first_substantive_access_at")}))
