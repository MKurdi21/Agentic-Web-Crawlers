"""Read-only recovery checks; no substantive access to reserved sources."""
import json,csv,hashlib,zipfile,subprocess,shutil
from pathlib import Path
from datetime import datetime,timezone
O=Path(__file__).resolve().parent;R=O.parents[1];BR=R/'analysis/phase4br_remediation'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def now():return datetime.now(timezone.utc).isoformat()
assert not (O/'BASELINE.json').exists(),'Existing baseline must be recovered, not replaced'
(O/'GIT_STATUS_INITIAL.txt').write_bytes(subprocess.check_output(['git','status','--porcelain=v1','-uall'],cwd=R))
errors=[];archives=read(BR/'PHASE4BR_BASELINE.json')['archives']
archives['phase4br']={'path':'analysis/phase4br_remediation_package.zip','expected':'bb9215c14f457b7d00156f955e2f34b8f80081ea0d2b9d9ec1a84337a51455b6'}
for label,a in archives.items():
    p=R/a['path'];a['observed']=sha(p)
    with zipfile.ZipFile(p) as z:a['crc_ok']=z.testzip() is None
    if a['observed']!=a['expected'] or not a['crc_ok']:errors.append('ARCHIVE_DRIFT:'+label)
cfg=read(BR/'REMEDIATED_WORKFLOW_CONFIGURATION.json');assert cfg['methodology_sha256']=='ad691060099fff81a3e75de6d4ffdfeb4a8906e006dbfbeefc80a6c601f1d07f'
definition={k:cfg[k] for k in ['methodology_version','evidence_schema_version','parent_methodology_sha256','candidate_files','dependency_manifest_sha256','runtime_python']}
assert hashlib.sha256(json.dumps(definition,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()==cfg['methodology_sha256']
for e in cfg['candidate_files']:
    if sha(BR/'candidate_v4br'/e['relative_path'])!=e['sha256']:errors.append('CODE_DRIFT:'+e['relative_path'])
deps=read(BR/'DEPENDENCY_MANIFEST.json')
for e in deps['files']:
    if sha(BR/'candidate_v4br/_deps'/e['relative_path'])!=e['sha256']:errors.append('DEPENDENCY_DRIFT:'+e['relative_path'])
old=list(csv.DictReader((BR/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8')))
expected={x['path']:x['sha256'] for x in old}
for p in BR.rglob('*'):
    if p.is_file():expected.setdefault(p.relative_to(R).as_posix(),None)
expected['analysis/phase4br_remediation_package.zip']=archives['phase4br']['expected']
rows=[]
for i,(rel,h) in enumerate(sorted(expected.items()),1):
    p=R/rel;observed=sha(p) if p.is_file() else None
    if h is not None and observed!=h:errors.append('PROTECTED_DRIFT:'+rel)
    rows.append({'path':rel,'sha256':observed,'size_bytes':p.stat().st_size if p.is_file() else None})
    if i%1500==0:print('Protected metadata/hash checks',i,flush=True)
with (O/'PROTECTED_FILES_INITIAL.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['path','sha256','size_bytes']);w.writeheader();w.writerows(rows)
reserve=read(BR/'PHASE4B_RESUME_HOLDOUT_MANIFEST.json');assert reserve['resumed_order']==['B02','B03','B04','B05','B06','B07','B08']
for x in reserve['reports']:
    if x['substantive_access'] or x['contamination_count'] or sha(R/x['path'])!=x['source_sha256']:errors.append('RESERVED_INPUT_DRIFT:'+x['holdout_id'])
assert read(R/'analysis/reviews.json')=={}
write(O/'BASELINE.json',{'recorded_at':now(),'phase':'PHASE4B_RESUMED_VALIDATION','authorization':'User resume after Phase4BR handoff','methodology_sha256':cfg['methodology_sha256'],'archives':archives,'protected_count':len(rows),'errors':errors,'passed':not errors,'live_source_verified':0,'live_promoted':0,'reserved_reports':reserve['reports']})
assert not errors,errors
for root in ('candidate_frozen','candidate_v4br'):
    for e in cfg['candidate_files']:
        src=BR/'candidate_v4br'/e['relative_path'];dst=O/root/e['relative_path'];dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst);assert sha(dst)==e['sha256']
shutil.copytree(BR/'candidate_v4br/_deps',O/'candidate_v4br/_deps',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
write(O/'FROZEN_CONFIGURATION.json',cfg);write(O/'CANDIDATE_CODE_MANIFEST.json',read(BR/'CANDIDATE_CODE_MANIFEST.json'));write(O/'DEPENDENCY_MANIFEST.json',deps)
ledger={'validation_type':'SEQUENTIAL_RESERVED_HOLDOUT_VALIDATION','reports':[{**x,'state':'UNTOUCHED_RESERVED_VALIDATION_EVIDENCE','consumed':False,'completed':False,'result':None,'primary_context_id':None,'verifier_context_ids':[]} for x in reserve['reports']],'events':[],'lane_b':'NOT_RUN_GATE_BLOCKED'}
write(O/'HOLDOUT_ACCESS_LEDGER.json',ledger)
write(O/'PROCESSING_ORDER.json',{'algorithm':'original_phase4b_csv_order_remainder_v1','order':reserve['resumed_order'],'original_selection_sha256':reserve['original_phase4b_selection_sha256'],'methodology_sha256':cfg['methodology_sha256']})
print('Preflight passed; no reserved substantive source access',flush=True)
