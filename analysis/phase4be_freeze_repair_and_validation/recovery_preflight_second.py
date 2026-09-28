"""One-shot, non-scientific recovery preflight for the second usage preemption."""
import hashlib, json, os, sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'analysis/phase4bc_supplement/recovery_protocol'))
import engine as e
sys.path.insert(0, str(HERE))
from validate_preparation_versions import validate

def check(condition, message):
    if not condition: raise RuntimeError(message)

def sha(path): return e.filehash(path)

def main():
    with e.Engine(HERE).lock('/root/phase4be_recovery_preflight_2') as eng:
        old = e.read(HERE/'RECOVERY_STATE.json')
        events = eng.journal()
        check(len(events)==8 and events[-1]['event_type']=='ATOMIC_UNIT_START' and events[-1]['unit']=='PREPARATION_SCIENCE_ROUTE_REPAIRS', 'FRONTIER_CHANGED')
        check(old['last_event_sha256']==events[-2]['event_sha256'], 'STATE_PROJECTION_CHANGED')
        check(old['last_committed_milestone']=='PREPARATION_TRANSITION_LANE_REPAIRS', 'LAST_COMMIT_CHANGED')
        receipts={x:e.read(HERE/'milestone_receipts'/f'{x}.json') for x in ('BOOTSTRAP_RECONCILIATION','PREPARATION_INTEGRITY_REPAIRS','PREPARATION_TRANSITION_LANE_REPAIRS')}
        check(sha(HERE/'milestone_receipts/PREPARATION_TRANSITION_LANE_REPAIRS.json')==old['last_committed_milestone_receipt_sha256']==events[-2]['receipt_sha256'], 'LAST_RECEIPT_CHANGED')
        check(receipts['PREPARATION_INTEGRITY_REPAIRS']['previous_receipt_sha256']==sha(HERE/'milestone_receipts/BOOTSTRAP_RECONCILIATION.json'), 'RECEIPT_CHAIN_1')
        check(receipts['PREPARATION_TRANSITION_LANE_REPAIRS']['previous_receipt_sha256']==sha(HERE/'milestone_receipts/PREPARATION_INTEGRITY_REPAIRS.json'), 'RECEIPT_CHAIN_2')
        check(events[4]['receipt_sha256']==sha(HERE/'milestone_receipts/PREPARATION_INTEGRITY_REPAIRS.json'), 'EVENT_RECEIPT_1')
        check(not (HERE/'milestone_receipts/PREPARATION_SCIENCE_ROUTE_REPAIRS.json').exists(), 'THIRD_UNIT_ALREADY_COMMITTED')
        intent=e.read(HERE/'PREPARATION_SCIENCE_ROUTE_INTENT.json'); addendum=e.read(HERE/'PREPARATION_SCIENCE_ROUTE_INTENT_ADDENDUM.json')
        check(sha(HERE/'PREPARATION_SCIENCE_ROUTE_INTENT.json')==events[-1]['intent_sha256']==addendum['prior_intent_sha256'], 'THIRD_INTENT_CHANGED')
        check(intent['replay_policy']=='REQUIRES_CLEAN_RESTART' and intent['bootstrap_receipt_sha256']==old['last_committed_milestone_receipt_sha256'], 'THIRD_REPLAY_POLICY')
        versions=validate(HERE)
        check(sha(HERE/'milestone_receipts/PREPARATION_VERSION_AUTHORITY_RECONCILIATION.json')==addendum['reconciliation_receipt_sha256'], 'VERSION_RECONCILIATION_CHANGED')
        check(versions['verified_count']==71, 'VERSION_COUNT')

        external=e.read(HERE/'PARENT_EXTERNAL_PINS.json')['files']
        external_bad=[x['path'] for x in external if not Path(x['path']).is_file() or sha(x['path'])!=x['sha256']]
        check(not external_bad, 'EXTERNAL_PIN_DRIFT '+str(external_bad[:3]))
        protected=e.read(HERE/'PROTECTED_BASELINE_EXTENDED.json')['files']
        protected_bad=[]
        for x in protected:
            p=ROOT/x['path']
            if not p.is_file() or p.stat().st_size!=int(x['size']) or sha(p)!=x['sha256']: protected_bad.append(x['path'])
        check(len(protected)==17245 and not protected_bad, 'PROTECTED_DRIFT '+str(protected_bad[:3]))
        cfg=e.read(ROOT/'analysis/phase4br_remediation/REMEDIATED_WORKFLOW_CONFIGURATION.json')
        definition={k:cfg[k] for k in ('methodology_version','evidence_schema_version','parent_methodology_sha256','candidate_files','dependency_manifest_sha256','runtime_python')}
        check(e.digest(e.canonical(definition))==cfg['methodology_sha256']==old['frozen_fingerprints']['methodology'], 'METHODOLOGY_DRIFT')
        check(intent['pins']==old['frozen_fingerprints'], 'PARENT_AGGREGATE_PIN_MISMATCH')
        check(len(old['frozen_fingerprints'])==6, 'SIX_PARENT_PINS')
        check(sha(HERE/'execution_candidate/MODEL_ROUTING_POLICY.json')==intent['routing_policy_sha256']=='93dd05d1aeca6ac109385a781d50e37535d72d69fa975ddda89d92f470cef00a', 'ROUTING_POLICY_DRIFT')
        order=e.read(HERE/'execution_candidate/HOLDOUT_PROCESSING_ORDER.json')['order']
        sources={x['holdout_id']:sha(ROOT/x['path']) for x in order}
        check(len(sources)==7 and all(sources[x['holdout_id']]==x['source_sha256'] for x in order), 'SOURCE_METADATA_HASH_DRIFT')
        check(e.read(ROOT/'analysis/reviews.json')=={}, 'LIVE_REVIEWS_NOT_EMPTY')
        checkpoint=e.read(ROOT/'analysis/checkpoint.json')
        check(checkpoint['counts'].get('source_verified',0)==0 and checkpoint['counts'].get('promoted',0)==0, 'LIVE_COUNTS_CHANGED')
        absent=('FREEZE_STATE.json','PREPARATION_COMPLETE_RECEIPT.json','FREEZE_RECEIPT.json','IMMUTABLE_MANIFEST.json','POST_FREEZE_EQUALITY_CHECK.json','PRE_B02_IMMUTABLE_EQUALITY_CHECK.json','STAGE_A_TO_B02_TRANSITION_RECEIPT.json','HOLDOUT_STATE_TRACKER.json','MODEL_ROUTING_LEDGER.jsonl')
        check(all(not (HERE/x).exists() for x in absent), 'ACTUAL_FREEZE_OR_STAGEB_EXISTS')
        check(not any((HERE/x).exists() for x in ('freeze','rehearsal_runtime','runtime_state','control_state')), 'ACTUAL_RUNTIME_EXISTS')
        check(not (HERE/'execution_candidate/registry').exists(), 'ACTUAL_REPORT_REGISTRY_EXISTS')
        test=e.read(HERE/'DRAFT_SCIENCE_INTEGRITY_TEST_ATTEMPT15.json')
        check(test['synthetic_transport_and_dispatch_only'] and test['actual_run_effects']==0 and test['reserved_pdf_parse_count']==0, 'TEST_SCOPE_CHANGED')
        candidate_changes=[]
        for x in intent['snapshot']:
            p=HERE/'execution_candidate'/x['path']
            if p.exists() and sha(p)!=x['sha256']: candidate_changes.append(x['path'])
        check(candidate_changes, 'NO_THIRD_UNIT_CHANGES_FOUND')
        nextop='CLEAN_RESTART_PREPARATION_SCIENCE_ROUTE_REPAIRS_UNDER_NEW_PROSPECTIVE_ATTEMPT; preserve original intent/addendum and uncommitted candidate/test evidence; reconcile each changed file, rerun current-byte private tests and independent review, then commit only after required receipt; no enrollment/quiescence/freeze/source'
        report={'kind':'SECOND_USAGE_LIMIT_RECOVERY_PREFLIGHT','request_id':'08b5aede-b26e-4dd3-841b-6f12573139e7','timestamp':e.now(),'reason':'PREEMPTED_BY_USAGE_LIMIT','run_id':old['run_id'],'previous_worker':'/root/phase4be_preparation_writer_v2','new_worker':'/root/phase4be_recovery_preflight_2','stage':'STAGE_A','lifecycle':'PREPARATION_UNENROLLED_DRAFTS','current_holdout':None,'last_committed_milestone':old['last_committed_milestone'],'interrupted_atomic_unit':'PREPARATION_SCIENCE_ROUTE_REPAIRS','interrupted_unit_state':'STARTED_UNCOMMITTED','replay_class':'REQUIRES_CLEAN_RESTART','next_permitted_operation':nextop,'verdict':'RECOVERY_PREFLIGHT_PASS','frozen_fingerprints':old['frozen_fingerprints'],'routing_policy_sha256':intent['routing_policy_sha256'],'historical_versions_verified':71,'protected_files_verified':len(protected),'external_parent_files_verified':len(external),'holdout_source_hashes':sources,'holdout_states':{x:'UNTOUCHED_RESERVED_VALIDATION_EVIDENCE' for x in sources},'live_source_verified':0,'live_promoted':0,'reviews_empty':True,'actual_freeze_committed':False,'actual_stage_b_started':False,'actual_lane_b_started':False,'candidate_files_changed_since_third_intent':candidate_changes,'latest_private_test':{'path':'DRAFT_SCIENCE_INTEGRITY_TEST_ATTEMPT15.json','sha256':sha(HERE/'DRAFT_SCIENCE_INTEGRITY_TEST_ATTEMPT15.json'),'scope':'SYNTHETIC_PRIVATE_DIAGNOSTIC_ONLY','status':test['status'],'passed_count':test['passed_count']},'partial_output_disposition':'UNCOMMITTED_DIAGNOSTIC_AND_CANDIDATE_BYTES_PRESERVED; REQUIRES_CLEAN_RESTART','operations_replayed':[],'duplicate_effects_detected':[],'quota':'UNKNOWN','tokens':'UNKNOWN','source_body_access':False,'lock_authority':'OS_EXCLUSIVE_LEASE_AND_PROCESS_START_LIVENESS_VERIFIED'}
        name='RECOVERY_SECOND_USAGE_PREFLIGHT.json'
        e.exclusive(HERE/name,e.canonical(report))
        event=eng.event('RECOVERY_PREFLIGHT_PASS',request_id=report['request_id'],reason=report['reason'],run_id=old['run_id'],previous_session_identity=report['previous_worker'],previous_durable_milestone=old['last_committed_milestone'],interrupted_atomic_unit=report['interrupted_atomic_unit'],current_stage='STAGE_A',current_holdout=None,frozen_fingerprints=old['frozen_fingerprints'],outputs_reconciled=report['partial_output_disposition'],operations_replayed=[],duplicate_effects_detected=[],quota='UNKNOWN',tokens='UNKNOWN',verdict='RECOVERY_PREFLIGHT_PASS',next_permitted_operation=nextop,preflight_sha256=sha(HERE/name))
        old['last_event_sha256']=event['event_sha256'];old['next_permitted_operation']=nextop;old['updated_at']=e.now()
        e.replace(HERE/'RECOVERY_STATE.json',old)
        check(eng.journal()[-1]['event_sha256']==event['event_sha256'], 'FINAL_EVENT_CHAIN')
        print(json.dumps({'verdict':report['verdict'],'last_committed':report['last_committed_milestone'],'interrupted':report['interrupted_atomic_unit'],'protected_verified':len(protected),'external_verified':len(external),'candidate_changed':len(candidate_changes),'next':nextop}))

if __name__=='__main__': main()
