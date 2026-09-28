"""Create disjoint, current-report-only verifier packets after sample freeze."""
import argparse
import hashlib
import json
import math
import uuid
from pathlib import Path

OUT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument("holdout_id")
parser.add_argument("--batches", type=int, default=3)
args = parser.parse_args()
report = OUT / "holdout_validation" / args.holdout_id
private = report / "private"
assert json.loads((private / "PRIMARY_STATUS.json").read_text())["complete"]
assert (report / "VERIFICATION_SAMPLE_MANIFEST.json").is_file()
primary_validation = json.loads((private / "PRIMARY_SEMANTIC_VALIDATION.json").read_text())
assert primary_validation["passed"] or primary_validation["accepted"] is False, "invalid primary payload must remain unaccepted"
sample = json.loads((report / "VERIFICATION_SAMPLE_MANIFEST.json").read_text())
items = json.loads((private / "normalized_evidence_items.json").read_text())
selected = set(sample["selected_item_ids"])
verify = [x for x in items if x["critical"] or x["stable_item_id"] in selected]
assert len(verify) == sample["critical_item_count"] + sample["required_sample_size"]
assert len({x["stable_item_id"] for x in verify}) == len(verify)
verify.sort(key=lambda x: x["stable_item_id"])
size = math.ceil(len(verify) / args.batches)
dispatch = {"holdout_id": args.holdout_id, "critical_item_count": sample["critical_item_count"], "sampled_lower_risk_count": sample["required_sample_size"], "primary_semantic_payload_passed": primary_validation["passed"], "primary_payload_accepted": primary_validation["accepted"], "batches": []}
for number in range(args.batches):
    batch = verify[number * size:(number + 1) * size]
    if not batch:
        continue
    context_id = "verifier_" + uuid.uuid4().hex
    folder = private / f"verifier_batch_{number + 1:02d}"
    folder.mkdir(parents=True, exist_ok=False)
    packet = {
        "context_protocol_version": "phase4b-context-isolation-v1",
        "context_id": context_id,
        "mode": "SEPARATE_CONTEXT_MODEL_VERIFICATION",
        "holdout_id": args.holdout_id,
        "paper_id": sample["paper_id"],
        "source_sha256": sample["source_sha256"],
        "source_snapshot": str(OUT / "private_source_material" / args.holdout_id / "source.pdf"),
        "frozen_verification_protocol": str(OUT / "candidate_frozen/frozen_inputs/phase4r/VERIFICATION_PROTOCOL_V2.md"),
        "frozen_scientific_protocol": str(OUT / "candidate_frozen/deploy_payload/protocols/SCIENTIFIC_EVIDENCE_V3.md"),
        "field_catalog": str(OUT / "candidate_frozen/frozen_inputs/phase3/FIELD_CATALOG.json"),
        "candidate_items": [
            {"stable_item_id": x["stable_item_id"], "stable_field_id": x["stable_field_id"], "claim": x["claim"], "proposed_support_locator": x["locator"], "critical": x["critical"], "primary_support_status": x["primary_support_status"]}
            for x in batch
        ],
        "output_private_root": str(folder),
        "previous_holdout_scientific_content_included": False,
        "coordinator_summary_included": False,
        "primary_rationale_included": False,
    }
    path = folder / "VERIFIER_CONTEXT_PACKET.json"
    path.write_text(json.dumps(packet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    dispatch["batches"].append({"batch": number + 1, "context_id": context_id, "packet_sha256": digest, "packet_path": str(path), "item_count": len(batch), "critical_count": sum(x["critical"] for x in batch), "item_ids": [x["stable_item_id"] for x in batch]})
dest = report / "VERIFIER_DISPATCH_MANIFEST.json"
assert not dest.exists()
dest.write_text(json.dumps(dispatch, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"holdout_id": args.holdout_id, "batches": [{k: b[k] for k in ("batch", "context_id", "item_count", "critical_count", "packet_path")} for b in dispatch["batches"]]}))
