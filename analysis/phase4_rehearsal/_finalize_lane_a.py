"""Finalize a failed Phase 4 holdout gate without entering Lane B."""
from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
HOLDOUT = ROOT / "holdout_validation"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(name: str, value):
    (ROOT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_md(name: str, value: str):
    (ROOT / name).write_text(value.strip() + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


now = datetime.now(timezone.utc).isoformat()
baseline = read_json(ROOT / "PHASE4_BASELINE.json")
sample_path = ROOT / "HOLDOUT_VERIFICATION_SAMPLE_MANIFEST.json"
sample = read_json(sample_path)
sample_by_id = {x["holdout_id"]: x for x in sample["units"]}
va = read_json(HOLDOUT / "verifier_a" / "VERIFIER_A_SUMMARY.json")
vb = read_json(HOLDOUT / "verifier_b" / "VERIFIER_B_SUMMARY.json")

rows = []
disagreements = []
for holdout_id in (f"H{i:02d}" for i in range(1, 7)):
    primary_dir = HOLDOUT / ("primary_a" if holdout_id <= "H03" else "primary_b")
    verifier_dir = HOLDOUT / ("verifier_a" if holdout_id <= "H03" else "verifier_b")
    primary_path = next(primary_dir.glob(f"{holdout_id}*.json"))
    verifier_path = next(verifier_dir.glob(f"{holdout_id}*.json"))
    primary = read_json(primary_path)
    verifier = read_json(verifier_path)
    evidence = primary["evidence_items"]
    fields = primary.get("field_records", primary.get("fields"))
    critical = {x["stable_item_id"] for x in evidence if x["critical"]}
    lower = {x["stable_item_id"] for x in evidence if not x["critical"]}
    selected = set(sample_by_id[holdout_id]["selected_item_ids"])
    assert len(fields) == 44
    assert len(critical) + len(lower) == len(evidence)
    assert selected <= lower
    assert len(selected) == sample_by_id[holdout_id]["required_sample_size"]
    reviewed = verifier.get("item_outcomes", verifier.get("verified_evidence_items"))
    reviewed_ids = {x["stable_item_id"] for x in reviewed}
    assert critical | selected <= reviewed_ids
    assert verifier["verification_mode"] == "SEPARATE_CONTEXT_MODEL_VERIFICATION"
    assert verifier["human_source_review_performed"] is False
    rows.append({
        "holdout_id": holdout_id,
        "paper_id": primary["paper_id"],
        "field_slots": len(fields),
        "evidence_items": len(evidence),
        "critical_items": len(critical),
        "lower_risk_items": len(lower),
        "selected_lower_risk_items": len(selected),
        "verified_critical_items": len(critical & reviewed_ids),
        "verified_selected_lower_risk_items": len(selected & reviewed_ids),
        "primary_sha256": sha(primary_path),
        "verifier_sha256": sha(verifier_path),
    })
    by_id = {x["stable_item_id"]: x for x in reviewed}
    for item_id in verifier["critical_disagreement_item_ids"]:
        item = by_id[item_id]
        disagreements.append({
            "holdout_id": holdout_id,
            "stable_item_id": item_id,
            "stable_field_id": item["stable_field_id"],
            "primary_finding": item.get("primary_finding", ""),
            "verifier_finding": item["verifier_finding"],
            "error_codes": ";".join(item.get("error_codes", [item.get("error_code", "")])),
            "coordinator_disposition": "EXCLUDED_FROM_SUPPORTED; SOURCE_REVIEW_PENDING" if holdout_id not in ("H03", "H04") else "EXCLUDED_FROM_SUPPORTED; DECISIVE_SOURCE_CHECK_RECORDED",
            "source_note": item.get("source_note", item.get("note", "")),
        })

assert len(rows) == 6
assert sum(r["field_slots"] for r in rows) == 264
assert sum(r["evidence_items"] for r in rows) == 233
assert sum(r["critical_items"] for r in rows) == 209
assert sum(r["lower_risk_items"] for r in rows) == 24
assert sum(r["selected_lower_risk_items"] for r in rows) == 18
assert len(disagreements) == 43

with (ROOT / "HOLDOUT_DISAGREEMENTS.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(disagreements[0]))
    writer.writeheader()
    writer.writerows(disagreements)

totals_a = va["totals"]
totals_b = vb["totals"]
metrics = {
    "status": "HOLDOUT_VALIDATION_FAIL",
    "evidence_phase": "UNTOUCHED_HOLDOUT_CONSUMED_FOR_VALIDATION; FAILED_WORKFLOW_CHALLENGE",
    "generated_at": now,
    "verification_mode": "SEPARATE_CONTEXT_MODEL_VERIFICATION",
    "human_source_review_performed": False,
    "human_source_review_item_count": 0,
    "trusted_human_approval": "UNAVAILABLE",
    "ground_truth_critical_false_accepts": "UNKNOWN",
    "holdout_report_count": 6,
    "holdout_selection_sha256": baseline["phase3_artifact_checks"][3]["actual"],
    "sample_manifest_sha256": sha(sample_path),
    "per_report_denominators": rows,
    "field_slots_total": sum(r["field_slots"] for r in rows),
    "evidence_items_total": sum(r["evidence_items"] for r in rows),
    "critical_items_total": 209,
    "lower_risk_items_total": 24,
    "selected_lower_risk_items_total": 18,
    "critical_items_verified_by_separate_context_model": 209,
    "selected_lower_risk_items_verified_by_separate_context_model": 18,
    "critical_items_supported_by_verifier": totals_a["critical_items_supported"] + totals_b["critical_items_supported"],
    "critical_items_partial_by_verifier": totals_a["critical_items_partial"] + totals_b["critical_items_partial"],
    "critical_items_unresolved_by_verifier": totals_a["critical_items_unresolved"] + totals_b["critical_items_unresolved"],
    "critical_primary_verifier_disagreements": len(disagreements),
    "critical_errors_detected": totals_a["critical_errors_detected"] + totals_b["critical_errors_detected"],
    "critical_false_accepts_detected": totals_a["critical_false_accepts_detected"] + totals_b["critical_false_accepts_detected"],
    "critical_incorrect_items_detected": totals_a["critical_incorrect_items_detected"] + totals_b["critical_incorrect_items_detected"],
    "critical_unsupported_items_detected": totals_a["critical_unsupported_items_detected"] + totals_b["critical_unsupported_items_detected"],
    "critical_locator_failures_detected": totals_a["critical_locator_failures_detected"] + totals_b["critical_locator_failures_detected"],
    "critical_quantitative_errors_detected": totals_a["critical_quantitative_errors_detected"] + totals_b["critical_quantitative_errors_detected"],
    "critical_errors_left_scientifically_accepted": 0,
    "scientific_acceptance_granted": False,
    "coordinator_source_adjudication": "DECISIVE_H03_H04_NUMERIC_ERRORS_CONFIRMED; ALL_OTHER_DISAGREEMENTS_EXCLUDED_FROM_SUPPORTED_PENDING_SOURCE_ADJUDICATION",
    "lane_b_permitted": False,
    "limitations": [
        "No qualified independent human source review occurred.",
        "Separate-context model verification does not establish human-reviewed ground truth.",
        "The 43 item disagreements were not all independently source-adjudicated by the coordinator; they are excluded from supported conclusions.",
        "No full-corpus performance inference follows from six holdout reports.",
    ],
}
write_json("HOLDOUT_VALIDATION_METRICS.json", metrics)

write_md("HOLDOUT_VALIDATION_REPORT.md", f"""
# Phase 4 Lane A: holdout validation

**Result: `HOLDOUT_VALIDATION_FAIL`.** The frozen Phase 3 workflow was applied to six untouched reports. The primary pass produced 264 field slots and 233 evidence items. A separate-context Codex verifier reviewed all 209 critical items and the 18 items selected by the frozen lower-risk sample. This is model-based source verification, not independent human source review or trusted-human approval.

The verifier reported 43 critical primary/verifier disagreements, including 42 locator failures, two quantitative errors, and four detected primary false accepts under its strict classification. Two decisive quantitative findings were separately checked by the coordinator against the exact source representations:

- H03 VisualWebArena: the primary `results.quantitative` field labels **16.37%** “best overall”; the source's later Appendix B/Table 5 reports **19.78%** for GPT-4o and explicitly compares it with 16.37%. The 16.37% figure belongs to the main baseline table and requires that qualifier. See the private H03 exact-source page 8 and page 13 text snapshots; source SHA-256 and item ID are in `HOLDOUT_DISAGREEMENTS.csv`.
- H04 AgentDoS: the primary `results.negative` field says **three** of 20 agents yielded no reported vulnerability. Source Table 2 has **four** zero-vulnerability rows: Quivr, Owl, Bisheng, and Taskweaver, consistent with 16 affected agents. The page-15 locator also fails to establish that numeric claim. See the private H04 source-derived layout and Table 2.

The H06 qualitative result is marked `NOT_LOCATABLE` at its supplied page-27 locator. The remaining disagreements remain excluded from supported conclusions pending source adjudication; none is silently treated as supported. No critical error was granted scientific acceptance, and no live scientific state changed. The detected defects mean the frozen workflow did not pass this holdout challenge. Lane B is prohibited by the Phase 4 dependency gate.

No critical false acceptance can be claimed absent. The defensible finding is that **four primary critical false accepts were detected by separate-context model verification**, with the two numeric defects above independently checked by the coordinator. `ground_truth_critical_false_accepts` remains `UNKNOWN` because no qualified human-reviewed ground truth exists.

The methodology cannot now be tuned against these six reports while preserving their status as untouched validation evidence. Any corrected methodology needs a new version and a new untouched holdout for another independent challenge. See `HOLDOUT_VALIDATION_METRICS.json` for named denominators and per-report counts.
""")

write_md("HOLDOUT_LIMITATIONS.md", """
# Holdout limitations

This was a six-report challenge to a frozen workflow, not a statistically representative estimate for 112 reports. Verification used separate Codex contexts and source checks; there was no qualified independent human source review and no production trusted-human approval. Model agreement or disagreement is useful error evidence but is not human ground truth. The 43 disagreement items were excluded from supported conclusions; only the decisive numeric defects received additional coordinator source checks. A failed holdout is development evidence for the next methodology version, not permission to tune and reuse the same reports as an untouched test set.
""")

write_md("EXECUTIVE_PHASE4.md", """
# Phase 4 executive result

**`NO_GO`.** Lane A found critical errors in the frozen extraction and source-locator workflow. Separate-context model verification covered 209 critical and 18 sampled lower-risk evidence items across six reports; it detected four strict primary false accepts, including two coordinator-confirmed quantitative misstatements. No human-reviewed ground truth exists. Lane B was not started, so no import, database, cross-store backup, rollback, or cutover simulation occurred. Live scientific state remains isolated, with no Phase 4 promotion or skill installation. A versioned repair and a new untouched validation set are required before repeating workflow validation.
""")

write_md("PHASE4_READINESS.md", """
# Phase 4 readiness

| Dimension | Result | Basis |
|---|---|---|
| Holdout workflow validation | FAIL | Critical quantitative and locator defects under the frozen protocol |
| Migration equivalence | NOT_RUN_GATE_BLOCKED | Lane B requires Lane A pass or pass with limitations |
| Controller reliability | NOT_RUN_GATE_BLOCKED | No Phase 4 controller rehearsal |
| Cross-store backup/restore | NOT_RUN_GATE_BLOCKED | No runtime database or store created |
| Rollback and cutover simulation | NOT_RUN_GATE_BLOCKED | No authority simulation |
| Scientific governance | BLOCKED | No independent human holdout review; owner decisions unresolved |

Overall: **`NO_GO`**. `CONDITIONAL_READY_FOR_PHASE5_AUTHORIZATION` is unavailable because Lane A failed. This result does not authorize Phase 5 or live deployment.
""")

blocked = {
    "status": "NOT_RUN_GATE_BLOCKED",
    "blocker": "HOLDOUT_VALIDATION_FAIL",
    "lane_a_result": "HOLDOUT_VALIDATION_FAIL",
    "runtime_created": False,
    "database_created": False,
    "artifact_store_created": False,
    "backup_created": False,
    "live_migration_performed": False,
    "phase5_started": False,
}
write_json("LANE_B_BLOCKED.json", blocked)
write_md("LANE_B_REHEARSAL_REPORT.md", """
# Lane B rehearsal status

**Not run: blocked by `HOLDOUT_VALIDATION_FAIL`.** The ordered Phase 4 gate does not permit a fresh import, idempotency or replay tests, controller exercise, cross-store backup, independent restore, rollback, or cutover simulation after a mandatory Lane A failure. No Phase 4 runtime database, store, or backup was created. These technical claims remain untested in Phase 4 rather than passing by inheritance from earlier phases.
""")
write_md("CROSS_STORE_SNAPSHOT_PROTOCOL.md", """
# Cross-store snapshot protocol for a later authorized rehearsal

This protocol was specified but **not executed** because Lane A failed. A future rehearsal must quiesce all logical writes under the coordinator lock, wait for active acceptance transactions to finish, capture a monotonic event watermark and accepted-pointer/registry fingerprint, back up SQLite at that watermark, copy the exact registered artifact closure, then verify the database and closure share the same snapshot identity. Read-only status and artifact reads may continue. Task creation, claim, heartbeat, lease reaping, artifact/result acceptance, review or scientific acceptance, research-object decisions, and migration commits must be deferred during quiescence. The exact write-boundary implementation must be tested against acceptance committing before the watermark and attempting after quiescence starts. Restore and rollback must use one receipt-bound database and artifact closure; separate `PRAGMA integrity_check`, `PRAGMA foreign_key_check`, and artifact registry/hash reconciliation are mandatory.
""")
write_json("CROSS_STORE_SNAPSHOT_RECEIPT.json", {**blocked, "snapshot_id": None, "event_watermark": None, "database_backup_sha256": None, "artifact_closure_sha256": None})
write_json("ARTIFACT_CLOSURE_MANIFEST.json", {**blocked, "artifacts": [], "artifact_manifest_sha256": None})
write_md("CROSS_STORE_SNAPSHOT_TESTS.md", "# Cross-store snapshot tests\n\nNot run: Lane B blocked by failed holdout validation. Both concurrent-acceptance boundary scenarios, restoration, database checks, and store reconciliation remain required in a later attempt.\n")
(ROOT / "test_results").mkdir(exist_ok=True)
(ROOT / "test_results" / "CROSS_STORE_SNAPSHOT_TESTS.json").write_text(json.dumps({**blocked, "scenarios_run": 0}, indent=2) + "\n", encoding="utf-8")

write_md("PHASE4_POLICY_STATUS.md", """
# Owner policy status

No Phase 3 recommendation was treated as approval. Production storage and artifact-store location; backup and recovery ownership; trusted-human identity and authentication; verification thresholds; contribution adjudication; inclusion and synthesis eligibility; partial synthesis; taxonomy authority; gap scoring; external search; and long-term retention remain `UNDECIDED` or `BLOCKS_LIVE_CUTOVER` according to the Phase 3 decision packet. Lane B did not run, so policy-configured candidate behavior was not exercised. No production trusted-human channel was configured.
""")
write_md("PHASE5_CUTOVER_PROPOSAL.md", "# Phase 5 status\n\nNot eligible for authorization on this Phase 4 result. Repair and version the scientific workflow, select a new untouched holdout, repeat Lane A, and only then consider the non-destructive Lane B rehearsal. Phase 5 requires separate explicit owner authorization and cannot be inferred from this report.\n")

write_json("FINAL_HANDOFF.json", {
    "phase": 4,
    "result": "NO_GO",
    "lane_a": "HOLDOUT_VALIDATION_FAIL",
    "lane_b": "NOT_RUN_GATE_BLOCKED",
    "verification_mode": metrics["verification_mode"],
    "human_source_review_performed": False,
    "human_source_review_item_count": 0,
    "ground_truth_critical_false_accepts": "UNKNOWN",
    "critical_items_total": 209,
    "critical_items_supported_by_verifier": metrics["critical_items_supported_by_verifier"],
    "critical_items_partial_by_verifier": metrics["critical_items_partial_by_verifier"],
    "critical_items_unresolved_by_verifier": metrics["critical_items_unresolved_by_verifier"],
    "critical_false_accepts_detected": metrics["critical_false_accepts_detected"],
    "critical_primary_verifier_disagreements": 43,
    "critical_locator_failures_detected": metrics["critical_locator_failures_detected"],
    "critical_quantitative_errors_detected": 2,
    "live_migration_performed": False,
    "skill_installation_performed": False,
    "phase5_started": False,
    "next_dependency": "VERSIONED_WORKFLOW_REPAIR_AND_NEW_UNTOUCHED_HOLDOUT",
})

print(json.dumps({"rows": len(rows), "disagreements": len(disagreements), "metrics": metrics["status"], "lane_b": blocked["status"]}))
