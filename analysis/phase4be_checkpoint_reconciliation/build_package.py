"""Build a metadata-only, allowlisted Phase 4BE-C archive and verify it."""
import hashlib
import json
import pathlib
import zipfile

here=pathlib.Path(__file__).resolve().parent
archive=here.parent/'phase4be_checkpoint_reconciliation_package.zip'
members=[
 'EXECUTIVE_PHASE4BE_C.md','DRIFTED_CHECKPOINT_FORENSIC_SNAPSHOT.json',
 'CHECKPOINT_GENERATOR_ANALYSIS.md','CURRENT_GENERATOR_REPRODUCTION.json',
 'WRITER_ATTRIBUTION_REPORT.md','UNMAPPED_PDF_FORENSIC_INVENTORY.csv',
 'UNMAPPED_PDF_FORENSIC_INVENTORY.json','CORPUS_ACCOUNTING_RECONCILIATION.json',
 'CORPUS_BOUNDARY_POLICY.md','CORPUS_BOUNDARY_POLICY.json','B02_B08_ACCESS_AUDIT.json',
 'POST_CHECKPOINT_PDF_DELTA.json','IO_INCIDENT.json',
 'PYC_CACHE_DRIFT_DIAGNOSTIC.json','PRE_INSTALL_ACCEPTANCE_GATE.json',
 'CHECKPOINT_SCANNER_CHANGE_RECEIPT.json','SCANNER_REGRESSION_TEST_RESULTS.json',
 'candidate/CHECKPOINT.md','candidate/checkpoint.json','CHECKPOINT_CANDIDATE_COMPARISON.json',
 'CHECKPOINT_RECONCILIATION_RECEIPT.json','AUTHORIZED_EXTERNAL_CHANGESET.json',
 'INDEPENDENT_CHECKPOINT_REVIEW.json','INDEPENDENT_PHASE4BE_RECOVERY_REVIEW.json',
 'FRESH_PHASE4BE_RECOVERY_PREFLIGHT.json','FINAL_HANDOFF.json','PRESERVATION_CHECK.json',
]
def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def write(name,obj): (here/name).write_text(json.dumps(obj,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf-8')
assert len(members)==len(set(members))
assert len(members)==len({m.casefold() for m in members})
assert all(not m.startswith('/') and '..' not in pathlib.PurePosixPath(m).parts and '\\' not in m for m in members)
assert all(not m.lower().endswith('.pdf') and 'private_source_material' not in m and 'source_delivery' not in m for m in members)
manifest={'kind':'PHASE4BE_C_PACKAGE_MANIFEST','members':[
    {'path':m,'sha256':sha_bytes((here/m).read_bytes()),'size':(here/m).stat().st_size}
    for m in members],
    'exclusions':['forensic/ exact drifted checkpoint byte copies','reproduction/ diagnostic copies and isolated scripts',
                  'PDFs and source-delivery material','temporary test files','runtime caches','prior ZIPs']}
write('PACKAGE_MANIFEST.json',manifest)
names=members+['PACKAGE_MANIFEST.json']
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for m in names: z.write(here/m,arcname=m)
with zipfile.ZipFile(archive,'r') as z:
    actual=z.namelist()
    assert actual==names
    assert z.testzip() is None
    assert len(actual)==len(set(actual))==len({n.casefold() for n in actual})
    for m in names:
        assert sha_bytes(z.read(m))==sha_bytes((here/m).read_bytes())
receipt={'kind':'PHASE4BE_C_PACKAGE_RECEIPT','archive_path':archive.relative_to(here.parents[1]).as_posix(),
         'sha256':sha_bytes(archive.read_bytes()),'size':archive.stat().st_size,
         'member_count':len(names),'crc':'PASS','exact_membership':'PASS','member_hashes':'PASS',
         'no_traversal':'PASS','no_duplicate_or_case_colliding_names':'PASS','no_pdf_or_source_content':'PASS',
         'receipt_external_to_archive':True}
write('PACKAGE_RECEIPT.json',receipt)
print(json.dumps(receipt))
