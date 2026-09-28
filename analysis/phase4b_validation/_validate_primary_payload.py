"""Run unchanged frozen semantic validator against a primary candidate artifact."""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("holdout_id")
args = parser.parse_args()
candidate = OUT / "candidate_v4r"
sys.path[:0] = [str(candidate / "_deps"), str(candidate / "hardened/scripts")]
from scientific_v3 import ScientificFailure, validate_scientific_payload

path = OUT / "holdout_validation" / args.holdout_id / "private/primary_evidence.json"
payload = json.loads(path.read_text(encoding="utf-8"))
schema = candidate / "hardened/schemas/scientific_evidence_v3.schema.json"
receipt = {
    "checked_at": datetime.now(timezone.utc).isoformat(),
    "holdout_id": args.holdout_id,
    "candidate_payload_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    "schema_sha256": hashlib.sha256(schema.read_bytes()).hexdigest(),
    "frozen_validator_sha256": hashlib.sha256((candidate / "hardened/scripts/scientific_v3.py").read_bytes()).hexdigest(),
    "accepted": False,
}
try:
    receipt["validator_result"] = validate_scientific_payload(payload, schema)
    receipt["passed"] = True
except ScientificFailure as error:
    receipt["passed"] = False
    receipt["error_code"] = error.code
    receipt["error"] = str(error)
dest = path.parent / "PRIMARY_SEMANTIC_VALIDATION.json"
dest.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: receipt.get(k) for k in ("holdout_id", "passed", "error_code", "error", "accepted")}))
