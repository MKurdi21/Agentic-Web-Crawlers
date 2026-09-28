"""Prospective administrative preparation intent; no actual execution enrollment."""
import sys,time,os
from pathlib import Path
sys.dont_write_bytecode=True
R=Path.cwd();O=R/'analysis/phase4be_freeze_repair_and_validation'
sys.path.insert(0,str(R/'analysis/phase4bc_supplement/recovery_protocol'))
import engine as e
with e.Engine(O).lock('/root/phase4be_preparation_writer_v2') as eng:
    state=e.read(O/'RECOVERY_STATE.json')
    assert state['lifecycle']=='PREPARATION_UNENROLLED_DRAFTS'
    assert state['last_committed_milestone']=='PREPARATION_TRANSITION_LANE_REPAIRS'
    assert not any((O/x).exists() for x in ['control_state','freeze_state','runtime_state'])
    snapshot=[]
    for p in sorted((O/'execution_candidate').rglob('*')):
        if p.is_file():
            data=p.read_bytes();rel=p.relative_to(O/'execution_candidate').as_posix()
            dest=O/'NEVER_PACKAGE/preparation_science_route_snapshot'/rel
            if dest.exists():assert dest.read_bytes()==data
            else:e.exclusive(dest,data)
            snapshot.append({'path':rel,'sha256':e.digest(data),'size':len(data)})
    for name in ['BEHAVIOR_FILE_INVENTORY.json','DEPENDENCY_CLOSURE.json']:
        dest=O/'NEVER_PACKAGE/preparation_science_route_snapshot'/name
        if dest.exists():assert dest.read_bytes()==(O/name).read_bytes()
        else:e.exclusive(dest,(O/name).read_bytes())
    intent={'kind':'PROSPECTIVE_PREPARATION_INTENT','timestamp':e.now(),'writer':'/root/phase4be_preparation_writer_v2','pid':os.getpid(),'process_start':e.process_start(os.getpid()),'scope':'bounded item projection/disposition consistency and frozen whole-report routing with invented tests; no actual enrollment/quiescence/freeze/source','bootstrap_receipt_sha256':state['last_committed_milestone_receipt_sha256'],'recovery_state_sha256':e.filehash(O/'RECOVERY_STATE.json'),'snapshot':snapshot,'pins':state['frozen_fingerprints'],'routing_policy_sha256':e.filehash(O/'execution_candidate/MODEL_ROUTING_POLICY.json'),'behavior_write_authority_count':1,'replay_policy':'REQUIRES_CLEAN_RESTART'}
    if (O/'PREPARATION_SCIENCE_ROUTE_INTENT.json').exists():
        original=e.read(O/'PREPARATION_SCIENCE_ROUTE_INTENT.json');assert original['snapshot']==snapshot
        intent={**intent,'previous_unstarted_intent_sha256':e.filehash(O/'PREPARATION_SCIENCE_ROUTE_INTENT.json'),'previous_failure':'SCHEMA_ENUM before journal; no behavior edits'}
        e.exclusive(O/'PREPARATION_SCIENCE_ROUTE_INTENT_RETRY.json',e.canonical(intent))
    else:e.exclusive(O/'PREPARATION_SCIENCE_ROUTE_INTENT.json',e.canonical(intent))
    eng.event('ATOMIC_UNIT_START',unit='PREPARATION_SCIENCE_ROUTE_REPAIRS',intent_sha256=e.filehash(O/'PREPARATION_SCIENCE_ROUTE_INTENT.json'),scientific_source_access=False)
    print('SOLE_WRITER_LEASE_HELD',flush=True)
    while not (O/'PREPARATION_SCIENCE_ROUTE_COMPLETION_REQUEST.json').exists():time.sleep(.5)
    request=e.read(O/'PREPARATION_SCIENCE_ROUTE_COMPLETION_REQUEST.json')
    assert all(e.filehash(O/path)==digest for path,digest in request['outputs'].items())
    assert e.filehash(O/'execution_candidate/MODEL_ROUTING_POLICY.json')==intent['routing_policy_sha256']
    receipt={'kind':'PROSPECTIVE_PREPARATION_COMMIT','atomic_unit_id':'PREPARATION_SCIENCE_ROUTE_REPAIRS','status':'COMMITTED_PREPARATION_ONLY','commit_time':e.now(),'intent_sha256':e.filehash(O/'PREPARATION_SCIENCE_ROUTE_INTENT.json'),'previous_receipt_sha256':state['last_committed_milestone_receipt_sha256'],'outputs':request['outputs'],'stage_a_pass':False,'freeze_committed':False,'scientific_source_access':False,'next_operation':'INDEPENDENT_REVIEW_OF_FINAL_PREPARATION_CANDIDATE_BEFORE_ENROLLMENT'}
    e.exclusive(O/'milestone_receipts/PREPARATION_SCIENCE_ROUTE_REPAIRS.json',e.canonical(receipt))
    event=eng.event('ATOMIC_UNIT_COMMIT',unit='PREPARATION_SCIENCE_ROUTE_REPAIRS',receipt_sha256=e.filehash(O/'milestone_receipts/PREPARATION_SCIENCE_ROUTE_REPAIRS.json'),stage_a_pass=False)
    state.update(last_committed_milestone='PREPARATION_SCIENCE_ROUTE_REPAIRS',last_committed_milestone_receipt_sha256=e.filehash(O/'milestone_receipts/PREPARATION_SCIENCE_ROUTE_REPAIRS.json'),last_event_sha256=event['event_sha256'],next_permitted_operation=receipt['next_operation'],updated_at=e.now())
    e.replace(O/'RECOVERY_STATE.json',state);eng.journal()
    print('PREPARATION_ONLY_COMMITTED',flush=True)
