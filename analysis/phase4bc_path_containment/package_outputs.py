"""Exact allowlist package; never recursively archive the design tree."""
from pathlib import Path
import hashlib,json,zipfile
O=Path(__file__).resolve().parent;Z=O.parent/'phase4bc_path_containment_package.zip'
def h(b):return hashlib.sha256(b).hexdigest()
def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
names='''EXECUTIVE_PHASE4BC_P.md PHASE4BC_P_BASELINE.json INPUT_DRIFT_REPORT.md SYMLINK_GATE_SUPERSESSION.md SYMLINK_GATE_SUPERSESSION.json PATH_CONTAINMENT_AND_CONTENT_IDENTITY_INVARIANT.md PATH_CONTAINMENT_POLICY.json APPROVED_ROOTS.json CONTENT_IDENTITY_REGISTRY.schema.json PATH_CONTAINMENT_TEST_MATRIX.md PATH_CONTAINMENT_TEST_RESULTS.json TRANSITIVE_PATH_CONTAINMENT_REPORT.json INDIRECT_RESOLVER_TEST_REPORT.json INDEPENDENT_CONTAINMENT_REVIEW.json SCIENTIFIC_CONTINUITY_ADAPTER.md SCIENTIFIC_CONTINUITY_ADAPTER_REPORT.md SCIENTIFIC_CONTINUITY_ADAPTER_REPORT.json CONTINUITY_TEST_RESULTS.json B02_B08_UNTOUCHED_CHECK.json PHASE4B_RESUME_READINESS_FINAL.md FINAL_HANDOFF.json PRESERVATION_CHECK.json IMPLEMENTATION_MANIFEST.json REQUIREMENTS_TRACEABILITY.json RECOVERY_COMPLETION_NOTES.md verify_preservation.py finalize_reports.py commit_milestone.py package_outputs.py validate_archive.py
path_containment/guard.py path_containment/parent_adapter.py path_containment/test_guard.py
continuity_adapter/adapter.py continuity_adapter/context_contract.py continuity_adapter/worker.py continuity_adapter/test_continuity.py
vendor/context_engine.py inherited_context/context_architecture/scripts/context_engine.py inherited_context/context_architecture/tests/test_context_engine.py
inherited_recovery/recovery_protocol/engine.py inherited_recovery/recovery_protocol/test_recovery.py inherited_recovery/recovery_protocol/build_schemas.py inherited_recovery/RECOVERY_STATE.schema.json inherited_recovery/RECOVERY_EVENTS.schema.json inherited_recovery/MILESTONE_RECEIPT.schema.json
test_results/INHERITED_CONTEXT_RESULTS.json test_results/PARENT_BUILDER_INTEGRATION.json test_results/EXACT_PACKET_SEMANTIC_REVIEW.json test_results/review_packets/primary.json test_results/review_packets/verifier.json test_results/FINAL_TEST_SUMMARY.json'''.split()
assert len(names)==len(set(names))
entries=[]
for n in sorted(names):
    p=O/n;data=p.read_bytes()
    assert p.suffix in ['.md','.json','.py'] and not p.is_symlink()
    assert not any(x in Path(n).parts for x in ['private_test_storage','private_diagnostic_material','shadow','recovery_coordination','__pycache__'])
    assert not data.startswith((b'%PDF-',b'PK\x03\x04',b'SQLite format 3',b'\x89PNG'))
    entries.append({'path':n,'sha256':h(data),'size_bytes':len(data),'classification':'PACKAGEABLE_DESIGN_OUTPUT'})
manifest={'version':1,'files':entries,'self_entry':'PACKAGE_MANIFEST.json is added once; its exact bytes are validated against external manifest, excluding recursive self-hash','package_receipt':'External PACKAGE_RECEIPT.json and external FINAL_HANDOFF.json contain archive hash after independent validation','never_package':['private_diagnostic_material','private_test_storage','runtime stores','databases','backups','sources','credentials','prior archives'],'synthetic_fixtures':'Tiny invented source literals in test/code files only; no runtime source copies'}
(O/'PACKAGE_MANIFEST.json').write_bytes(canonical(manifest))
assert not Z.exists(),'Existing archive must be reconciled, never silently overwritten'
with zipfile.ZipFile(Z,'x',compression=zipfile.ZIP_DEFLATED) as z:
    for entry in entries:z.writestr(entry['path'],(O/entry['path']).read_bytes())
    z.writestr('PACKAGE_MANIFEST.json',(O/'PACKAGE_MANIFEST.json').read_bytes())
print('PACKAGED',len(entries)+1)
