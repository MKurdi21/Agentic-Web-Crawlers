"""Bind the completed preflight to an explicit owner-reclaim receipt."""
import sys
from pathlib import Path
sys.dont_write_bytecode=True
root=Path(__file__).resolve().parents[2]
here=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'analysis/phase4bc_supplement/recovery_protocol'))
import engine as e
with e.Engine(here).lock('/root/phase4be_recovery_preflight_2') as eng:
    events=eng.journal()
    assert len(events)==9 and events[-1]['event_type']=='RECOVERY_PREFLIGHT_PASS'
    report=e.read(here/'RECOVERY_SECOND_USAGE_PREFLIGHT.json')
    assert events[-1]['preflight_sha256']==e.filehash(here/'RECOVERY_SECOND_USAGE_PREFLIGHT.json')
    assert report['verdict']=='RECOVERY_PREFLIGHT_PASS'
    diagnostics=list((here/'lock_diagnostics').glob('*.json'))
    matches=[]
    for path in diagnostics:
        item=e.read(path)
        if item.get('old',{}).get('pid')==9356 and item.get('old',{}).get('process_start')=='134350177213069765' and item.get('observed_start') is None:
            matches.append(path)
    assert len(matches)==1
    assert e.process_start(9356) is None
    assert not (here/'PREPARATION_SCIENCE_ROUTE_COMPLETION_REQUEST.json').exists()
    assert not (here/'milestone_receipts/PREPARATION_SCIENCE_ROUTE_REPAIRS.json').exists()
    receipt={'kind':'RECOVERY_PREFLIGHT_RECEIPT','request_id':report['request_id'],'created_at':e.now(),'status':'RECOVERY_PREFLIGHT_PASS','preflight_sha256':e.filehash(here/'RECOVERY_SECOND_USAGE_PREFLIGHT.json'),'pass_event_sha256':events[-1]['event_sha256'],'last_committed_milestone':report['last_committed_milestone'],'last_committed_receipt_sha256':e.read(here/'RECOVERY_STATE.json')['last_committed_milestone_receipt_sha256'],'interrupted_atomic_unit':report['interrupted_atomic_unit'],'previous_worker_pid':9356,'previous_worker_process_start':'134350177213069765','previous_worker_command':'python -B analysis/phase4be_freeze_repair_and_validation/preparation_science_route_lease.py','lease_script_sha256':'70eed63687c8e5e4a138ed35f8c8ee3c7ed9066f84134b35d4c55ce9e54770e4','old_owner_release':'FORCED_PREEMPTION_AFTER_FAILED_GRACEFUL_INTERRUPT','old_owner_exit_verified':True,'os_lock_reclaim':'EXCLUSIVE_LOCK_GRANTED_AFTER_OWNER_EXIT_AND_PROCESS_START_CHECK','lock_diagnostic_path':str(matches[0].relative_to(here)).replace('\\','/'),'lock_diagnostic_sha256':e.filehash(matches[0]),'operations_replayed':[],'duplicate_effects_detected':[],'next_permitted_operation':report['next_permitted_operation'],'no_third_unit_commit':True,'no_freeze_or_source_access':True}
    path=here/'milestone_receipts/RECOVERY_SECOND_USAGE_PREFLIGHT.json'
    if path.exists():
        existing=e.read(path)
        assert all(existing[k]==receipt[k] for k in receipt if k!='created_at')
    else:e.exclusive(path,e.canonical(receipt))
    event=eng.event('MILESTONE_RECOVERED',request_id=receipt['request_id'],forced_preemption=True,receipt_sha256=e.filehash(path),old_owner_pid=9356,old_owner_process_start=receipt['previous_worker_process_start'],os_lock_reclaim=receipt['os_lock_reclaim'],next_permitted_operation=receipt['next_permitted_operation'])
    state=e.read(here/'RECOVERY_STATE.json')
    assert state['last_event_sha256']==events[-1]['event_sha256']
    state['last_event_sha256']=event['event_sha256'];state['updated_at']=e.now()
    e.replace(here/'RECOVERY_STATE.json',state)
    assert eng.journal()[-1]['event_sha256']==event['event_sha256']
    print('RECOVERY_RECEIPT_RECORDED',e.filehash(path))
