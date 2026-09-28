"""Exact allowlist packager and independent archive reader, metadata-only outputs."""
import csv
from pathlib import Path
import sys
import zipfile
O=Path(__file__).resolve().parent;R=O.parents[1]
sys.path.insert(0,str(O/'recovery_protocol'))
from engine import *
NAMES='''EXECUTIVE_PHASE4BC_S.md PHASE4BC_S_BASELINE.json INPUT_DRIFT_REPORT.md SYMLINK_ENVIRONMENT_PROBE.json REAL_SYMLINK_TEST_SPEC.md REAL_SYMLINK_TEST_RESULT.json REAL_SYMLINK_TEST_REPORT.md PHASE4BC_RECOVERY_TIMELINE.jsonl RECOVERY_INTEGRITY_AUDIT.md RECOVERY_INTEGRITY_AUDIT.json PREEMPTION_RECOVERY_PROTOCOL.md PREEMPTION_RECOVERY_PROTOCOL.json RECOVERY_STATE.schema.json RECOVERY_EVENTS.schema.json MILESTONE_RECEIPT.schema.json RECOVERY_TEST_REPORT.md RECOVERY_TEST_RESULTS.json RECOVERY_CONTEXT_FIREWALL.md B02_B08_UNTOUCHED_CHECK.json PHASE4B_RESUME_READINESS_SUPPLEMENT.md PHASE4B_RESUME_WITH_RECOVERY_PROTOCOL.md FINAL_HANDOFF.json PRESERVATION_CHECK.json RECOVERY_IMPLEMENTATION_MANIFEST.json RECOVERY_COORDINATION_INDEX.json TEST_ATTEMPT_INVENTORY.json REQUIREMENTS_TRACEABILITY.json INDEPENDENT_FINAL_REVIEW.json INDEPENDENT_RETROSPECTIVE_REVIEW.json recovery_protocol/engine.py recovery_protocol/test_recovery.py recovery_protocol/build_schemas.py'''.split()
assert len(NAMES)==len(set(NAMES))
entries=[{'path':n,'sha256':filehash(O/n),'size_bytes':(O/n).stat().st_size,'classification':'PACKAGEABLE_DESIGN_OUTPUT'} for n in sorted(NAMES)]
manifest={'phase':'PHASE4BC-S','files':entries,'self_entry':'PACKAGE_MANIFEST.json; exact inventory excludes self to avoid circularity','never_package':['private_test_storage','private_diagnostic_material','recovery_coordination','private_quarantine','source PDFs','raw transcripts','databases','backups','prior archives'],'external_receipt':'PACKAGE_RECEIPT.json','external_handoff_convention':True}
exclusive(O/'PACKAGE_MANIFEST.json',canonical(manifest))
e=Engine(O/'recovery_coordination')
with e.lock('/root'):
    e.recover({k:e.state()[k] for k in PIN_KEYS},session_mode='RESUMED_SESSION')
    e.begin('PACKAGE_AND_VERIFY',{'manifest_sha256':filehash(O/'PACKAGE_MANIFEST.json')},['outputs/package_receipt.json'])
archive=O.parent/'phase4bc_supplement_package.zip'
with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED) as z:
    for x in entries:z.write(O/x['path'],x['path'])
    z.write(O/'PACKAGE_MANIFEST.json','PACKAGE_MANIFEST.json')
# Independent reader verifies bytes in the completed archive rather than builder buffers.
errors=[]
protected=list(csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig')))
source_hashes={x['sha256'] for x in protected if x['path'].lower().endswith('.pdf') or '/summaries/' in x['path'].lower() or x['path'].lower().endswith('/article.txt')}
with zipfile.ZipFile(archive) as z:
    members=z.namelist();stored=loads(z.read('PACKAGE_MANIFEST.json'))
    expected={x['path']:x for x in stored['files']}
    if set(members)!=set(expected)|{'PACKAGE_MANIFEST.json'}:errors.append('MEMBERSHIP')
    if len(members)!=len(set(members)) or len(members)!=len({n.casefold() for n in members}):errors.append('COLLISION')
    if z.testzip() is not None:errors.append('CRC')
    for n in members:
        if n.startswith(('/','\\')) or '..' in Path(n).parts or ':' in n or '\\' in n:errors.append('PATH:'+n)
        if Path(n).suffix.lower() in ['.pdf','.sqlite','.db','.bak','.zip','.png','.jpg','.pyc'] or any(p in n.lower() for p in ['private_test_storage/','private_diagnostic_material/','shadow/','rehearsal_runtime/']):errors.append('FORBIDDEN:'+n)
        b=z.read(n);h=digest(b)
        if h in source_hashes or b.startswith((b'%PDF-',b'SQLite format 3\x00')):errors.append('SOURCE_SIGNATURE:'+n)
        if n in expected and (len(b)!=expected[n]['size_bytes'] or h!=expected[n]['sha256']):errors.append('HASH:'+n)
    if z.read('PACKAGE_MANIFEST.json')!=(O/'PACKAGE_MANIFEST.json').read_bytes():errors.append('MANIFEST')
receipt={'archive':str(archive),'sha256':filehash(archive),'members':len(members),'crc_passed':'CRC' not in errors,'exact_allowlist':not errors,'errors':errors,'timestamp':now(),'manifest_sha256':filehash(O/'PACKAGE_MANIFEST.json'),'private_content_excluded':True,'scanning_limit':'Known names/hashes/signatures; constrained generation and read-only source boundary are primary controls. Not arbitrary semantic exfiltration proof.','convention':'This external receipt and external final handoff are not inserted into archive after hashing.'}
exclusive(O/'PACKAGE_RECEIPT.json',canonical(receipt))
assert not errors,errors
with e.lock('/root'):
    e.commit({'outputs/package_receipt.json':canonical(receipt)},next_operation='STOP_WITH_SUPPLEMENTAL_CLASSIFICATION')
    e.finish()
handoff=read(O/'FINAL_HANDOFF.json');handoff['package']['sha256']=receipt['sha256'];replace(O/'FINAL_HANDOFF.json',handoff)
print(canonical(receipt).decode())
