"""Explicit-allowlist failure handoff. Private contexts are never packaged."""
import sys,json,zipfile,hashlib,csv
from pathlib import Path,PurePosixPath
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;R=O.parents[1]
def h(p):
 q=hashlib.sha256()
 with Path(p).open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):q.update(chunk)
 return q.hexdigest()
def put(p,x):p.write_text(json.dumps(x,sort_keys=True,indent=2),encoding='utf-8')
handoff=json.loads((O/'FINAL_HANDOFF.json').read_bytes());review=json.loads((O/'INDEPENDENT_FINAL_TECHNICAL_REVIEW.json').read_bytes())
assert review['status']=='PASS_FOR_NO_GO_CLASSIFICATION'
handoff['independent_review_status']=review['status'];handoff['independent_review_context_id']=review.get('reviewer_context_id',review.get('context_id'));put(O/'FINAL_HANDOFF.json',handoff)
handoff['event_accounting']={'session_recovery_attempts':0,'usage_limit_preemptions':0,'engineering_integrity_failure_events':1,'journal_type_for_engineering_failure':'RECOVERY_PREFLIGHT_FAIL','scientific_source_access_events':0}
handoff['candidate_integrity']={'immutable_equality_final':False,'silent_refreeze':False,'parent_scientific_and_transport_hashes_preserved':True}
put(O/'FINAL_HANDOFF.json',handoff)
names=['EXECUTIVE_PHASE4B_FINAL.md','PHASE4B_FINAL_BASELINE.json','INPUT_DRIFT_DIAGNOSTIC.json','IMMUTABLE_GATE_FAILURE.json','INDEPENDENT_FINAL_TECHNICAL_REVIEW.json','MODEL_ROUTING_POLICY.json','MODEL_ROUTING_POLICY.md','MODEL_ROUTING_WORKER_RULES.json','MODEL_ROUTING_CONTROL_CLASSIFICATION.json','MODEL_ROUTING_LEDGER.jsonl','HOLDOUT_PROCESSING_ORDER.json','HOLDOUT_STATE_TRACKER.json','HOLDOUT_CONTEXT_ISOLATION.json','HOLDOUT_CONSERVATION_REPORT.md','HOLDOUT_VALIDATION_REPORT.md','HOLDOUT_VALIDATION_METRICS.json','HOLDOUT_DISAGREEMENTS.csv','HOLDOUT_LIMITATIONS.md','ORCHESTRATION_IMMUTABLE_MANIFEST.json','RECOVERY_STATE.json','RECOVERY_EVENTS.jsonl','RECOVERY_INITIALIZATION_BINDINGS.json','PHASE4B_READINESS.md','FINAL_HANDOFF.json','PRESERVATION_CHECK.json','GIT_STATUS_INITIAL.txt','GIT_STATUS_FINAL.txt','test_results/MODEL_BOUNDARY_TEST_REPORT.json']
names += ['FINAL_TECHNICAL_REVIEW_TERMINAL.json']
names += ['orchestration/'+x for x in ['model_transport.py','release_current.py','extract_current.py','run_control.py','freeze_code.py','test_model_boundary.py','PRIMARY_TASK_TEMPLATE.json','VERIFIER_TASK_TEMPLATE.json','PRIMARY_DISPATCH_TEMPLATE.txt','RECOVERY_AUTHORITY_PROTOCOL.md']]
names += [p.relative_to(O).as_posix() for p in sorted((O/'milestone_receipts').glob('*.json'))]
names=sorted(names)
assert len(set(names))==len(names)
original_hashes={r['sha256'] for r in csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8-sig',newline='')) if int(r['size'])>=128}
records=[]
for n in names:
 p=O/n;assert p.is_file() and not p.is_symlink()
 assert p.suffix.lower() in {'.py','.md','.json','.jsonl','.csv','.txt'}
 assert not any(x in PurePosixPath(n).parts for x in ['private_worker_material','shadow','durable_run','rehearsal_runtime','source_delivery'])
 assert h(p) not in original_hashes or n in ['GIT_STATUS_INITIAL.txt','GIT_STATUS_FINAL.txt'],'COPIED_PROTECTED_INPUT'
 records.append({'path':n,'size_bytes':p.stat().st_size,'sha256':h(p),'classification':'PACKAGEABLE_DESIGN_OUTPUT'})
manifest={'package_kind':'FAILED_PREACCESS_RUN_HANDOFF_NOT_EXECUTION_READY','inventory':records,'manifest_self_convention':'PACKAGE_MANIFEST.json is the sole unhashed self-member; exact byte CRC remains validated','forbidden_roots':['private_worker_material','durable_run','rehearsal_runtime'],'source_content_permitted':False,'external_receipt':'PACKAGE_RECEIPT.json'}
put(O/'PACKAGE_MANIFEST.json',manifest)
archive=R/'analysis/phase4b_validation_final_package.zip'
assert not archive.exists(),'PACKAGE_ALREADY_EXISTS'
with zipfile.ZipFile(archive,'x',zipfile.ZIP_DEFLATED) as z:
 for n in names+['PACKAGE_MANIFEST.json']:z.write(O/n,n)
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None
 entries=z.namelist();assert set(entries)==set(names+['PACKAGE_MANIFEST.json']) and len(entries)==len(set(entries))
 assert len({x.casefold() for x in entries})==len(entries)
 for n in entries:
  path=PurePosixPath(n);assert not path.is_absolute() and '..' not in path.parts and '\\' not in n and ':' not in n
 for row in records:assert hashlib.sha256(z.read(row['path'])).hexdigest()==row['sha256']
 for n in entries:
  data=z.read(n);assert hashlib.sha256(data).hexdigest() not in original_hashes or n in ['GIT_STATUS_INITIAL.txt','GIT_STATUS_FINAL.txt']
  assert not data.startswith(b'%PDF-') and not data.startswith(b'SQLite format 3')
receipt={'status':'PASS','archive_path':str(archive),'archive_sha256':h(archive),'archive_member_count':len(entries),'crc':'PASS','membership':'PASS','hashes':'PASS','private_exclusion':'PASS','source_content_scan_limit':'Explicit separation and constrained generation; signatures/hashes do not detect every transformed private excerpt','manifest_sha256':h(O/'PACKAGE_MANIFEST.json'),'non_circular_convention':'Receipt excluded; archive handoff refers to this external receipt. External handoff is updated only after ZIP creation.'}
put(O/'PACKAGE_RECEIPT.json',receipt)
handoff.update(package_sha256=receipt['archive_sha256'],package_member_count=len(entries));put(O/'FINAL_HANDOFF.json',handoff)
print(json.dumps(receipt),flush=True)
