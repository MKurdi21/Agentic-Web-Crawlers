"""Independent archive reader; does not import the package builder."""
from pathlib import Path,PurePosixPath
import hashlib,json,zipfile,csv,unicodedata
O=Path(__file__).resolve().parent;Z=O.parent/'phase4bc_path_containment_package.zip'
def h(b):return hashlib.sha256(b).hexdigest()
def read(n):return json.loads((O/n).read_text(encoding='utf-8'))
m=read('PACKAGE_MANIFEST.json');expected={x['path']:x for x in m['files']};expected['PACKAGE_MANIFEST.json']={'sha256':h((O/'PACKAGE_MANIFEST.json').read_bytes()),'size_bytes':(O/'PACKAGE_MANIFEST.json').stat().st_size}
# Metadata paths may name sources. Original source bodies/hashes must not be packaged.
protected=list(csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig')))
source_hashes={x['sha256'] for x in protected if Path(x['path']).suffix.lower() in ['.pdf','.png','.jpg','.jpeg','.zip','.sqlite','.db'] or ('summar' in x['path'].lower() and Path(x['path']).suffix.lower() in ['.txt','.md'])}
fail=[]
with zipfile.ZipFile(Z) as z:
    names=z.namelist()
    if z.testzip() is not None:fail.append('CRC')
    if set(names)!=set(expected):fail.append('MEMBERSHIP')
    if len(names)!=len(set(names)) or len(names)!=len({unicodedata.normalize('NFC',n).casefold() for n in names}):fail.append('COLLISION')
    for n in names:
        p=PurePosixPath(n)
        if p.is_absolute() or '..' in p.parts or '\\' in n or ':' in n:fail.append('PATH:'+n)
        if any(t in p.parts for t in ['private_test_storage','private_diagnostic_material','recovery_coordination','shadow','__pycache__']):fail.append('PRIVATE:'+n)
        if p.suffix not in ['.md','.py','.json']:fail.append('TYPE:'+n)
        b=z.read(n);e=expected[n]
        if h(b)!=e['sha256'] or len(b)!=e['size_bytes']:fail.append('HASH:'+n)
        if h(b) in source_hashes:fail.append('PROTECTED_CONTENT:'+n)
        if b.startswith((b'%PDF-',b'PK\x03\x04',b'SQLite format 3',b'\x89PNG',b'\xff\xd8\xff')):fail.append('CONTENT_SIGNATURE:'+n)
    manifest_equal=z.read('PACKAGE_MANIFEST.json')==(O/'PACKAGE_MANIFEST.json').read_bytes()
    if not manifest_equal:fail.append('MANIFEST_BYTES')
receipt={'status':'PASS' if not fail else 'FAIL','path':str(Z),'sha256':h(Z.read_bytes()),'member_count':len(names),'failures':fail,'checks':['CRC','exact membership','member hashes and sizes','duplicate/case collisions','traversal','private roots','forbidden extensions','binary source signatures','protected source hashes'],'limitations':'Constrained authored outputs and exact allowlist are primary controls; signatures cannot prove absence of every transformed excerpt. Code may contain synthetic fixture literals and names of prohibited operations without containing original source material.','package_manifest_sha256':h((O/'PACKAGE_MANIFEST.json').read_bytes()),'handoff_convention':'Archived FINAL_HANDOFF references this external receipt; external handoff adds archive hash without modifying the ZIP.'}
(O/'PACKAGE_RECEIPT.json').write_text(json.dumps(receipt,indent=2,sort_keys=True),encoding='utf-8')
assert not fail,fail
handoff=read('FINAL_HANDOFF.json');handoff['package']['sha256']=receipt['sha256'];(O/'FINAL_HANDOFF.json').write_text(json.dumps(handoff,indent=2,sort_keys=True),encoding='utf-8')
print('ARCHIVE PASS',receipt['member_count'],receipt['sha256'])
