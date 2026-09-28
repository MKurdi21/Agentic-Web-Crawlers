import csv, hashlib, json, os, shutil, subprocess, zipfile
from pathlib import Path
from datetime import datetime, timezone
O=Path(__file__).resolve().parent; R=O.parents[1]; B=R/'analysis/phase4b_validation'
def h(p):
 d=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''): d.update(b)
 return d.hexdigest()
def j(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def w(p,x):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def now():return datetime.now(timezone.utc).isoformat()
if __name__=='__main__':
 assert not (O/'PHASE4BR_BASELINE.json').exists(), 'Do not replace baseline'
 git=subprocess.check_output(['git','status','--porcelain=v1','-uall'],cwd=R);(O/'GIT_STATUS_INITIAL.txt').write_bytes(git)
 base=j(B/'PHASE4B_BASELINE.json'); archives=base['archives'];archives['phase4b']={'path':'analysis/phase4b_validation_package.zip','expected':'f6b416f7ebb3626e512564e34fba235e22fc13d870d4019cc0e47ae67246bd1b'}
 for a in archives.values():
  p=R/a['path'];a['observed']=h(p)
  with zipfile.ZipFile(p) as z:a['crc_ok']=z.testzip() is None;a['members']=len(z.namelist())
  assert a['observed']==a['expected'] and a['crc_ok'],a
 print('All six package hashes and CRC checks pass',flush=True)
 with (B/'PROTECTED_FILE_HASHES_INITIAL.csv').open(encoding='utf-8-sig') as f:old=list(csv.DictReader(f))
 protected={x['path']:x['sha256'] for x in old}
 # Include all later phase outputs, including runtime/private evidence, without interpreting their content.
 for name in ['workspace_audit','integration_design','phase3_calibration','phase4_rehearsal','phase4r_remediation','phase4b_validation']:
  for p in (R/'analysis'/name).rglob('*'):
   if p.is_file():protected.setdefault(p.relative_to(R).as_posix(),None)
 rows=[];drift=[]
 for i,(rel,expected) in enumerate(sorted(protected.items())):
  p=R/rel;obs=h(p) if p.is_file() else None
  if expected is not None and expected!=obs:drift.append(rel)
  rows.append({'path':rel,'size_bytes':p.stat().st_size if p.is_file() else None,'sha256':obs})
  if i%1000==0:print('Protected hashes',i,flush=True)
 with (O/'PROTECTED_FILES_INITIAL.csv').open('w',encoding='utf-8',newline='') as f:
  q=csv.DictWriter(f,fieldnames=['path','size_bytes','sha256']);q.writeheader();q.writerows(rows)
 assert not drift,drift
 ledger=j(B/'HOLDOUT_ACCESS_LEDGER.json');hand=j(B/'FINAL_HANDOFF.json');pres=j(B/'PRESERVATION_CHECK.json')
 assert hand['overall_classification']=='NO_GO' and hand['lane_b']=='NOT_RUN_GATE_BLOCKED' and pres['passed']
 assert j(R/'analysis/reviews.json')=={}
 assert not (B/'rehearsal_runtime').exists() and not (B/'candidate_v4r/shadow').exists()
 reserve=[]
 with (R/'analysis/phase4r_remediation/PHASE4B_VALIDATION_HOLDOUT.csv').open(encoding='utf-8-sig') as f:hold=list(csv.DictReader(f))
 for a,s,c in zip(ledger['reports'][1:],base['holdout_sources'][1:],hold[1:]):
  assert not a['substantive_access'] and not a['consumed'] and not a['primary_context_id'] and not a['verifier_context_ids']
  assert h(R/s['path'])==a['source_sha256']
  reserve.append({'holdout_id':a['holdout_id'],'report_id':a['paper_id'],'source_file_id':c.get('source_file_id'),'source_sha256':a['source_sha256'],'path':s['path'],'untouched_status':'UNTOUCHED_RESERVED_VALIDATION_EVIDENCE','last_verified_at':now(),'contamination_count':0,'substantive_access':False})
 w(O/'B02_B08_RESERVATION_MANIFEST.json',{'reports':reserve,'access_policy':'METADATA_AND_HASH_ONLY','evidence':'Phase 4B access ledger, context receipts and absent B02-B08 runtime artifacts','proof_limit':'Audited records and controlled tool access; not an OS-wide access attestation.'})
 w(O/'PHASE4BR_BASELINE.json',{'at':now(),'archives':archives,'protected_count':len(rows),'original_protected_count':len(old),'input_drift':drift,'live_source_verified':0,'live_promoted':0,'lane_b_absent':True,'phase4b_facts':hand,'reservation_count':7})
 (O/'INPUT_DRIFT_REPORT.md').write_text('# Input drift\n\nNO_RELEVANT_DRIFT. All six packages match their expected hashes and CRC checks; the original 5,737 protected paths match. Additional phase outputs are baselined independently.\n',encoding='utf-8')
 manifest=j(B/'CANDIDATE_CODE_MANIFEST.json')
 for x in manifest['immutable_files']:
  s=B/'candidate_frozen'/x['relative_path'];assert h(s)==x['sha256'];d=O/'candidate_v4br'/x['relative_path'];d.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(s,d)
 failure=[]
 sources=list((B/'holdout_validation/B01').rglob('*'))+[B/x for x in ['FINAL_HANDOFF.json','HOLDOUT_VALIDATION_METRICS.json','HOLDOUT_DISAGREEMENTS.csv','FROZEN_PHASE4B_CONFIGURATION.json','CANDIDATE_CODE_MANIFEST.json','HOLDOUT_CONTEXT_ISOLATION.json','HOLDOUT_ACCESS_LEDGER.json']]+[B/'private_source_material/B01/source.pdf']
 for s in sources:
  if not s.is_file():continue
  rel=s.relative_to(B);d=O/'private_source_material/original_phase4b'/rel;d.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(s,d)
  assert h(s)==h(d);failure.append({'original_path':s.relative_to(R).as_posix(),'private_copy':d.relative_to(O).as_posix(),'sha256':h(d),'size_bytes':d.stat().st_size})
 w(O/'PHASE4B_B01_FAILURE_MANIFEST.json',{'classification':'NEVER_PACKAGE','evidence_status':'CONSUMED_VALIDATION_SET_AND_DEVELOPMENT_REMEDIATION_DATA','files':failure})
 # Local pinned dependency copy; no installation or protected-input bytecode writes.
 shutil.copytree(B/'candidate_v4r/_deps',O/'candidate_v4br/_deps',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
 print('Baseline and exact B01 copies complete',len(rows),len(failure),flush=True)
