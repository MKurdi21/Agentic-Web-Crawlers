"""Read-only Phase 4BE recovery gate after authorized checkpoint reconciliation."""
import hashlib
import importlib
import json
import msvcrt
import pathlib
import sys
from datetime import datetime,timezone

sys.dont_write_bytecode = True

here=pathlib.Path(__file__).resolve().parent
root=here.parents[1]
phase=root/'analysis'/'phase4be_freeze_repair_and_validation'
sys.path.insert(0,str(root/'analysis'/'phase4bc_supplement'/'recovery_protocol'))
import engine as e

def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p): return e.filehash(p)
def fail_if(condition,msg,errors):
    if condition: errors.append(msg)

def main():
    errors=[]
    receipt=read(here/'CHECKPOINT_RECONCILIATION_RECEIPT.json')
    auth=read(here/'AUTHORIZED_EXTERNAL_CHANGESET.json')
    state=read(phase/'RECOVERY_STATE.json')
    diagnostic=read(phase/'RECOVERY_LATEST_USAGE_BLOCKED_DIAGNOSTIC.json')
    journal=e.Engine(phase).journal()
    fail_if(not journal or journal[-1]['event_type']!='RECOVERY_PREFLIGHT_FAIL','JOURNAL_FRONTIER_CHANGED',errors)
    fail_if(state['last_event_sha256']!=journal[-1]['event_sha256'],'JOURNAL_STATE_ANCHOR_MISMATCH',errors)
    fail_if(state['last_committed_milestone']!='PREPARATION_SCIENCE_ROUTE_REPAIRS','DURABLE_MILESTONE_CHANGED',errors)
    last=phase/'milestone_receipts'/'PREPARATION_SCIENCE_ROUTE_REPAIRS.json'
    fail_if(not last.is_file() or sha(last)!=state['last_committed_milestone_receipt_sha256'],'LAST_COMMIT_RECEIPT_MISMATCH',errors)
    fail_if(state['last_committed_milestone_receipt_sha256']!=diagnostic['last_committed_receipt_sha256'],'LAST_RECEIPT_DIAGNOSTIC_MISMATCH',errors)
    fail_if(any(x['event_type']=='ATOMIC_UNIT_COMMIT' and x.get('unit','').startswith('PREPARATION_CUTOVER_ROLLBACK_REPAIRS') for x in journal),'UNEXPECTED_CUTOVER_COMMIT',errors)
    fail_if(any(x['event_type']=='SOURCE_ACCESS_BEGAN' for x in journal),'SOURCE_ACCESS_EVENT_FOUND',errors)
    for unit in ('PREPARATION_CUTOVER_ROLLBACK_REPAIRS','PREPARATION_CUTOVER_ROLLBACK_REPAIRS_RESTART','PREPARATION_CUTOVER_ROLLBACK_REPAIRS_CLEAN'):
        fail_if((phase/'milestone_receipts'/f'{unit}.json').exists(),f'UNEXPECTED_COMMIT_RECEIPT:{unit}',errors)
    abort=read(phase/'PREPARATION_CUTOVER_ROLLBACK_REPAIRS_CLEAN_ABORT_RECEIPT.json')
    fail_if(abort.get('milestone_committed') is not False,'CLEAN_ABORT_NOT_DURABLE',errors)
    old_pid=abort['binding']['pid']
    old_start=abort['binding']['process_start']
    observed_old_start=e.process_start(old_pid)
    fail_if(observed_old_start==old_start,'OLD_LEASE_OWNER_STILL_ALIVE',errors)
    lock=phase/'coordinator.lock'
    with lock.open('r+b') as f:
        f.seek(0)
        try:
            msvcrt.locking(f.fileno(),msvcrt.LK_NBLCK,1)
        except OSError:
            errors.append('OS_COORDINATOR_LOCK_BUSY')
        else:
            f.seek(0)
            msvcrt.locking(f.fileno(),msvcrt.LK_UNLCK,1)
    run_lock=read(phase/'RUN_LOCK.json')
    fail_if(run_lock.get('status')=='HELD' and e.process_start(run_lock['pid'])==run_lock.get('process_start'),'ACTIVE_RUN_LOCK_OWNER',errors)
    baseline=read(phase/'PROTECTED_BASELINE_EXTENDED.json')['files']
    authorized={x['path']:x['new_sha256'] for x in auth['changes']}
    authorized.update(receipt['installed_corrected_hashes'])
    protected_drift=[]
    for i,x in enumerate(baseline,1):
        p=root/x['path']
        expected=authorized.get(x['path'],x['sha256'])
        if not p.is_file() or sha(p)!=expected or (x['path'] not in authorized and p.stat().st_size!=int(x['size'])):
            protected_drift.append(x['path'])
        if i%3000==0: print(f'protected_checked={i}',flush=True)
    fail_if(bool(protected_drift),'UNEXPLAINED_PROTECTED_DRIFT',errors)
    pins=read(phase/'PARENT_EXTERNAL_PINS.json')['files']
    pin_drift=[x['path'] for x in pins if not pathlib.Path(x['path']).is_file() or sha(x['path'])!=x['sha256']]
    fail_if(bool(pin_drift),'PARENT_EXTERNAL_PIN_DRIFT',errors)
    route=sha(phase/'execution_candidate'/'MODEL_ROUTING_POLICY.json')
    fail_if(route!='93dd05d1aeca6ac109385a781d50e37535d72d69fa975ddda89d92f470cef00a','ROUTING_POLICY_DRIFT',errors)
    order=read(phase/'execution_candidate'/'HOLDOUT_PROCESSING_ORDER.json')['order']
    holdout_checks={x['holdout_id']:{'expected':x['source_sha256'],'actual':sha(root/x['path'])} for x in order}
    fail_if(len(holdout_checks)!=7 or any(x['actual']!=x['expected'] for x in holdout_checks.values()),'HOLDOUT_HASH_DRIFT',errors)
    checkpoint=read(root/'analysis'/'checkpoint.json')
    fail_if(checkpoint['counts'].get('source_verified',0)!=0 or checkpoint['counts'].get('promoted',0)!=0,'SCIENTIFIC_STATUS_CHANGED',errors)
    fail_if(read(root/'analysis'/'reviews.json')!={},'LIVE_REVIEWS_NONEMPTY',errors)
    absent=['FREEZE_STATE.json','PREPARATION_COMPLETE_RECEIPT.json','FREEZE_RECEIPT.json','IMMUTABLE_MANIFEST.json','POST_FREEZE_EQUALITY_CHECK.json','PRE_B02_IMMUTABLE_EQUALITY_CHECK.json','STAGE_A_TO_B02_TRANSITION_RECEIPT.json','HOLDOUT_STATE_TRACKER.json','MODEL_ROUTING_LEDGER.jsonl']
    fail_if(any((phase/x).exists() for x in absent),'FREEZE_OR_STAGE_B_ARTIFACT_EXISTS',errors)
    fail_if(any((phase/x).exists() for x in ('control_state','freeze_state','runtime_state','rehearsal_runtime')),'LIVE_RUNTIME_EXISTS',errors)
    candidate_uncommitted=diagnostic['candidate_uncommitted_drift']
    fail_if(len(candidate_uncommitted)!=4 or any(not (phase/x).exists() for x in candidate_uncommitted),'UNCOMMITTED_CANDIDATE_EVIDENCE_CHANGED',errors)
    fail_if(state.get('source_access_started') is not False or state.get('reserved_untouched')!=7,'HOLDOUT_STATE_CHANGED',errors)
    fail_if(state['frozen_fingerprints']!=diagnostic['frozen_fingerprints'],'FROZEN_FINGERPRINT_RECORD_DRIFT',errors)
    result={'kind':'FRESH_PHASE4BE_RECOVERY_PREFLIGHT','observed_at_utc':datetime.now(timezone.utc).isoformat(),
            'verdict':'PASS' if not errors else 'RECOVERY_BLOCKED','blockers':errors,
            'authorized_phase4be_c_changes':authorized,'protected_count':len(baseline),'protected_unexplained_drift':protected_drift,
            'external_parent_pin_count':len(pins),'external_parent_pin_drift':pin_drift,
            'journal_event_count':len(journal),'journal_tail_sha256':journal[-1]['event_sha256'],
            'last_committed_milestone':state['last_committed_milestone'],'last_committed_receipt_sha256':sha(last),
            'interrupted_atomic_unit':diagnostic['interrupted_atomic_unit'],'interrupted_unit_state':'ABORTED_NO_COMMIT',
            'uncommitted_candidate_files':candidate_uncommitted,'old_lease_pid':old_pid,'old_lease_process_start':old_start,
            'observed_old_pid_process_start':observed_old_start,'run_lock_status':run_lock.get('status'),
            'routing_policy_sha256':route,'frozen_fingerprints':state['frozen_fingerprints'],
            'holdout_source_hash_checks':holdout_checks,'B02_B08_state':read(here/'B02_B08_ACCESS_AUDIT.json')['states'],
            'source_verified':checkpoint['counts'].get('source_verified',0),'promoted':checkpoint['counts'].get('promoted',0),
            'next_permitted_operation':'CLEAN_RESTART_PREPARATION_CUTOVER_ROLLBACK_REPAIRS; prior draft tests are non-authoritative; no enrollment, freeze, source access, or Lane B',
            'source_content_accessed':False}
    (here/'FRESH_PHASE4BE_RECOVERY_PREFLIGHT.json').write_text(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'verdict':result['verdict'],'protected_checked':len(baseline),'parent_pins_checked':len(pins),'journal_events':len(journal),'blockers':errors}),flush=True)
    if errors: raise SystemExit(2)

if __name__=='__main__': main()
