"""Explicit allowlist archive builder. Never recursively ZIP integration_design."""
import base64,csv,zipfile
from common import *
from build_docs import DOCS
REPORTS=['INITIAL_BASELINE.json','AUDIT_CONSUMPTION.json','COMPATIBILITY_EXPORT.json','IDEMPOTENCY_REPORT.json','BACKUP_REPORT.json','CALIBRATION_FIXTURES.json','UNIT_INTEGRATION_RESULTS.json','STATIC_CHECKS.json','PRESERVATION_REPORT.json','COMPLETION_REPORT.json','REQUIREMENTS_TRACEABILITY.json','TEST_RESULTS.md']
ROOTS=set(n+'.md' for n in DOCS)|{'OPEN_DECISIONS.md','WEB_ARCHITECTURE_SOURCES.md','REFERENCE_DESIGN_DISPOSITION.md','CHANGE_PLAN.csv','INSTALL_MANIFEST.json','requirements.txt'}
FORBIDDEN_EXT={'.pdf','.png','.jpg','.jpeg','.gif','.webp','.sqlite','.sqlite3','.db','.zip','.log','.pyc'}
FORBIDDEN_NAMES={'article.txt','accessibility.json','generation.log','checkpoint.json','baseline.json','reviews.json','manifest.csv','prompt.md','agents.md'}
def allowed(rel):
 p=pathlib.PurePosixPath(rel)
 if p.is_absolute() or '..' in p.parts or '\\' in rel or ':' in rel:return False
 if any(x in p.parts for x in ['shadow','_deps','__pycache__','.agents','.codex-plugin']):return False
 if p.suffix.lower() in FORBIDDEN_EXT or p.name.lower() in FORBIDDEN_NAMES or p.name.endswith('_comprehensive_summary.md'):return False
 if len(p.parts)==1:return rel in ROOTS
 if p.parts[0]=='test_results':return len(p.parts)==2 and p.name in REPORTS
 if p.parts[0]=='hardened':
  return len(p.parts)==3 and ((p.parts[1] in ('scripts','tests') and p.suffix=='.py') or (p.parts[1]=='schemas' and p.name.endswith('.schema.json')) or rel=='hardened/db/schema_v2.sql')
 if p.parts[0]=='deploy_payload':return p.name=='AGENTS.proposed.md' and len(p.parts)==2 or len(p.parts)==4 and p.parts[1]=='skills' and p.name=='SKILL.md' or len(p.parts)==3 and p.parts[1]=='protocols' and p.suffix=='.md'
 return False
def original_signatures():
 baseline=json.loads((DESIGN/'test_results/INITIAL_BASELINE.json').read_text());hashes={r['sha256'] for r in baseline['files'].values()};samples=[]
 with (WORKSPACE/'analysis/workspace_audit/ARTIFACT_INVENTORY.csv').open(encoding='utf-8-sig') as f:rows=list(csv.DictReader(f))
 for row in rows:
  p=WORKSPACE/row['artifact_path']
  if p.suffix.lower() in ('.md','.txt','.log') and p.stat().st_size>1024:
   data=p.read_bytes();positions=[0,len(data)//2,max(0,len(data)-512)]
   for start in positions:
    sample=data[start:start+512]
    if len(sample)==512:samples.extend([sample,base64.b64encode(sample)])
 return hashes,samples
def inspect_candidate(rel,data,hashes,samples):
 if not allowed(rel):raise Failure('PACKAGE_FORBIDDEN_PATH',rel)
 if sha(data) in hashes or any(sample in data for sample in samples) or data.startswith((b'%PDF-',b'\x89PNG',b'SQLite format 3')):raise Failure('PACKAGE_PRIVATE_CONTENT',rel)
def inventory():
 paths=[DESIGN/p for p in sorted(ROOTS)]+[DESIGN/'test_results'/p for p in REPORTS]
 for sub in ['hardened/scripts','hardened/tests','hardened/schemas','hardened/db']:
  paths.extend(p for p in (DESIGN/sub).iterdir() if p.is_file())
 paths.extend(p for p in (DESIGN/'deploy_payload').rglob('*') if p.is_file())
 hashes,samples=original_signatures();rows=[]
 for p in sorted(set(paths)):
  if not p.is_file():raise Failure('PACKAGE_MISSING_OUTPUT',str(p))
  guard(p,DESIGN);rel=p.relative_to(DESIGN).as_posix();data=p.read_bytes();inspect_candidate(rel,data,hashes,samples);rows.append({'path':rel,'size':len(data),'sha256':sha(data),'classification':'PACKAGEABLE_DESIGN_OUTPUT'})
 return rows
def build():
 rows=inventory();manifest={'version':2,'allowlist':rows,'never_package':['shadow/','_deps/'],'self_entry':'PACKAGE_MANIFEST.json','self_hash':'Excluded to avoid self-reference; archive SHA in external receipt','content_scanning_limitations':'Known hashes and selected 512-byte raw/base64 samples; not arbitrary steganography detection. Exact allowlist and constrained exports are primary.'}
 write_json(DESIGN/'PACKAGE_MANIFEST.json',manifest)
 target=DESIGN.parent/'integration_design_package.zip'
 with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
  for r in rows:z.write(DESIGN/r['path'],'integration_design/'+r['path'])
  z.write(DESIGN/'PACKAGE_MANIFEST.json','integration_design/PACKAGE_MANIFEST.json')
 return target
if __name__=='__main__':print(build())
