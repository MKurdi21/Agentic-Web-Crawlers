"""Freeze an untouched metadata-only Phase 4B challenge set after methodology freeze."""
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


config_path = OUT / "REMEDIATED_WORKFLOW_CONFIGURATION.json"
config = json.loads(config_path.read_text(encoding="utf-8"))
assert config["candidate_test_count"] == config["candidate_test_passed"] == 86
assert config["methodology_version"] == "phase4r-scientific-v2.0.0"
before = {p: sha(ROOT / p) for p in [
    "analysis/integration_design/test_results/COMPATIBILITY_EXPORT.json",
    "analysis/workspace_audit/CORPUS_INVENTORY.csv",
    "analysis/phase3_calibration/CALIBRATION_CASES.csv",
    "analysis/phase3_calibration/PHASE4_VALIDATION_HOLDOUT.csv",
    "analysis/phase4r_remediation/REMEDIATED_WORKFLOW_CONFIGURATION.json",
]}
snapshot_body = "\n".join(f"{path}\0{digest}" for path, digest in sorted(before.items()))
snapshot_sha = hashlib.sha256(snapshot_body.encode("utf-8")).hexdigest()

reports = json.loads((ROOT / "analysis/integration_design/test_results/COMPATIBILITY_EXPORT.json").read_text(encoding="utf-8"))["reports"]
by_id = {x["paper_report_id"]: x for x in reports}
corpus = {x["path"].replace("\\", "/"): x for x in read_csv(ROOT / "analysis/workspace_audit/CORPUS_INVENTORY.csv") if x["canonical_status"] == "ACTIVE_MANIFEST"}
calibration = {x["paper_id"] for x in read_csv(ROOT / "analysis/phase3_calibration/CALIBRATION_CASES.csv")}
consumed = {x["paper_report_id"] for x in read_csv(ROOT / "analysis/phase3_calibration/PHASE4_VALIDATION_HOLDOUT.csv")}
assert len(calibration) == 15 and len(consumed) == 6 and not calibration & consumed

# Preferred identities were chosen from frozen audit category, title and page
# count metadata, not by opening their scientific contents.
strata = [
    ("B01", "SECURITY_BENCHMARK", "report_e30d9cfd6055ddd8e085a0ff"),
    ("B02", "DEFENSE_ARCHITECTURE", "report_6f57206775618d3dc16a3f86"),
    ("B03", "BENCHMARK_COMPLEX_PRESENTATION", "report_5ddfe04670e9d956978cbe50"),
    ("B04", "RESOURCE_AVAILABILITY", "report_9b77b416c08c4534e8c90b0b"),
    ("B05", "LONG_HORIZON_BEHAVIOR", "report_854539293a7335577e2e873e"),
    ("B06", "TRADITIONAL_CRAWLER", "report_99acfcc0adf8c2330981bafd"),
    ("B07", "SURVEY_TAXONOMY", "report_272be28ea93b06f8bff67eef"),
    ("B08", "MULTIMODAL_ATTACK", "report_bd3e6221914e4d3b26c19eb9"),
]
selected = []
used = set()
for holdout_id, stratum, preferred in strata:
    candidate = by_id[preferred]
    path = candidate["source_path"].replace("\\", "/")
    meta = corpus[path]
    assert preferred not in calibration | consumed | used
    assert not meta["version_relation"] and meta["canonical_status"] == "ACTIVE_MANIFEST"
    assert sha(ROOT / path) == candidate["source_sha256"] == meta["sha256"]
    used.add(preferred)
    selected.append({
        "holdout_id": holdout_id,
        "paper_report_id": preferred,
        "source_file_id": "sha256:" + candidate["source_sha256"],
        "source_sha256": candidate["source_sha256"],
        "summary_name": candidate["summary_name"],
        "audit_category": meta["collection"],
        "processing_state": candidate["legacy_status"],
        "pdf_pages": meta["pdf_pages"],
        "selection_stratum": stratum,
        "selection_rationale": "Metadata-only category, title and structural page-count coverage; no substantive paper inspection.",
        "selection_protocol_version": "phase4b-holdout-selection-v1",
        "selection_snapshot_sha256": snapshot_sha,
        "methodology_fingerprint": config["configuration_sha256"],
    })

assert len(selected) == 8 and len({x["source_sha256"] for x in selected}) == 8
csv_path = OUT / "PHASE4B_VALIDATION_HOLDOUT.csv"
with csv_path.open("w", encoding="utf-8", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=list(selected[0]))
    writer.writeheader()
    writer.writerows(selected)
frozen_at = datetime.now(timezone.utc).isoformat()
receipt = {
    "selection_protocol_version": "phase4b-holdout-selection-v1",
    "selection_timestamp": frozen_at,
    "selection_inputs": before,
    "selection_snapshot_sha256": snapshot_sha,
    "methodology_fingerprint": config["configuration_sha256"],
    "report_ids": [x["paper_report_id"] for x in selected],
    "source_sha256s": [x["source_sha256"] for x in selected],
    "report_count": len(selected),
    "holdout_sha256": sha(csv_path),
    "scientific_content_opened": False,
    "holdout_status": "FROZEN_UNTOUCHED_FOR_PHASE4B",
}
(OUT / "PHASE4B_HOLDOUT_SELECTION_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
(OUT / "PHASE4B_HOLDOUT_CONTAMINATION_LOG.json").write_text(json.dumps({"schema_version": "phase4b-contamination-log-v1", "holdout_sha256": receipt["holdout_sha256"], "events": [], "contamination_count": 0, "status": "UNTOUCHED"}, indent=2) + "\n", encoding="utf-8")

protocol = f"""# Phase 4B holdout selection protocol

`selection_protocol_version = phase4b-holdout-selection-v1`  
`selection_timestamp = {frozen_at}`  
`methodology_fingerprint = {config['configuration_sha256']}`  
`selection_snapshot_sha256 = {snapshot_sha}`  
`holdout_sha256 = {receipt['holdout_sha256']}`

The eight-report holdout was selected **after** methodology version `{config['methodology_version']}` was frozen and before scientific inspection of these reports. Selection used only the Phase 2 report crosswalk and Phase 1 corpus category/title/page-count metadata plus source-hash confirmation. It is a challenge set for quantitative, comparative, negative, availability, security, benchmark, long-horizon, crawler, survey, and multimodal workflow behavior; it is not statistically representative of all 112 reports. These dimensions are selection intentions inferred from bibliographic and structural metadata, not assessed paper findings.

Exclusions: all 15 Phase 3 calibration reports, six consumed Phase 4 reports, exact duplicate physical copies, unresolved version/contribution groups, and any report substantively opened during Phase 4R. Every selected report is an active manifest identity with a distinct verified source hash and no recorded version relation. Synthetic fixtures contain no additional report identity. One report fills each stratum; preferred IDs and rationale are frozen in the CSV.

If a preferred report later proves ineligible through metadata drift **before Phase 4B substantive access**, a new version must select an eligible active report from the same audit category by lexicographically smallest source SHA-256 after applying the same exclusions. Record the replacement and new CSV hash. Never use Phase 4R failure details or apparent likelihood of success to choose a replacement. Once Phase 4B begins, contamination or methodology tuning invalidates untouched status and requires a new validation set.

Phase 4R may confirm identity, source hash, processing state, and pre-existing artifact inventory. It may not extract claims, results, locators, taxonomy codes, summaries, or reuse judgments from these eight sources. No PDF content was opened during selection. The empty `PHASE4B_HOLDOUT_CONTAMINATION_LOG.json` records this boundary; Phase 4B must recheck it before Lane A2.

Selection inputs and exact SHA-256 values are recorded in `PHASE4B_HOLDOUT_SELECTION_RECEIPT.json`. Report identities and source hashes are frozen in `PHASE4B_VALIDATION_HOLDOUT.csv`.
"""
(OUT / "PHASE4B_HOLDOUT_SELECTION_PROTOCOL.md").write_text(protocol, encoding="utf-8")
print(json.dumps({"reports": len(selected), "holdout_sha256": receipt["holdout_sha256"], "methodology_fingerprint": config["configuration_sha256"]}))
