import csv,json,hashlib,sys,os
from pathlib import Path
from datetime import datetime,timezone
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;R=O.parents[1];BC=R/'analysis/phase4bc_context_isolation'
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def h(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,x):
 with p.open('xb') as f:f.write(canon(x));f.flush();os.fsync(f.fileno())
assert not (O/'RECOVERY_PREFLIGHT.json').exists()
existing=[p for p in O.rglob('*') if p.is_file() and p.name!='recover_bootstrap.py'];inventory=[{'path':p.relative_to(O).as_posix(),'sha256':h(p),'size':p.stat().st_size,'mtime_ns':p.stat().st_mtime_ns,'initial_status':'UNCOMMITTED_RECOVERY_MATERIAL'} for p in existing]
missing=[n for n in ['RECOVERY_STATE.json','RECOVERY_EVENTS.jsonl','RUN_LOCK.json','ACTIVE_OPERATION.json'] if not (O/n).exists()]
errors=[]
for p in existing:
 if p.suffix=='.json':read(p)
b=read(O/'PHASE4BC_S_BASELINE.json');assert b['passed']
rows=list(csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig')))
for i,x in enumerate(rows,1):
 p=R/x['path'];obs=h(p) if p.is_file() else None
 if obs!=x['sha256']:errors.append({'path':x['path'],'expected':x['sha256'],'observed':obs})
 if i%3000==0:print('Recovery protected checks',i,flush=True)
cfg=read(BC/'CONTEXT_PACKET_ARCHITECTURE_CONFIGURATION.json');pinned=cfg.pop('context_packet_architecture_sha256');assert hashlib.sha256(canon(cfg)).hexdigest()==pinned=='63927844eaac94765a7a804ab128076a88cad6eac2f534b715b08b17c4e21606'
sys.path.insert(0,str(BC/'context_architecture/scripts'));import context_engine as e
m=read(BC/'IMMUTABLE_EXECUTION_MANIFEST.json');assert e.verify_immutable(BC/'context_architecture',m['files'])==m['sha256']==cfg['immutable_execution_code_sha256']
parent=read(R/'analysis/phase4br_remediation/REMEDIATED_WORKFLOW_CONFIGURATION.json');assert parent['methodology_version']=='phase4br-scientific-v3.0.0'
assert cfg['scientific_methodology_sha256']=='ad691060099fff81a3e75de6d4ffdfeb4a8906e006dbfbeefc80a6c601f1d07f'
for x in read(O/'B02_B08_UNTOUCHED_CHECK.json')['reports']:assert h(R/x['path'])==x['source_sha256'] and not x['consumed'] and not x['substantive_access']
assert read(R/'analysis/reviews.json')=={} and not (O/'rehearsal_runtime').exists()
probe=read(O/'SYMLINK_ENVIRONMENT_PROBE.json');result=read(O/'REAL_SYMLINK_TEST_RESULT.json');assert result['status']=='ENVIRONMENT_BLOCKED' and '1314' in result['reason']
assert not Path(probe['test_path']).exists();assert result['guard_sha256']==h(BC/'context_architecture/scripts/context_engine.py')
assert result['original_test_source_sha256']==h(BC/'context_architecture/tests/test_context_engine.py')
assert h(R/'analysis/phase4bc_context_isolation_package.zip')=='8d15d680358ba7530ccfcdd82fd13a625c9b6a29410ad6bb9ee9d76e67b99389'
now=datetime.now(timezone.utc).isoformat()
verdict='RECOVERY_BLOCKED' if errors else 'RECOVERABLE'
report={'timestamp':now,'verdict':verdict,'prior_durable_protocol_missing':missing,'last_preexisting_committed_milestone':None,'interruption_position':'AFTER_OUTPUTS_BEFORE_FORMAL_COMMIT_PROTOCOL_EXISTED','inventory':inventory,'protected_count':len(rows),'protected_changes':errors,'reconciled_outputs':['Baseline independently rehashed','Symlink privilege-blocked receipt agrees with observed prior tool completion and fixture absence'],'no_symlink_replay':True,'next_permitted_operation':'IMPLEMENT_RECOVERY_PROTOCOL' if not errors else None,'source_access_started':False,'reserved_untouched':7,'live_source_verified':0,'live_promoted':0,'limitations':['No historical atomic commit receipt exists; reconciliation committed now, not backdated.','Current coordinator context /root known; durable session ID unavailable.','No OS-wide access proof.']}
write(O/'RECOVERY_PREFLIGHT.json',report)
assert not errors
(O/'milestone_receipts').mkdir(exist_ok=True)
receipt={'run_id':'phase4bc-s-current','atomic_unit_id':'BOOTSTRAP_RECONCILIATION','status':'COMMITTED_RECONCILIATION','commit_time':now,'historical_completion_time':None,'input_fingerprints':inventory,'output_fingerprints':{'RECOVERY_PREFLIGHT.json':h(O/'RECOVERY_PREFLIGHT.json')},'scientific_source_access':False,'validation_consumption_effect':0,'next_operation':'IMPLEMENT_RECOVERY_PROTOCOL','previous_receipt_sha256':None}
write(O/'milestone_receipts/BOOTSTRAP_RECONCILIATION.json',receipt)
event={'event_id':'bootstrap-recovery-001','sequence':1,'timestamp':now,'event_type':'RECOVERY_PREFLIGHT_PASS','run_id':'phase4bc-s-current','previous_event_sha256':None,'previous_durable_milestone':None,'session_id':None,'context_id':'/root','receipt_sha256':h(O/'milestone_receipts/BOOTSTRAP_RECONCILIATION.json'),'replayed_operations':[],'quarantine':'Logical classification retained in inventory; complete baseline and symlink outputs independently reconciled','verdict':'RECOVERABLE'}
with (O/'RECOVERY_EVENTS.jsonl').open('xb') as f:f.write(canon(event)+b'\n');f.flush();os.fsync(f.fileno())
write(O/'RECOVERY_STATE.json',{'run_id':'phase4bc-s-current','phase_id':'PHASE4BC-S','protocol_version':'BOOTSTRAP_RECONCILIATION_V1','status':'RECOVERABLE','last_committed_milestone':'BOOTSTRAP_RECONCILIATION','last_committed_milestone_receipt_sha256':h(O/'milestone_receipts/BOOTSTRAP_RECONCILIATION.json'),'next_permitted_operation':'IMPLEMENT_RECOVERY_PROTOCOL','source_access_started':False,'reserved_untouched':7,'methodology_sha256':cfg['scientific_methodology_sha256'],'context_architecture_sha256':pinned,'immutable_code_sha256':m['sha256'],'protected_file_manifest_sha256':h(O/'PROTECTED_FILES_INITIAL.csv'),'updated_at':now})
print('Recovery preflight PASS; baseline and blocked symlink result reconciled without replay')
