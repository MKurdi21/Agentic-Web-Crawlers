"""Explicit release inventory only. Never recursively ZIP the Phase4BR tree."""
import json,hashlib,zipfile,csv
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(b):return hashlib.sha256(b).hexdigest()
ROOTS='''EXECUTIVE_PHASE4BR.md PHASE4BR_BASELINE.json INPUT_DRIFT_REPORT.md PHASE4B_B01_FAILURE_MANIFEST.json B01_SUPPORT_ADJUDICATION.md B01_SUPPORT_ADJUDICATION.json B01_SUPPORT_ADJUDICATION_MATRIX.csv B01_SUPPORT_ROOT_CAUSE_TAXONOMY.md B01_SUPPORT_ROOT_CAUSE_TAXONOMY.json PROPOSITION_SUPPORT_MODEL.md SUPPORT_LOCATOR_ROLE_MODEL.md COMPARATIVE_SUPPORT_PROTOCOL.md PER_REPORT_PRE_ACCESS_RECEIPT_PROTOCOL.md VERIFICATION_PROTOCOL_V3.md SCHEMA_MIGRATION_NOTE.md SKILL_REMEDIATION_REPORT.md REMEDIATION_DEVELOPMENT_RESULTS.md REMEDIATION_DEVELOPMENT_METRICS.json REMEDIATED_WORKFLOW_CONFIGURATION.json CANDIDATE_CODE_MANIFEST.json DEPENDENCY_MANIFEST.json B02_B08_RESERVATION_MANIFEST.json PHASE4B_RESUME_HOLDOUT_MANIFEST.json PHASE4B_RESUME_PLAN.md DEVELOPMENT_ITEM_CROSSWALK.json PRESERVATION_CHECK.json REVIEW_FINDINGS_AND_RESOLUTIONS.md HANDOFF_SNAPSHOT.json PACKAGE_POLICY.md package_phase4br.py validate_package_phase4br.py'''.split()
TESTS=['UNIT_INTEGRATION_RESULTS.json','B01_REGRESSION_RESULTS.json','B01_DEVELOPMENT_GRAPH_RESULTS.json','PRE_ACCESS_FINAL_RECEIPT_CHECK.json','INACTIVE_PAYLOAD_AND_TEST_PRESERVATION.json','INDEPENDENT_EQUIVALENCE_CHECK.json']
if __name__=='__main__':
    cfg=read(O/'CANDIDATE_CODE_MANIFEST.json')
    paths=list(ROOTS)+['test_results/'+x for x in TESTS]+['candidate_v4br/'+x['relative_path'] for x in cfg['immutable_files']]
    paths+=['candidate_v4br/test_results/INITIAL_BASELINE.json']
    for root in ('b01_failure_fixtures','phase4_failure_fixtures'):
        paths += [p.relative_to(O).as_posix() for p in sorted((O/root).glob('*.json'))]
    assert len(paths)==len(set(paths))
    forbidden_hashes={r['sha256'] for r in csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8')) if Path(r['path']).suffix.lower() in ('.pdf','.png','.jpg','.jpeg','.txt') or 'summary' in Path(r['path']).name.lower() and Path(r['path']).suffix.lower()=='.md'}
    entries=[]
    for rel in sorted(paths):
        p=O/rel;data=p.read_bytes();h=sha(data)
        assert h not in forbidden_hashes or p.name=='requirements.txt',('PROTECTED_RESEARCH_BYTES',rel)
        assert not any(s in Path(rel).parts for s in ('private_source_material','shadow','_deps','__pycache__','rehearsal_runtime'))
        assert p.suffix.lower() in ('.md','.json','.csv','.py','.sql','.txt','.yaml','.yml'),rel
        assert not data.startswith((b'%PDF-',b'\x89PNG',b'PK\x03\x04',b'SQLite format 3')),rel
        if p.suffix=='.txt':assert p.name=='requirements.txt'
        # Original article extracts/renderings are never eligible; path references in reports are metadata.
        assert b'='*10+b' PDF PAGE ' not in data,rel
        entries.append({'path':rel,'size_bytes':len(data),'sha256':h,'classification':'PACKAGEABLE_DESIGN_OUTPUT'})
    manifest={'phase':'PHASE4BR','archive_self_member':'PACKAGE_MANIFEST.json','allowlist':entries,'never_package_roots':['private_source_material','candidate_v4br/shadow','candidate_v4br/_deps','rehearsal_runtime'],'external_receipts':['FINAL_HANDOFF.json','PACKAGE_RECEIPT.json','INDEPENDENT_FINAL_REVIEW.json'],'self_hash_rule':'Manifest does not list its own hash. ZIP hash lives in external receipts; HANDOFF_SNAPSHOT is immutable package-time handoff.'}
    (O/'PACKAGE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    archive=R/'analysis/phase4br_remediation_package.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for e in entries:z.write(O/e['path'],e['path'])
        z.write(O/'PACKAGE_MANIFEST.json','PACKAGE_MANIFEST.json')
    print(json.dumps({'archive':str(archive),'sha256':sha(archive.read_bytes()),'members':len(entries)+1}))
