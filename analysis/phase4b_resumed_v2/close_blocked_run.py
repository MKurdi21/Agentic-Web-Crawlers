"""Document pre-access NO_GO; never calls any source-delivery function."""
import csv,hashlib,json,sys,subprocess
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parents[1];S=R/'analysis/phase4bc_supplement'
sys.path.insert(0,str(S/'recovery_protocol'))
from engine import Engine,canonical,filehash
def read(n):return json.loads((O/n).read_text(encoding='utf-8'))
def put(n,x):(O/n).write_text(json.dumps(x,sort_keys=True,indent=2),encoding='utf-8')
def md(n,x):(O/n).write_text(x.strip()+'\n',encoding='utf-8')
e=Engine(O)
assert read('RESUMED_PHASE4B_BASELINE.json')['preservation_pass']
assert read('PREACCESS_INTERFACE_REVIEW.json')['status']=='BLOCKED'
with e.lock('/root'):
    existing=e.begin('PREACCESS_INTERFACE_GATE',{'review_sha256':filehash(O/'PREACCESS_INTERFACE_REVIEW.json')},['outputs/preaccess_gate.json'])
    if not existing.get('already_committed'):
        e.commit({'outputs/preaccess_gate.json':canonical(read('PREACCESS_INTERFACE_REVIEW.json'))},next_operation='CLOSE_NO_GO_WITHOUT_SOURCE_ACCESS')
tracker=read('HOLDOUT_STATE_TRACKER.json')
for x in tracker['reports']:
    x.update(state='NOT_RUN_EARLY_STOP',untouched_status='UNTOUCHED_RESERVED_VALIDATION_EVIDENCE',reason='PREACCESS_INFRASTRUCTURE_GATE_BLOCKED')
put('HOLDOUT_STATE_TRACKER.json',tracker)
put('HOLDOUT_CONTEXT_ISOLATION.json',{'primary_contexts_created':0,'verifier_scientific_contexts_created':0,'source_packets_delivered':0,'contamination_events':0,'technical_reviewer':'/root/resume_preaccess_review','technical_review_only':True,'status':'NOT_RUN_PREACCESS_GATE_BLOCKED','ambient_context_isolation_tested':False})
metrics={'reports_selected':7,'reports_opened':0,'reports_consumed':0,'reports_completed':0,'reports_not_run':7,'untouched_remaining':7,'field_slots':0,'evidence_items':0,'critical_items':0,'lower_risk_items':0,'verifier_disagreements':0,'critical_errors_detected':None,'critical_errors_left_accepted':0,'locator_failures':None,'comparative_failures':None,'derived_numeric_failures':None,'compound_claim_failures':None,'unresolved_critical_items':None,'contamination_events':0,'ground_truth_critical_false_accepts':'UNKNOWN','scientific_measurement_status':'NOT_RUN','null_reason':'No report opened; no scientific error/accuracy measurement exists','zero_count_scope':'Zero created records/accepted items, not proof of error-free workflow','early_stop_triggered':True,'early_stop_holdout_id':'B02','early_stop_stage':'PRE_ACCESS','early_stop_reason':'FROZEN_REAL_REPORT_CONTINUITY_INTEGRATION_UNAVAILABLE','lane_a2':'NOT_RUN_PREACCESS_GATE_BLOCKED','verification_mode':'NOT_RUN','human_source_review_performed':False,'human_source_review_item_count':0}
put('HOLDOUT_VALIDATION_METRICS.json',metrics)
(O/'HOLDOUT_DISAGREEMENTS.csv').write_text('holdout_id,item_id,primary_outcome,verifier_outcome,resolution\n',encoding='utf-8')
md('HOLDOUT_VALIDATION_REPORT.md','''# Resumed validation result

Lane A2: NOT_RUN_PREACCESS_GATE_BLOCKED. Overall: NO_GO.

B02 was the first scheduled report; no report was scientifically processed. Seven selected, zero opened/consumed/completed, seven untouched. No extraction, result inventory, primary or verifier source pass, sample selection, locator adjudication or scientific gate was executed. The empty disagreement table represents no observations, not agreement.

The frozen stack has a real-report preaccess helper and a generic context reconstruction contract, but lacks their integrated durable real-report acknowledgement, source-consumption and recovery path. The runnable continuity driver remains synthetic-only. Separate technical review confirmed the gap; see PREACCESS_INTERFACE_REVIEW.json. Building a new bridge would require explicit binding/transition/recovery tests before using untouched evidence. Neither synthetic identity relabeling nor direct low-level state manipulation was used.

No scientific claim is supported by this stop. It is an infrastructure failure, not SCIENTIFIC_METHOD_FAILURE or HOLDOUT_VALIDATION_FAIL on a paper. The prior readiness assessment proved synthetic mechanics but overstated operational real-report readiness; the prior handoff remains preserved, and this report corrects its interpretation.

Lane B: NOT_RUN_GATE_BLOCKED. No database, import, migration, backup, restore, rollback or cutover environment was created.''')
md('HOLDOUT_LIMITATIONS.md','''# Limitations

No scientific validation occurred. Critical error, locator, comparative and numeric error observations are null/NOT_RUN; zero accepted critical errors means no accepted artifacts exist, not that the workflow is accurate. Ground-truth critical false accepts remain UNKNOWN. No independent human source review occurred.

Only frozen code, metadata and streamed source hashes were inspected. Untouched-state assertions rely on recorded access and artifact inventory, not an OS-wide audit. Separate-context model technical review is not human scientific review. No packet semantic cleanliness result is claimed because operational source delivery failed its prerequisite gate.

All seven sources remain reserved. No methodology or prior phase was modified, and no new transport was inserted during validation. Future continuation requires resolving and testing the real-report integration outside scientific holdout execution, followed by a new pre-access check.''')
md('PHASE4B_READINESS.md','''# Readiness

NO_GO — FROZEN_REAL_REPORT_CONTINUITY_INTEGRATION_UNAVAILABLE.

The user has authorized validation; additional permission is not the missing element. A tested composition between real preaccess, exact packet acknowledgement, durable consumption and recovery is missing from the frozen executable path. Scientific methodology is unchanged and has not been tested in this run. All seven reports remain untouched. Lane B is NOT_RUN_GATE_BLOCKED; Phase 5 is not started.

This stop does not revoke preservation or the successful synthetic security tests of prior phases. It corrects the scope of their readiness interpretation. No silent refreeze, synthetic label substitution or low-level bypass was performed.''')
md('EXECUTIVE_RESUMED_PHASE4B_V2.md','''# Resumed Phase4B v2

NO_GO at B02 pre-access. Zero of seven reports consumed; seven remain untouched. Frozen code/source hashes and prior readiness metadata were checked, but separate technical review confirmed missing end-to-end real-report continuity integration. This is not a scientific validation failure.

No Lane B, migration, skills, checkpoint refresh or promotion. Final preservation and package checks are recorded separately; FINAL_HANDOFF.json references the external package receipt to avoid circular archive hashing.''')
hand={'phase':'RESUMED_PHASE4B_V2','classification':'NO_GO','reason':'FROZEN_REAL_REPORT_CONTINUITY_INTEGRATION_UNAVAILABLE','first_scheduled_report':'B02','first_processed_report':None,'lane_a2':'NOT_RUN_PREACCESS_GATE_BLOCKED','lane_b':'NOT_RUN_GATE_BLOCKED','holdout_metrics':metrics,'usage_limit_events_this_run':0,'recovery_events_this_run':0,'run_type':'NEW_RUN_AFTER_COMPLETED_PARENT','prior_phase_recovery_history_not_recounted':True,'frozen_pins':read('RESUMED_PHASE4B_BASELINE.json')['frozen_pins'],'migration_equivalence':'NOT_RUN','idempotency':'NOT_RUN','database_integrity':'NOT_RUN_NO_DATABASE','artifact_store_integrity':'NOT_RUN_NO_STORE','snapshot':'NOT_RUN','restore':'NOT_RUN','rollback':'NOT_RUN','cutover':'NOT_RUN','live_source_verified':0,'live_promoted':0,'independent_review':'SEPARATE_CONTEXT_READ_ONLY_TECHNICAL_REVIEW_CONFIRMED_BLOCKER','live_migration':False,'skills_installed':False,'live_promotion':False,'checkpoint_refreshed':False,'phase5_started':False,'package':{'path':'analysis/phase4b_resumed_v2_package.zip','sha256':None,'convention':'Archived handoff refers to external PACKAGE_RECEIPT.json; external handoff receives final archive hash after validation'},'preservation':'SEE_PRESERVATION_CHECK','stop':'No report opened. No next report or Lane B authorized by a failed gate.'}
put('FINAL_HANDOFF.json',hand)
print('NO_GO recorded; 0/7 consumed')
