"""Record current-report verifier context dispatch without source findings."""
import argparse
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("holdout_id")
args = parser.parse_args()
dispatch = json.loads((OUT / "holdout_validation" / args.holdout_id / "VERIFIER_DISPATCH_MANIFEST.json").read_text())
context_path = OUT / "HOLDOUT_CONTEXT_ISOLATION.json"
context = json.loads(context_path.read_text(encoding="utf-8-sig"))
receipt = next(r for r in context["receipts"] if r["holdout_id"] == args.holdout_id)
ids = [b["context_id"] for b in dispatch["batches"]]
assert not receipt["verifier_context_ids"]
receipt["verifier_context_ids"] = ids
receipt["verifier_packet_sha256s"] = [b["packet_sha256"] for b in dispatch["batches"]]
context["verifier_fresh_contexts"] += len(ids)
context_path.write_text(json.dumps(context, indent=2) + "\n", encoding="utf-8")
ledger_path = OUT / "HOLDOUT_ACCESS_LEDGER.json"
ledger = json.loads(ledger_path.read_text())
record = next(r for r in ledger["reports"] if r["holdout_id"] == args.holdout_id)
assert record["consumed"] and not record["verifier_context_ids"]
record["verifier_context_ids"] = ids
ledger_path.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"holdout_id": args.holdout_id, "verifier_context_count": len(ids)}))
