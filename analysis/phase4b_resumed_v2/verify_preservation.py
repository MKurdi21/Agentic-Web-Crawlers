"""Separate final verifier; streamed hashes only, no scientific parsing."""
import csv,hashlib,json,subprocess
from pathlib import Path
from datetime import datetime,timezone
O=Path(__file__).resolve().parent;R=O.parents[1]
def h(p):
 d=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):d.update(b)
 return d.hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
rows=list(csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig')));changed=[]
for i,x in enumerate(rows,1):
 p=R/x['path']
 if not p.is_file() or h(p)!=x['sha256']:changed.append(x['path'])
 if i%4000==0:print('Final hashes',i,flush=True)
git=subprocess.run(['git','status','--porcelain=v1','--untracked-files=all'],cwd=R,capture_output=True,check=True).stdout
(O/'GIT_STATUS_FINAL.txt').write_bytes(git)
def strip(data):return [x for x in data.decode().splitlines() if 'analysis/phase4b_resumed_v2/' not in x and 'analysis/phase4b_resumed_v2_package.zip' not in x]
same=strip(git)==strip((O/'GIT_STATUS_INITIAL.txt').read_bytes())
events=[json.loads(x) for x in (O/'RECOVERY_EVENTS.jsonl').read_text().splitlines()];access=[x for x in events if x['event_type']=='SOURCE_ACCESS_BEGAN']
tracker=read(O/'HOLDOUT_STATE_TRACKER.json');untouched=all(not x['consumed'] and not x['substantive_access'] for x in tracker['reports'])
reviews_empty=read(R/'analysis/reviews.json')=={}
unexpected_runtime=[str(p.relative_to(O)) for p in O.rglob('*') if p.is_file() and p.suffix.lower() in ['.pdf','.sqlite','.db','.png','.jpg']]
ok=not changed and same and not access and untouched and reviews_empty and not unexpected_runtime and not (O/'rehearsal_runtime').exists()
r={'status':'PASS' if ok else 'FAIL','at':datetime.now(timezone.utc).isoformat(),'protected_count':len(rows),'changed':changed,'git_protected_status_unchanged':same,'source_access_events':len(access),'untouched':7 if untouched else None,'consumed':0 if untouched else None,'contamination_events':0,'live_source_verified':0 if reviews_empty else 'UNKNOWN','live_promoted':0 if reviews_empty else 'UNKNOWN','runtime_or_source_artifacts':unexpected_runtime,'lane_b_created':False,'evidence_limit':'Recorded events/inventory and streamed hashes; not OS-wide access audit','independence':'Separate verification script, no producer counting helpers; same host and hashlib dependency'}
(O/'PRESERVATION_CHECK.json').write_text(json.dumps(r,sort_keys=True,indent=2),encoding='utf-8')
assert ok,r
f=read(O/'FINAL_HANDOFF.json');f['preservation']='PASS';f['protected_file_count']=len(rows);(O/'FINAL_HANDOFF.json').write_text(json.dumps(f,sort_keys=True,indent=2),encoding='utf-8')
print('PRESERVATION PASS',len(rows))
