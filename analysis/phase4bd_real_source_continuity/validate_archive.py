"""Independent ZIP-side validator; does not call builder helpers."""
from pathlib import Path,PurePosixPath
import json,hashlib,zipfile
O=Path(__file__).resolve().parent;R=O.parents[1];Z=R/'analysis/phase4bd_real_source_continuity_package.zip'
def sha(b):return hashlib.sha256(b).hexdigest()
forbidden_suffixes={'.pdf','.png','.jpg','.jpeg','.db','.sqlite','.sqlite3','.zip','.bak','.pyc','.pyd','.dll'}
forbidden_parts={'private_development_source_material','inherited_candidate','shadow','outbox','__pycache__','private_diagnostic_material'}
# Independent release inventory: deliberately not imported from builder or ZIP.
expected_roots='''EXECUTIVE_PHASE4BD.md PHASE4BD_BASELINE.json INPUT_DRIFT_REPORT.md REAL_SOURCE_INTEGRATION_FIXTURE.json REAL_SOURCE_CONTINUITY_PROTOCOL.md PACKET_ACKNOWLEDGEMENT.schema.json PRE_ACCESS_RECEIPT.schema.json SOURCE_ACCESS_EVENT.schema.json CONSUMPTION_STATE.schema.json REAL_SOURCE_HELPER_INTEGRATION_REPORT.md REAL_SOURCE_CONTINUITY_TEST_PLAN.md REAL_SOURCE_CONTINUITY_TEST_RESULTS.json FAILURE_BOUNDARY_TEST_REPORT.md FRESH_SESSION_RECOVERY_REPORT.md IDEMPOTENCY_REPORT.md CONTEXT_FIREWALL_RECOVERY_REPORT.md INDEPENDENT_REAL_SOURCE_CONTINUITY_REVIEW.json B02_B08_UNTOUCHED_CHECK.json PHASE4B_RESUME_READINESS_FINAL.md FINAL_HANDOFF.json PRESERVATION_CHECK.json INTEGRATION_MANIFEST.json REQUIREMENTS_TRACEABILITY.json PROTECTED_FILES_INITIAL.csv DEVELOPMENT_AUTHORIZATION.json RECOVERY_PREFLIGHT_SUMMARY.json EXECUTION_ENVIRONMENT.json PACKAGE_CONVENTION.md package_phase.py validate_archive.py check_preservation.py parent_integration_checks.py retained_demo.py'''.split()
expected_code=['integration_layer/'+n for n in ['bridge.py','worker.py','worker_contract.json','runtime_guard.py','cli.py','test_real.py','build_schemas.py']]
expected_tests=['test_results/'+n for n in ['INHERITED_CONTEXT.json','INHERITED_RECOVERY.json','INHERITED_PATH.json','INHERITED_CONTINUITY.json','INHERITED_PARENT_INTEGRATION.json','PACKET_SEMANTIC_REVIEW.json','PACKET_STATIC_SCAN.json','PACKET_BUILD.json','RETAINED_REAL_E2E.json','FINAL_TEST_SUMMARY.json']]
independent_inventory=set(expected_roots+expected_code+expected_tests+['firewall_acceptance.py','test_results/FIREWALL_ACCEPTANCE.json'])
protected_source_hashes=set()
import csv
for row in csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig')):
 p=Path(row['path'])
 if p.suffix.lower()=='.pdf' or p.name=='article.txt' or 'summaries' in p.parts or 'evidence' in p.parts:protected_source_hashes.add(row['sha256'])
with zipfile.ZipFile(Z) as z:
 names=z.namelist();assert len(names)==len(set(names))==len(set(x.casefold() for x in names))
 assert z.testzip() is None
 m=json.loads(z.read('PACKAGE_MANIFEST.json'));expected={x['path']:x for x in m['files']};assert len(expected)==len(m['files']);assert set(expected)==independent_inventory;assert set(names)==independent_inventory|{'PACKAGE_MANIFEST.json'}
 for name in names:
  p=PurePosixPath(name);assert not p.is_absolute() and '..' not in p.parts and '\\' not in name and ':' not in name
  assert not forbidden_parts.intersection(p.parts) and p.suffix.lower() not in forbidden_suffixes and p.name.lower()!='article.txt'
  data=z.read(name);assert not data.startswith(b'%PDF') and sha(data) not in protected_source_hashes
  if name in expected:assert len(data)==expected[name]['size'] and sha(data)==expected[name]['sha256']
  # Packaged structured records cannot be the private extracted development item.
  if p.suffix=='.json':
   obj=json.loads(data)
   def inspect(v):
    if isinstance(v,dict):
     assert not (v.get('namespace')=='DEVELOPMENT_TRANSPORT_ONLY' and 'value' in v)
     for item in v.values():inspect(item)
    elif isinstance(v,list):
     for item in v:inspect(item)
   inspect(obj)
 receipt={'status':'PASS','path':Z.relative_to(R).as_posix(),'sha256':sha(Z.read_bytes()),'members':len(names),'crc':'PASS','membership':'EXACT','hashes':'PASS','path_and_collision_safety':'PASS','forbidden_content_checks':'PASS','private_content_scan_limit':'Constrained output generation, exact allowlist, full protected-source hashes and structured-record checks; not a universal paraphrase detector','packaged_handoff_sha256':sha(z.read('FINAL_HANDOFF.json')),'manifest_sha256':sha(z.read('PACKAGE_MANIFEST.json')),'receipt_location':'EXTERNAL_ONLY'}
(O/'PACKAGE_RECEIPT.json').write_text(json.dumps(receipt,sort_keys=True,indent=2),encoding='utf-8')
hand=json.loads((O/'FINAL_HANDOFF.json').read_text());hand['package']['sha256']=receipt['sha256'];hand['package']['validation']='PASS';hand['edition']='EXTERNAL_FINAL_WITH_ARCHIVE_HASH';(O/'FINAL_HANDOFF.json').write_text(json.dumps(hand,sort_keys=True,indent=2),encoding='utf-8')
print(json.dumps(receipt))
