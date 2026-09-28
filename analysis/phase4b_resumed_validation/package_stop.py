import hashlib,json,zipfile
from pathlib import Path
O=Path(__file__).resolve().parent
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
review={'reviewer_context':'/root/resume_b02_verifier','mode':'SEPARATE_CONTEXT_MODEL_BOUNDARY_REVIEW','result':'CONFIRMED_PRE_ACCESS_CONTEXT_BLOCKER','source_review_performed':False,'writes_performed_by_reviewer':False,'candidate_manifest_check':True,'source_access_began_absent':True,'reserved_source_extraction_absent':True,'reviewed_scope':['Frozen input history leakage','Candidate immutable equality','Access metadata and output inventory'],'limitations':['Not independent human scientific review','Not an OS-wide access audit','Archive verified separately after this review'],'future_scientific_context_eligible':False}
save(O/'INDEPENDENT_BOUNDARY_REVIEW.json',review)
handoff=json.loads((O/'FINAL_HANDOFF.json').read_text(encoding='utf-8'))
handoff['independent_final_review']='SEPARATE_CONTEXT_MODEL_BOUNDARY_REVIEW_COMPLETED; ARCHIVE_VALIDATION_SEPARATE'
handoff['package_path']='analysis/phase4b_resumed_validation/phase4b_resumed_validation_package.zip'
handoff['package_hash_receipt']='PACKAGE_RECEIPT.json'
save(O/'FINAL_HANDOFF.json',handoff)
names=['EXECUTIVE_RESUMED_PHASE4B.md','RECOVERY.md','BASELINE.json','PROCESSING_ORDER.json','HOLDOUT_ACCESS_LEDGER.json','HOLDOUT_CONTEXT_ISOLATION.json','CONTEXT_CONTAMINATION_LOG.json','HOLDOUT_CONSERVATION_REPORT.md','HOLDOUT_VALIDATION_REPORT.md','HOLDOUT_VALIDATION_METRICS.json','HOLDOUT_LIMITATIONS.md','PHASE4B_READINESS.md','PRESERVATION_CHECK.json','INDEPENDENT_BOUNDARY_REVIEW.json','FINAL_HANDOFF.json','holdout_validation/B02/PRIMARY_CONTEXT_PACKET.json','holdout_validation/B02/SOURCE_BINDING.json','holdout_validation/B02/PRE_ACCESS_RECEIPT.json','holdout_validation/B02/IMMUTABLE_BEFORE.json','holdout_validation/B02/IMMUTABLE_AFTER.json']
rows=[{'relative_path':s,'size_bytes':(O/s).stat().st_size,'sha256':h(O/s),'classification':'PACKAGEABLE_METADATA_OR_NEW_REPORT'} for s in sorted(names)]
manifest={'release_type':'PRE_ACCESS_NO_GO_HANDOFF','allowed_exact_members':sorted(names+['PACKAGE_MANIFEST.json']),'inventory':rows,'manifest_self_hash_excluded':True,'never_package':['private_source_material/','candidate_v4br/','candidate_frozen/','rehearsal_runtime/','**/private/'],'forbidden_classes':['PDF','full source text','complete summaries','page renderings','original control copies','runtime DB','artifact blobs','backups','credentials','nested archives']}
save(O/'PACKAGE_MANIFEST.json',manifest)
z=O/'phase4b_resumed_validation_package.zip'
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as f:
 for s in manifest['allowed_exact_members']:f.write(O/s,s)
save(O/'PACKAGE_RECEIPT.json',{'path':str(z),'sha256':h(z),'size_bytes':z.stat().st_size,'member_count':len(manifest['allowed_exact_members']),'independent_archive_validation':'PENDING'})
print('Packaged',len(manifest['allowed_exact_members']),'metadata/report members',h(z))
