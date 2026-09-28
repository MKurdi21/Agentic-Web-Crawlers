"""Exact metadata/report allowlist. No source or runtime stores."""
from pathlib import Path
import json,hashlib,zipfile,sys
O=Path(__file__).resolve().parent;Z=O.parent/'phase4b_resumed_v2_package.zip'
sys.path.insert(0,str(O.parent/'phase4bc_supplement/recovery_protocol'))
from engine import Engine,canonical,filehash
assert json.loads((O/'PRESERVATION_CHECK.json').read_text())['status']=='PASS'
assert json.loads((O/'INDEPENDENT_FINAL_REVIEW.json').read_text())['status']=='CONFIRMED_NO_GO'
names='''EXECUTIVE_RESUMED_PHASE4B_V2.md RESUMED_PHASE4B_BASELINE.json RESUMED_HOLDOUT_PROCESSING_ORDER.json HOLDOUT_STATE_TRACKER.json HOLDOUT_CONTEXT_ISOLATION.json HOLDOUT_VALIDATION_REPORT.md HOLDOUT_VALIDATION_METRICS.json HOLDOUT_DISAGREEMENTS.csv HOLDOUT_LIMITATIONS.md PHASE4B_READINESS.md FINAL_HANDOFF.json PRESERVATION_CHECK.json PREACCESS_INTERFACE_REVIEW.json INDEPENDENT_FINAL_REVIEW.json REPORTING_DIAGNOSTIC.json preflight.py close_blocked_run.py verify_preservation.py package_run.py verify_package.py'''.split()
e=Engine(O)
with e.lock('/root-package'):
    report_pins={n:filehash(O/n) for n in names}
    started=e.begin('NO_GO_HANDOFF',{'report_manifest':hashlib.sha256(canonical(report_pins)).hexdigest()},['outputs/no_go_handoff.json'])
    if not started.get('already_committed'):
        e.commit({'outputs/no_go_handoff.json':canonical({'classification':'NO_GO','files':report_pins,'source_access':False})},next_operation='PACKAGE_AND_STOP')
    chain=e.receipts()
names+=['RECOVERY_STATE.json','RECOVERY_EVENTS.jsonl','INITIAL_STATE.json']
for receipt_hash,receipt in chain:
    receipt_path='milestone_receipts/'+receipt['attempt_id']+'.json'
    assert filehash(O/receipt_path)==receipt_hash
    names.append(receipt_path)
    names.append('intents/'+receipt['attempt_id']+'.json')
    names.extend(receipt['expected_outputs'])
names=sorted(set(names));entries=[]
for n in names:
    p=O/n;data=p.read_bytes()
    assert p.suffix in ['.json','.jsonl','.md','.csv','.py'] and not p.is_symlink()
    entries.append({'path':n,'sha256':hashlib.sha256(data).hexdigest(),'size_bytes':len(data)})
manifest={'files':entries,'classification':'METADATA_AND_AUTHORED_REPORTS_ONLY','manifest_self_entry':'PACKAGE_MANIFEST.json excluded from its own hash inventory and independently compared as exact bytes','archive_convention':'Archive contains durable state through NO_GO_HANDOFF. Final package receipt and terminal state are external after archive validation; archived handoff hash is intentionally null.','forbidden':['PDF','full source text','summaries','page images','databases','blobs','backups','caches','credentials','prior ZIPs','private diagnostics']}
(O/'PACKAGE_MANIFEST.json').write_bytes(canonical(manifest))
assert not Z.exists()
with zipfile.ZipFile(Z,'x',zipfile.ZIP_DEFLATED) as z:
    for n in names:z.writestr(n,(O/n).read_bytes())
    z.writestr('PACKAGE_MANIFEST.json',(O/'PACKAGE_MANIFEST.json').read_bytes())
print('PACKAGED',len(names)+1)
