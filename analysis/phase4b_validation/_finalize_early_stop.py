"""Record the B01 fail-closed gate and conserve the seven unopened holdouts."""
import csv
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
B01 = OUT / "holdout_validation/B01"
PRIVATE = B01 / "private"


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


verification = read(PRIVATE / "COMBINED_VERIFICATION_RESULTS.json")
verifier_metrics = read(B01 / "VERIFIER_METRICS.json")
validator = read(PRIVATE / "PRIMARY_SEMANTIC_VALIDATION.json")
primary = read(PRIVATE / "PRIMARY_STATUS.json")
sample = read(B01 / "VERIFICATION_SAMPLE_MANIFEST.json")
before = read(B01 / "IMMUTABLE_CHECK_BEFORE.json")
after = read(B01 / "IMMUTABLE_CHECK_AFTER.json")
ledger = read(OUT / "HOLDOUT_ACCESS_LEDGER.json")
assert len(ledger["reports"]) == 8
assert ledger["reports"][0]["holdout_id"] == "B01"
assert all(not row["substantive_access"] for row in ledger["reports"][1:])
assert verifier_metrics["coverage_passed"] and verifier_metrics["verified_item_count"] == 130
assert not validator["passed"] and validator["error_code"] == "COMPARATIVE_FALSE_SUPPORT"
assert before["candidate_frozen_equals_execution_copy"] and after["candidate_frozen_equals_execution_copy"]
assert primary["complete"] and primary["eligible_set_complete"]

items = verification["results"]
critical = [item for item in items if item["critical"]]
counts = Counter(item["verdict"] for item in critical)
false_accept_flags = sum(bool(item.get("detected_false_accept")) for item in critical)
locators_not_full = sum(
    item["locator_status"] not in {"ENTAILS", "EXACT", "ENTAILS_WITH_COMPETING_SOURCE", "ENTAILS_WITH_SOURCE_INCONSISTENCY"}
    for item in critical
)
assert len(critical) == 127 and false_accept_flags == 80
assert counts == {"PARTIALLY_SUPPORTED": 78, "AMBIGUOUS": 3, "SUPPORTED": 44, "CONTRADICTED": 2}

now = datetime.now(timezone.utc).isoformat()
reason = (
    "B01 did not produce a payload passing the frozen scientific validator "
    "(COMPARATIVE_FALSE_SUPPORT: TARGET_LOCATOR_MISMATCH). Separate-context model "
    "verification found 80 critical primary support decisions requiring correction or "
    "qualification, including incomplete support locators. The rejected candidate "
    "cannot meet the frozen per-report evidence/locator gate. No artifact was accepted."
)
gate = {
    "holdout_id": "B01",
    "evaluated_at": now,
    "result": "HOLDOUT_VALIDATION_FAIL",
    "mandatory_failure": True,
    "failure_reason": reason,
    "validation_layers": {"frozen_semantic_validator": "FAIL", "separate_context_model_verification_coverage": "PASS", "scientific_acceptance": "NONE"},
    "frozen_validator_error_code": validator["error_code"],
    "frozen_validator_error": validator["error"],
    "primary_fields_total": primary["fields_total"],
    "primary_evidence_items_total": primary["evidence_items_total"],
    "verified_items_total": len(items),
    "verified_critical_items": len(critical),
    "critical_verifier_verdicts": dict(counts),
    "critical_primary_support_decisions_flagged_by_model": false_accept_flags,
    "critical_locator_statuses_not_full_entailment": locators_not_full,
    "ground_truth_critical_false_accepts": "UNKNOWN",
    "qualified_independent_human_source_review": False,
    "coordinator_disposition": (
        "FAIL_CLOSED: preserve original candidate and model findings; do not reclassify "
        "partial, ambiguous, or contradicted items as supported; do not repair the "
        "frozen workflow using this holdout and continue validation."
    ),
    "candidate_code_changed": False,
    "lane_b": "NOT_RUN_GATE_BLOCKED",
}
write(B01 / "PER_REPORT_GATE.json", gate)

ledger["reports"][0]["state"] = "CONSUMED_VALIDATION_EVIDENCE"
ledger["reports"][0]["completed"] = True
ledger["reports"][0]["result"] = "HOLDOUT_VALIDATION_FAIL"
ledger["reports"][0]["completed_at"] = now
for row in ledger["reports"][1:]:
    row["state"] = "NOT_RUN_EARLY_STOP"
    row["completed"] = False
    row["consumed"] = False
    row["substantive_access"] = False
ledger["events"].append({"event": "MANDATORY_EARLY_STOP", "holdout_id": "B01", "at": now, "reason_code": validator["error_code"]})
write(OUT / "HOLDOUT_ACCESS_LEDGER.json", ledger)

metrics = {
    "schema_version": "phase4b-holdout-validation-metrics-v1",
    "lane_a2_result": "HOLDOUT_VALIDATION_FAIL",
    "verification_mode": "PRIMARY_MODEL_EXTRACTION_PLUS_SEPARATE_CONTEXT_MODEL_VERIFICATION",
    "human_source_review_performed": False,
    "human_source_review_item_count": 0,
    "holdout_total_selected": 8,
    "holdout_opened": 1,
    "holdout_completed": 1,
    "holdout_consumed": 1,
    "holdout_not_run": 7,
    "holdout_untouched_remaining": 7,
    "early_stop_triggered": True,
    "early_stop_holdout_id": "B01",
    "early_stop_reason": reason,
    "evaluated_report_denominator": 1,
    "selected_report_denominator": 8,
    "excluded_from_evaluated_denominator": [row["holdout_id"] for row in ledger["reports"][1:]],
    "field_slots_primary": primary["fields_total"],
    "evidence_items_primary": primary["evidence_items_total"],
    "evidence_items_verified": len(items),
    "critical_items_total": len(critical),
    "critical_items_supported_by_separate_context_model": counts["SUPPORTED"],
    "critical_items_partial": counts["PARTIALLY_SUPPORTED"],
    "critical_items_ambiguous": counts["AMBIGUOUS"],
    "critical_items_contradicted": counts["CONTRADICTED"],
    "critical_items_unresolved_or_not_fully_supported": len(critical) - counts["SUPPORTED"],
    "critical_primary_support_decisions_flagged_by_model": false_accept_flags,
    "critical_false_accepts_detected_by_model": false_accept_flags,
    "critical_errors_left_accepted": 0,
    "critical_locator_statuses_not_full_entailment": locators_not_full,
    "critical_quantitative_errors_flagged_by_model": sum(bool(item.get("quantitative_error")) for item in critical),
    "critical_comparative_errors_flagged_by_model": sum(bool(item.get("comparative_error")) for item in critical),
    "ground_truth_critical_false_accepts": "UNKNOWN",
    "frozen_semantic_validation": "FAIL",
    "candidate_artifacts_accepted": 0,
    "lower_risk_eligible": sample.get("eligible_lower_risk_count"),
    "lower_risk_sampled": sample.get("required_sample_size"),
    "verifier_context_count": verifier_metrics["verifier_context_count"],
    "notes": [
        "Model verification findings are not independently human-adjudicated ground truth.",
        "The zero accepted-error count reflects rejection of the whole candidate, not successful extraction.",
        "No Phase 4B metric estimates eight-report or corpus-level performance.",
    ],
}
write(OUT / "HOLDOUT_VALIDATION_METRICS.json", metrics)

with (OUT / "HOLDOUT_DISAGREEMENTS.csv").open("w", encoding="utf-8", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=["holdout_id", "stable_item_id", "critical", "model_verdict", "locator_status", "detected_primary_false_accept", "disposition"])
    writer.writeheader()
    for item in items:
        if item["verdict"] == "SUPPORTED" and not item.get("detected_false_accept"):
            continue
        writer.writerow({
            "holdout_id": "B01",
            "stable_item_id": item["stable_item_id"],
            "critical": str(item["critical"]).lower(),
            "model_verdict": item["verdict"],
            "locator_status": item["locator_status"],
            "detected_primary_false_accept": str(bool(item.get("detected_false_accept"))).lower(),
            "disposition": "FAIL_CLOSED_NOT_ACCEPTED",
        })

order = read(OUT / "PHASE4B_HOLDOUT_PROCESSING_ORDER.json")
report = f"""# Phase 4B holdout validation

**Lane A2: HOLDOUT_VALIDATION_FAIL.** The frozen per-report gate failed on B01, the first of eight selected reports. B02–B08 were not opened for scientific review; Lane B is `NOT_RUN_GATE_BLOCKED`.

B01 used 44 primary field slots and 131 candidate evidence items. The complete lower-risk set had four items and the frozen algorithm selected three. Three fresh separate-context model verifiers covered all 127 critical items and the three selected lower-risk items. They classified critical items as 44 supported, 78 partially supported, three ambiguous, and two contradicted. They flagged 80 critical primary support decisions for correction or qualification; 83 critical items were not fully supported by model verification. These are model findings, not independently human-adjudicated ground truth.

The unchanged scientific validator rejected the candidate payload with `{validator['error']}`. Earlier serialization errors and the original payload are retained privately. The paper itself contains unresolved conflicting tool totals and attack-success figures; neither was silently resolved. Because no valid candidate evidence artifact emerged under the frozen workflow, the coordinator failed the per-report gate and accepted nothing. Thus `critical_errors_left_accepted = 0` describes a fail-closed rejection, **not** successful scientific validation. `ground_truth_critical_false_accepts = UNKNOWN`.

The immutable candidate inputs matched their frozen manifest before and after B01; the pre-access whole-candidate check also passed. No methodology was tuned against B01. No qualified independent human source review occurred. B01 is consumed validation evidence. The seven later reports retain an untouched/not-run state pending any separately designed future protocol.

The actual source and verifier records remain under the private Phase 4B area. This report omits full source text and substantive excerpts so it can be packaged.
"""
(OUT / "HOLDOUT_VALIDATION_REPORT.md").write_text(report, encoding="utf-8")

conservation = f"""# Holdout conservation

- Selected: 8 in frozen B01–B08 order; consumed/opened/completed: **1** (B01).
- Early stop: **yes**, after the confirmed B01 mandatory failure.
- Not run and untouched: **7** (B02–B08). No substantive PDF opening, source excerpt generation, primary/verifier context, or scientific output for those reports occurred in Phase 4B.
- Lane B: `NOT_RUN_GATE_BLOCKED`. No rehearsal database, backup, rollback, or cutover simulation was created.
- The remaining reports' potential reuse was preserved as an evidence-status question; Phase 4B does not authorize or claim their future reuse.

The frozen order is recorded in `PHASE4B_HOLDOUT_PROCESSING_ORDER.json`. B01 substantive access and the early stop are recorded in `HOLDOUT_ACCESS_LEDGER.json`.
"""
(OUT / "HOLDOUT_CONSERVATION_REPORT.md").write_text(conservation, encoding="utf-8")
(OUT / "HOLDOUT_LIMITATIONS.md").write_text(
    "# Holdout limitations\n\nOnly B01 was evaluated; seven selected reports remain untouched. The result is a mandatory workflow failure, not an eight-report performance estimate. Verification used separate Codex contexts, not independent human source review. Detected model disagreements are not complete human ground truth. The frozen candidate payload failed semantic validation; no B01 artifact was accepted.\n", encoding="utf-8"
)

handoff = {
    "phase": "PHASE4B",
    "overall_classification": "NO_GO",
    "lane_a2": "HOLDOUT_VALIDATION_FAIL",
    "lane_b": "NOT_RUN_GATE_BLOCKED",
    "reason": reason,
    "methodology_version": "phase4r-scientific-v2.0.0",
    "methodology_sha256": "ab28253c49940db4cd28ba0ea224185c8f3b03289312dba3c64322a33d95f1bb",
    "holdout_execution": {
        "selected_count": 8,
        "frozen_order": [row["holdout_id"] for row in ledger["reports"]],
        "consumed_count": 1,
        "completed_count": 1,
        "untouched_remaining": 7,
        "early_stop_triggered": True,
        "early_stop_holdout_id": "B01",
        "early_stop_reason": reason,
    },
    "context_isolation": {
        "protocol_version": "phase4b-context-isolation-v1",
        "primary_fresh_contexts": 1,
        "verifier_fresh_contexts": 3,
        "contamination_events": [],
    },
    "candidate_integrity": {
        "immutable_manifest_sha256": read(OUT / "CANDIDATE_CODE_MANIFEST.json")["manifest_fingerprint"],
        "candidate_frozen_manifest_sha256": read(OUT / "CANDIDATE_CODE_MANIFEST.json")["manifest_fingerprint"],
        "candidate_execution_manifest_sha256": read(OUT / "CANDIDATE_CODE_MANIFEST.json")["manifest_fingerprint"],
        "immutable_equality_initial": True,
        "immutable_equality_final": True,
        "methodology_drift_detected": False,
    },
    "verification_mode": metrics["verification_mode"],
    "human_source_review_performed": False,
    "ground_truth_critical_false_accepts": "UNKNOWN",
    "critical_items_total_evaluated": len(critical),
    "critical_primary_support_decisions_flagged_by_model": false_accept_flags,
    "critical_errors_left_accepted": 0,
    "live_migration_performed": False,
    "skill_installation_performed": False,
    "scientific_promotion_performed": False,
    "lane_b_execution_artifacts": "ABSENT_NOT_RUN",
    "package": "PENDING",
    "preservation": "PENDING_FINAL_CHECK",
}
write(OUT / "FINAL_HANDOFF.json", handoff)
(OUT / "EXECUTIVE_PHASE4B.md").write_text(
    "# Phase 4B executive result\n\n**NO_GO.** The first frozen holdout report failed the scientific workflow gate. One of eight reports was consumed; seven remain untouched. The frozen validator rejected the candidate payload and separate-context model verification found substantial support/locator defects. No evidence artifact was accepted. Lane B was not started. No live migration, scientific promotion, checkpoint refresh, or skill installation occurred.\n", encoding="utf-8"
)
(OUT / "PHASE4B_READINESS.md").write_text(
    "# Phase 4B readiness\n\nOverall: `NO_GO`. Lane A2: `HOLDOUT_VALIDATION_FAIL`. Lane B: `NOT_RUN_GATE_BLOCKED`. AI-only verification is not independent human scientific review. The holdout result prevents a Phase 5 authorization recommendation; owner-policy statuses were not advanced. Corrective work, if authorized later, requires a new versioned methodology and an untouched validation design.\n", encoding="utf-8"
)
(OUT / "PHASE5_CUTOVER_PROPOSAL.md").write_text(
    "# Phase 5 cutover disposition\n\nNo Phase 5 cutover is proposed from this run. Lane A2 failed on B01 and Lane B was not run. Phase 5 remains separately authorized; the seven unopened reports are reserved pending a future protocol.\n", encoding="utf-8"
)
(OUT / "PHASE4B_POLICY_STATUS.md").write_text(
    "# Policy status\n\nPhase 4B made no owner or trusted-human decisions. Prior unresolved production governance decisions remain unresolved. The scientific failure blocks Lane B independently of those decisions.\n", encoding="utf-8"
)
print(json.dumps({"lane_a2": gate["result"], "consumed": 1, "untouched": 7, "critical": len(critical), "critical_model_flagged": false_accept_flags}))
