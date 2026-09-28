import csv,hashlib,json,pathlib,subprocess,zipfile
from datetime import datetime,timezone
R=pathlib.Path(__file__).resolve().parent;ROOT=R.parents[1]
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
initial=list(csv.DictReader((R/'PROTECTED_FILE_HASHES_INITIAL.csv').open(encoding='utf-8')))
changed=[];missing=[]
for row in initial:
 p=ROOT/row['path']
 if not p.is_file():missing.append(row['path'])
 else:
  actual=digest(p)
  if actual!=row['sha256']:changed.append({'path':row['path'],'initial_sha256':row['sha256'],'final_sha256':actual})
phase1=ROOT/'analysis/workspace_audit_for_integration.zip';phase2=ROOT/'analysis/integration_design_package.zip'
def z(p,expected):
 with zipfile.ZipFile(p) as f:bad=f.testzip();n=len(f.infolist())
 return {'path':p.relative_to(ROOT).as_posix(),'sha256':digest(p),'expected':expected,'member_count':n,'crc_ok':bad is None,'matches':digest(p)==expected}
git=subprocess.run(['git','status','--porcelain=v1','--untracked-files=all'],cwd=ROOT,text=True,capture_output=True)
(R/'GIT_STATUS_FINAL.txt').write_text(git.stdout,encoding='utf-8')
manifest=list(csv.DictReader((ROOT/'analysis/manifest.csv').open(encoding='utf-8-sig')))
pdfs=[p for p in ROOT.rglob('*.pdf') if not p.is_relative_to(R)]
result={'checked_at':datetime.now(timezone.utc).isoformat(),'initial_protected_file_count':len(initial),'missing_count':len(missing),'changed_count':len(changed),'missing':missing,'changed':changed,'phase1':z(phase1,'ae594106080cbe9469d242fb3378079368552178142c4984f3211cce85eb7abd'),'phase2':z(phase2,'8b63bb35d632496bd98303c6878d9030941538180cf47ca5569ba1448fa54b76'),'live_counts':{'physical_pdfs':len(pdfs),'active_reports':len(manifest),'legacy_summaries':len(list((ROOT/'Summaries').glob('*.md'))),'v2_drafts':len(list((ROOT/'.summary_v2').glob('*.md'))),'review_records':len(json.loads((ROOT/'analysis/reviews.json').read_text())),'source_verified':0,'promoted':0},'phase3_paths_only':not missing and not changed,'note':'Git status may include pre-existing and Phase 3 untracked files; content-hash comparison is authoritative for protected files.'}
(R/'PRESERVATION_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'missing':len(missing),'changed':len(changed),'live_counts':result['live_counts'],'phase1':result['phase1']['matches'],'phase2':result['phase2']['matches']}))
