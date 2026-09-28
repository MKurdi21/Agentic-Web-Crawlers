"""Phase4BC-P metadata/hash baseline; no source interpretation."""
import csv,hashlib,json,subprocess,zipfile
from pathlib import Path
from datetime import datetime,timezone
O=Path(__file__).resolve().parent;R=O.parents[1];S=R/'analysis/phase4bc_supplement'
def h(p):
 d=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):d.update(b)
 return d.hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def put(n,v): (O/n).write_text(json.dumps(v,sort_keys=True,indent=2),encoding='utf-8')
assert not (O/'PHASE4BC_P_BASELINE.json').exists()
(O/'GIT_STATUS_INITIAL.txt').write_bytes(subprocess.run(['git','status','--porcelain=v1','--untracked-files=all'],cwd=R,capture_output=True,check=True).stdout)
old=list(csv.DictReader((S/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig')));expected={x['path']:x['sha256'] for x in old}
paths={x['path']:R/x['path'] for x in old}
for p in S.rglob('*'):
 if p.is_file():paths[p.relative_to(R).as_posix()]=p
paths['analysis/phase4bc_supplement_package.zip']=R/'analysis/phase4bc_supplement_package.zip'
rows=[];errors=[]
for i,(rel,p) in enumerate(sorted(paths.items()),1):
 got=h(p)
 if rel in expected and got!=expected[rel]:errors.append({'path':rel,'reason':'PRIOR_PROTECTED_DRIFT'})
 rows.append({'path':rel,'sha256':got,'size':p.stat().st_size})
 if i%3000==0:print('Baseline hashes',i,flush=True)
with (O/'PROTECTED_FILES_INITIAL.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=['path','sha256','size']);w.writeheader();w.writerows(rows)
archives=[]
for a in read(S/'PHASE4BC_S_BASELINE.json')['archives']+[{'path':'analysis/phase4bc_supplement_package.zip','expected':'b1e057a6b8c37c50f008eefedb2b2a8b2af657d697cafc87cf0ca61dfc61f7c6'}]:
 p=R/a['path']
 with zipfile.ZipFile(p) as z:crc=z.testzip() is None
 ok=h(p)==a['expected'] and crc
 archives.append({'path':a['path'],'sha256':h(p),'expected':a['expected'],'crc_ok':crc})
 if not ok:errors.append({'path':a['path'],'reason':'ARCHIVE_DRIFT'})
cfg=read(R/'analysis/phase4bc_context_isolation/CONTEXT_PACKET_ARCHITECTURE_CONFIGURATION.json')
assert cfg['context_packet_architecture_sha256']=='63927844eaac94765a7a804ab128076a88cad6eac2f534b715b08b17c4e21606'
assert cfg['scientific_methodology_sha256']=='ad691060099fff81a3e75de6d4ffdfeb4a8906e006dbfbeefc80a6c601f1d07f'
impl=read(S/'RECOVERY_IMPLEMENTATION_MANIFEST.json')
assert impl['sha256']=='5f5adf341fac45c68cb23d6e97714ec7324625ca1ee9b3bfa6b8fbe5ab2ac0d0'
for x in impl['files']:assert h(S/x['path'])==x['sha256']
res=read(S/'B02_B08_UNTOUCHED_CHECK.json')
for x in res['reports']:assert h(R/x['path'])==x['source_sha256'] and not x['consumed'] and not x['substantive_access']
assert read(R/'analysis/reviews.json')=={}
assert not (O/'rehearsal_runtime').exists()
put('B02_B08_UNTOUCHED_CHECK.json',{**res,'phase':'PHASE4BC-P','evidence_limit':'Recorded access and artifacts, not OS-wide audit. Only streamed source hashes.'})
put('PHASE4BC_P_BASELINE.json',{'at':datetime.now(timezone.utc).isoformat(),'protected_count':len(rows),'archives':archives,'frozen_methodology':cfg['scientific_methodology_sha256'],'frozen_context':cfg['context_packet_architecture_sha256'],'frozen_recovery':impl['sha256'],'live_source_verified':0,'live_promoted':0,'lane_b':False,'errors':errors,'passed':not errors})
(O/'INPUT_DRIFT_REPORT.md').write_text('# Input drift\n\n'+('NO_RELEVANT_DRIFT' if not errors else json.dumps(errors)),encoding='utf-8')
assert not errors
print('BASELINE PASS',len(rows))
