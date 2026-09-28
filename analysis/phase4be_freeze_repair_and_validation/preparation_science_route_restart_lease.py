"""One clean-restart preparation lease; no enrollment, freeze, or source access."""
import os,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
R=Path.cwd();O=R/'analysis/phase4be_freeze_repair_and_validation'
sys.path.insert(0,str(R/'analysis/phase4bc_supplement/recovery_protocol'))
import engine as e
SESSION='/root/phase4be_science_recovery_writer'
with e.Engine(O).lock(SESSION) as eng:
    state=e.read(O/'RECOVERY_STATE.json')
    assert state['last_committed_milestone']=='PREPARATION_TRANSITION_LANE_REPAIRS'
    assert state['lifecycle']=='PREPARATION_UNENROLLED_DRAFTS'
    assert e.filehash(O/'execution_candidate/MODEL_ROUTING_POLICY.json')=='93dd05d1aeca6ac109385a781d50e37535d72d69fa975ddda89d92f470cef00a'
    assert not (O/'milestone_receipts/PREPARATION_SCIENCE_ROUTE_REPAIRS.json').exists()
    assert not any((O/x).exists() for x in ['control_state','freeze_state','runtime_state'])
    original=e.read(O/'PREPARATION_SCIENCE_ROUTE_INTENT.json')
    changed=[]
    for row in original['snapshot']:
        p=O/'execution_candidate'/row['path']
        current=e.filehash(p)
        if current!=row['sha256']:changed.append({'path':row['path'],'original_sha256':row['sha256'],'restart_sha256':current})
    intent={'kind':'CLEAN_RESTART_PROSPECTIVE_PREPARATION_INTENT','timestamp':e.now(),'session_id':SESSION,'pid':os.getpid(),'process_start':e.process_start(os.getpid()),'unit':'PREPARATION_SCIENCE_ROUTE_REPAIRS','previous_receipt_sha256':state['last_committed_milestone_receipt_sha256'],'recovery_state_sha256':e.filehash(O/'RECOVERY_STATE.json'),'second_preflight_sha256':e.filehash(O/'RECOVERY_SECOND_USAGE_PREFLIGHT.json'),'original_intent_sha256':e.filehash(O/'PREPARATION_SCIENCE_ROUTE_INTENT.json'),'original_addendum_sha256':e.filehash(O/'PREPARATION_SCIENCE_ROUTE_INTENT_ADDENDUM.json'),'uncommitted_attempt15_sha256':e.filehash(O/'DRAFT_SCIENCE_INTEGRITY_TEST_ATTEMPT15.json'),'changed_candidate_files':changed,'routing_policy_sha256':'93dd05d1aeca6ac109385a781d50e37535d72d69fa975ddda89d92f470cef00a','scope':'complete frozen model routing and item graph guards with synthetic tests; preparation only; no enrollment, quiescence, freeze or source access','replay_policy':'REQUIRES_CLEAN_RESTART'}
    e.exclusive(O/'PREPARATION_SCIENCE_ROUTE_RESTART_INTENT.json',e.canonical(intent))
    eng.event('ATOMIC_UNIT_START',unit='PREPARATION_SCIENCE_ROUTE_REPAIRS',clean_restart=True,intent_sha256=e.filehash(O/'PREPARATION_SCIENCE_ROUTE_RESTART_INTENT.json'),scientific_source_access=False)
    print('CLEAN_RESTART_LEASE_HELD',flush=True)
    request_path=O/'PREPARATION_SCIENCE_ROUTE_RESTART_COMPLETION_REQUEST.json'
    while not request_path.exists():time.sleep(.5)
    request=e.read(request_path)
    assert request['intent_sha256']==e.filehash(O/'PREPARATION_SCIENCE_ROUTE_RESTART_INTENT.json')
    assert request['previous_receipt_sha256']==state['last_committed_milestone_receipt_sha256']
    assert e.filehash(O/'execution_candidate/MODEL_ROUTING_POLICY.json')==intent['routing_policy_sha256']
    for path,digest in request['outputs'].items():
        assert path.startswith('NEVER_PACKAGE/immutable_preparation_versions/PREPARATION_SCIENCE_ROUTE_REPAIRS/')
        assert e.filehash(O/path)==digest
    receipt={'kind':'PROSPECTIVE_PREPARATION_COMMIT','atomic_unit_id':'PREPARATION_SCIENCE_ROUTE_REPAIRS','status':'COMMITTED_PREPARATION_ONLY','commit_time':e.now(),'intent_sha256':request['intent_sha256'],'previous_receipt_sha256':state['last_committed_milestone_receipt_sha256'],'outputs':request['outputs'],'working_views':request['working_views'],'test_results':request['test_results'],'stage_a_pass':False,'freeze_committed':False,'scientific_source_access':False,'next_operation':'INDEPENDENT_REVIEW_OF_FINAL_PREPARATION_CANDIDATE_BEFORE_ENROLLMENT'}
    receipt_path=O/'milestone_receipts/PREPARATION_SCIENCE_ROUTE_REPAIRS.json'
    e.exclusive(receipt_path,e.canonical(receipt))
    event=eng.event('ATOMIC_UNIT_COMMIT',unit='PREPARATION_SCIENCE_ROUTE_REPAIRS',receipt_sha256=e.filehash(receipt_path),stage_a_pass=False)
    state.update(last_committed_milestone='PREPARATION_SCIENCE_ROUTE_REPAIRS',last_committed_milestone_receipt_sha256=e.filehash(receipt_path),last_event_sha256=event['event_sha256'],next_permitted_operation=receipt['next_operation'],updated_at=e.now())
    e.replace(O/'RECOVERY_STATE.json',state);eng.journal()
    print('PREPARATION_ONLY_COMMITTED',flush=True)
