import sys,pathlib,shutil,json,unittest
sys.dont_write_bytecode=True
O=pathlib.Path(__file__).resolve().parent;R=O.parents[1];P=O/'private_diagnostic_material';C=P/'inherited_candidate'
old=C/'test_results/UNIT_INTEGRATION_RESULTS.json'
if old.exists():shutil.copyfile(old,P/'INCOMPLETE_FIXTURE_LAYOUT_ATTEMPT.json')
for d in ['b01_failure_fixtures','phase4_failure_fixtures']:
 shutil.copytree(R/'analysis/phase4br_remediation'/d,P/d,dirs_exist_ok=True)
sys.path.insert(0,str(C/'hardened/scripts'))
import common
# Harness-only dependency injection: original code and every assertion unchanged.
# The synthetic root prevents an inherited archive test reading live artifact bodies.
W=P/'synthetic_workspace';(W/'analysis/workspace_audit').mkdir(parents=True,exist_ok=True)
(W/'analysis/PROMPT.md').write_text('SYNTHETIC_TEST prompt identity for pinning\n',encoding='utf-8')
(W/'analysis/workspace_audit/ARTIFACT_INVENTORY.csv').write_text('artifact_path\n',encoding='utf-8')
(C/'test_results/INITIAL_BASELINE.json').write_text(json.dumps({'files':{'synthetic':{'sha256':common.sha(b'Synthetic protected input')}}}),encoding='utf-8')
common.WORKSPACE=W
from run_tests import Results
suite=unittest.defaultTestLoader.discover(str(C/'hardened/tests'))
result=unittest.TextTestRunner(verbosity=1,resultclass=Results).run(suite)
out={'tests_run':result.testsRun,'passed':sum(x['status']=='PASS' for x in result.rows),'failed':len(result.failures)+len(result.errors),'skipped':len(result.skipped),'tests':result.rows,'harness':'Original test assertions/code unchanged; WORKSPACE injected to synthetic private root, required sanitized regression fixtures copied privately.','prior_attempts':['INCOMPLETE_DEPENDENCY_COPY_ATTEMPT.json','INCOMPLETE_FIXTURE_LAYOUT_ATTEMPT.json']}
(O/'test_results').mkdir(exist_ok=True)
(O/'test_results/INHERITED_TEST_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
assert result.wasSuccessful()
