"""Freeze Phase 4B candidate bytes, holdout order, and context rules."""
import csv
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
P4R = ROOT / "analysis/phase4r_remediation"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def write(name, data):
    (OUT / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


assert json.loads((OUT / "PHASE4B_BASELINE.json").read_text(encoding="utf-8"))["passed"]
config = json.loads((P4R / "REMEDIATED_WORKFLOW_CONFIGURATION.json").read_text(encoding="utf-8"))
release = json.loads((P4R / "PACKAGE_MANIFEST.json").read_text(encoding="utf-8"))
roots = [OUT / "candidate_frozen", OUT / "candidate_v4r"]
assert not any(root.exists() for root in roots), "candidate copy already exists"

entries = []
for member in release["inventory"]:
    rel = member["path"]
    if not rel.startswith("candidate_v4r/"):
        continue
    child = rel[len("candidate_v4r/"):]
    source = P4R / rel
    assert sha(source) == member["sha256"]
    for dest_root in roots:
        dest = dest_root / child
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, dest)
    entries.append({"relative_path": child, "size_bytes": member["size_bytes"], "sha256": member["sha256"], "role": "FROZEN_CANDIDATE_SOURCE", "scientific_behavior_relevant": True})

external = [
    (P4R / name, "frozen_inputs/phase4r/" + name)
    for name in [
        "DOCUMENT_WIDE_COMPARATIVE_RECONCILIATION.md", "DERIVED_NUMERIC_VERIFICATION.md",
        "LOCATOR_ENTAILMENT_PROTOCOL.md", "ATOMIC_CLAIM_DECOMPOSITION.md", "TABLE_EVIDENCE_MODEL.md",
        "VERIFICATION_PROTOCOL_V2.md", "FIELD_AUTOMATION_MATRIX_V2.csv", "ROOT_CAUSE_TAXONOMY.json",
        "PHASE4B_VALIDATION_PLAN.md",
    ]
]
external.extend([
    (ROOT / "analysis/phase3_calibration/FIELD_CATALOG.json", "frozen_inputs/phase3/FIELD_CATALOG.json"),
    (ROOT / "analysis/phase3_calibration/CALIBRATION_PROTOCOL.md", "frozen_inputs/phase3/CALIBRATION_PROTOCOL.md"),
])
for source, child in external:
    assert source.is_file()
    digest = sha(source)
    for dest_root in roots:
        dest = dest_root / child
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, dest)
    entries.append({"relative_path": child, "size_bytes": source.stat().st_size, "sha256": digest, "role": "FROZEN_EXTERNAL_METHOD_INPUT", "scientific_behavior_relevant": True})

entries.sort(key=lambda x: x["relative_path"])
manifest_fingerprint = hashlib.sha256(canonical(entries)).hexdigest()
code_manifest = {
    "schema_version": "phase4b-candidate-code-manifest-v1",
    "methodology_version": config["methodology_version"],
    "parent_methodology_sha256": config["configuration_sha256"],
    "manifest_fingerprint": manifest_fingerprint,
    "candidate_names": ["candidate_frozen", "candidate_v4r"],
    "immutable_files": entries,
    "excluded_mutable_roots": ["shadow", "outbox", "runtime", "test_results", "__pycache__", "_deps"],
}
write("CANDIDATE_CODE_MANIFEST.json", code_manifest)
(OUT / "CANDIDATE_CODE_MANIFEST.md").write_text(
    "# Phase 4B immutable candidate code\n\n"
    f"Frozen methodology: `{config['methodology_version']}` / `{config['configuration_sha256']}`.\n\n"
    f"{len(entries)} exact immutable files; manifest fingerprint `{manifest_fingerprint}`. "
    "Both candidate roots have identical normalized paths, sizes, and SHA-256 values. "
    "Only candidate_v4r is executable; candidate_frozen is the reference. "
    "Mutable shadow databases, artifact blobs, outboxes, logs, receipts, backups and caches are excluded from code equality and checked by runtime integrity gates.\n",
    encoding="utf-8",
)
for root in roots:
    for item in entries:
        p = root / item["relative_path"]
        assert p.stat().st_size == item["size_bytes"] and sha(p) == item["sha256"]

holdout_path = P4R / "PHASE4B_VALIDATION_HOLDOUT.csv"
with holdout_path.open(encoding="utf-8-sig", newline="") as f:
    holdout = list(csv.DictReader(f))
assert [r["holdout_id"] for r in holdout] == [f"B{i:02d}" for i in range(1, 9)]
selection_protocol_sha = sha(P4R / "PHASE4B_HOLDOUT_SELECTION_PROTOCOL.md")
holdout_sha = sha(holdout_path)
order = {
    "algorithm_version": "phase4r-csv-row-order-v1",
    "selection_protocol_sha256": selection_protocol_sha,
    "holdout_list_sha256": holdout_sha,
    "entries": [
        {"ordinal": index, "holdout_id": row["holdout_id"], "paper_id": row["paper_report_id"], "source_sha256": row["source_sha256"]}
        for index, row in enumerate(holdout, 1)
    ],
}
write("PHASE4B_HOLDOUT_PROCESSING_ORDER.json", order)
(OUT / "PHASE4B_HOLDOUT_PROCESSING_ORDER.md").write_text(
    "# Frozen Phase 4B holdout processing order\n\n"
    "Algorithm `phase4r-csv-row-order-v1`: preserve the Phase 4R holdout CSV row order B01–B08. "
    "Complete and gate each report before opening the next. Stop on the first mandatory failure. "
    f"Selection protocol SHA-256 `{selection_protocol_sha}`; holdout CSV SHA-256 `{holdout_sha}`.\n\n"
    + "\n".join(f"{x['ordinal']}. `{x['holdout_id']}` — `{x['paper_id']}` — `{x['source_sha256']}`" for x in order["entries"]) + "\n",
    encoding="utf-8",
)

frozen = {
    "frozen_at": datetime.now(timezone.utc).isoformat(),
    "methodology_version": config["methodology_version"],
    "methodology_sha256": config["configuration_sha256"],
    "scientific_schema_version": config["scientific_schema_version"],
    "evidence_workflow_name": "frozen Phase 4R evidence workflow",
    "evidence_workflow_independent_version": None,
    "candidate_code_manifest_fingerprint": manifest_fingerprint,
    "candidate_code_manifest_sha256": sha(OUT / "CANDIDATE_CODE_MANIFEST.json"),
    "phase4r_package_sha256": sha(ROOT / "analysis/phase4r_remediation_package.zip"),
    "holdout_order_sha256": sha(OUT / "PHASE4B_HOLDOUT_PROCESSING_ORDER.json"),
    "holdout_selection_csv_sha256": holdout_sha,
    "holdout_selection_protocol_sha256": selection_protocol_sha,
    "field_catalog_sha256": sha(ROOT / "analysis/phase3_calibration/FIELD_CATALOG.json"),
    "components": config["components"],
}
write("FROZEN_PHASE4B_CONFIGURATION.json", frozen)
(OUT / "FROZEN_PHASE4B_CONFIGURATION.md").write_text(
    "# Frozen Phase 4B configuration\n\n"
    f"Methodology `{config['methodology_version']}` / `{config['configuration_sha256']}`. "
    f"Scientific evidence schema `{config['scientific_schema_version']}`. "
    "There is no separate formally versioned evidence workflow. "
    f"Immutable candidate manifest fingerprint `{manifest_fingerprint}`. "
    f"Holdout CSV SHA-256 `{holdout_sha}`. "
    "Any behavior-affecting byte change stops Lane A2; mutable shadow state is checked separately.\n",
    encoding="utf-8",
)

write("HOLDOUT_ACCESS_LEDGER.json", {
    "schema_version": "phase4b-holdout-access-v1",
    "frozen_order_sha256": sha(OUT / "PHASE4B_HOLDOUT_PROCESSING_ORDER.json"),
    "reports": [dict(x, state="UNTOUCHED_RESERVED_VALIDATION_EVIDENCE", substantive_access=False, consumed=False, completed=False, primary_context_id=None, verifier_context_ids=[], result=None) for x in order["entries"]],
    "events": [],
})
write("HOLDOUT_CONTEXT_ISOLATION.json", {
    "context_protocol_version": "phase4b-context-isolation-v1",
    "frozen_protocol_hash": config["configuration_sha256"],
    "primary_fresh_contexts": 0,
    "verifier_fresh_contexts": 0,
    "contamination_events": [],
    "receipts": [],
})
print(json.dumps({"immutable_files": len(entries), "manifest_fingerprint": manifest_fingerprint, "holdout_order": [x["holdout_id"] for x in order["entries"]], "candidate_equal": True}))
