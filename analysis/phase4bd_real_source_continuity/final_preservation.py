"""Final external check without changing any packaged artifact bytes."""
from pathlib import Path
import csv,json,hashlib,subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
O=Path(__file__).resolve().parent;R=O.parents[1]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
rows=list(csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig')))
def compare(x):return x['path'] if not (R/x['path']).is_file() or sha(R/x['path'])!=x['sha256'] else None
with ThreadPoolExecutor(max_workers=12) as pool:changed=[x for x in pool.map(compare,rows) if x]
git=subprocess.run(['git','--no-optional-locks','status','--porcelain=v1','--untracked-files=all'],cwd=R,capture_output=True,check=True).stdout
def filtergit(b):return sorted(x for x in b.decode(errors='replace').splitlines() if 'analysis/phase4bd_real_source_continuity' not in x)
same=filtergit(git)==filtergit((O/'GIT_STATUS_INITIAL.txt').read_bytes())
assert json.loads((R/'analysis/reviews.json').read_text(encoding='utf-8-sig'))=={}
reserved=json.loads((O/'B02_B08_UNTOUCHED_CHECK.json').read_text())
assert all(sha(R/x['path'])==x['source_sha256'] and not x['consumed'] and not x['substantive_access'] for x in reserved['reports'])
receipt=json.loads((O/'PACKAGE_RECEIPT.json').read_text());assert sha(R/receipt['path'])==receipt['sha256'] and receipt['status']=='PASS'
report={'status':'PASS' if not changed and same else 'FAIL','at':datetime.now(timezone.utc).isoformat(),'protected_files_checked':len(rows),'changed':changed,'git_outside_boundary_matches':same,'reserved_untouched':7,'reserved_consumed':0,'live_source_verified':0,'live_promoted':0,'package_sha256':receipt['sha256'],'scope':'Final streaming hashes plus previously validated source-access inventory; not OS-wide access audit'}
(O/'PRESERVATION_FINAL.json').write_text(json.dumps(report,sort_keys=True,indent=2),encoding='utf-8')
print(json.dumps(report));assert report['status']=='PASS'
