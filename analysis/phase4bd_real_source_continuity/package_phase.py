"""Exact allowlist packaging; external receipt avoids circular ZIP hashes."""
from pathlib import Path
import json,hashlib,zipfile,sys
O=Path(__file__).resolve().parent;R=O.parents[1];Z=R/'analysis/phase4bd_real_source_continuity_package.zip'
def h(b):return hashlib.sha256(b).hexdigest()
def dump(p,v):p.write_text(json.dumps(v,sort_keys=True,indent=2),encoding='utf-8')
ROOTS='''EXECUTIVE_PHASE4BD.md PHASE4BD_BASELINE.json INPUT_DRIFT_REPORT.md REAL_SOURCE_INTEGRATION_FIXTURE.json REAL_SOURCE_CONTINUITY_PROTOCOL.md PACKET_ACKNOWLEDGEMENT.schema.json PRE_ACCESS_RECEIPT.schema.json SOURCE_ACCESS_EVENT.schema.json CONSUMPTION_STATE.schema.json REAL_SOURCE_HELPER_INTEGRATION_REPORT.md REAL_SOURCE_CONTINUITY_TEST_PLAN.md REAL_SOURCE_CONTINUITY_TEST_RESULTS.json FAILURE_BOUNDARY_TEST_REPORT.md FRESH_SESSION_RECOVERY_REPORT.md IDEMPOTENCY_REPORT.md CONTEXT_FIREWALL_RECOVERY_REPORT.md INDEPENDENT_REAL_SOURCE_CONTINUITY_REVIEW.json B02_B08_UNTOUCHED_CHECK.json PHASE4B_RESUME_READINESS_FINAL.md FINAL_HANDOFF.json PRESERVATION_CHECK.json INTEGRATION_MANIFEST.json REQUIREMENTS_TRACEABILITY.json PROTECTED_FILES_INITIAL.csv DEVELOPMENT_AUTHORIZATION.json RECOVERY_PREFLIGHT_SUMMARY.json EXECUTION_ENVIRONMENT.json PACKAGE_CONVENTION.md'''.split()
CODE=['bridge.py','worker.py','worker_contract.json','runtime_guard.py','cli.py','test_real.py','build_schemas.py']
TEST=['INHERITED_CONTEXT.json','INHERITED_RECOVERY.json','INHERITED_PATH.json','INHERITED_CONTINUITY.json','INHERITED_PARENT_INTEGRATION.json','PACKET_SEMANTIC_REVIEW.json','PACKET_STATIC_SCAN.json','PACKET_BUILD.json','RETAINED_REAL_E2E.json','FINAL_TEST_SUMMARY.json','FIREWALL_ACCEPTANCE.json']
ALLOWED=ROOTS+['integration_layer/'+x for x in CODE]+['test_results/'+x for x in TEST]+['package_phase.py','validate_archive.py','check_preservation.py','parent_integration_checks.py','retained_demo.py','firewall_acceptance.py']
assert len(ALLOWED)==len(set(x.casefold() for x in ALLOWED))
records=[]
protected=json.loads((O/'REAL_SOURCE_INTEGRATION_FIXTURE.json').read_text())['source_sha256']
source_hashes={protected}|{x['source_sha256'] for x in json.loads((O/'B02_B08_UNTOUCHED_CHECK.json').read_text())['reports']}
for name in sorted(ALLOWED):
 p=O/name;data=p.read_bytes();assert p.suffix.lower() in {'.json','.md','.csv','.py'}
 assert not data.startswith(b'%PDF') and h(data) not in source_hashes
 assert not any(part in {'private_development_source_material','inherited_candidate','shadow','__pycache__'} for part in Path(name).parts)
 records.append({'path':name,'size':len(data),'sha256':h(data),'classification':'PACKAGEABLE_DESIGN_OUTPUT'})
manifest={'version':'phase4bd-package-v1','files':records,'self_entry':'PACKAGE_MANIFEST.json','self_hash_convention':'Manifest excludes its own hash; exact membership is files plus this self_entry','excluded_classes':['PDF','source bodies','private development material','runtime state','databases','backups','credentials','caches','prior archives'],'external_receipt':'PACKAGE_RECEIPT.json','external_handoff':'FINAL_HANDOFF.json is finalized after ZIP creation; packaged copy references external receipt'}
dump(O/'PACKAGE_MANIFEST.json',manifest)
assert not Z.exists(),'Do not overwrite a previous archive without explicit diagnostic reconciliation'
with zipfile.ZipFile(Z,'x',compression=zipfile.ZIP_DEFLATED) as z:
 for name in sorted(ALLOWED+['PACKAGE_MANIFEST.json']):z.write(O/name,name)
print(json.dumps({'archive':str(Z),'members':len(ALLOWED)+1,'sha256':h(Z.read_bytes())}))
