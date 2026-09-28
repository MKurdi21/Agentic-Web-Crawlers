"""Write immutable preparation outputs and a completion request; no freeze or source access."""
import hashlib,json,sys
from pathlib import Path
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;EX=O/'execution_candidate'
sys.path.insert(0,str(O.parent/'phase4bc_supplement/recovery_protocol'))
import engine as e

def main():
    intent=e.read(O/'PREPARATION_SCIENCE_ROUTE_RESTART_INTENT.json')
    assert intent['unit']=='PREPARATION_SCIENCE_ROUTE_REPAIRS'
    assert e.filehash(EX/'MODEL_ROUTING_POLICY.json')==intent['routing_policy_sha256']
    state=e.read(O/'RECOVERY_STATE.json')
    assert state['last_committed_milestone']=='PREPARATION_TRANSITION_LANE_REPAIRS'
    assert not (O/'milestone_receipts/PREPARATION_SCIENCE_ROUTE_REPAIRS.json').exists()
    tests={
        'science':'DRAFT_SCIENCE_INTEGRITY_TEST_ATTEMPT18.json',
        'routing':'DRAFT_ROUTING_GUARD_TEST_ATTEMPT3.json',
        'freeze':'DRAFT_FREEZE_TEST_RESULTS_V6.json',
        'model_boundary':'DRAFT_MODEL_BOUNDARY_TEST_RESULTS_V5.json',
        'concurrency':'DRAFT_CONCURRENCY_STRESS_RESULTS_V4.json',
        'transition':'DRAFT_TRANSITION_LANE_TEST_ATTEMPT5.json',
        'copied_controller':'DRAFT_COPIED_CONTROLLER_TEST_RESULTS.json',
    }
    test_summary={}
    for label,name in tests.items():
        report=e.read(O/name)
        assert report['status']=='PASS',(label,report.get('status'))
        assert report.get('actual_model_calls',0)==0,(label,'MODEL_CALLS')
        test_summary[label]={'path':name,'sha256':e.filehash(O/name),'status':'PASS','passed_count':report.get('passed_count',report.get('attempt_count',report.get('metrics',{}).get('tests_run')))}
    assert test_summary['science']['passed_count']==83
    assert test_summary['routing']['passed_count']==29
    assert test_summary['freeze']['passed_count']==18
    assert test_summary['model_boundary']['passed_count']==8
    assert test_summary['concurrency']['passed_count']==13
    assert test_summary['transition']['passed_count']==31
    assert test_summary['copied_controller']['passed_count']==44
    science=e.read(O/tests['science']);current={p.name:e.filehash(p) for p in (EX/'orchestration').glob('*.py')}
    assert all(science['code_sha256'][name]==digest for name,digest in current.items()),'SCIENCE_TEST_NOT_CURRENT_BYTES'
    inventory=e.read(O/'BEHAVIOR_FILE_INVENTORY.json');candidate=sorted(p.relative_to(EX).as_posix() for p in EX.rglob('*') if p.is_file())
    assert inventory['expected_paths']==candidate==inventory['discovered_paths']
    assert not inventory['missing'] and not inventory['extra']
    deps=e.read(O/'DEPENDENCY_CLOSURE.json');assert deps['local_file_dependencies']==candidate
    assert all(not (O/name).exists() for name in ['control_state','freeze_state','runtime_state'])
    checkpoint={'kind':'PREPARATION_SCIENCE_ROUTE_CHECKPOINT','status':'CANDIDATE_TESTED_NOT_ENROLLED','run_id':state['run_id'],'stage':'STAGE_A','lifecycle':state['lifecycle'],'intent_sha256':e.filehash(O/'PREPARATION_SCIENCE_ROUTE_RESTART_INTENT.json'),'previous_receipt_sha256':state['last_committed_milestone_receipt_sha256'],'candidate_files':{p:e.filehash(EX/p) for p in candidate},'behavior_inventory_sha256':e.filehash(O/'BEHAVIOR_FILE_INVENTORY.json'),'dependency_closure_sha256':e.filehash(O/'DEPENDENCY_CLOSURE.json'),'frozen_routing_policy_sha256':intent['routing_policy_sha256'],'tests':test_summary,'historical_version_authority_count':71,'actual_model_calls':0,'reserved_pdf_parse_count':0,'actual_freeze':False,'actual_stage_b':False,'actual_lane_b':False,'live_source_verified':0,'live_promoted':0,'limitation':'D/F/H/I and nonstructural A require source-anchored first-pass semantic assessments; synthetic tests and graph syntax cannot prove their absence or establish scientific accuracy. Actual runtime independent review remains required before enrollment.'}
    e.exclusive(O/'PREPARATION_SCIENCE_ROUTE_CHECKPOINT.json',e.canonical(checkpoint))
    to_copy=[*('execution_candidate/'+p for p in candidate),'BEHAVIOR_FILE_INVENTORY.json','DEPENDENCY_CLOSURE.json','build_candidate_drafts.py','PREPARATION_SCIENCE_ROUTE_RESTART_INTENT.json','PREPARATION_SCIENCE_ROUTE_CHECKPOINT.json',*tests.values(),'finalize_science_route_candidate.py']
    prefix='NEVER_PACKAGE/immutable_preparation_versions/PREPARATION_SCIENCE_ROUTE_REPAIRS/'
    outputs={};views={};entries=[]
    for rel in sorted(set(to_copy)):
        data=(O/rel).read_bytes();digest=e.digest(data);immutable=prefix+rel
        e.exclusive(O/immutable,data)
        assert e.filehash(O/immutable)==digest
        outputs[immutable]=digest;views[rel]=digest
        entries.append({'working_view_path':rel,'immutable_artifact_path':immutable,'sha256':digest,'authority':'IMMUTABLE_VERSION_ARTIFACT','working_view_role':'DIAGNOSTIC_ONLY'})
    mapping={'kind':'PREPARATION_SCIENCE_ROUTE_VERSION_AUTHORITY','status':'VERIFIED','unit':'PREPARATION_SCIENCE_ROUTE_REPAIRS','previous_receipt_sha256':state['last_committed_milestone_receipt_sha256'],'entries':entries,'historical_prior_map_sha256':e.filehash(O/'PREPARATION_VERSION_AUTHORITY_MAP.json'),'historical_prior_count':71}
    map_rel='PREPARATION_SCIENCE_ROUTE_VERSION_AUTHORITY.json';e.exclusive(O/map_rel,e.canonical(mapping));map_bytes=(O/map_rel).read_bytes();map_dest=prefix+map_rel;e.exclusive(O/map_dest,map_bytes);outputs[map_dest]=e.digest(map_bytes);views[map_rel]=e.digest(map_bytes)
    assert all(e.filehash(O/path)==digest for path,digest in outputs.items())
    request={'kind':'PREPARATION_SCIENCE_ROUTE_RESTART_COMPLETION_REQUEST','intent_sha256':checkpoint['intent_sha256'],'previous_receipt_sha256':state['last_committed_milestone_receipt_sha256'],'outputs':outputs,'working_views':views,'test_results':test_summary,'version_authority_map_path':map_dest,'no_actual_freeze_or_source':True}
    e.exclusive(O/'PREPARATION_SCIENCE_ROUTE_RESTART_COMPLETION_REQUEST.json',e.canonical(request))
    print(json.dumps({'status':'IMMUTABLE_OUTPUTS_READY','output_count':len(outputs),'science_tests':test_summary['science']['passed_count'],'routing_tests':test_summary['routing']['passed_count'],'request_sha256':e.filehash(O/'PREPARATION_SCIENCE_ROUTE_RESTART_COMPLETION_REQUEST.json')}))

if __name__=='__main__':main()
