import csv,hashlib,json,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;R=O.parents[1];C=O/'candidate_v4br'
sys.path.insert(0,str(C/'hardened/scripts'))
from validation_guard import verify_manifest
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
now=datetime.now(timezone.utc).isoformat()
cfg=read(O/'FROZEN_CONFIGURATION.json');frozen=cfg['candidate_files']
verify_manifest(C,frozen);verify_manifest(O/'candidate_frozen',frozen)
assert not (O/'holdout_validation/B02/SOURCE_ACCESS_BEGAN.json').exists()
assert not list((O/'holdout_validation').rglob('SOURCE_ACCESS_BEGAN.json'))
evidence=[]
for name,needles in [('FIELD_AUTOMATION_MATRIX_V2.csv',['H05 sampled','H04 zero-row','H03 global-best']),('DERIVED_NUMERIC_VERIFICATION.md',['actual H04']),('DOCUMENT_WIDE_COMPARATIVE_RECONCILIATION.md',['Phase 4 H03'])]:
 p=C/'frozen_inputs/phase4r'/name
 lines=p.read_text(encoding='utf-8').splitlines()
 evidence.append({'path':p.relative_to(O).as_posix(),'sha256':h(p),'line_numbers':[i for i,s in enumerate(lines,1) if any(t in s for t in needles)],'finding':'Earlier holdout findings or failure triggers embedded in dispatched frozen generic input'})
event={'event':'VALIDATION_CONTEXT_CONTAMINATION','detected_at':now,'holdout_id':'B02','context_id':'/root/resume_b02_primary','stage':'PRE_SOURCE_ACCESS_PROTOCOL_LOADING','source_opened':False,'classification':'MANDATORY_CONTEXT_ISOLATION_BLOCKER','basis':evidence,'agent_report':'Agent stopped before open_source; SOURCE_ACCESS_BEGAN absent. No source extraction or writes reported.','coordinator_confirmation':'Read frozen files and confirmed named earlier-holdout error findings. No reserved scientific source opened.','limitation':'Dispatched inputs and recorded operations support conservation; not an OS-wide access audit.'}
save(O/'CONTEXT_CONTAMINATION_LOG.json',{'events':[event]})
ledger=read(O/'HOLDOUT_ACCESS_LEDGER.json')
for r in ledger['reports']:
 r.update(state='NOT_RUN_EARLY_STOP',untouched_status='UNTOUCHED_RESERVED_VALIDATION_EVIDENCE',substantive_access=False,consumed=False,completed=False,result='NOT_RUN_PRE_ACCESS_CONTEXT_BLOCKER')
ledger.update(early_stop_triggered=True,early_stop_holdout_id='B02',early_stop_reason='VALIDATION_CONTEXT_CONTAMINATION',lane_b='NOT_RUN_GATE_BLOCKED')
save(O/'HOLDOUT_ACCESS_LEDGER.json',ledger)
packet=read(O/'holdout_validation/B02/PRIMARY_CONTEXT_PACKET.json')
isolation={'protocol_version':'fresh-current-report-only-v1','primary_fresh_contexts':1,'verifier_fresh_contexts':0,'scientific_verifier_passes':0,'contamination_events':[event],'records':[{'holdout_id':'B02','primary_context_id':'/root/resume_b02_primary','verifier_context_id_or_ids':[],'context_protocol_version':'fresh-current-report-only-v1','allowed_context_manifest_sha256':h(O/'holdout_validation/B02/PRIMARY_CONTEXT_PACKET.json'),'previous_holdout_scientific_content_included':True,'coordinator_summary_included':False,'frozen_protocol_hash':packet['frozen_protocol_hash'],'source_sha256':ledger['reports'][0]['source_sha256'],'packet_declaration_failed':True,'outcome':'NO_GO_BEFORE_SOURCE_ACCESS'}]}
save(O/'HOLDOUT_CONTEXT_ISOLATION.json',isolation)
counts=dict(holdout_total_selected=7,holdout_opened=0,holdout_completed=0,holdout_consumed=0,holdout_not_run=7,holdout_untouched_remaining=7,early_stop_triggered=True,early_stop_holdout_id='B02',early_stop_reason='VALIDATION_CONTEXT_CONTAMINATION_BEFORE_SOURCE_ACCESS')
metrics={**counts,'validation_type':'SEQUENTIAL_RESERVED_HOLDOUT_VALIDATION','original_phase4b_selected_count':8,'excluded_development_reports':['B01'],'verification_mode':'NOT_RUN','human_source_review_performed':False,'human_source_review_item_count':0,'structured_fields_evaluated':0,'evidence_items_evaluated':0,'critical_items_total':0,'critical_items_supported':0,'critical_items_partial':0,'critical_items_unresolved':0,'critical_errors_detected':0,'critical_false_accepts_detected':0,'critical_primary_verifier_disagreements':0,'critical_locator_failures_detected':0,'critical_quantitative_errors_detected':0,'critical_errors_left_accepted':0,'ground_truth_critical_false_accepts':'UNKNOWN','scientific_rates':'NOT_COMPUTABLE_NO_REPORTS_EVALUATED','lane_a2':'HOLDOUT_VALIDATION_FAIL','failure_scope':'PRE_ACCESS_CONTEXT_ISOLATION_NOT_PAPER_SCIENTIFIC_FAILURE','lane_b':'NOT_RUN_GATE_BLOCKED'}
save(O/'HOLDOUT_VALIDATION_METRICS.json',metrics)
save(O/'holdout_validation/B02/IMMUTABLE_AFTER.json',{'passed':True,'source_opened':False,'methodology_sha256':packet['frozen_protocol_hash'],'manifest_sha256':h(O/'CANDIDATE_CODE_MANIFEST.json')})
pres=[]
with (O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
for i,row in enumerate(rows,1):
 path=row.get('path',row.get('relative_path'));p=R/path
 observed=h(p) if p.is_file() else None
 if observed!=row['sha256']:pres.append({'path':path,'expected':row['sha256'],'observed':observed})
 if i%2000==0:print('Preservation verified',i,flush=True)
status=subprocess.run(['git','status','--porcelain=v1','--untracked-files=all'],cwd=R,capture_output=True,text=True,encoding='utf-8').stdout
(O/'GIT_STATUS_FINAL.txt').write_text(status,encoding='utf-8')
reviews=read(R/'analysis/reviews.json')
preservation={'checked_at':datetime.now(timezone.utc).isoformat(),'protected_file_count':len(rows),'changed_protected_files':pres,'passed':not pres,'live_review_records_empty':reviews=={},'live_source_verified':0 if reviews=={} else 'UNKNOWN','live_promoted':0 if reviews=={} else 'UNKNOWN','candidate_immutable_equality':True,'source_access_events':0,'new_rehearsal_database_count':len(list(O.rglob('*.sqlite')))+len(list(O.rglob('*.db'))),'limitations':['Filesystem hash comparison and recorded source-access evidence; no OS-wide audit.','No checkpoint refresh; zero starting scientific state remains supported by unchanged live controls and empty review records.']}
save(O/'PRESERVATION_CHECK.json',preservation)
handoff={'phase':'PHASE4B_RESUMED_VALIDATION','overall_result':'NO_GO','lane_a2':metrics['lane_a2'],'lane_a2_failure_scope':metrics['failure_scope'],'lane_b':'NOT_RUN_GATE_BLOCKED','mandatory_blockers':['VALIDATION_CONTEXT_CONTAMINATION_BEFORE_SOURCE_ACCESS'],**counts,'holdout_execution':{'selected_count':7,'frozen_order':[r['holdout_id'] for r in ledger['reports']],'consumed_count':0,'completed_count':0,'untouched_remaining':7,'early_stop_triggered':True,'early_stop_holdout_id':'B02','early_stop_reason':counts['early_stop_reason']},'context_isolation':isolation,'candidate_integrity':{'immutable_manifest_sha256':h(O/'CANDIDATE_CODE_MANIFEST.json'),'immutable_equality_initial':True,'immutable_equality_final':True,'methodology_drift_detected':False},'verification_mode':'NOT_RUN','ground_truth_critical_false_accepts':'UNKNOWN','live_source_verified':preservation['live_source_verified'],'live_promoted':preservation['live_promoted'],'preservation_passed':preservation['passed'],'no_live_migration':True,'no_skill_installation':True,'no_scientific_promotion':True,'independent_final_review':'PENDING','required_next_step':'Separate remediation/versioned packet design to remove historical findings from executable agent context; fresh contexts and revalidated access records before any future reserved-source use. No automatic reuse authorization.'}
save(O/'FINAL_HANDOFF.json',handoff)
print('Pre-access NO_GO recorded; 0/7 consumed; preservation',preservation['passed'])
