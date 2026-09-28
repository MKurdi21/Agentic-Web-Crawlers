import sys,os,json,hashlib,tempfile,stat,subprocess,unittest,ctypes
from pathlib import Path
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;R=O.parents[1];BC=R/'analysis/phase4bc_context_isolation'
assert json.loads((O/'PHASE4BC_S_BASELINE.json').read_text())['passed']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ps(s):
 p=subprocess.run(['powershell','-NoProfile','-Command',s],capture_output=True,text=True)
 return {'stdout':p.stdout.strip(),'stderr':p.stderr.strip(),'exit_code':p.returncode}
env={'volumes':ps('Get-CimInstance Win32_LogicalDisk | Select-Object DeviceID,FileSystem,DriveType | ConvertTo-Json'),'privileges':subprocess.run(['whoami','/priv'],capture_output=True,text=True).stdout,'developer_mode':ps("Get-ItemProperty -LiteralPath 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\AppModelUnlock' -Name AllowDevelopmentWithoutDevLicense -ErrorAction SilentlyContinue | Select-Object AllowDevelopmentWithoutDevLicense | ConvertTo-Json"),'elevated':bool(ctypes.windll.shell32.IsUserAnAdmin()),'os':sys.platform,'python':sys.version,'temp_root':tempfile.gettempdir(),'workspace':'G:','workspace_filesystem':'FAT32'}
vols=json.loads(env['volumes']['stdout']);drive=Path(tempfile.gettempdir()).drive.upper();assert next(v['FileSystem'] for v in vols if v['DeviceID'].upper()==drive)=='NTFS'
env['test_filesystem']='NTFS'
sys.path.insert(0,str(BC/'context_architecture/tests'));import test_context_engine as t
sys.path.insert(0,str(BC/'context_architecture/scripts'));import context_engine as e
fixture=Path(tempfile.mkdtemp(prefix='phase4bc_s_symlink_')).resolve();env['test_path']=str(fixture)
assert fixture.is_relative_to(Path(tempfile.gettempdir()).resolve())
test=t.PacketTests('test_symlink_rejected');test.root=fixture;test.doc=fixture/'method.md';test.doc.write_text('Require exact source identity and located atomic propositions.',encoding='utf-8')
test.registry={'artifacts':[{'artifact_id':'method','path':'method.md','sha256':e.digest(test.doc.read_bytes()),'layer':'A','role':'both','reason':'generic science','permitted_content_category':'generic_methodology','dependencies':[]}]}
test.allow={'primary':['method'],'verifier':['method']};test.binding={'phase':'SYNTHETIC_TEST','holdout_id':'SYNTHETIC_01','paper_id':'SYNTHETIC_REPORT','source_sha256':e.digest(b'SYNTHETIC_EXAMPLE'),'methodology_sha256':'a'*64,'context_protocol_version':e.VERSION,'current_report_source':'NOT_YET_OPENED'}
positive=test.build();assert positive[0]
observed={};original=test.build
def audited_build():
 link=fixture/'link.md';s=link.lstat();observed.update(is_symlink=link.is_symlink(),reparse_tag=getattr(s,'st_reparse_tag',None),target=str(link.resolve()),target_matches=link.resolve()==test.doc.resolve(),regular_target=stat.S_ISREG(test.doc.stat().st_mode))
 assert observed['is_symlink'] and observed['reparse_tag']==0xA000000C and observed['target_matches']
 try:return original()
 except e.GuardError as exc:observed['guard_rejection']=str(exc);raise
test.build=audited_build
result={'original_test_id':'test_context_engine.PacketTests.test_symlink_rejected','original_test_source_sha256':sha(BC/'context_architecture/tests/test_context_engine.py'),'guard_sha256':sha(BC/'context_architecture/scripts/context_engine.py'),'architecture_sha256':'63927844eaac94765a7a804ab128076a88cad6eac2f534b715b08b17c4e21606','original_status':'SKIP','positive_regular_file_passed':True,'fixture_synthetic':True,'fixture_adapter':'Original test method unchanged; identical relevant setUp fields populated with fixture root on NTFS; no old setUp writes. Instrumented build records real link properties then calls unchanged builder.'}
try:
 test.test_symlink_rejected();assert observed.get('guard_rejection');result.update(status='PASS',symlink_capability='SYMLINK_SUPPORTED_AND_TESTABLE',invariant_satisfied=True)
except unittest.SkipTest as exc:
 result.update(status='ENVIRONMENT_BLOCKED',symlink_capability='SYMLINK_PRIVILEGE_BLOCKED' if '1314' in str(exc) else 'UNKNOWN_ENVIRONMENT_FAILURE',reason=str(exc),invariant_satisfied=False)
except Exception as exc:result.update(status='FAIL',symlink_capability='SYMLINK_TEST_IMPLEMENTATION_FAILURE',reason=repr(exc),invariant_satisfied=False)
finally:
 link=fixture/'link.md'
 if link.is_symlink():link.unlink()
 elif link.exists():result['cleanup_unexpected_object']=str(link)
 if test.doc.resolve().is_relative_to(fixture):test.doc.unlink()
 try:fixture.rmdir();result['cleanup']='REMOVED_SYNTHETIC_ROOT'
 except OSError as exc:result['cleanup']='LEFTOVERS_RECORDED';result['cleanup_error']=str(exc)
result['link_observation']=observed;env['capability']=result['symlink_capability']
(O/'SYMLINK_ENVIRONMENT_PROBE.json').write_text(json.dumps(env,indent=2),encoding='utf-8');(O/'REAL_SYMLINK_TEST_RESULT.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
