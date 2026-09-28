"""Read-only historical preparation receipt validation; never treats mutable views as historical authority."""
from pathlib import Path
import hashlib,json

def validate(root):
    root=Path(root).resolve()
    digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    receipt=json.loads((root/'milestone_receipts/PREPARATION_VERSION_AUTHORITY_RECONCILIATION.json').read_bytes())
    mapping=root/receipt['map_path']
    assert digest(mapping)==receipt['map_sha256'],'VERSION_MAP_CHANGED'
    data=json.loads(mapping.read_bytes()); rows=data['entries'];seen=set()
    for row in rows:
        key=(row['unit'],row['historical_path']);assert key not in seen,'DUPLICATE_VERSION';seen.add(key)
        original=root/'milestone_receipts'/ (row['unit']+'.json')
        assert digest(original)==row['original_receipt_sha256'],'ORIGINAL_RECEIPT_CHANGED'
        authority=json.loads(original.read_bytes())['outputs']
        assert authority[row['historical_path']]==row['historical_sha256'],'HISTORICAL_BINDING_CHANGED'
        artifact=(root/row['immutable_artifact_path']).resolve()
        assert artifact.is_relative_to(root/'NEVER_PACKAGE/immutable_preparation_versions'),'VERSION_PATH_ESCAPE'
        assert digest(artifact)==row['historical_sha256']==row['immutable_sha256'],'HISTORICAL_BYTES_CHANGED'
    expected={(unit,p) for unit in {x['unit'] for x in rows} for p in json.loads((root/'milestone_receipts'/(unit+'.json')).read_bytes())['outputs']}
    assert seen==expected,'INCOMPLETE_VERSION_MAP'
    return {'status':'PASS','verified_count':len(rows),'authority':'IMMUTABLE_VERSION_ARTIFACTS','mutable_views':'NON_AUTHORITATIVE'}

if __name__=='__main__':
    print(json.dumps(validate(Path(__file__).parent)))
