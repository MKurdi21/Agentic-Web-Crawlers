from __future__ import annotations

import csv
import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent

UNITS = [
    ("C01", "C01", ["report_f65b70426e7cad20f3bca498"], "DURABLE_EVIDENCE_PARTIAL_REVIEW", "Test provenance, partial review, locators, and summary reuse"),
    ("C02", "C02", ["report_e1a4d04452c57f69534e5603"], "EXTRACTION_ONLY", "Test independent reuse of extraction-only evidence"),
    ("C03", "C03", ["report_4a25815942a0fae3db98433d"], "LEGACY_AND_V2", "Compare two historical summary generations"),
    ("C04", "C04", ["report_5f96daa6c80a1d5839a1d991"], "LEGACY_ONLY", "Measure legacy-summary reuse"),
    ("C05", "C05", ["report_a4988586b3a9b60e43f89eda"], "UNPROCESSED", "Test minimum new structured extraction without summary generation"),
    ("C06", "C06", ["report_97ce3e361031031820f35361"], "EXACT_DUPLICATE_OBSERVATION", "Verify one source identity with two physical observations"),
    ("C07", "C07a", ["report_05dbe40340050b30d7fb7462", "report_29316d7f064e35b04ddd17fa"], "REPORT_VERSION_AND_CONTRIBUTION_RELATIONSHIPS", "Adjudication evidence for Mind the Web pair"),
    ("C07", "C07b", ["report_17b162af40f95b9ba51cb157", "report_23e9445a563eb86c07c0ac0b"], "REPORT_VERSION_AND_CONTRIBUTION_RELATIONSHIPS", "Adjudication evidence for AgentVigil pair"),
    ("C08", "C08", ["report_d0c5b16dc9dbc30b0d49815f"], "SECURITY_ATTACK", "Calibrate adversarial and attack fields"),
    ("C09", "C09", ["report_c16f40cd135ffcbb595294e7"], "DEFENSE", "Calibrate defense assumptions and architecture"),
    ("C10", "C10", ["report_db40269d76c4e5b83043918b"], "BENCHMARK_ENVIRONMENT", "Calibrate benchmarks, metrics, and comparative results"),
    ("C11", "C11", ["report_da6cfb0488d945c042abd882"], "TRADITIONAL_CRAWLER", "Test applicability outside LLM-agent papers"),
    ("C12", "C12", ["report_a772a6285ca222fd2e193e7f"], "SURVEY_SOK", "Test survey role, taxonomy, and contribution denominator"),
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    protocol_sha = digest(OUT / "CALIBRATION_PROTOCOL.md")
    field_sha = digest(OUT / "FIELD_CATALOG.json")
    inventory = {
        r["summary_name"]: r
        for r in csv.DictReader((ROOT / "analysis/workspace_audit/CORPUS_INVENTORY.csv").open(encoding="utf-8-sig"))
        if r.get("canonical_status") == "ACTIVE_MANIFEST"
    }
    db = sqlite3.connect(f"file:{(ROOT / 'analysis/integration_design/shadow/current.sqlite3').as_posix()}?mode=ro", uri=True)
    reports = {
        row[0]: {
            "paper_id": row[0], "summary_name": row[1], "source_file_id": row[2],
            "source_path": row[3], "existing_processing_state": row[5]
        }
        for row in db.execute("SELECT paper_report_id,summary_name,source_id,source_path,legacy_status,scientific_state FROM reports")
    }
    observations = dict(db.execute("SELECT source_id,COUNT(*) FROM observations GROUP BY source_id"))
    rows = []
    for category, unit, ids, kind, question in UNITS:
        for paper_id in ids:
            report = reports[paper_id]
            inv = inventory[report["summary_name"]]
            artifacts = [x for x in [inv.get("legacy_summary"), inv.get("v2_summary"), inv.get("evidence_workspace"), inv.get("scratch_workspaces")] if x]
            rows.append({
                "calibration_category_id": category,
                "calibration_unit_id": unit,
                "paper_id": paper_id,
                "summary_name": report["summary_name"],
                "source_file_id": report["source_file_id"],
                "source_sha256": report["source_file_id"].removeprefix("sha256:"),
                "category": kind,
                "reason_selected": question,
                "existing_artifacts": ";".join(artifacts) or "NONE",
                "existing_processing_state": report["existing_processing_state"],
                "version_group": inv.get("version_relation") or "NONE",
                "physical_observation_count": observations.get(report["source_file_id"], 1),
                "expected_calibration_question": question,
                "protocol_sha256": protocol_sha,
            })
    fields = list(rows[0])
    with (OUT / "CALIBRATION_CASES.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)
    meta = {
        "frozen_at": datetime.now(timezone.utc).isoformat(),
        "protocol_version": "phase3-calibration-v1",
        "protocol_sha256": protocol_sha,
        "field_catalog_sha256": field_sha,
        "calibration_cases_sha256": digest(OUT / "CALIBRATION_CASES.csv"),
        "top_level_categories": 12,
        "concrete_calibration_units": 13,
        "active_report_identities": len(rows),
        "additional_duplicate_physical_observations": 1,
        "physical_source_observations": sum(int(r["physical_observation_count"]) for r in rows),
        "substantive_review_started": False,
    }
    (OUT / "CALIBRATION_PROTOCOL_FINGERPRINT.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
