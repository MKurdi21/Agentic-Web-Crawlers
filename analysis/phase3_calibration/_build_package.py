import csv,hashlib,json,pathlib,zipfile,re
from datetime import datetime,timezone
R=pathlib.Path(__file__).resolve().parent;ROOT=R.parents[1]
ARCHIVE=R.parent/'phase3_calibration_package.zip'
FORBIDDEN_SEGMENTS={'_deps','private_source_material','private','shadow','holdout_lane','__pycache__','.pytest_cache','uv_cache','deps'}
FORBIDDEN_SUFFIXES={'.pdf','.sqlite','.sqlite3','.db','.tmp','.zip','.7z','.png','.jpg','.jpeg','.pyc','.pyd'}
ROOT_FILES={
 'EXECUTIVE_PHASE3.md','UNEXPECTED_FILE_RESOLUTION.md','CONTROLLER_V3_CHANGELOG.md','CALIBRATION_PROTOCOL.md','CALIBRATION_PROTOCOL_FINGERPRINT.json','FIELD_CATALOG.json','CALIBRATION_CASES.csv','CALIBRATION_RESULTS.md','CALIBRATION_METRICS.json','CALIBRATION_LIMITATIONS.md','VERIFICATION_SAMPLE_MANIFEST.json','HOLDOUT_SELECTION_PROTOCOL.md','PHASE4_VALIDATION_HOLDOUT.csv','HOLDOUT_CONTAMINATION_LOG.json','HOLDOUT_DENYLIST.json','HOLDOUT_FINGERPRINTS.json','FIELD_AUTOMATION_MATRIX.csv','EXISTING_ARTIFACT_REUSE_MATRIX.csv','VERIFICATION_THRESHOLD_STUDY.md','RESEARCH_OBJECT_ADJUDICATION_PACKET.md','INCLUSION_POLICY_OPTIONS.md','PARTIAL_SYNTHESIS_POLICY.md','TAXONOMY_GOVERNANCE_OPTIONS.md','TRUST_AND_REVIEW_POLICY_OPTIONS.md','STORAGE_DECISION_PACKET.md','RETENTION_POLICY_OPTIONS.md','GAP_SCORING_POLICY_OPTIONS.md','EXTERNAL_SEARCH_POLICY_OPTIONS.md','SKILL_CALIBRATION_REPORT.md','POLICY_DECISION_PACKET.md','DEPLOYMENT_READINESS.md','PHASE4_MIGRATION_REHEARSAL_PLAN.md','WEB_METHOD_AND_ARCHITECTURE_SOURCES.md','PHASE3_FINGERPRINTS.json','PRESERVATION_CHECK.json','INITIAL_BASELINE.json',
 '_build_calibration_records.py','_build_holdout_denylist.py','_freeze_calibration.py','_write_phase3_reports.py','_final_preservation.py','_build_package.py','_validate_package.py'}

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def allowed_file(p):
 rel=p.relative_to(R);parts=set(rel.parts)
 if parts&FORBIDDEN_SEGMENTS or p.suffix.lower() in FORBIDDEN_SUFFIXES:return False
 if len(rel.parts)==1:return rel.name in ROOT_FILES
 if rel.parts[0]=='candidate_v3':return rel.parts[1] in {'hardened','deploy_payload'} or rel.as_posix()=='candidate_v3/requirements.txt'
 if rel.parts[0]=='test_results':return True
 if rel.parts[:2]==('calibration_records','sanitized'):return True
 return False

files=sorted([p for p in R.rglob('*') if p.is_file() and allowed_file(p)],key=lambda p:p.relative_to(R).as_posix().casefold())
manifest_path=R/'PACKAGE_MANIFEST.json'
# Do not permit exact bytes from protected research/evidence/control inputs.
forbidden_hashes=set()
for row in csv.DictReader((R/'PROTECTED_FILE_HASHES_INITIAL.csv').open(encoding='utf-8')):
 path=row['path'].replace('\\','/').casefold()
 forbidden = path.endswith('.pdf') or path.startswith('summaries/') or path.startswith('.summary_v2/') or path.startswith('analysis/evidence/') or path in {'analysis/baseline.json','analysis/checkpoint.json','analysis/reviews.json','analysis/workspace_audit_for_integration.zip','analysis/integration_design_package.zip'} or any(x in path for x in ('article.txt','accessibility','generation_log','page_images'))
 if forbidden:forbidden_hashes.add(row['sha256'])
inventory=[]
for p in files:
 data=p.read_bytes();h=hashlib.sha256(data).hexdigest();rel=p.relative_to(R).as_posix()
 if h in forbidden_hashes:raise SystemExit('FORBIDDEN_ORIGINAL_HASH:'+rel)
 if data.startswith(b'%PDF-'):raise SystemExit('PDF_SIGNATURE:'+rel)
 if re.search(rb'JVBERi0[0-9A-Za-z+/=]{80,}',data):raise SystemExit('BASE64_PDF:'+rel)
 inventory.append({'path':'phase3_calibration/'+rel,'size':len(data),'sha256':h,'classification':'PACKAGEABLE_DESIGN_OUTPUT'})
manifest={'schema_version':'1.0.0','created_at':datetime.now(timezone.utc).isoformat(),'package_root':'phase3_calibration/','manifest_self_rule':'PACKAGE_MANIFEST.json is the sole control member outside payload_inventory; self-hashing is excluded to avoid recursion. All other members are exact.','allowed_roots':['candidate_v3/hardened/','candidate_v3/deploy_payload/','test_results/','calibration_records/sanitized/'],'forbidden_classes':['PRIVATE_SHADOW_TEST_INPUT','PDF','legacy/v2 summary','article.txt','page image','accessibility extraction','historical log','raw evidence text','existing control file','audit/reference package','database','backup','runtime store','nested archive'],'payload_inventory':inventory}
manifest_path.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8');manifest_bytes=manifest_path.read_bytes()
if ARCHIVE.exists():ARCHIVE.unlink()
with zipfile.ZipFile(ARCHIVE,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 z.writestr('phase3_calibration/PACKAGE_MANIFEST.json',manifest_bytes)
 for p,row in zip(files,inventory):z.write(p,row['path'])

# Independent membership/hash/CRC/path/content check reads the finished archive.
errors=[]
with zipfile.ZipFile(ARCHIVE) as z:
 infos=z.infolist();names=[i.filename for i in infos];expected={'phase3_calibration/PACKAGE_MANIFEST.json',*[x['path'] for x in inventory]}
 if set(names)!=expected:errors.append('MEMBERSHIP')
 if len(names)!=len(set(names)):errors.append('DUPLICATE')
 if len({n.casefold() for n in names})!=len(names):errors.append('CASE_COLLISION')
 if any(pathlib.PurePosixPath(n).is_absolute() or '..' in pathlib.PurePosixPath(n).parts for n in names):errors.append('TRAVERSAL')
 if z.testzip() is not None:errors.append('CRC')
 lookup={x['path']:x for x in inventory}
 for n in names:
  if n.endswith('PACKAGE_MANIFEST.json'):continue
  data=z.read(n);row=lookup.get(n)
  if not row or len(data)!=row['size'] or hashlib.sha256(data).hexdigest()!=row['sha256']:errors.append('HASH:'+n)
  pp=pathlib.PurePosixPath(n)
  if set(pp.parts)&FORBIDDEN_SEGMENTS or pp.suffix.lower() in FORBIDDEN_SUFFIXES:errors.append('FORBIDDEN_PATH:'+n)
  if hashlib.sha256(data).hexdigest() in forbidden_hashes:errors.append('FORBIDDEN_HASH:'+n)
  if data.startswith(b'%PDF-') or re.search(rb'JVBERi0[0-9A-Za-z+/=]{80,}',data):errors.append('FORBIDDEN_CONTENT:'+n)
result={'validated_at':datetime.now(timezone.utc).isoformat(),'archive':str(ARCHIVE),'archive_sha256':digest(ARCHIVE),'member_count':len(inventory)+1,'payload_member_count':len(inventory),'manifest_sha256':hashlib.sha256(manifest_bytes).hexdigest(),'crc_ok':not errors,'membership_exact':not errors,'forbidden_content_found':any('FORBIDDEN' in x for x in errors),'errors':errors,'passed':not errors}
(R/'test_results/PACKAGE_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
if errors:raise SystemExit(1)
