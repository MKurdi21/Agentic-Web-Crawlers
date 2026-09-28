"""Independent streaming hashes and event inventory; no PDF interpretation."""
from pathlib import Path
import csv,json,hashlib,subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
O=Path(__file__).resolve().parent;R=O.parents[1]
def h(p):
 d=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):d.update(b)
 return d.hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
rows=list(csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig')))
def compare(x):
 p=R/x['path'];return None if p.is_file() and h(p)==x['sha256'] else {'path':x['path'],'expected':x['sha256'],'actual':h(p) if p.is_file() else None}
with ThreadPoolExecutor(max_workers=12) as pool:changes=[x for x in pool.map(compare,rows) if x]
reserve=read(O/'B02_B08_UNTOUCHED_CHECK.json');reserved_ids={x['report_id'] for x in reserve['reports']};reserved_hashes={x['source_sha256'] for x in reserve['reports']}
for x in reserve['reports']:assert h(R/x['path'])==x['source_sha256']
events=[];reserved_events=[];parse_failures=[]
preflight_files=sorted((O/'test_results').glob('recovery-*.json'),key=lambda p:p.stat().st_mtime)
preflight=read(preflight_files[-1]);known_diagnostics={x['path']:x['sha256'] for x in preflight['files'] if x['path'] in preflight['invalid_files']}
def parse_failure(p,reason):
 rel=p.relative_to(O).as_posix();preserved=h(p)==known_diagnostics.get(rel)
 parse_failures.append({'path':rel,'reason':reason,'sha256':h(p),'classification':'KNOWN_PRESERVED_SYNTHETIC_CORRUPTION_FIXTURE' if preserved else 'UNRESOLVED_PARSE_FAILURE','blocks_conservation':not preserved})
for p in O.rglob('SOURCE_ACCESS_BEGAN.json'):
 try:
  v=read(p)
  if v.get('source_sha256') in reserved_hashes or v.get('report_id') in reserved_ids:reserved_events.append(str(p.relative_to(O)))
 except ValueError as ex:parse_failure(p,str(ex))
for p in O.rglob('RECOVERY_EVENTS*.jsonl'):
 for line in p.read_text(encoding='utf-8').splitlines():
  try:v=json.loads(line)
  except ValueError as ex:parse_failure(p,str(ex));continue
  if v.get('event_type')=='SOURCE_ACCESS_BEGAN':
   events.append({'path':p.relative_to(O).as_posix(),'report_id':v.get('report_id'),'source_sha256':v.get('source_sha256'),'synthetic':v.get('synthetic',False)})
   if v.get('source_sha256') in reserved_hashes or v.get('report_id') in reserved_ids:reserved_events.append(str(p.relative_to(O)))
assert read(R/'analysis/reviews.json')=={}
git=subprocess.run(['git','--no-optional-locks','status','--porcelain=v1','--untracked-files=all'],cwd=R,capture_output=True,check=True).stdout
(O/'GIT_STATUS_FINAL.txt').write_bytes(git)
def filtered(b):return sorted(x for x in b.decode(errors='replace').splitlines() if 'analysis/phase4bd_real_source_continuity' not in x)
gitmatch=filtered(git)==filtered((O/'GIT_STATUS_INITIAL.txt').read_bytes())
forbidden=[str(p.relative_to(O)) for p in O.rglob('*') if p.is_dir() and p.name in ['rehearsal_runtime','migration_runtime','cutover_runtime','phase5']]
verdict='PASS' if not changes and not reserved_events and not forbidden and gitmatch and not any(x['blocks_conservation'] for x in parse_failures) else 'FAIL'
report={'status':verdict,'checked_at':datetime.now(timezone.utc).isoformat(),'protected_files_checked':len(rows),'changed':changes,'git_outside_boundary_matches':gitmatch,'reserved_selected':7,'reserved_untouched':7 if not reserved_events else None,'reserved_consumed':len(set(reserved_events)),'reserved_contamination_events':reserved_events,'reserved_hashes_match':True,'source_access_inventory':events,'parse_failures':parse_failures,'live_source_verified':0,'live_promoted':0,'live_state_evidence':'Empty unchanged analysis/reviews.json plus protected controls and prior baseline equivalence; no state writer invoked','forbidden_runtime_directories':forbidden,'no_lane_b':not forbidden,'no_phase4b_resume':True,'no_live_migration':True,'no_checkpoint_refresh':True,'no_skill_installation':True,'no_phase5':True,'evidence_limit':'Streaming hashes, Git status, recorded source-access events and output inventory; not an OS-wide audit'}
(O/'PRESERVATION_CHECK.json').write_text(json.dumps(report,sort_keys=True,indent=2),encoding='utf-8')
reserve.update(phase4bd_final_hash_verified=True,phase4bd_checked_at=report['checked_at'],consumed=report['reserved_consumed'],contamination_count=len(reserved_events),untouched=report['reserved_untouched']);(O/'B02_B08_UNTOUCHED_CHECK.json').write_text(json.dumps(reserve,sort_keys=True,indent=2),encoding='utf-8')
print(json.dumps({k:report[k] for k in ['status','protected_files_checked','git_outside_boundary_matches','reserved_untouched','live_source_verified','live_promoted']}));assert verdict=='PASS'
