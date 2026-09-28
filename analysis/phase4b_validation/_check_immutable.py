"""Recheck frozen candidate byte equality around each holdout report."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("holdout_id")
parser.add_argument("phase", choices=["before", "after"])
args = parser.parse_args()
manifest = json.loads((OUT / "CANDIDATE_CODE_MANIFEST.json").read_text(encoding="utf-8"))
expected = {item["relative_path"]: item for item in manifest["immutable_files"]}
excluded = set(manifest["excluded_mutable_roots"])
errors = []
for root_name in manifest["candidate_names"]:
    root = OUT / root_name
    actual = {p.relative_to(root).as_posix(): p for p in root.rglob("*") if p.is_file() and not excluded.intersection(p.relative_to(root).parts)}
    if set(actual) != set(expected):
        errors.append({"root": root_name, "missing": sorted(set(expected) - set(actual)), "unexpected": sorted(set(actual) - set(expected))})
    for rel, entry in expected.items():
        p = actual.get(rel)
        if p is None:
            continue
        observed = hashlib.sha256(p.read_bytes()).hexdigest()
        if observed != entry["sha256"] or p.stat().st_size != entry["size_bytes"]:
            errors.append({"root": root_name, "path": rel, "expected_sha256": entry["sha256"], "observed_sha256": observed})
receipt = {
    "checked_at": datetime.now(timezone.utc).isoformat(),
    "holdout_id": args.holdout_id,
    "phase": args.phase,
    "manifest_fingerprint": manifest["manifest_fingerprint"],
    "candidate_frozen_equals_execution_copy": not errors,
    "methodology_drift_detected": bool(errors),
    "errors": errors,
}
path = OUT / "holdout_validation" / args.holdout_id / f"IMMUTABLE_CHECK_{args.phase.upper()}.json"
path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"holdout_id": args.holdout_id, "phase": args.phase, "passed": not errors, "error_count": len(errors)}))
if errors:
    raise SystemExit(1)
