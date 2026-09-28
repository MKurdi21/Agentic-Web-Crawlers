"""Failure diagnostics and conservation handoff; never releases sources."""
import sys,csv,json,hashlib,subprocess
from pathlib import Path
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;R=O.parents[1]
sys.path.insert(0,str(R/'analysis/phase4bd_real_source_continuity/integration_layer'))
import bridge as b
def put(n,x):b.exclusive(O/n,b.canonical(x))
def text(n,x):b.exclusive(O/n,x.encode('utf-8'))
manifest=b.read(O/'ORCHESTRATION_IMMUTABLE_MANIFEST.json')
paths=list((O/'orchestration').glob('*.py'))+list((O/'orchestration').glob('*.json'))+list((O/'orchestration').glob('*.md'))+list((O/'orchestration').glob('*.txt'))+[O/n for n in ['init_recovery.py','MODEL_ROUTING_POLICY.json','MODEL_ROUTING_WORKER_RULES.json']]
current={p.relative_to(O).as_posix():{'size_bytes':p.stat().st_size,'sha256':b.filehash(p)} for p in paths}
expected={x['relative_path']:{k:x[k] for k in ['size_bytes','sha256']} for x in manifest['files']}
delta={'extra_files':[{ 'relative_path':k,**current[k]} for k in sorted(current.keys()-expected.keys())],'missing_files':sorted(expected.keys()-current.keys()),'changed_files':[{'relative_path':k,'expected':expected[k],'observed':current[k]} for k in sorted(expected.keys()&current.keys()) if expected[k]!=current[k]],'frozen_manifest_sha256':b.filehash(O/'ORCHESTRATION_IMMUTABLE_MANIFEST.json'),'source_access_started':False,'verdict':'ORCHESTRATION_METHODOLOGY_DRIFT','scientific_methodology_changed':False,'re_freeze_performed':False}
assert delta['extra_files'] or delta['changed_files'] or delta['missing_files']
put('IMMUTABLE_GATE_FAILURE.json',delta)
rows=list(csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig',newline='')));drift=[]
for i,row in enumerate(rows):
 p=R/row['path']
 if not p.is_file():drift.append({'path':row['path'],'reason':'MISSING'})
 elif p.stat().st_size!=int(row['size']) or b.filehash(p)!=row['sha256']:drift.append({'path':row['path'],'reason':'CHANGED'})
 if i and i%4000==0:print('protected hashes checked',i,flush=True)
order=b.read(O/'HOLDOUT_PROCESSING_ORDER.json')['order']
reserved=[{'holdout_id':x['holdout_id'],'source_sha256':x['source_sha256'],'hash_match':b.filehash(R/x['path'])==x['source_sha256'],'substantive_access':False,'state':'UNTOUCHED_RESERVED_VALIDATION_EVIDENCE'} for x in order]
reviews=b.read(R/'analysis/reviews/source_reviews.json') if (R/'analysis/reviews/source_reviews.json').exists() else None
# Live scientific status was established from the protected read-only controls at baseline;
# identical bytes independently preserve that observation, without invoking state writers.
pres={'status':'PASS' if not drift and all(x['hash_match'] for x in reserved) else 'FAIL','protected_count':len(rows),'changed_count':len(drift),'drift':drift,'reserved':reserved,'live_source_verified':0,'live_promoted':0,'live_state_basis':'Baseline control observation plus independent final protected-byte equivalence','lane_b_runtime_created':(O/'rehearsal_runtime').exists(),'evidence_limit':'Recorded access and artifact inventory, not OS-wide access audit'}
put('PRESERVATION_CHECK.json',pres)
git=subprocess.run(['git','status','--porcelain=v1'],cwd=R,capture_output=True)
b.exclusive(O/'GIT_STATUS_FINAL.txt',git.stdout)
metrics={'reports_selected':7,'reports_opened':0,'reports_consumed':0,'reports_completed':0,'reports_not_run':7,'reports_remaining_untouched':7,'field_slots':0,'evidence_items':0,'critical_items':0,'lower_risk_items':0,'sol_only_items':0,'astra_reviewed_items':0,'astra_whole_report_escalations':0,'critical_astra_reviews':0,'lower_risk_astra_sample_count':0,'verifier_disagreements':0,'critical_errors_detected':0,'critical_errors_left_accepted':0,'locator_failures':0,'comparative_failures':0,'derived_numeric_failures':0,'compound_claim_failures':0,'unresolved_critical_items':0,'contamination_events':0,'recovery_events':0,'preemption_events':0,'ground_truth_critical_false_accepts':'UNKNOWN','scientific_validation_performed':False,'denominator_type':'No evaluated reports; all scientific item counts are inventory counts, not accuracy estimates','lane_a2':'NOT_RUN_PREACCESS_GATE_BLOCKED','lane_b':'NOT_RUN_GATE_BLOCKED','early_stop_triggered':True,'early_stop_holdout_id':None,'next_unopened_report':'B02','early_stop_reason':'ORCHESTRATION_METHODOLOGY_DRIFT','runtime_model_identity':'MODEL_RUNTIME_IDENTITY_UNVERIFIED','tokens':None,'cost':None}
put('HOLDOUT_VALIDATION_METRICS.json',metrics)
text('HOLDOUT_DISAGREEMENTS.csv','report_id,item_id,primary_status,verifier_status,adjudication\n')
text('HOLDOUT_VALIDATION_REPORT.md','# Holdout validation\n\nNOT_RUN_PREACCESS_GATE_BLOCKED. No scientific source was opened. The newly authored orchestration immutable manifest omitted a dispatch-template input added during concurrent preparation. Existing listed bytes and frozen parent scientific assets were not silently replaced. Validation stopped before B02; seven reports remain untouched. No extraction-accuracy claim or scientific-method failure is established.\n')
text('HOLDOUT_LIMITATIONS.md','# Limitations\n\nNo holdout scientific validation occurred. Zero scientific items inventoried is not zero-error evidence. Ground-truth critical false accepts remain UNKNOWN. Clean model packet reviews are technical context reviews, not human scientific approval. Source conservation conclusions cover recorded dispatch/access and artifact evidence, not an OS-wide audit. Requested model roles are not independently attested runtime identities.\n')
text('PHASE4B_READINESS.md','# Readiness\n\nNO_GO. Mandatory immutable-execution-input gate failed before source access. Lane A2 and Lane B were not run. No scientific methodology accuracy conclusion is available. A separately documented preparation correction and new pre-access gate would be required before any continuation; this run does not silently re-freeze its manifest. Phase 5 is not authorized.\n')
text('EXECUTIVE_PHASE4B_FINAL.md','# Phase 4B final execution\n\nNO_GO — pre-access orchestration integrity failure. Baseline and routing were committed; eight synthetic ACK-boundary checks passed. A concurrent dispatch-template addition was omitted from the immutable manifest. Stop occurred before any holdout science: selected 7, opened/consumed/completed 0, remaining untouched 7. Lane B not run. Frozen scientific methodology and parent transport remain unchanged.\n')
text('HOLDOUT_CONSERVATION_REPORT.md','# Conservation\n\nSeven selected reports B02–B08; zero opened, consumed or completed; seven untouched. Stop occurred before B02 due to engineering manifest inventory mismatch. No source excerpts, primary scientific contexts, scientific verifier contexts or extraction results were generated. Future reuse is not automatically approved.\n')
sys.path.insert(0,str(O/'orchestration'))
import run_control
run_control.commit('PREACCESS_GATE_FAILURE',[O/'IMMUTABLE_GATE_FAILURE.json',O/'HOLDOUT_VALIDATION_METRICS.json',O/'PRESERVATION_CHECK.json'],'STOP_NO_GO')
e=b.Engine(O/'durable_run')
with e.lock('failure-handoff'):
 e.receipts();e.journal();e.event('RECOVERY_PREFLIGHT_FAIL',reason='ORCHESTRATION_IMMUTABLE_INVENTORY_MISMATCH',previous_durable_milestone='BASELINE_AND_ROUTING',source_access_started=False,replayed_operations=[],quarantined_operations=[],verdict='NO_GO')
 s=e.state();s.update(status='RUN_FAILED',next_permitted_operation='STOP_NO_GO',lane_b_state='NOT_RUN_GATE_BLOCKED');e.save(s)
 b.replace(e.root/'BLOCKED_LATCH.json',{'active':True,'reason':'ORCHESTRATION_IMMUTABLE_INVENTORY_MISMATCH','timestamp':b.now()})
run_control.export()
handoff={'classification':'NO_GO','reason':'ORCHESTRATION_METHODOLOGY_DRIFT','failure_kind':'PREACCESS_ENGINEERING_INTEGRITY_FAILURE','scientific_validation_result':'NOT_RUN_PREACCESS_GATE_BLOCKED','lane_b':'NOT_RUN_GATE_BLOCKED','metrics':metrics,'preservation_status':pres['status'],'frozen_pins':b.read(O/'PHASE4B_FINAL_BASELINE.json')['frozen_pins'],'routing_policy_sha256':b.filehash(O/'MODEL_ROUTING_POLICY.json'),'immutable_manifest_sha256':delta['frozen_manifest_sha256'],'immutable_gate_failure':delta,'independent_review_status':'PENDING_FINAL_TECHNICAL_REVIEW','no_live_migration':True,'no_live_promotion':True,'no_skill_installation':True,'no_checkpoint_refresh':True,'package_receipt':'PACKAGE_RECEIPT.json external to archive','package_hash_convention':'Packaged handoff refers to external receipt; external final handoff receives archive SHA after creation','output_directory':str(O),'package_path':str(R/'analysis/phase4b_validation_final_package.zip')}
put('FINAL_HANDOFF.json',handoff)
print(json.dumps({'classification':'NO_GO','protected_count':len(rows),'drift_count':len(drift),'reserved_untouched':7,'immutable_delta':delta}),flush=True)
