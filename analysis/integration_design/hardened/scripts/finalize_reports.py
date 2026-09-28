"""Independent static/preservation evidence and explicit limitations for the release."""
import ast,re,subprocess,csv
from common import *
from db import connect,integrity,verify_profile
from artifact_store import reconcile
from verify_equivalence import verify
from build_docs import DOCS
def main():
 static=[];calls=[]
 for p in (DESIGN/'hardened').rglob('*.py'):
  tree=ast.parse(p.read_text(encoding='utf-8'));static.append({'check':'python_syntax','path':p.relative_to(DESIGN).as_posix(),'passed':True})
  for n in ast.walk(tree):
   if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and isinstance(n.func.value,ast.Name) and n.func.value.id=='sqlite3' and n.func.attr=='connect':calls.append(p.relative_to(DESIGN).as_posix())
 static.append({'check':'single_bootstrap_connection_site','passed':calls==['hardened/scripts/db.py'],'sites':calls})
 for p in (DESIGN/'deploy_payload/skills').glob('*/SKILL.md'):
  text=p.read_text();ok=text.startswith('---\n') and 'name:' in text.split('---')[1] and 'description:' in text.split('---')[1]
  links=re.findall(r'\]\(([^)]+)\)',text);ok=ok and all((p.parent/x).resolve().is_file() for x in links)
  static.append({'check':'skill_frontmatter_and_references','path':p.relative_to(DESIGN).as_posix(),'passed':ok})
 static.append({'check':'inactive_payload_only','passed':not any(p.name=='AGENTS.md' or '.agents' in p.parts or '.codex-plugin' in p.parts for p in (DESIGN/'deploy_payload').rglob('*'))})
 write_json(DESIGN/'test_results/STATIC_CHECKS.json',{'passed':all(r['passed'] for r in static),'checks':static,'skill_trigger_validation':'Descriptions and scoped examples reviewed in source; no model-based routing trial performed (no generation authorized).','shared_dependencies':'Independent verifiers share Python hashing,SQLite runtime and mandatory bootstrap; they do not use importer counts or builder acceptance decisions.'})
 equivalence=verify(WORKSPACE,SHADOW/'current.sqlite3');write_json(DESIGN/'test_results/COMPATIBILITY_EXPORT.json',equivalence)
 with connect(SHADOW/'current.sqlite3',readonly=True) as c:
  dbcheck=integrity(c);store=reconcile(c,[SHADOW/'private_source_material/raw']);config=verify_profile(c)
 baseline=json.loads((DESIGN/'test_results/INITIAL_BASELINE.json').read_text());changes=[];errors=[]
 for rel,old in baseline['files'].items():
  p=WORKSPACE/rel
  try:
   actual=digest(p) if p.is_file() else None
   if actual!=old['sha256']:changes.append({'path':rel,'before':old['sha256'],'after':actual})
  except OSError as e:errors.append({'path':rel,'error':str(e)})
 additions=[]
 for p in WORKSPACE.rglob('*'):
  if p.is_file() and not p.is_relative_to(DESIGN) and p!=DESIGN.parent/'integration_design_package.zip' and p.relative_to(WORKSPACE).as_posix() not in baseline['files']:additions.append(p.relative_to(WORKSPACE).as_posix())
 status=subprocess.run(['git','--no-optional-locks','status','--porcelain=v1','--untracked-files=all'],capture_output=True,text=True,check=True).stdout
 def outside(text):return [line for line in text.splitlines() if 'analysis/integration_design/' not in line and 'analysis/integration_design_package.zip' not in line]
 non_git=[r for r in changes if not r['path'].startswith('.git/')];non_git_added=[p for p in additions if not p.startswith('.git/')]
 preservation={'checked_at':stamp(),'preexisting_files_checked':len(baseline['files']),'research_control_unchanged':not non_git and not errors,'non_git_changes':non_git,'non_git_additions_outside_boundary':non_git_added,'git_metadata_changes':[r for r in changes if r['path'].startswith('.git/')],'git_metadata_additions':[r for r in additions if r.startswith('.git/')],'git_status_outside_outputs_unchanged':outside(status)==outside(baseline['git_status']),'errors':errors,'intentional_preexisting_modifications':False,'attribution':'No Git mutation command issued. Metadata writers are not independently attributable; preserve/report,do not repair.'}
 write_json(DESIGN/'test_results/PRESERVATION_REPORT.json',preservation)
 tests=json.loads((DESIGN/'test_results/UNIT_INTEGRATION_RESULTS.json').read_text());idem=json.loads((DESIGN/'test_results/IDEMPOTENCY_REPORT.json').read_text());backup=json.loads((DESIGN/'test_results/BACKUP_REPORT.json').read_text())
 areas=[('audit_and_boundary','MIGRATION_SPEC','boundary'),('private_material','PACKAGING_SPEC','private'),('three_identities','IDENTITY_MODEL','alias'),('historical_artifacts','PROVENANCE_MODEL','equivalence'),('state_crosswalk','STATE_CROSSWALK','equivalence'),('sqlite_bootstrap','SQLITE_BOOTSTRAP','configuration'),('extra_durability_profile','STORAGE_DEPLOYMENT_DECISION','configuration'),('two_integrity_checks','SQLITE_BOOTSTRAP','foreign_key_integrity'),('five_validation_layers','SCHEMA_SEMANTICS','schema'),('typed_locators','SCHEMA_SEMANTICS','locator'),('lease_retry','WORKER_PROTOCOL_V2','retry'),('stale_reaped_workers','WORKER_PROTOCOL_V2','expired'),('authoritative_pins','VERSIONING_AND_INVALIDATION','authoritative'),('publication_atomicity','ACCEPTANCE_AND_ATOMICITY','crash'),('existing_blob_corruption','ARTIFACT_INTEGRITY','corruption'),('explicit_replay','REPLAY_PROTOCOL','replay'),('source_mutation','IDENTITY_MODEL','mutation'),('orphan_retention','ARTIFACT_INTEGRITY','orphan'),('store_db_distinction','ARTIFACT_INTEGRITY','missing_blob'),('human_review_hashes','PROVENANCE_MODEL','review'),('semantic_idempotency','MIGRATION_DRY_RUN_PLAN','equivalence'),('independent_counts','MIGRATION_SPEC','equivalence'),('backup_restore','BACKUP_VERIFICATION','backup'),('taxonomy','TAXONOMY_GOVERNANCE','taxonomy'),('synthesis_eligibility','SYNTHESIS_ARCHITECTURE','synthesis'),('selective_invalidation','VERSIONING_AND_INVALIDATION','invalidation'),('archive_allowlist','PACKAGING_SPEC','archive'),('rename_base64_exclusions','PACKAGING_SPEC','renamed'),('inactive_skills','INTEGRATION_ARCHITECTURE','static')]
 trace=[]
 for name,doc,pattern in areas:
  evidence=[r['test'] for r in tests['tests'] if pattern in r['test'] and r['status']=='PASS']
  if pattern=='equivalence':evidence=['test_results/COMPATIBILITY_EXPORT.json','test_results/IDEMPOTENCY_REPORT.json']
  if pattern=='static':evidence=['test_results/STATIC_CHECKS.json']
  trace.append({'requirement':name,'design':doc+'.md','evidence':evidence,'status':'IMPLEMENTED_WITH_EVIDENCE' if evidence else 'DESIGN_AND_CODE_REVIEW','limitations':'See OPEN_DECISIONS and completion report; engineering evidence is not scientific correctness'})
 for name,reason in [('scientific_calibration','User prohibited paper regeneration and scientific acceptance in this phase'),('external_gap_validation','Future separately authorized protocol only'),('production_storage_cutover','Human deployment decision and separate authorization required'),('live_reviewer_authentication','No configured trusted production approval source; fail closed'),('independent_subagent_review','Delegated workers failed on usage limit; no retries; independent executable verification paths used'),('power_loss_and_remote_sync','Same-host process tests cannot prove device/Drive durability'),('multi_machine_client_server','Profile compared; no such deployment authorized'),('model_based_skill_routing','No model generation in Phase2; static scope/reference checks only')]:trace.append({'requirement':name,'status':'EXPLICITLY_DEFERRED','reason':reason})
 write_json(DESIGN/'test_results/REQUIREMENTS_TRACEABILITY.json',{'requirements':trace,'audit_unknowns_retained':13,'audit_components_disposition_rows':43})
 gates={'tests':tests['failed']==0,'static':all(x['passed'] for x in static),'independent_equivalence':equivalence['passed'],'semantic_idempotency':idem['passed'],'sqlite_configuration':config['synchronous']==3 and config['foreign_keys']==1,'database_integrity':dbcheck['integrity_check']==['ok'] and not dbcheck['foreign_key_check'],'artifact_store_integrity':store['passed'],'backup_restoration':backup['passed'],'preservation':preservation['research_control_unchanged'] and not non_git_added and preservation['git_status_outside_outputs_unchanged']}
 report={'created_at':stamp(),'status':'MIGRATION_CANDIDATE_SHADOW_ONLY','tests_passed':tests['passed'],'tests_failed':tests['failed'],'gates':gates,'counts':equivalence['counts'],'source_verified':equivalence['source_verified'],'promoted':equivalence['promoted'],'no_live_migration':True,'no_paper_generation':True,'no_checkpoint_refresh':True,'no_skills_installed':True,'store_classifications':{kind:sum(r['classification']==kind for r in store['blobs']) for kind in ['VALID_REFERENCED_BLOB','ORPHAN_BLOB','MISSING_REFERENCED_BLOB','HASH_MISMATCH','UNEXPECTED_FILE']},'packaging_gate':'Final independent archive result is in external test_results/PACKAGE_RECEIPT.json; no circular claim inside archive','remaining_decisions':'OPEN_DECISIONS.md','explicit_deferred':[r for r in trace if r['status']=='EXPLICITLY_DEFERRED'],'limitations':['No scientific review/novelty validation','No production trust/storage location selected','No arbitrary power-loss or Drive sync guarantee','Live relocation/authority adapter requires separate review','Independent verifiers share SQLite/hash/bootstrap dependencies','Known-content scan is not steganography detection']}
 write_json(DESIGN/'test_results/COMPLETION_REPORT.json',report)
 (DESIGN/'test_results/TEST_RESULTS.md').write_text('# Test and verification results\n\n'+f"{tests['passed']} tests passed; {tests['failed']} failed. Detailed named outcomes: UNIT_INTEGRATION_RESULTS.json.\n\n"+'\n'.join(f'- {k}: {"PASS" if v else "FAIL"}' for k,v in gates.items())+'\n\nPrivate source material and all shadow databases are excluded from the ZIP. Final packaging validation is recorded outside the archive in PACKAGE_RECEIPT.json.\n\nNo live migration,paper generation,checkpoint refresh or skill installation occurred. Subagent review was unavailable due usage limits; executable independent SQL/filesystem/archive paths were used. Scientific calibration,production trust/storage and sync durability remain deferred.\n',encoding='utf-8')
 print(canonical({'gates':gates,'tests_passed':tests['passed'],'tests_failed':tests['failed'],'preservation_non_git_changes':len(non_git),'git_metadata_changes':len(preservation['git_metadata_changes'])}))
 if not all(gates.values()):raise Failure('FINAL_GATE')
if __name__=='__main__':main()
