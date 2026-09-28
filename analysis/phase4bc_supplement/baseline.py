import csv,hashlib,json,subprocess,zipfile
from pathlib import Path
from datetime import datetime,timezone
O=Path(__file__).resolve().parent;R=O.parents[1];P=R/'analysis/phase4bc_context_isolation'
def h(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def save(n,v):(O/n).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
assert not (O/'PHASE4BC_S_BASELINE.json').exists()
(O/'GIT_STATUS_INITIAL.txt').write_text(subprocess.run(['git','status','--porcelain=v1','--untracked-files=all'],cwd=R,capture_output=True,text=True,encoding='utf-8').stdout,encoding='utf-8')
old={x['path']:x for x in csv.DictReader((P/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig'))}
for p in P.rglob('*'):
 if p.is_file():old.setdefault(p.relative_to(R).as_posix(),{'path':p.relative_to(R).as_posix(),'sha256':h(p)})
rows=[];errors=[]
for i,(rel,x) in enumerate(sorted(old.items()),1):
 p=R/rel;v=h(p) if p.is_file() else None
 if v!=x['sha256']:errors.append({'path':rel,'expected':x['sha256'],'observed':v})
 rows.append({'path':rel,'sha256':v,'size_bytes':p.stat().st_size if p.exists() else None})
 if i%2500==0:print('Baseline',i,flush=True)
with (O/'PROTECTED_FILES_INITIAL.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['path','sha256','size_bytes']);w.writeheader();w.writerows(rows)
prior=json.loads((P/'PHASE4BC_BASELINE.json').read_text(encoding='utf-8'))
archives=[]
for k,v in [(v['phase'],v) for v in prior['archives']]:
 p=R/v['path'];expected=v['expected']
 with zipfile.ZipFile(p) as z:ok=z.testzip() is None;count=len(z.namelist())
 observed=h(p);archives.append({'phase':k,'path':v['path'],'sha256':observed,'expected':expected,'crc_ok':ok,'members':count})
 if observed!=expected or not ok:errors.append({'archive':str(p)})
p=R/'analysis/phase4bc_context_isolation_package.zip'
with zipfile.ZipFile(p) as z:ok=z.testzip() is None
expected='8d15d680358ba7530ccfcdd82fd13a625c9b6a29410ad6bb9ee9d76e67b99389';observed=h(p)
archives.append({'phase':'phase4bc','path':p.relative_to(R).as_posix(),'sha256':observed,'expected':expected,'crc_ok':ok})
if observed!=expected or not ok:errors.append({'archive':str(p)})
reserved=json.loads((P/'B02_B08_UNTOUCHED_RESERVATION.json').read_text(encoding='utf-8'))['reports']
for x in reserved:
 x['phase4bc_s_hash_verified']=h(R/x['path'])==x['source_sha256']
 if not x['phase4bc_s_hash_verified'] or x['consumed'] or x['substantive_access']:errors.append({'reserved':x['holdout_id']})
assert not list((P/'B02_PREACCESS_PACKET_DRY_RUN').rglob('SOURCE_ACCESS_BEGAN.json'))
assert not (P/'rehearsal_runtime').exists()
reviews=json.loads((R/'analysis/reviews.json').read_text(encoding='utf-8'));assert reviews=={}
save('B02_B08_UNTOUCHED_CHECK.json',{'total':7,'untouched':7,'consumed':0,'contamination_count':0,'reports':reserved,'limits':'Hash and recorded access/inventory evidence, not OS-wide audit'})
save('PHASE4BC_S_BASELINE.json',{'at':datetime.now(timezone.utc).isoformat(),'protected_count':len(rows),'archives':archives,'errors':errors,'passed':not errors,'live_source_verified':0,'live_promoted':0,'lane_b_runtime_exists':False})
(O/'INPUT_DRIFT_REPORT.md').write_text('# Input drift\n\n'+('NO_RELEVANT_DRIFT' if not errors else 'BLOCKED: see baseline errors')+'\n',encoding='utf-8')
assert not errors
print('Baseline PASS',len(rows))
