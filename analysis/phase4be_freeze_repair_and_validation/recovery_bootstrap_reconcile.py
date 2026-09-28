"""Prospective bootstrap reconciliation after full byte preflight, never backdated."""
import sys,os
from pathlib import Path
sys.dont_write_bytecode=True
R=Path.cwd();O=R/'analysis/phase4be_freeze_repair_and_validation'
sys.path.insert(0,str(R/'analysis/phase4bc_supplement/recovery_protocol'))
import engine as e
p=e.read(O/'RECOVERY_PREFLIGHT.json'); inv=e.read(O/'RECOVERY_PREFLIGHT_INVENTORY.json')
cfg=e.read(R/'analysis/phase4br_remediation/REMEDIATED_WORKFLOW_CONFIGURATION.json')
definition={k:cfg[k] for k in ['methodology_version','evidence_schema_version','parent_methodology_sha256','candidate_files','dependency_manifest_sha256','runtime_python']}
actual=e.digest(e.canonical(definition))
assert actual==cfg['methodology_sha256']=='ad691060099fff81a3e75de6d4ffdfeb4a8906e006dbfbeefc80a6c601f1d07f'
p['frozen_fingerprints']['methodology']=actual
p['all_six_fingerprints_pass']=True
p['aggregate_definitions']='Methodology exact six-key definition from freeze_and_evaluate.py and independent_equivalence.py (not full metadata configuration); other five definitions as recorded initial observation. Initial methodology mismatch was observer formula error, not protected drift.'
assert not p['protected_drift'] and not p['external_pin_failures']
assert p['all_six_fingerprints_pass'] and p['routing_pass'] and p['reviews_empty']
assert all(x['actual_sha256']==x['expected_sha256'] for x in p['source_hash_checks'])
assert not p['actual_authority_records_found'] and not p['lane_b_runtime_exists']
assert not (O/'RECOVERY_STATE.json').exists() and not (O/'GENESIS.json').exists()
# Reverify original draft and diagnostic inventory has remained stable throughout hashing.
assert all((O/x['path']).stat().st_size==x['size'] and e.filehash(O/x['path'])==x['sha256'] for x in inv['files'])
checkpoint=e.read(R/'analysis/checkpoint.json');counts=checkpoint['counts']
assert counts.get('source_verified',0)==0 and counts.get('promoted',0)==0
assert e.read(R/'analysis/reviews.json')=={}
nextop='COMPLETE_UNFINISHED_PREPARATION_DRAFT_IMPLEMENTATION_AND_DEPENDENCY_CLOSURE_UNDER_SINGLE_WRITER; establish prospective intent before edits, preserve snapshot; then latest-byte tests and independent review; no enrollment/quiescence/freeze/source yet'
report={**p,'timestamp':e.now(),'recovery_verdict':'RECOVERY_PREFLIGHT_PASS','blockers':[],'supersedes_observational_attempt_sha256':e.filehash(O/'RECOVERY_PREFLIGHT.json'),'bootstrap_basis':'Inherited phase4bc_supplement/recover_bootstrap.py explicitly supports preprotocol uncommitted-output reconciliation. No initialized actual run found; absence is uninitialized preparation, not receipt-chain recovery. New reconciliation commits now and never certifies historic preparation.','historical_last_committed_atomic_unit':'NONE','current_committed_unit':'BOOTSTRAP_RECONCILIATION only; administrative not Stage A','next_permitted_operation':nextop,'live_source_verified':0,'live_promoted':0,'live_count_basis':'unchanged protected checkpoint exact counts and empty reviews; absent statuses default0 by summary_state state semantics','stage_a_pass':False,'freeze_committed':False,'reports_opened':0,'reports_consumed':0,'reports_untouched':7,'lane_b_executed':False,'actual_runtime_directories':{n:(O/n).exists() for n in ['rehearsal_runtime','runtime_state','control_state','freeze_state']},'source_access_limit':'No OS-wide historical access proof; all actual run artifacts inventoried with no source delivery/consumption/worker outputs; metadata/hash streaming only in recovery','protocol_limitation':'BOOTSTRAP_RECONCILIATION_V1 observational state; not an initialized Engine genesis. Next sole writer must use prospective intent/authority before any preparation mutation. Previous RECOVERY_PREFLIGHT_FAIL retained as conservative initial interpretation, superseded by inherited bootstrap reconciliation.'}
with e.Engine(O).lock('/root/phase4be_recovery_preflight') as eng:
    e.exclusive(O/'RECOVERY_BOOTSTRAP_PREFLIGHT.json',e.canonical(report))
    receipt={'run_id':'phase4be-bootstrap-recovery','atomic_unit_id':'BOOTSTRAP_RECONCILIATION','status':'COMMITTED_RECONCILIATION','commit_time':e.now(),'historical_completion_time':None,'previous_receipt_sha256':None,'input_fingerprints':{'inventory_sha256':e.filehash(O/'RECOVERY_PREFLIGHT_INVENTORY.json'),'initial_observation_sha256':e.filehash(O/'RECOVERY_PREFLIGHT.json')},'output_fingerprints':{'RECOVERY_BOOTSTRAP_PREFLIGHT.json':e.filehash(O/'RECOVERY_BOOTSTRAP_PREFLIGHT.json')},'scientific_source_access':False,'validation_consumption_effect':0,'stage_a_pass':False,'next_operation':nextop}
    e.exclusive(O/'milestone_receipts/BOOTSTRAP_RECONCILIATION.json',e.canonical(receipt))
    event=eng.event('RECOVERY_PREFLIGHT_PASS',verdict='RECOVERY_PREFLIGHT_PASS',run_id=receipt['run_id'],receipt_sha256=e.filehash(O/'milestone_receipts/BOOTSTRAP_RECONCILIATION.json'),previous_historical_milestone=None,replayed_operations=[],next_permitted_operation=nextop)
    state={'run_id':receipt['run_id'],'phase_id':'PHASE4BE','protocol_version':'BOOTSTRAP_RECONCILIATION_V1','status':'RECOVERABLE','current_stage':'STAGE_A','lifecycle':'PREPARATION_UNENROLLED_DRAFTS','historical_last_committed_atomic_unit':None,'last_committed_milestone':'BOOTSTRAP_RECONCILIATION','last_committed_milestone_receipt_sha256':e.filehash(O/'milestone_receipts/BOOTSTRAP_RECONCILIATION.json'),'last_event_sha256':event['event_sha256'],'next_permitted_operation':nextop,'source_access_started':False,'reserved_untouched':7,'frozen_fingerprints':p['frozen_fingerprints'],'updated_at':e.now()}
    e.exclusive(O/'RECOVERY_STATE.json',e.canonical(state));eng.journal()
print('RECOVERY_PREFLIGHT_PASS; historical frontier NONE; current-only BOOTSTRAP_RECONCILIATION. '+nextop)
