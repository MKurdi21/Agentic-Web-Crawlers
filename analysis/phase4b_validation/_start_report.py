"""Prepare exactly the next frozen holdout report, without reading PDF content."""
import argparse
import hashlib
import json
import shutil
import uuid
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument("holdout_id")
args = parser.parse_args()
assert json.loads((OUT / "PHASE4B_BASELINE.json").read_text())["passed"]
assert json.loads((OUT / "HOLDOUT_PREVALIDATION_CHECK.json").read_text())["passed"]
manifest = json.loads((OUT / "CANDIDATE_CODE_MANIFEST.json").read_text())
for root_name in ("candidate_frozen", "candidate_v4r"):
    for entry in manifest["immutable_files"]:
        p = OUT / root_name / entry["relative_path"]
        assert p.is_file() and p.stat().st_size == entry["size_bytes"] and sha(p) == entry["sha256"], f"METHODOLOGY_DRIFT: {root_name}/{entry['relative_path']}"

ledger_path = OUT / "HOLDOUT_ACCESS_LEDGER.json"
ledger = json.loads(ledger_path.read_text())
pending = [r for r in ledger["reports"] if not r["completed"]]
assert pending and pending[0]["holdout_id"] == args.holdout_id, "not next report"
assert all(r["result"] in ("HOLDOUT_VALIDATION_PASS", "HOLDOUT_VALIDATION_PASS_WITH_LIMITATIONS") for r in ledger["reports"] if r["completed"]), "previous gate blocked"
record = pending[0]
assert record["state"] == "UNTOUCHED_RESERVED_VALIDATION_EVIDENCE"
baseline = json.loads((OUT / "PHASE4B_BASELINE.json").read_text())
source = next(r for r in baseline["holdout_sources"] if r["holdout_id"] == args.holdout_id)
path = ROOT / source["path"]
assert sha(path) == record["source_sha256"] == source["expected_sha256"], "HOLDOUT_SOURCE_DRIFT"

private = OUT / "private_source_material" / args.holdout_id
private.mkdir(parents=True, exist_ok=False)
snapshot = private / "source.pdf"
shutil.copyfile(path, snapshot)
assert sha(snapshot) == record["source_sha256"]
report_dir = OUT / "holdout_validation" / args.holdout_id
(report_dir / "private").mkdir(parents=True, exist_ok=False)
context_id = "primary_" + uuid.uuid4().hex
packet = {
    "context_protocol_version": "phase4b-context-isolation-v1",
    "context_id": context_id,
    "mode": "PRIMARY_MODEL_EXTRACTION",
    "holdout_id": args.holdout_id,
    "paper_id": record["paper_id"],
    "source_sha256": record["source_sha256"],
    "source_snapshot": str(snapshot),
    "field_catalog": str(OUT / "candidate_frozen/frozen_inputs/phase3/FIELD_CATALOG.json"),
    "frozen_methodology": str(OUT / "FROZEN_PHASE4B_CONFIGURATION.json"),
    "candidate_schema": str(OUT / "candidate_frozen/hardened/schemas/scientific_evidence_v3.schema.json"),
    "protocol_root": str(OUT / "candidate_frozen/frozen_inputs/phase4r"),
    "candidate_protocol": str(OUT / "candidate_frozen/deploy_payload/protocols/SCIENTIFIC_EVIDENCE_V3.md"),
    "output_private_root": str(report_dir / "private"),
    "output_public_root": str(report_dir),
    "disallowed_context": ["other holdout PDF content", "prior holdout results", "prior disagreements", "running aggregate metrics", "coordinator scientific findings"],
    "previous_holdout_scientific_content_included": False,
    "coordinator_summary_included": False,
}
packet_path = report_dir / "PRIMARY_CONTEXT_PACKET.json"
packet_path.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
packet_sha = sha(packet_path)
record["state"] = "VALIDATION_IN_PROGRESS"
record["primary_context_id"] = context_id
ledger["events"].append({"at": datetime.now(timezone.utc).isoformat(), "holdout_id": args.holdout_id, "event": "PREPARED_NO_SUBSTANTIVE_ACCESS", "context_id": context_id, "packet_sha256": packet_sha})
ledger_path.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"holdout_id": args.holdout_id, "primary_context_id": context_id, "packet_sha256": packet_sha, "snapshot_sha256": sha(snapshot), "packet_path": str(packet_path)}))
