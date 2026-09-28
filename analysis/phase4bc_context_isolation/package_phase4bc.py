import json,hashlib,zipfile
from pathlib import Path
O=Path(__file__).resolve().parent;Z=O.parent/'phase4bc_context_isolation_package.zip'
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,x):(O/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
names='''EXECUTIVE_PHASE4BC.md PHASE4BC_BASELINE.json INPUT_DRIFT_REPORT.md B02_B08_UNTOUCHED_RESERVATION.json CONTEXT_LEAKAGE_INVENTORY.csv CONTEXT_LEAKAGE_ANALYSIS.md CONTEXT_ARCHITECTURE.md CONTEXT_ARCHITECTURE_CHANGELOG.md PRIMARY_CONTEXT_ALLOWLIST.json VERIFIER_CONTEXT_ALLOWLIST.json VALIDATION_CONTEXT_DENYLIST.json VALIDATION_CONTEXT_DENY_POLICY.md HISTORICAL_TO_GENERIC_RULE_MAPPING.csv PRIMARY_CONTEXT_PACKET_TEMPLATE.json VERIFIER_CONTEXT_PACKET_TEMPLATE.json COORDINATOR_CONTEXT_TEMPLATE.json COORDINATOR_FIREWALL_PROTOCOL.md CONTEXT_PACKET_MANIFEST.schema.json VALIDATION_PACKET_CONTENT_REGISTRY.csv TRANSITIVE_CONTEXT_DEPENDENCY_REPORT.json STATIC_CONTEXT_SCAN.json SEMANTIC_CONTEXT_REVIEW.json SEMANTIC_REVIEW_PROTOCOL.md PER_REPORT_PRE_ACCESS_RECEIPT_PROTOCOL.md CONTEXT_PACKET_ARCHITECTURE_CONFIGURATION.json INDEPENDENT_PACKET_REVIEW.json INDEPENDENT_FINAL_REVIEW.json B02_B08_POST_PHASE4BC_UNTOUCHED_CHECK.json PHASE4B_RESUME_V2_PLAN.md FINAL_HANDOFF.json PRESERVATION_CHECK.json IMMUTABLE_EXECUTION_MANIFEST.json REQUIREMENTS_TRACEABILITY.csv'''.split()
roots=['context_architecture/methodology_generic','context_architecture/policy_frozen','context_architecture/packet_templates','context_architecture/deny_rules','context_architecture/historical_forbidden','context_architecture/scripts','context_architecture/tests','B02_PREACCESS_PACKET_DRY_RUN','test_results']
for root in roots:
 for p in (O/root).rglob('*'):
  if p.is_file():
   assert p.suffix in ('.py','.md','.csv','.json'),str(p)
   assert not p.is_symlink()
   names.append(p.relative_to(O).as_posix())
handoff=json.loads((O/'FINAL_HANDOFF.json').read_text(encoding='utf-8'));handoff['package']['sha256']='SEE_EXTERNAL_PACKAGE_RECEIPT';save('FINAL_HANDOFF.json',handoff)
names=sorted(set(names));assert len(names)==len({n.casefold() for n in names})
rows=[{'path':n,'size_bytes':(O/n).stat().st_size,'sha256':h(O/n),'classification':'SANITIZED_DESIGN_CODE_OR_METADATA'} for n in names]
manifest={'allowlist':rows,'manifest_self_hash_excluded':True,'allowed_roots':roots,'private_roots':['private_diagnostic_material','private_test_storage'],'no_recursive_phase_zip':True,'historical_control_data':'Denylists and leakage references are coordinator-only; not worker packets. No raw research source bytes packaged.','copied_contract_exceptions':['context_architecture/methodology_generic/FIELD_CATALOG.json','context_architecture/methodology_generic/scientific_evidence_v4.schema.json','context_architecture/methodology_generic/PROPOSITION_SUPPORT_MODEL.md','context_architecture/methodology_generic/SCHEMA_SEMANTICS.md','context_architecture/methodology_generic/SUPPORT_LOCATOR_ROLE_MODEL.md'],'handoff_hash_convention':'ZIP contains pre-archive handoff referencing external receipt. External handoff updated with package hash afterwards.'}
save('PACKAGE_MANIFEST.json',manifest)
with zipfile.ZipFile(Z,'w',zipfile.ZIP_DEFLATED) as z:
 for n in names+['PACKAGE_MANIFEST.json']:z.write(O/n,n)
receipt={'path':str(Z),'sha256':h(Z),'size_bytes':Z.stat().st_size,'member_count':len(names)+1,'archive_validation':'PENDING','handoff_hash_convention':manifest['handoff_hash_convention']}
save('PACKAGE_RECEIPT.json',receipt)
handoff=json.loads((O/'FINAL_HANDOFF.json').read_text(encoding='utf-8'));handoff['package']['sha256']=receipt['sha256'];save('FINAL_HANDOFF.json',handoff)
print(receipt)
