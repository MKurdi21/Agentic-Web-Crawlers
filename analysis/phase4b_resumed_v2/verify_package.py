"""Independent ZIP validation; no package builder import."""
import json,csv,hashlib,zipfile,sys
from pathlib import Path,PurePosixPath
O=Path(__file__).resolve().parent;Z=O.parent/'phase4b_resumed_v2_package.zip'
def h(b):return hashlib.sha256(b).hexdigest()
m=json.loads((O/'PACKAGE_MANIFEST.json').read_text());expected={x['path']:x for x in m['files']};expected['PACKAGE_MANIFEST.json']={'sha256':h((O/'PACKAGE_MANIFEST.json').read_bytes()),'size_bytes':(O/'PACKAGE_MANIFEST.json').stat().st_size}
rows=list(csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig')))
sourcehashes={x['sha256'] for x in rows if Path(x['path']).suffix.lower() in ['.pdf','.zip','.db','.sqlite','.png','.jpg'] or 'summar' in x['path'].lower()}
with zipfile.ZipFile(Z) as z:
    names=z.namelist();assert z.testzip() is None
    assert set(names)==set(expected) and len(names)==len(set(names))==len({n.casefold() for n in names})
    for n in names:
        p=PurePosixPath(n);assert not p.is_absolute() and '..' not in p.parts and '\\' not in n and ':' not in n
        assert not any(x in p.parts for x in ['private_source_material','rehearsal_runtime','shadow','__pycache__','private_diagnostics'])
        assert p.suffix in ['.json','.jsonl','.md','.csv','.py']
        b=z.read(n);assert len(b)==expected[n]['size_bytes'] and h(b)==expected[n]['sha256'] and h(b) not in sourcehashes
        assert not b.startswith((b'%PDF-',b'SQLite format 3',b'PK\x03\x04',b'\x89PNG'))
receipt={'status':'PASS','sha256':h(Z.read_bytes()),'path':str(Z),'members':len(names),'checks':['CRC','exact membership','hashes/sizes','duplicates/case','traversal','forbidden paths/types/signatures','protected-source hashes'],'limits':'Exact authored-file allowlist is primary isolation; signature scan does not prove absence of every possible transformed excerpt. No source was parsed or copied in this run.','manifest_sha256':h((O/'PACKAGE_MANIFEST.json').read_bytes())}
(O/'PACKAGE_RECEIPT.json').write_text(json.dumps(receipt,sort_keys=True,indent=2),encoding='utf-8')
f=json.loads((O/'FINAL_HANDOFF.json').read_text());f['package']['sha256']=receipt['sha256'];(O/'FINAL_HANDOFF.json').write_text(json.dumps(f,sort_keys=True,indent=2),encoding='utf-8')
sys.path.insert(0,str(O.parent/'phase4bc_supplement/recovery_protocol'))
from engine import Engine,canonical
e=Engine(O)
with e.lock('/root-complete'):
    started=e.begin('PACKAGE_VERIFIED',{'archive':receipt['sha256']},['outputs/package_receipt.json'])
    if not started.get('already_committed'):
        e.commit({'outputs/package_receipt.json':canonical(receipt)},next_operation='STOP_NO_GO_WITHOUT_SOURCE_ACCESS')
    if e.state()['status']!='RUN_COMPLETE':e.finish()
print('PACKAGE PASS',receipt['members'],receipt['sha256'])
