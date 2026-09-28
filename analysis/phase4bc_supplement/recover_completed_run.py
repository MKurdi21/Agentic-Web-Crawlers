"""Read-only completion validation, then append recovery observation; no replay."""
import csv
import subprocess
import sys
import zipfile
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parents[1]
sys.path.insert(0,str(O/'recovery_protocol'))
from engine import *
request_id=uuid.uuid4().hex;errors=[];prior=read(O/'recovery_coordination/RECOVERY_STATE.json')
index=read(O/'RECOVERY_COORDINATION_INDEX.json')
assert index['canonical_state']=='recovery_coordination/RECOVERY_STATE.json'
assert filehash(O/'milestone_receipts/BOOTSTRAP_RECONCILIATION.json')==index['bootstrap_receipt_sha256']
bootstrap=read(O/'milestone_receipts/BOOTSTRAP_RECONCILIATION.json')
for rel,h in bootstrap['output_fingerprints'].items():
    if filehash(O/rel)!=h:errors.append('BOOTSTRAP_OUTPUT:'+rel)
inventory=[]
for p in O.rglob('*'):
    if not p.is_file():continue
    rel=p.relative_to(O).as_posix()
    status='UNCOMMITTED_RECOVERY_MATERIAL'
    if rel.startswith('private_test_storage/'):status='SYNTHETIC_TEST_FIXTURE_NEVER_AUTHORITATIVE'
    elif rel.startswith('recovery_coordination/'):status='CHECKED_BY_RECEIPT_JOURNAL_ENGINE'
    elif rel.startswith('test_results/'):status='PRESERVED_DEVELOPMENT_ATTEMPT_NOT_FINAL_AUTHORITY'
    inventory.append({'path':rel,'size':p.stat().st_size,'sha256':filehash(p),'mtime_ns':p.stat().st_mtime_ns,'classification':status})
impl=read(O/'RECOVERY_IMPLEMENTATION_MANIFEST.json')
if digest(canonical(impl['files']))!=impl['sha256'] or impl['sha256']!=prior['immutable_code_sha256']:errors.append('IMPLEMENTATION_MANIFEST')
for x in impl['files']:
    if filehash(O/x['path'])!=x['sha256']:errors.append('CODE_DRIFT:'+x['path'])
baseline=read(O/'PHASE4BC_S_BASELINE.json');archive_results=[]
for a in baseline['archives']:
    p=R/a['path']
    with zipfile.ZipFile(p) as z:crc=z.testzip() is None
    ok=filehash(p)==a['expected'] and crc
    archive_results.append({'path':a['path'],'passed':ok})
    if not ok:errors.append('PRIOR_ARCHIVE:'+a['path'])
rows=list(csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig')))
for i,x in enumerate(rows,1):
    p=R/x['path']
    if not p.is_file() or filehash(p)!=x['sha256']:errors.append('PROTECTED_DRIFT:'+x['path'])
    if i%3000==0:print('Recovery revalidated',i,'protected files',flush=True)
bc=R/'analysis/phase4bc_context_isolation';cfg=read(bc/'CONTEXT_PACKET_ARCHITECTURE_CONFIGURATION.json');claimed=cfg.pop('context_packet_architecture_sha256')
if digest(canonical(cfg))!=claimed or claimed!=prior['context_architecture_sha256']:errors.append('CONTEXT_ARCHITECTURE')
parent=read(R/'analysis/phase4br_remediation/REMEDIATED_WORKFLOW_CONFIGURATION.json')
if parent['methodology_version']!=prior['methodology_version'] or cfg['scientific_methodology_sha256']!=prior['methodology_sha256']:errors.append('SCIENTIFIC_PARENT')
sys.path.insert(0,str(bc/'context_architecture/scripts'))
import context_engine
m=read(bc/'IMMUTABLE_EXECUTION_MANIFEST.json')
if context_engine.verify_immutable(bc/'context_architecture',m['files'])!=m['sha256']:errors.append('PARENT_IMMUTABLE_CODE')
reservations=read(O/'B02_B08_UNTOUCHED_CHECK.json')
for x in reservations['reports']:
    if filehash(R/x['path'])!=x['source_sha256'] or x['consumed'] or x['substantive_access']:errors.append('RESERVATION:'+x['holdout_id'])
if read(R/'analysis/reviews.json')!={}:errors.append('LIVE_REVIEW_STATE')
git=subprocess.run(['git','status','--porcelain=v1','--untracked-files=all'],cwd=R,capture_output=True,check=True).stdout.decode('utf-8').splitlines()
old=(O/'GIT_STATUS_FINAL.txt').read_text(encoding='utf-8-sig').splitlines()
def filtered(xs):return sorted(x for x in xs if 'analysis/phase4bc_supplement/' not in x and 'analysis/phase4bc_supplement_package.zip' not in x)
if filtered(git)!=filtered(old):errors.append('GIT_DRIFT_OUTSIDE_BOUNDARY')
if (O/'rehearsal_runtime').exists():errors.append('LANE_B_RUNTIME')
receipt=read(O/'PACKAGE_RECEIPT.json');zpath=O.parent/'phase4bc_supplement_package.zip'
if filehash(zpath)!=receipt['sha256']:errors.append('PACKAGE_HASH')
with zipfile.ZipFile(zpath) as z:
    manifest=loads(z.read('PACKAGE_MANIFEST.json'));names=z.namelist();expected={x['path']:x for x in manifest['files']}
    if z.testzip() or set(names)!=set(expected)|{'PACKAGE_MANIFEST.json'} or len(names)!=len({n.casefold() for n in names}):errors.append('PACKAGE_INVENTORY_CRC')
    for n,x in expected.items():
        if digest(z.read(n))!=x['sha256'] or len(z.read(n))!=x['size_bytes']:errors.append('PACKAGE_MEMBER:'+n)
        if n!='FINAL_HANDOFF.json' and filehash(O/n)!=x['sha256']:errors.append('EXTERNAL_MEMBER:'+n)
    archived=loads(z.read('FINAL_HANDOFF.json'));external=read(O/'FINAL_HANDOFF.json')
    external['package']['sha256']=None
    if external!=archived:errors.append('HANDOFF_CONVENTION_MISMATCH')
    authenticated=set(expected)|{'PACKAGE_MANIFEST.json','PACKAGE_RECEIPT.json'}
for x in inventory:
    if x['path'] in authenticated:x['classification']='RECONCILED_AGAINST_COMMITTED_PACKAGE_RECEIPT'
tests=read(O/'RECOVERY_TEST_RESULTS.json')
if tests['tests']!=46 or tests['failed']!=0:errors.append('FINAL_TEST_RESULTS')
e=Engine(O/'recovery_coordination');last_receipts=e.receipts();journal=e.journal()
active=read(O/'recovery_coordination/ACTIVE_OPERATION.json')
if active['attempt_id'] not in {r['attempt_id'] for _,r in last_receipts}:errors.append('UNCOMMITTED_ACTIVE_OPERATION')
uncommitted=[x['path'] for x in inventory if x['classification']=='UNCOMMITTED_RECOVERY_MATERIAL']
report={'recovery_request_id':request_id,'timestamp':now(),'context_id':'/root','session_id':None,'session_id_reason':'No authoritative current session identifier exposed','previous_durable_milestone':prior['last_committed_milestone'],'previous_receipt_sha256':prior['last_committed_milestone_receipt_sha256'],'interruption_position':'AFTER_FINAL_ATOMIC_UNIT_DURABLY_COMMITTED','prior_status':prior['status'],'next_permitted_operation':'STOP_AND_REPORT' if not errors else None,'protected_count':len(rows),'prior_archives':archive_results,'reserved_untouched':7,'reserved_consumed':0,'source_contamination_events':0,'live_source_verified':0,'live_promoted':0,'lane_b_executed':False,'replayed_operations':[],'quarantined_operations':[],'logical_quarantine_material':uncommitted,'quarantine_disposition':'Uncommitted helper/development files remain retained and excluded from completion authority; no replay. Deliberately partial synthetic fixtures remain isolated.','inventory':inventory,'errors':errors,'verdict':'RECOVERABLE_RUN_ALREADY_COMPLETE' if not errors else 'RECOVERY_BLOCKED','hashes_before_recovery':{'canonical_state':filehash(O/'recovery_coordination/RECOVERY_STATE.json'),'journal':filehash(O/'recovery_coordination/RECOVERY_EVENTS.jsonl'),'package':filehash(zpath),'implementation':impl['sha256'],'methodology':prior['methodology_sha256'],'architecture':prior['context_architecture_sha256']},'limitations':['Recorded access and inventories are not OS-wide audit.','No expensive tests, archive rebuild or symlink retry performed.']}
out=O/'recovery_observations'/f'{request_id}.json';exclusive(out,canonical(report))
with e.lock('/root'):
    if errors:
        e.event('RECOVERY_PREFLIGHT_FAIL',request_id=request_id,errors=errors,report_sha256=filehash(out))
        replace(e.root/'BLOCKED_LATCH.json',{'active':True,'reason':'EXTERNAL_PREFLIGHT_FAILED','timestamp':now()})
    else:
        s=e.recover({k:prior[k] for k in PIN_KEYS},session_mode='RESUMED_SESSION')
        assert s['status']=='RUN_COMPLETE' and s['next_permitted_operation']=='STOP'
        e.event('RECOVERY_PREFLIGHT_PASS',request_id=request_id,previous_durable_milestone=prior['last_committed_milestone'],context_id='/root',hashes_before_recovery=report['hashes_before_recovery'],replayed_operations=[],quarantined_operations=[],logical_quarantine_material=uncommitted,recovery_verdict=report['verdict'],report_sha256=filehash(out))
print(canonical({k:v for k,v in report.items() if k not in ['inventory','hashes_before_recovery','logical_quarantine_material']}).decode())
raise SystemExit(1 if errors else 0)
