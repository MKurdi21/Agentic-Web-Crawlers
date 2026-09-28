import hashlib,json,sys
from pathlib import Path
O=Path(__file__).resolve().parent;C=O/'candidate_v4br';sys.path.insert(0,str(C/'hardened/scripts'))
from pre_access import commit_preaccess,open_source,digest,canonical
files=[{'path':p.relative_to(C).as_posix(),'sha256':digest(p.read_bytes())} for p in sorted(C.rglob('*')) if p.is_file() and not set(p.relative_to(C).parts)&{'_deps','test_runtime','__pycache__','shadow','test_results'}]
manifest_hash=digest(canonical(files))
source=O/'private_source_material/original_phase4b/private_source_material/B01/source.pdf'
binding={'phase':'PHASE4BR_DEVELOPMENT_ADJUDICATION','holdout_id':'B01','paper_id':'report_e30d9cfd6055ddd8e085a0ff','source_file_id':'source_'+digest(source.read_bytes()),'source_sha256':digest(source.read_bytes()),'candidate_manifest_sha256':manifest_hash,'methodology_sha256':'ab28253c49940db4cd28ba0ea224185c8f3b03289312dba3c64322a33d95f1bb','protocol_hashes':{'pre_access':digest((C/'hardened/scripts/pre_access.py').read_bytes())},'field_catalog_sha256':digest((C/'frozen_inputs/phase3/FIELD_CATALOG.json').read_bytes()),'holdout_state':'DEVELOPMENT_REMEDIATION_DATA','context_protocol_version':'phase4br-development-context-v1'}
receipt_dir=O/'private_source_material/access/adjudication'
commit_preaccess(receipt_dir,binding,allowed_reports={'B01'})
data=open_source(receipt_dir,source,binding,allowed_reports={'B01'})
(O/'B01_ADJUDICATION_ACCESS.json').write_text(json.dumps({'binding':binding,'receipt_directory':receipt_dir.relative_to(O).as_posix(),'bytes_confirmed':len(data),'mode':'DEVELOPMENT_ONLY'},indent=2)+'\n')
print('Durable pre-access receipt and subsequent source-access event recorded')
