"""Independent finished-archive validation; no import of builder helpers."""
import zipfile,json,hashlib,csv,re
from pathlib import Path,PurePosixPath
O=Path(__file__).resolve().parent;R=O.parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
archive=R/'analysis/phase4br_remediation_package.zip'
protected={x['sha256'] for x in csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8')) if Path(x['path']).suffix.lower() in ('.pdf','.png','.jpg','.jpeg','.txt') or ('summary' in Path(x['path']).name.lower() and Path(x['path']).suffix.lower()=='.md')}
fail=[]
with zipfile.ZipFile(archive) as z:
    names=z.namelist();manifest=json.loads(z.read('PACKAGE_MANIFEST.json'));allow={x['path']:x for x in manifest['allowlist']}
    if len(names)!=len(set(names)) or len(names)!=len({x.casefold() for x in names}):fail.append('duplicate/case collision')
    if set(names)!=set(allow)|{'PACKAGE_MANIFEST.json'}:fail.append('membership mismatch')
    if z.testzip() is not None:fail.append('CRC failure')
    for n in names:
        p=PurePosixPath(n);b=z.read(n);suffix=p.suffix.lower()
        if p.is_absolute() or '..' in p.parts or '\\' in n or ':' in n:fail.append('unsafe path '+n)
        if any(x in p.parts for x in ['private_source_material','shadow','rehearsal_runtime','_deps','__pycache__','outbox']):fail.append('private/runtime member '+n)
        if suffix in ['.pdf','.png','.jpg','.jpeg','.db','.sqlite','.zip','.bak','.pyc'] or suffix=='.txt' and p.name!='requirements.txt':fail.append('forbidden type '+n)
        if b.startswith((b'%PDF-',b'\x89PNG',b'PK\x03\x04',b'SQLite format 3')):fail.append('forbidden signature '+n)
        if sha(b) in protected and p.name!='requirements.txt':fail.append('protected source bytes '+n)
        if b'='*10+b' PDF PAGE ' in b:fail.append('full article extraction '+n)
        if n in allow and (sha(b)!=allow[n]['sha256'] or len(b)!=allow[n]['size_bytes']):fail.append('content mismatch '+n)
    # No packaged development graph may reconstruct full paper tables.
    if any('development_graphs/' in x or '/original_phase4b/' in x for x in names):fail.append('private development content')
receipt={'phase':'PHASE4BR','path':str(archive),'sha256':sha(archive.read_bytes()),'size_bytes':archive.stat().st_size,'archive_member_count':len(names),'allowlist_content_count':len(allow),'crc_passed':not any('CRC' in x for x in fail),'exact_membership_and_hashes':not fail,'failures':fail,'passed':not fail,'validation_independence':'Separate implementation reopens completed archive; no builder functions imported. Content scanners have limits; exact allowlisting and private storage separation are primary controls.'}
(O/'PACKAGE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt));raise SystemExit(bool(fail))
