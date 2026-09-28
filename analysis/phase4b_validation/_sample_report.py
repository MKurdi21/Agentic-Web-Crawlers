"""Frozen per-report lower-risk sampler; run after complete primary extraction."""
import argparse
import hashlib
import json
import math
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("holdout_id")
args = parser.parse_args()
report = OUT / "holdout_validation" / args.holdout_id
private = report / "private"
status = json.loads((private / "PRIMARY_STATUS.json").read_text(encoding="utf-8"))
assert status.get("complete") is True and status.get("eligible_set_complete") is True
assert (private / "FIRST_SUBSTANTIVE_ACCESS.json").is_file()
raw = json.loads((private / "primary_evidence_items.json").read_text(encoding="utf-8"))
assert isinstance(raw, list) and raw
order = json.loads((OUT / "PHASE4B_HOLDOUT_PROCESSING_ORDER.json").read_text(encoding="utf-8"))
record = next(x for x in order["entries"] if x["holdout_id"] == args.holdout_id)
field_catalog = json.loads((ROOT / "analysis/phase3_calibration/FIELD_CATALOG.json").read_text(encoding="utf-8"))
fields = {f["stable_field_id"] for f in field_catalog["fields"]}


def norm(value):
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, list):
        return [norm(v) for v in value]
    if isinstance(value, dict):
        return {norm(k): norm(v) for k, v in value.items()}
    return value


def canonical(value):
    return json.dumps(norm(value), sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")


protocol_sha = hashlib.sha256((ROOT / "analysis/phase3_calibration/CALIBRATION_PROTOCOL.md").read_bytes()).hexdigest()
field_sha = hashlib.sha256((ROOT / "analysis/phase3_calibration/FIELD_CATALOG.json").read_bytes()).hexdigest()
items = []
seen = set()
for item in raw:
    assert item["stable_field_id"] in fields
    assert item["source_sha256"] == record["source_sha256"] and item["paper_id"] == record["paper_id"]
    assert isinstance(item["critical"], bool)
    field = unicodedata.normalize("NFC", item["stable_field_id"])
    stable = "ei_" + hashlib.sha256(b"\x00".join([
        record["source_sha256"].encode("utf-8"), field.encode("utf-8"),
        canonical(item["claim"]), canonical(item["locator"]),
    ])).hexdigest()
    if item.get("stable_item_id") not in (None, stable):
        raise RuntimeError("primary stable ID differs from frozen algorithm")
    if stable in seen:
        continue
    seen.add(stable)
    items.append(dict(item, stable_item_id=stable))

eligible = []
for item in items:
    if item["critical"]:
        continue
    parts = [protocol_sha, args.holdout_id, record["paper_id"], item["stable_field_id"], item["stable_item_id"]]
    parts = [unicodedata.normalize("NFC", str(p)) for p in parts]
    assert all(parts)
    digest = hashlib.sha256(b"\x00".join(p.encode("utf-8") for p in parts)).hexdigest()
    eligible.append({"stable_item_id": item["stable_item_id"], "stable_field_id": item["stable_field_id"], "selection_digest": digest})
eligible.sort(key=lambda x: (x["selection_digest"], x["stable_item_id"]))
n = len(eligible)
size = min(n, max(3, math.ceil(0.25 * n)))
manifest = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "holdout_id": args.holdout_id,
    "paper_id": record["paper_id"],
    "source_sha256": record["source_sha256"],
    "selection_algorithm_version": "sha256-lexicographic-v1",
    "protocol_sha256": protocol_sha,
    "field_catalog_sha256": field_sha,
    "candidate_evidence_set_sha256": hashlib.sha256(canonical(sorted(x["stable_item_id"] for x in eligible))).hexdigest(),
    "evidence_item_count": len(items),
    "critical_item_count": sum(x["critical"] for x in items),
    "eligible_lower_risk_count": n,
    "required_sample_size": size,
    "selected_item_ids": [x["stable_item_id"] for x in eligible[:size]],
    "selection_digests": [x["selection_digest"] for x in eligible[:size]],
}
dest = report / "VERIFICATION_SAMPLE_MANIFEST.json"
assert not dest.exists(), "sample already frozen"
(private / "normalized_evidence_items.json").write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
dest.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: manifest[k] for k in ["holdout_id", "evidence_item_count", "critical_item_count", "eligible_lower_risk_count", "required_sample_size"]}))
