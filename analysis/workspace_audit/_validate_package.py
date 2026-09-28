from pathlib import Path
import json,csv,hashlib,datetime,subprocess,importlib.util,sys,zipfile,collections,ast
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[2];O=R/'analysis/workspace_audit'
def j(n):return json.loads((O/n).read_text(encoding='utf-8-sig'))
def cr(n):return list(csv.DictReader((O/n).open(encoding='utf-8-sig')))
def h(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def save(n,v):(O/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
checks=[]
def check(name,ok,detail=None):checks.append({'name':name,'passed':bool(ok),'detail':detail})
required=['EXECUTIVE_SUMMARY.md','WORKSPACE_ARCHITECTURE.md','CURRENT_PIPELINE.md','CURRENT_STATE_MODEL.md','CORPUS_INVENTORY.csv','PAPER_PROCESSING_MATRIX.csv','ARTIFACT_INVENTORY.csv','DUPLICATE_AND_VERSION_REPORT.md','PROVENANCE_AUDIT.md','STATE_DRIFT_REPORT.md','EXISTING_VS_PROPOSED_ARCHITECTURE.md','MIGRATION_PRESERVATION_MAP.md','UNRESOLVED_QUESTIONS.md','WORKSPACE_SNAPSHOT.json','INTEGRATION_HANDOFF.md','REFERENCE_ARCHITECTURE_COMPATIBILITY.csv']
for n in required:check('deliverable:'+n,(O/n).is_file() and (O/n).stat().st_size>0)
pdfs={p.relative_to(R).as_posix():p for p in R.rglob('*') if p.is_file() and p.suffix.lower()=='.pdf' and not p.is_relative_to(O)}
c=cr('CORPUS_INVENTORY.csv');m=cr('PAPER_PROCESSING_MATRIX.csv');a=cr('ARTIFACT_INVENTORY.csv');comp=cr('REFERENCE_ARCHITECTURE_COMPATIBILITY.csv');manifest=list(csv.DictReader((R/'analysis/manifest.csv').open(encoding='utf-8-sig')))
check('every_PDF_exactly_one_inventory_row',len(c)==len(pdfs) and len({r['path'] for r in c})==len(c) and {r['path'] for r in c}==set(pdfs),len(pdfs))
check('every_PDF_hash_correct',all(h(pdfs[r['path']])==r['sha256'] for r in c))
check('every_relevant_source_in_processing_matrix',{r['source_pdf'] for r in m}=={p for p in pdfs if '99_Duplicates/' not in p} and len(m)==112)
check('manifest_reconciled',{r['summary_name'] for r in m}=={r['SummaryName'] for r in manifest})
groups=collections.defaultdict(list)
for r in c:groups[r['sha256']].append(r)
check('all_exact_duplicates_marked',all(all(r['identical_paths'] for r in g) and sum(bool(r['duplicate_of']) for r in g)==len(g)-1 for g in groups.values() if len(g)>1),{'groups':sum(len(g)>1 for g in groups.values()),'extra_copies':sum(len(g)-1 for g in groups.values())})
covered={r['artifact_path'] for r in a};actual_artifacts={p.relative_to(R).as_posix() for base in [R/'Summaries',R/'.summary_v2',R/'analysis/evidence',*R.glob('.summary_work_*')] for p in base.rglob('*') if p.is_file()}
check('all_summary_and_evidence_files_accounted',actual_artifacts<=covered,{'actual_files':len(actual_artifacts),'missing':sorted(actual_artifacts-covered)})
check('artifact_hashes_correct',all(h(R/r['artifact_path'])==r['sha256'] for r in a))
check('all_artifacts_mapping_explicit',all(r['mapping_status'] in ['MAPPED','UNMAPPED','INTENTIONAL_NON_PAPER'] for r in a))
evdirs={p.relative_to(R).as_posix() for p in (R/'analysis/evidence').iterdir() if p.is_dir()};check('all_evidence_directories_mapped',evdirs=={r['evidence_workspace'] for r in m if r['evidence_workspace']})
spec=importlib.util.spec_from_file_location('audit_readonly_state',R/'scripts/summary_state.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
check('state_structure_independently_matches_current_code',all(module.check_structure(R/r['StageTarget'])['passed']==(next(x for x in m if x['summary_name']==r['SummaryName'])['structure_pass']=='True') for r in manifest))
cp=json.loads((R/'analysis/checkpoint.json').read_text());cpby={r['SummaryName']:r for r in cp['papers']};check('every_checkpoint_record_reconciled',set(cpby)=={r['summary_name'] for r in m} and all(cpby[r['summary_name']]['status']==r['observed_status'] for r in m))
rv=json.loads((R/'analysis/reviews.json').read_text());check('every_review_record_reconciled',set(rv)<={r['summary_name'] for r in m},len(rv))
check('current_PowerShell_syntax',all(x['error_count']==0 for x in j('CURRENT_SCRIPT_STATIC_CHECKS.json')))
for p in [*R.glob('*.py'),*(R/'scripts').glob('*.py')]:ast.parse(p.read_text(encoding='utf-8-sig'))
check('current_Python_syntax',True)
check('reference_component_rows_unique',len(comp)==len({r['component_id'] for r in comp})==43)
refhash='55902ec025685c1f4f2afb37672cc885222eab9952b39eb7ee48429100633e42';zpath=R/'Codex_Literature_Review_Production_Architecture.zip'
check('reference_ZIP_byte_identical',h(zpath)==refhash)
with zipfile.ZipFile(zpath) as z:
    names=z.namelist();check('reference_member_inventory_complete',set(names)=={r['reference_path'] for r in cr('REFERENCE_PACKAGE_INVENTORY.csv')});check('all_reference_skills_compared',all('skill:'+Path(n).parent.name in {r['component_id'] for r in comp} for n in names if n.endswith('SKILL.md')));check('all_reference_schemas_compared',all('schema:'+Path(n).name.removesuffix('.schema.json') in {r['component_id'] for r in comp} for n in names if '/schemas/' in n and n.endswith('.schema.json')))
check('handoff_A_through_Z',all('\n## '+chr(i)+'. ' in (O/'INTEGRATION_HANDOFF.md').read_text(encoding='utf-8') for i in range(65,91)))
# Full pre-audit file comparison, including Git internals. Do not hide host metadata changes.
b=j('INITIAL_BASELINE.json');changes=[]
for r in b['files']:
    p=R/r['path']
    if not p.is_file():changes.append({'path':r['path'],'change':'missing'})
    else:
        digest=h(p)
        if digest!=r['sha256']:changes.append({'path':r['path'],'change':'content_changed','before':r['sha256'],'after':digest})
old={x['path'] for x in b['files']};new=[p.relative_to(R).as_posix() for p in R.rglob('*') if p.is_file() and not p.is_relative_to(O) and p.relative_to(R).as_posix() not in old and p!=R/'analysis/workspace_audit_for_integration.zip']
gs=subprocess.run(['git','--no-optional-locks','status','--porcelain=v1','-uall'],cwd=R,capture_output=True,text=True).stdout
clean=lambda s:sorted(x for x in s.splitlines() if 'analysis/workspace_audit' not in x)
pres={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'preexisting_files_checked':len(b['files']),'content_changes':changes,'new_files_outside_approved_outputs':new,'git_status':gs,'git_status_outside_audit_unchanged':clean(gs)==clean(b['git_status']),'preexisting_non_git_content_changes':[x for x in changes if not x['path'].startswith('.git/')],'non_git_additions_outside_approved_outputs':[x for x in new if not x.startswith('.git/')],'intentional_preexisting_modifications_by_audit':False,'attribution':'OBSERVED Git metadata changes; Codex turn-diff paths suggest host capture activity. Exact index-writer attribution UNKNOWN. Audit issued no Git mutation command.'}
save('PRESERVATION_CHECK.json',pres)
check('research_and_control_files_preserved',not pres['preexisting_non_git_content_changes'])
check('no_non_git_files_added_outside_allowed_outputs',not pres['non_git_additions_outside_approved_outputs'])
check('Git_worktree_status_preserved_outside_audit',pres['git_status_outside_audit_unchanged'])
check('reference_not_extracted_into_live_tree',not pres['non_git_additions_outside_approved_outputs'] and not (O/'_reference_architecture').exists())
exceptions=[]
if changes or new:exceptions.append('Pre-existing Git index changed and Codex turn-diff metadata changed/appeared. All non-Git inputs remain byte-identical; exact metadata writer attribution unknown. See PRESERVATION_CHECK.json.')
u=j('UNRESOLVED_REGISTER.json')
if exceptions and not any(x['id']=='U13' for x in u):
    u.append({'id':'U13','unknown':'Exact writer of changed Git index/runtime capture metadata during multi-session audit','why':'No mutation command issued by audit; automatic Codex capture paths changed across recovery','examined':'INITIAL_BASELINE.json; PRESERVATION_CHECK.json; Git status before/after','resolving_evidence':'Host/runtime file-write logs','migration_effect':'Does not block audit or preservation of research inputs; prevents claim every Git-internal byte stayed unchanged'})
    save('UNRESOLVED_REGISTER.json',u)
    with (O/'UNRESOLVED_QUESTIONS.md').open('a',encoding='utf-8') as f:f.write('\n## U13. Git metadata writer\n\nUNKNOWN: exact writer of changed Git index and Codex turn-diff capture metadata during the recovered session. OBSERVED: all pre-existing non-Git files are byte-identical and Git status outside audit outputs is unchanged. No Git mutation command was issued. Host capture activity is an inference from `.git/refs/codex/turn-diffs/` paths, not a proven actor for every index byte. Runtime write logs would resolve attribution; this does not block research-file preservation or audit handoff. See PRESERVATION_CHECK.json.\n')
notice='''\n## Final preservation observation\n\nOBSERVED: all pre-existing non-Git research/control files and the original reference ZIP remain byte-identical. Git status outside audit outputs is unchanged. Git-internal metadata did change: the index differs and Codex turn-diff capture files were added/replaced. The audit issued no Git mutation command and intentionally modified no pre-existing file; exact metadata writer attribution is UNKNOWN. Do not interpret this as an all-Git-bytes-unchanged guarantee. Full paths and before/after hashes are in PRESERVATION_CHECK.json. The session also observed PowerShell7.6.5 initially and7.6.6 after recovery; both environment observations are retained.\n'''
for name in ['EXECUTIVE_SUMMARY.md','INTEGRATION_HANDOFF.md','STATE_DRIFT_REPORT.md','WORKSPACE_ARCHITECTURE.md']:
    p=O/name;t=p.read_text(encoding='utf-8')
    if '## Final preservation observation' not in t:t+=notice
    if name=='INTEGRATION_HANDOFF.md':t=t.replace('lists 12 unknowns','lists 13 unknowns').replace('lists12 unknowns','lists 13 unknowns')
    p.write_text(t,encoding='utf-8')
snapshot=j('WORKSPACE_SNAPSHOT.json');snapshot['audit_timestamp']=datetime.datetime.now(datetime.timezone.utc).isoformat();snapshot['unresolved_issue_count']=len(u);snapshot['environment']['final_observation']=j('ENVIRONMENT_OBSERVATIONS.json');snapshot['preservation']={k:v for k,v in pres.items() if k not in ['git_status','new_files_outside_approved_outputs']};snapshot['preservation']['new_git_metadata_count']=len(new)
final_names=sorted(p.name for p in O.iterdir() if p.is_file() and p.suffix in ['.md','.csv','.json'] and not p.name.startswith('_') and p.name not in ['PACKAGE_RECEIPT.json','OUTPUT_HASHES.json'])
final_names=sorted(set(final_names+['VALIDATION_REPORT.json','WORKSPACE_SNAPSHOT.json']))
snapshot['audit_output_file_list']=sorted(set(final_names+['OUTPUT_HASHES.json','PACKAGE_RECEIPT.json']));snapshot['package_file_list']=sorted(set(final_names+['OUTPUT_HASHES.json']));save('WORKSPACE_SNAPSHOT.json',snapshot)
validation={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'all_coverage_and_research_preservation_checks_passed':all(x['passed'] for x in checks),'safety_exceptions':exceptions,'all_preexisting_bytes_unchanged':not changes,'intentionally_modified_preexisting_files':False,'tests_not_run':['No summarization pipeline or state refresh','No reference initialization/migration/controller execution','No scientific source verification suite','No jsonschema runtime test (dependency unavailable); JSON/AST/constraint inspection performed'],'scope':'Audit outputs only; no migration'}
save('VALIDATION_REPORT.json',validation)
if not all(x['passed'] for x in checks):
    print(json.dumps([x for x in checks if not x['passed']],indent=2));raise SystemExit('Audit validation failed; no archive created')
hashes={n:{'sha256':h(O/n),'size_bytes':(O/n).stat().st_size} for n in final_names};save('OUTPUT_HASHES.json',{'files':hashes,'note':'Hashes exclude this self-referential manifest and the post-archive receipt.'})
archive=R/'analysis/workspace_audit_for_integration.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for n in sorted(set(final_names+['OUTPUT_HASHES.json'])):z.write(O/n,arcname='workspace_audit/'+n)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert set(z.namelist())=={'workspace_audit/'+n for n in snapshot['package_file_list']}
    assert all(Path(n).suffix in ['.md','.csv','.json'] and not Path(n).name.startswith('_') for n in z.namelist())
    for n,d in hashes.items():assert hashlib.sha256(z.read('workspace_audit/'+n)).hexdigest()==d['sha256']
receipt={'archive_path':str(archive),'sha256':h(archive),'size_bytes':archive.stat().st_size,'member_count':len(snapshot['package_file_list']),'member_list':snapshot['package_file_list'],'zip_integrity':'PASS','contained_output_hashes':'PASS','excluded':['Source PDFs','Existing summaries/logs/raw extracted text/images','Original reference ZIP and member files','Audit helper scripts and PDF scratch excerpts/renderings','This post-archive receipt'],'note':'Only final audit outputs are packaged; Git metadata safety exception disclosed in reports.'};save('PACKAGE_RECEIPT.json',receipt)
print(json.dumps({'checks':len(checks),'passed':validation['all_coverage_and_research_preservation_checks_passed'],'exceptions':exceptions,'archive':receipt},indent=2))
