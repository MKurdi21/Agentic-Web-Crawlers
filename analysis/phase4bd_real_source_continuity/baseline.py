"""Metadata/streaming-hash baseline. No scientific source interpretation."""
import csv,json,hashlib,sys,subprocess,zipfile
from pathlib import Path
from datetime import datetime,timezone
O=Path(__file__).resolve().parent;R=O.parents[1];PREV=R/'analysis/phase4b_resumed_v2';P=R/'analysis/phase4bc_path_containment';S=R/'analysis/phase4bc_supplement'
sys.path.insert(0,str(P/'continuity_adapter'))
from adapter import code_pins,c
def h(p):
 d=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):d.update(b)
 return d.hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def put(n,v):(O/n).write_text(json.dumps(v,sort_keys=True,indent=2),encoding='utf-8')
assert not (O/'PHASE4BD_BASELINE.json').exists()
(O/'GIT_STATUS_INITIAL.txt').write_bytes(subprocess.run(['git','status','--porcelain=v1','--untracked-files=all'],cwd=R,capture_output=True,check=True).stdout)
old=list(csv.DictReader((PREV/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig')));expected={x['path']:x['sha256'] for x in old};paths={x['path']:R/x['path'] for x in old}
for p in PREV.rglob('*'):
 if p.is_file():paths[p.relative_to(R).as_posix()]=p
paths['analysis/phase4b_resumed_v2_package.zip']=R/'analysis/phase4b_resumed_v2_package.zip'
rows=[];errors=[]
for i,(rel,p) in enumerate(sorted(paths.items()),1):
 actual=h(p)
 if rel in expected and actual!=expected[rel]:errors.append(rel)
 rows.append({'path':rel,'sha256':actual,'size':p.stat().st_size})
 if i%4000==0:print('Baseline',i,flush=True)
with (O/'PROTECTED_FILES_INITIAL.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=['path','sha256','size']);w.writeheader();w.writerows(rows)
hand=read(PREV/'FINAL_HANDOFF.json');assert hand['classification']=='NO_GO' and hand['reason']=='FROZEN_REAL_REPORT_CONTINUITY_INTEGRATION_UNAVAILABLE'
assert hand['holdout_metrics']['reports_consumed']==0 and hand['holdout_metrics']['untouched_remaining']==7
pins=code_pins();assert pins['path_containment']=='41fa409998ec492286c81e01efb8484a4805074f97093ae795b0c11911ce43dd' and pins['immutable_code']=='3494b44b5316a9ed98bbd4d903299e48f347dccd05330b369590e382015b373e'
for x in read(P/'IMPLEMENTATION_MANIFEST.json')['files']:assert h(P/x['path'])==x['sha256']
rec=read(S/'RECOVERY_IMPLEMENTATION_MANIFEST.json');assert rec['sha256']=='5f5adf341fac45c68cb23d6e97714ec7324625ca1ee9b3bfa6b8fbe5ab2ac0d0'
for x in rec['files']:assert h(S/x['path'])==x['sha256']
archives=[]
for x in read(PREV/'RESUMED_PHASE4B_BASELINE.json')['archives']+[{'path':hand['package']['path'],'sha256':hand['package']['sha256']}]:
 p=R/x['path'];want=x['sha256'];assert h(p)==want
 with zipfile.ZipFile(p) as z:assert z.testzip() is None
 archives.append({'path':x['path'],'sha256':want,'crc_pass':True})
assert archives[-1]['sha256']=='ac6321b7ee2d5f2a0faa084085b5fcca4e3855fbb190776c77f9923877a3820a'
reserve=read(P/'B02_B08_UNTOUCHED_CHECK.json')
for x in reserve['reports']:assert h(R/x['path'])==x['source_sha256'] and not x['consumed'] and not x['substantive_access']
assert read(R/'analysis/reviews.json')=={}
put('B02_B08_UNTOUCHED_CHECK.json',{**reserve,'phase':'PHASE4BD','evidence_limit':'Hash and recorded access evidence; not OS-wide audit'})
assert not errors
put('PHASE4BD_BASELINE.json',{'status':'PASS','protected_count':len(rows),'changed':errors,'at':datetime.now(timezone.utc).isoformat(),'frozen_pins':pins,'recovery_sha256':rec['sha256'],'archives':archives,'prior_reason':hand['reason'],'live_source_verified':0,'live_promoted':0,'reserved_untouched':7,'reserved_consumed':0,'lane_b':False})
(O/'INPUT_DRIFT_REPORT.md').write_text('# Input drift\n\nNO_RELEVANT_DRIFT. Protected prior files, frozen component manifests and prior archive CRC/hashes match. No scientific source interpreted.\n')
source=R/'02_Web_Agent_Benchmarks_Environments/AgentDojo_A_Dynamic_Environment_to_Evaluate_Prompt_Injection_Attacks_and_Defenses_for_LLM_Agents.pdf'
if not source.exists():
 matches=[p for p in R.glob('*/*.pdf') if p.name.lower().startswith('agentdojo')];assert len(matches)==1;source=matches[0]
assert h(source)=='26a3f0426ee1d533e4dd9f62d1343a7a1d231fe718cfaf3a362cc7de829ae913'
fixture={'source_role':'CONSUMED_DEVELOPMENT_EVIDENCE','report_id':'report_e30d9cfd6055ddd8e085a0ff','development_id':'B01','source_file_id':'sha256:'+h(source),'source_sha256':h(source),'source_path':str(source),'prior_consumption_state':'CONSUMED_VALIDATION_EVIDENCE','reason':'B01 was previously consumed and used for remediation; never new untouched validation evidence','reserved_reports_excluded':[x['report_id'] for x in reserve['reports']],'field_scope':'First nonempty source text line on PDF page 1, then deterministic current-source recheck; no scientific validation claim'}
put('REAL_SOURCE_INTEGRATION_FIXTURE.json',fixture)
print('BASELINE PASS',len(rows),'B01 fixture identity confirmed',flush=True)
