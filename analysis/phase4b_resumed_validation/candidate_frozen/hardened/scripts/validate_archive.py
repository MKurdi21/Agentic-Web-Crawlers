"""Independent archive membership/hash/private-material checks; no builder invocation."""
import zipfile,base64,csv
from common import *
def verify_archive(path,manifest):
 expected={'integration_design/'+r['path']:r for r in manifest['allowlist']};expected['integration_design/PACKAGE_MANIFEST.json']=None
 original=json.loads((DESIGN/'test_results/INITIAL_BASELINE.json').read_text());hashes={v['sha256'] for v in original['files'].values()}
 samples=[]
 with (WORKSPACE/'analysis/workspace_audit/ARTIFACT_INVENTORY.csv').open(encoding='utf-8-sig') as f:
  for r in csv.DictReader(f):
   p=WORKSPACE/r['artifact_path']
   if p.suffix in ('.md','.txt','.log') and p.stat().st_size>1024:
    data=p.read_bytes()
    for start in (0,len(data)//2,max(0,len(data)-512)):samples.extend([data[start:start+512],base64.b64encode(data[start:start+512])])
 with zipfile.ZipFile(path) as z:
  names=z.namelist()
  if len(names)!=len(set(n.casefold() for n in names)) or set(names)!=set(expected):raise Failure('ARCHIVE_MEMBERSHIP')
  for name in names:
   p=pathlib.PurePosixPath(name)
   if p.is_absolute() or '..' in p.parts or '\\' in name or ':' in name or any(x in p.parts for x in ('shadow','private_source_material','_deps','.agents','.codex-plugin','__pycache__')):raise Failure('ARCHIVE_BOUNDARY')
   if p.suffix.lower() in ('.pdf','.png','.jpg','.jpeg','.sqlite3','.db','.zip','.log','.pyc') or p.name.lower() in ('article.txt','accessibility.json','baseline.json','checkpoint.json','reviews.json','prompt.md','agents.md') or p.name.endswith('_comprehensive_summary.md'):raise Failure('ARCHIVE_FORBIDDEN_TYPE')
   data=z.read(name)
   if sha(data) in hashes or any(s in data for s in samples) or data.startswith((b'%PDF-',b'\x89PNG',b'SQLite format 3')):raise Failure('ARCHIVE_PRIVATE_CONTENT')
   r=expected[name]
   if r and (sha(data)!=r['sha256'] or len(data)!=r['size']):raise Failure('ARCHIVE_HASH')
  if json.loads(z.read('integration_design/PACKAGE_MANIFEST.json'))!=manifest:raise Failure('ARCHIVE_MANIFEST')
  if z.testzip() is not None:raise Failure('ARCHIVE_CRC')
 return {'passed':True,'member_count':len(names),'sha256':digest(path),'size_bytes':pathlib.Path(path).stat().st_size,'archive_integrity':'PASS','private_material_present':False,'exact_allowlist_match':True}
if __name__=='__main__':
 result=verify_archive(DESIGN.parent/'integration_design_package.zip',json.loads((DESIGN/'PACKAGE_MANIFEST.json').read_text()));write_json(DESIGN/'test_results/PACKAGE_RECEIPT.json',result);print(canonical(result))
