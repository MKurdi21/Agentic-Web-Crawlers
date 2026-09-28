"""Unmodified inherited test modules in a phase-local copied package."""
from pathlib import Path
import sys,json,hashlib,zipfile,importlib.util,unittest
O=Path(__file__).resolve().parent;R=O.parents[1];D=O/'inherited_candidate'
if sys.argv[1]=='setup':
 zpath=R/'analysis/phase4bc_path_containment_package.zip'
 assert hashlib.sha256(zpath.read_bytes()).hexdigest()=='25f599dfc78992aef8ac0adb6d82f9243298fddfc3cc7030752dc0edc9f7019d'
 with zipfile.ZipFile(zpath) as z:
  manifest=json.loads(z.read('PACKAGE_MANIFEST.json'))
  for x in manifest['files']:
   n=x['path']
   if n.startswith(('path_containment/','continuity_adapter/','vendor/','inherited_context/','inherited_recovery/','test_results/')) or n in ['CONTENT_IDENTITY_REGISTRY.schema.json','PATH_CONTAINMENT_POLICY.json','APPROVED_ROOTS.json']:
    data=z.read(n);assert hashlib.sha256(data).hexdigest()==x['sha256']
    p=D/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 print('Inherited copies verified')
else:
 label=sys.argv[1];paths={'context':'inherited_context/context_architecture/tests/test_context_engine.py','recovery':'inherited_recovery/recovery_protocol/test_recovery.py','path':'path_containment/test_guard.py','continuity':'continuity_adapter/test_continuity.py'}
 p=D/paths[label];sys.path.insert(0,str(p.parent));spec=importlib.util.spec_from_file_location('inherited_'+label,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 class Result(unittest.TextTestResult):
  def startTest(self,t):super().startTest(t);self.records=getattr(self,'records',[])
  def addSuccess(self,t):super().addSuccess(t);self.records.append({'id':t.id(),'status':'PASS'})
  def addSkip(self,t,reason):super().addSkip(t,reason);self.records.append({'id':t.id(),'status':'SKIP','reason':reason})
  def addError(self,t,e):super().addError(t,e);self.records.append({'id':t.id(),'status':'ERROR','diagnostic':self._exc_info_to_string(e,t)})
  def addFailure(self,t,e):super().addFailure(t,e);self.records.append({'id':t.id(),'status':'FAIL','diagnostic':self._exc_info_to_string(e,t)})
 r=unittest.TextTestRunner(verbosity=1,resultclass=Result).run(unittest.defaultTestLoader.loadTestsFromModule(m))
 output={'suite':label,'tests':r.testsRun,'passed':r.testsRun-len(r.errors)-len(r.failures)-len(r.skipped),'failed':len(r.errors)+len(r.failures),'skipped':len(r.skipped),'records':r.records,'source_test_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'unchanged_assertions':True}
 (O/'test_results'/('INHERITED_'+label.upper()+'.json')).write_text(json.dumps(output,sort_keys=True,indent=2),encoding='utf-8')
 raise SystemExit(not r.wasSuccessful())
