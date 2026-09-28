"""Read-only input verification and durable pre-access baseline. No PDF parsing."""
import csv,hashlib,json,sys,subprocess,zipfile
from pathlib import Path
from datetime import datetime,timezone
O=Path(__file__).resolve().parent;R=O.parents[1];P=R/'analysis/phase4bc_path_containment';S=R/'analysis/phase4bc_supplement';C=R/'analysis/phase4bc_context_isolation';BR=R/'analysis/phase4br_remediation'
sys.path.insert(0,str(P/'continuity_adapter'))
from adapter import code_pins,c
sys.path.insert(0,str(S/'recovery_protocol'))
from engine import Engine,canonical
def h(p):
 d=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):d.update(b)
 return d.hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def put(n,v):(O/n).write_text(json.dumps(v,sort_keys=True,indent=2),encoding='utf-8')
def now():return datetime.now(timezone.utc).isoformat()
if __name__=='__main__':
 assert not (O/'RESUMED_PHASE4B_BASELINE.json').exists(),'Existing state requires recovery, not reinitialization'
 (O/'GIT_STATUS_INITIAL.txt').write_bytes(subprocess.run(['git','status','--porcelain=v1','--untracked-files=all'],cwd=R,capture_output=True,check=True).stdout)
 previous=list(csv.DictReader((P/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig')))
 expected={x['path']:x['sha256'] for x in previous};paths={x['path']:R/x['path'] for x in previous}
 for p in P.rglob('*'):
  if p.is_file():paths[p.relative_to(R).as_posix()]=p
 paths['analysis/phase4bc_path_containment_package.zip']=P.parent/'phase4bc_path_containment_package.zip'
 rows=[];errors=[]
 for i,(rel,p) in enumerate(sorted(paths.items()),1):
  actual=h(p)
  if rel in expected and actual!=expected[rel]:errors.append({'path':rel,'reason':'PROTECTED_DRIFT'})
  rows.append({'path':rel,'sha256':actual,'size':p.stat().st_size})
  if i%4000==0:print('Protected hashes',i,flush=True)
 with (O/'PROTECTED_FILES_INITIAL.csv').open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=['path','sha256','size']);w.writeheader();w.writerows(rows)
 hand=read(P/'FINAL_HANDOFF.json');assert hand['classification']=='READY_TO_RESUME_PHASE4B_AT_B02'
 assert hand['reserved_holdout']=={'selected':7,'untouched':7,'consumed':0,'contamination_events':0,'resume_start':'B02'}
 assert hand['live_state']=={'source_verified':0,'promoted':0} and not hand['lane_b_executed'] and not hand['phase5_started']
 assert read(P/'PRESERVATION_CHECK.json')['status']=='PASS'
 pins=code_pins();assert pins['path_containment']=='41fa409998ec492286c81e01efb8484a4805074f97093ae795b0c11911ce43dd' and pins['immutable_code']=='3494b44b5316a9ed98bbd4d903299e48f347dccd05330b369590e382015b373e'
 for x in read(P/'IMPLEMENTATION_MANIFEST.json')['files']:assert h(P/x['path'])==x['sha256']
 cfg=read(BR/'REMEDIATED_WORKFLOW_CONFIGURATION.json');definition={k:cfg[k] for k in ['methodology_version','evidence_schema_version','parent_methodology_sha256','candidate_files','dependency_manifest_sha256','runtime_python']}
 assert c.fingerprint(definition)==pins['methodology']==cfg['methodology_sha256']
 for x in cfg['candidate_files']:assert h(BR/'candidate_v4br'/x['relative_path'])==x['sha256']
 cm=read(C/'IMMUTABLE_EXECUTION_MANIFEST.json')
 for x in cm['files']:assert h(C/'context_architecture'/x['relative_path'])==x['sha256']
 context=read(C/'CONTEXT_PACKET_ARCHITECTURE_CONFIGURATION.json');assert context['context_packet_architecture_sha256']==pins['context_architecture']
 recovery=read(S/'RECOVERY_IMPLEMENTATION_MANIFEST.json');assert recovery['sha256']=='5f5adf341fac45c68cb23d6e97714ec7324625ca1ee9b3bfa6b8fbe5ab2ac0d0'
 for x in recovery['files']:assert h(S/x['path'])==x['sha256']
 archives=[]
 for x in read(P/'PHASE4BC_P_BASELINE.json')['archives']+[{'path':hand['package']['path'],'expected':hand['package']['sha256']}]:
  p=R/x['path']
  with zipfile.ZipFile(p) as z:crc=z.testzip() is None
  assert crc and h(p)==x['expected'];archives.append({'path':x['path'],'sha256':x['expected'],'crc_pass':crc})
 reservation=read(P/'B02_B08_UNTOUCHED_CHECK.json');reports=reservation['reports'];assert len(reports)==7
 for x in reports:assert h(R/x['path'])==x['source_sha256'] and not x['consumed'] and not x['substantive_access']
 assert read(R/'analysis/reviews.json')=={}
 assert not (O/'rehearsal_runtime').exists()
 baseline={'at':now(),'protected_count':len(rows),'errors':errors,'preservation_pass':not errors,'archives':archives,'frozen_pins':pins,'recovery_protocol_sha256':recovery['sha256'],'prior_handoff_sha256':h(P/'FINAL_HANDOFF.json'),'prior_ready_claim_verified':True,'operational_real_source_interface':'UNDER_SEPARATE_PREACCESS_REVIEW','reserved_selected':7,'untouched':7,'consumed':0,'contamination_events':0,'live_source_verified':0,'live_promoted':0,'lane_b_runtime_created':False,'source_observation':'Hashes and recorded access evidence, not OS-wide audit'}
 put('RESUMED_PHASE4B_BASELINE.json',baseline);assert not errors
 order=[{'ordinal':i,'holdout_id':x['holdout_id'],'report_id':x['report_id'],'path':x['path'],'source_sha256':x['source_sha256']} for i,x in enumerate(reports,1)]
 assert [x['holdout_id'] for x in order]==['B02','B03','B04','B05','B06','B07','B08']
 put('RESUMED_HOLDOUT_PROCESSING_ORDER.json',{'algorithm':'UNCHANGED_FROZEN_ORIGINAL_ORDER','reports':order,'frozen_before_source_access':True})
 put('HOLDOUT_STATE_TRACKER.json',{'reports':[{**x,'state':'UNTOUCHED_RESERVED_VALIDATION_EVIDENCE','substantive_access':False,'consumed':False,'completed':False} for x in order]})
 e=Engine(O)
 rp={'methodology_sha256':pins['methodology'],'context_architecture_sha256':pins['context_architecture'],'immutable_code_sha256':pins['immutable_code'],'protected_file_manifest_sha256':h(O/'PROTECTED_FILES_INITIAL.csv'),'source_sha256':order[0]['source_sha256'],'current_packet_sha256':None}
 with e.lock('/root'):
  e.init('phase4b-resumed-v2',rp,phase='PHASE4B_RESUMED_V2',bindings=[{'path':str(P/'IMPLEMENTATION_MANIFEST.json'),'sha256':h(P/'IMPLEMENTATION_MANIFEST.json')}])
  e.begin('BASELINE_PREFLIGHT',{'baseline':h(O/'RESUMED_PHASE4B_BASELINE.json')},['outputs/baseline_receipt.json'])
  e.commit({'outputs/baseline_receipt.json':canonical({'baseline_sha256':h(O/'RESUMED_PHASE4B_BASELINE.json'),'order_sha256':h(O/'RESUMED_HOLDOUT_PROCESSING_ORDER.json'),'source_access':False})},next_operation='PREACCESS_INTERFACE_GATE')
 print('BASELINE PASS',len(rows),flush=True)
