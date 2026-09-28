"""Bounded prospective preparation lease with session-bound abort."""
import os,secrets,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path.cwd();OUT=ROOT/'analysis/phase4be_freeze_repair_and_validation'
sys.path.insert(0,str(ROOT/'analysis/phase4bc_supplement/recovery_protocol'))
import engine as e

UNIT=sys.argv[1] if len(sys.argv)>1 else 'PREPARATION_CUTOVER_ROLLBACK_REPAIRS'
assert UNIT in ('PREPARATION_CUTOVER_ROLLBACK_REPAIRS','PREPARATION_CUTOVER_ROLLBACK_REPAIRS_RESTART','PREPARATION_CUTOVER_ROLLBACK_REPAIRS_CLEAN')
SESSION='/root/phase4be_rollback_repair_writer'

def main():
    with e.Engine(OUT).lock(SESSION) as eng:
        state=e.read(OUT/'RECOVERY_STATE.json')
        assert state['last_committed_milestone']=='PREPARATION_SCIENCE_ROUTE_REPAIRS'
        assert state['last_committed_milestone_receipt_sha256']=='e1878fac325638a51aef67907b4bf4711d231a7e67038e5f042fde22f84ee987'
        assert state['lifecycle']=='PREPARATION_UNENROLLED_DRAFTS'
        assert not (OUT/'milestone_receipts'/f'{UNIT}.json').exists()
        assert not any((OUT/x).exists() for x in ['control_state','freeze_state','runtime_state'])
        routing=e.filehash(OUT/'execution_candidate/MODEL_ROUTING_POLICY.json')
        assert routing=='93dd05d1aeca6ac109385a781d50e37535d72d69fa975ddda89d92f470cef00a'
        intent={'kind':'PROSPECTIVE_PREPARATION_INTENT','unit':UNIT,'session_id':SESSION,'run_id':state['run_id'],'pid':os.getpid(),'process_start':e.process_start(os.getpid()),'attempt_token':secrets.token_hex(24),'created_at':e.now(),'previous_receipt_sha256':state['last_committed_milestone_receipt_sha256'],'recovery_state_sha256':e.filehash(OUT/'RECOVERY_STATE.json'),'previous_event_sha256':state['last_event_sha256'],'routing_policy_sha256':routing,'scope':'private rehearsal paired rollback and fault recovery only; no enrollment, freeze, source or model access','replay_policy':'REQUIRES_CLEAN_RESTART'}
        intent_path=OUT/f'{UNIT}_INTENT.json';e.exclusive(intent_path,e.canonical(intent));intent_sha=e.filehash(intent_path)
        eng.event('ATOMIC_UNIT_START',unit=UNIT,intent_sha256=intent_sha,scientific_source_access=False)
        print('CUTOVER_REPAIR_LEASE_HELD',flush=True)
        request_path=OUT/f'{UNIT}_COMPLETION_REQUEST.json';abort_path=OUT/f'{UNIT}_ABORT_NO_COMMIT.json'
        binding={k:intent[k] for k in ['unit','session_id','run_id','pid','process_start','attempt_token']}
        binding['intent_sha256']=intent_sha
        while True:
            if abort_path.exists():
                try:abort=e.read(abort_path)
                except Exception:abort={}
                if all(abort.get(k)==v for k,v in binding.items()) and abort.get('operation')=='ABORT_NO_COMMIT':
                    diagnostic={'kind':'PREPARATION_ABORT_NO_COMMIT','unit':UNIT,'binding':binding,'reason':abort.get('reason','usage_preemption'),'timestamp':e.now(),'milestone_committed':False}
                    e.exclusive(OUT/f'{UNIT}_ABORT_RECEIPT.json',e.canonical(diagnostic))
                    eng.event('OTHER_INTERRUPTION',unit=UNIT,intent_sha256=intent_sha,abort_receipt_sha256=e.filehash(OUT/f'{UNIT}_ABORT_RECEIPT.json'),milestone_committed=False,reason=abort.get('reason','engineering_preparation_abort'))
                    eng.journal();print('ABORT_NO_COMMIT_RELEASED',flush=True);return
            if request_path.exists():break
            time.sleep(.25)
        request=e.read(request_path)
        assert request['intent_sha256']==intent_sha and request['previous_receipt_sha256']==intent['previous_receipt_sha256']
        assert e.filehash(OUT/'execution_candidate/MODEL_ROUTING_POLICY.json')==routing
        for path,digest in request['outputs'].items():
            assert path.startswith('NEVER_PACKAGE/immutable_preparation_versions/'+UNIT+'/')
            assert e.filehash(OUT/path)==digest
        receipt={'kind':'PROSPECTIVE_PREPARATION_COMMIT','atomic_unit_id':UNIT,'status':'COMMITTED_PREPARATION_ONLY','commit_time':e.now(),'intent_sha256':intent_sha,'previous_receipt_sha256':intent['previous_receipt_sha256'],'outputs':request['outputs'],'working_views':request['working_views'],'test_results':request['test_results'],'stage_a_pass':False,'freeze_committed':False,'scientific_source_access':False,'next_operation':'INDEPENDENT_REVIEW_OF_FINAL_PREPARATION_CANDIDATE_BEFORE_ENROLLMENT'}
        receipt_path=OUT/'milestone_receipts'/f'{UNIT}.json';e.exclusive(receipt_path,e.canonical(receipt))
        event=eng.event('ATOMIC_UNIT_COMMIT',unit=UNIT,receipt_sha256=e.filehash(receipt_path),stage_a_pass=False)
        state.update(last_committed_milestone=UNIT,last_committed_milestone_receipt_sha256=e.filehash(receipt_path),last_event_sha256=event['event_sha256'],next_permitted_operation=receipt['next_operation'],updated_at=e.now())
        e.replace(OUT/'RECOVERY_STATE.json',state);eng.journal();print('CUTOVER_REPAIR_PREPARATION_COMMITTED',flush=True)

if __name__=='__main__':main()
