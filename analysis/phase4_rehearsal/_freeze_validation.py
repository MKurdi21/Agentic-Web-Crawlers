import csv,hashlib,json,pathlib
from datetime import datetime,timezone
ROOT=pathlib.Path(__file__).resolve().parents[2];OUT=pathlib.Path(__file__).resolve().parent
P3=ROOT/'analysis/phase3_calibration';C=OUT/'candidate_frozen'
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def tree(paths,base):
 files=sorted([p for root in paths for p in pathlib.Path(root).rglob('*') if p.is_file()],key=lambda p:p.relative_to(base).as_posix().casefold())
 body='\n'.join(f'{p.relative_to(base).as_posix()}\0{p.stat().st_size}\0{sha(p)}' for p in files)
 return {'sha256':hashlib.sha256(body.encode()).hexdigest(),'file_count':len(files),'files':[{'path':p.relative_to(base).as_posix(),'sha256':sha(p)} for p in files]}
scripts=C/'hardened/scripts';schemas=C/'hardened/schemas';skills=C/'deploy_payload/skills';protocols=C/'deploy_payload/protocols'
holdout=list(csv.DictReader((P3/'PHASE4_VALIDATION_HOLDOUT.csv').open(encoding='utf-8-sig',newline='')))
config={
 'frozen_at':datetime.now(timezone.utc).isoformat(),'status':'FROZEN_BEFORE_SUBSTANTIVE_HOLDOUT_ACCESS','candidate_version':'3.0.0-calibration.1','candidate_fingerprint':'483d13258b55d7b4e1ab7f7ecbc0d2af2a95ae344d3461653a48afa3e4124cf8','phase3_package_sha256':sha(ROOT/'analysis/phase3_calibration_package.zip'),'holdout_selection_sha256':sha(P3/'PHASE4_VALIDATION_HOLDOUT.csv'),'calibration_protocol_sha256':sha(P3/'CALIBRATION_PROTOCOL.md'),'field_catalog_sha256':sha(P3/'FIELD_CATALOG.json'),'automation_policy_sha256':sha(P3/'FIELD_AUTOMATION_MATRIX.csv'),'verification_threshold_policy_sha256':sha(P3/'VERIFICATION_THRESHOLD_STUDY.md'),'controller_code':tree([scripts],C),'schemas':tree([schemas],C),'semantic_validator_hashes':{p.name:sha(p) for p in sorted(scripts.glob('*validate*.py'))},'locator_protocol_hash':hashlib.sha256((sha(P3/'CALIBRATION_PROTOCOL.md')+'\0'+sha(schemas/'normalized_paper.schema.json')+'\0'+sha(schemas/'evidence.schema.json')).encode()).hexdigest(),'verification_protocol_hash':hashlib.sha256((sha(P3/'CALIBRATION_PROTOCOL.md')+'\0'+sha(schemas/'verification.schema.json')+'\0'+sha(P3/'VERIFICATION_THRESHOLD_STUDY.md')).encode()).hexdigest(),'research_object_protocol_hash':sha(protocols/'RESEARCH_OBJECT_PROTOCOL.md'),'taxonomy_protocol_hash':hashlib.sha256((sha(P3/'TAXONOMY_GOVERNANCE_OPTIONS.md')+'\0'+sha(skills/'taxonomy-synthesis/SKILL.md')).encode()).hexdigest(),'skill_bundle':tree([skills],C),'holdout_ids':[r['paper_report_id'] for r in holdout],'verification_mode_policy':['PRIMARY_MODEL_EXTRACTION','SEPARATE_CONTEXT_MODEL_VERIFICATION','NON_INDEPENDENT_SECOND_PASS','INDEPENDENT_HUMAN_SOURCE_REVIEW','TRUSTED_HUMAN_APPROVAL'],'human_source_review_available':False,'trusted_human_approval_available':False}
raw=json.dumps(config,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode();config['frozen_configuration_sha256']=hashlib.sha256(raw).hexdigest()
(OUT/'FROZEN_VALIDATION_CONFIGURATION.json').write_text(json.dumps(config,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
(OUT/'FROZEN_VALIDATION_CONFIGURATION.md').write_text(f'''# Frozen validation configuration

Frozen before substantive holdout access at `{config['frozen_at']}`.

- Candidate: `3.0.0-calibration.1`
- Candidate fingerprint: `{config['candidate_fingerprint']}`
- Configuration fingerprint: `{config['frozen_configuration_sha256']}`
- Phase 3 package: `{config['phase3_package_sha256']}`
- Holdout selection: `{config['holdout_selection_sha256']}`
- Field catalog: `{config['field_catalog_sha256']}`
- Calibration protocol: `{config['calibration_protocol_sha256']}`
- Human source review available: **no**
- Trusted-human approval available: **no**

The configuration, schemas, validators, extraction rules, verification policy, automation policy, research-object rules, taxonomy guidance, and inactive skills may not change after holdout inspection begins. Separate-context Codex verification is model verification, not independent human source review. AI-only validation is capped at `HOLDOUT_VALIDATION_PASS_WITH_LIMITATIONS`.
''',encoding='utf-8')
print(json.dumps({'frozen_configuration_sha256':config['frozen_configuration_sha256'],'candidate':config['candidate_fingerprint'],'holdout':config['holdout_selection_sha256']}))
