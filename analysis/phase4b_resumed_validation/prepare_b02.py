import sys,json,hashlib,shutil
from pathlib import Path
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent
R=O.parents[1]
C=O/'candidate_v4br'
sys.path.insert(0,str(C/'hardened/scripts'))
from pre_access import commit_preaccess
from validation_guard import verify_manifest,verify_packet
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
cfg=json.loads((O/'FROZEN_CONFIGURATION.json').read_text(encoding='utf-8'))
frozen=cfg['candidate_files']
verify_manifest(C,frozen);verify_manifest(O/'candidate_frozen',frozen)
b=json.loads((O/'BASELINE.json').read_text(encoding='utf-8'))['reserved_reports'][0]
assert b['holdout_id']=='B02'
out=O/'holdout_validation/B02'
src=O/'private_source_material/B02/source.pdf';src.parent.mkdir(parents=True,exist_ok=True)
assert not src.exists()
shutil.copyfile(R/b['path'],src);assert h(src)==b['source_sha256']
protocols={x['relative_path']:x['sha256'] for x in frozen if x['relative_path'].startswith(('deploy_payload/protocols/','frozen_inputs/'))}
field=next(x for x in frozen if x['relative_path'].endswith('FIELD_CATALOG.json'))
binding=dict(phase='PHASE4B_RESUMED_VALIDATION',holdout_id='B02',paper_id=b['report_id'],source_file_id=b['source_file_id'],source_sha256=b['source_sha256'],candidate_manifest_sha256=h(O/'CANDIDATE_CODE_MANIFEST.json'),methodology_sha256=b' '.decode().strip() or 'ad691060099fff81a3e75de6d4ffdfeb4a8906e006dbfbeefc80a6c601f1d07f',protocol_hashes=protocols,field_catalog_sha256=field['sha256'],holdout_state='UNTOUCHED_RESERVED_VALIDATION_EVIDENCE',context_protocol_version='fresh-current-report-only-v1')
packet=dict(report_id=b['report_id'],frozen_protocol_hash=binding['methodology_sha256'],fork_history='none',previous_holdout_scientific_content_included=False,coordinator_summary_included=False,input_hashes=list(protocols.values())+[b['source_sha256']],primary_context_id='/root/resume_b02_primary',source_path=str(src),output_root=str(out),candidate_root=str(C))
verify_packet(packet,current_report=b['report_id'],frozen_protocol_hash=binding['methodology_sha256'],allowed_input_hashes=packet['input_hashes'])
save(out/'PRIMARY_CONTEXT_PACKET.json',packet)
save(out/'SOURCE_BINDING.json',binding)
commit_preaccess(out,binding,allowed_reports={'B02'})
save(out/'IMMUTABLE_BEFORE.json',{'passed':True,'methodology_sha256':binding['methodology_sha256'],'manifest_sha256':h(O/'CANDIDATE_CODE_MANIFEST.json')})
ledger=json.loads((O/'HOLDOUT_ACCESS_LEDGER.json').read_text(encoding='utf-8'))
ledger['reports'][0].update(state='VALIDATION_IN_PROGRESS',primary_context_id='/root/resume_b02_primary')
save(O/'HOLDOUT_ACCESS_LEDGER.json',ledger)
save(O/'EXTRACTION_TOOL_PROVENANCE.json',{'tool':'PyMuPDF','version':'1.26.4','classification':'PRIVATE_TOOLING_NEVER_PACKAGE','files':[{'path':p.relative_to(O).as_posix(),'sha256':h(p)} for p in sorted((O/'private_source_material/tool_deps').rglob('*')) if p.is_file()]})
print('B02 receipt committed; source not substantively opened')
