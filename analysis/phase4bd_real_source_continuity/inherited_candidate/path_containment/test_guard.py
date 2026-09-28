import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).parent))
from guard import *
O=Path(__file__).resolve().parents[1]
PRIVATE=O/'private_test_storage';PRIVATE.mkdir(exist_ok=True)
class PathTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(dir=PRIVATE);self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name);self.root=self.base/'approved';self.root.mkdir();self.outside=self.base/'forbidden';self.outside.mkdir()
        (self.root/'method.md').write_text('Use exact source identity and atomic propositions.',encoding='utf-8')
        (self.outside/'history.md').write_text('SYNTHETIC_FORBIDDEN_HISTORY',encoding='utf-8')
        self.records=[self.entry('method','method.md')];self.allow={'primary':['method'],'verifier':['method']}
        self.binding={'phase':'SYNTHETIC_TEST','holdout_id':'SYNTHETIC_X','paper_id':'SYNTHETIC_REPORT_X','source_sha256':'a'*64,'methodology_sha256':'b'*64,'context_protocol_version':context.VERSION,'current_report_source':'NOT_YET_OPENED'}
    def entry(self,id,path,**kw):
        return dict(artifact_id=id,path=path,root_id='approved',sha256=context.digest((self.root/path).read_bytes()),content_class='GENERIC_METHODOLOGY',packet_types=['primary','verifier'],immutable=True,dependencies=[],layer='A',role='both',**kw)
    def guard(self,**kw):return Guard({'approved':self.root},self.records,self.allow,**kw)
    def test_01_approved_relative(self):self.assertTrue(self.guard().packet(self.binding,'primary')[0])
    def test_02_parent_escape(self):
        with self.assertRaises(Rejected):self.guard().read('method','primary','../forbidden/history.md')
    def test_03_deep_escape(self):
        with self.assertRaises(Rejected):self.guard().read('method','primary','a/../../forbidden/history.md')
    def test_04_absolute_outside(self):
        with self.assertRaises(Rejected):self.guard().read('method','primary',str(self.outside/'history.md'))
    def test_05_other_drive(self):
        with self.assertRaises(Rejected):self.guard().read('method','primary','Z:/outside.md')
    def test_06_exit_reenter(self):
        with self.assertRaises(Rejected):self.guard().read('method','primary','../approved/method.md')
    def test_07_unregistered_inside(self):
        (self.root/'unregistered.md').write_text('invented')
        with self.assertRaises(Rejected):self.guard().read('unregistered','primary')
    def test_08_hash_mutation(self):
        (self.root/'method.md').write_text('mutated')
        with self.assertRaises(Rejected):self.guard().packet(self.binding,'primary')
    def test_09_history_class(self):
        self.records[0]['content_class']='HISTORICAL_DEVELOPMENT_ONLY'
        with self.assertRaises(Rejected):self.guard().packet(self.binding,'primary')
    def test_10_glob(self):
        with self.assertRaises(Rejected):self.guard().read('method','primary','../**/*.md')
    def test_11_injected_escape(self):
        with self.assertRaises(Rejected):self.guard(resolver=lambda p:self.outside/'history.md').packet(self.binding,'primary')
    def test_12_case_handling(self):
        self.records.append({**self.records[0],'artifact_id':'alias','path':'METHOD.MD'})
        with self.assertRaises(Rejected):self.guard()
    def test_13_separator(self):
        (self.root/'sub').mkdir();(self.root/'sub/m.md').write_text('generic')
        self.records=[self.entry('method','sub/m.md')]
        a=self.guard().read('method','primary','sub\\m.md');b=self.guard().read('method','primary','sub/m.md');self.assertEqual(a,b)
    def test_14_dot_alias_duplicate(self):
        self.records.append({**self.records[0],'artifact_id':'alias','path':'./method.md'})
        with self.assertRaises(Rejected):self.guard()
    def test_15_content_match(self):
        b,r=self.guard().read('method','primary');self.assertEqual(context.digest(b),r['sha256'])
    def test_16_unregistered_copy(self):
        (self.root/'copy.md').write_bytes((self.root/'method.md').read_bytes())
        with self.assertRaises(Rejected):self.guard().read('method','primary','copy.md')
    def test_17_classification(self):
        self.records[0]['content_class']='RAW_SOURCE'
        with self.assertRaises(Rejected):self.guard().packet(self.binding,'primary')
    def chain(self):
        (self.root/'method.md').write_text('[child](child.md)')
        (self.root/'child.md').write_text('[leaf](leaf.md)')
        (self.root/'leaf.md').write_text('Require direct support.')
        self.records=[self.entry('method','method.md'),self.entry('child','child.md'),self.entry('leaf','leaf.md')]
        self.records[0]['dependencies']=['child'];self.records[1]['dependencies']=['leaf']
        self.allow={r:['method','child','leaf'] for r in ['primary','verifier']}
    def test_18_nested_escape(self):
        self.chain();self.records[2]['path']='../forbidden/history.md'
        with self.assertRaises(Rejected):self.guard().packet(self.binding,'primary')
    def test_19_nested_allowed(self):
        self.chain();packet,meta=self.guard().packet(self.binding,'primary');self.assertEqual(len(meta['transitive_inventory']),3)
    def test_20_template_history(self):
        self.chain();self.records[2]['layer']='D'
        with self.assertRaises(Rejected):self.guard().packet(self.binding,'primary')
    def test_21_prefix_not_containment(self):
        with self.assertRaises(Rejected):lexical(str(self.base/'approved2/method.md'),self.root)
    def test_22_cycle(self):
        self.chain();self.records[2]['dependencies']=['method']
        with self.assertRaises(Rejected):self.guard().packet(self.binding,'primary')
    def test_23_unknown_reference(self):
        (self.root/'method.md').write_text('[secret](unknown.md)');self.records=[self.entry('method','method.md')]
        with self.assertRaises(context.GuardError):self.guard().packet(self.binding,'primary')
    def test_24_windows_aliases(self):
        for p in ['method.md:stream','method.md.','method.md ','CON.txt','%TEMP%/method.md','//server/share/file','G:method.md']:
            with self.assertRaises(Rejected):self.guard().read('method','primary',p)
    def test_25_dot_normalization(self):self.assertEqual(self.guard().read('method','primary','./method.md'),self.guard().read('method','primary'))
    def test_26_inside_indirect_identity(self):
        (self.root/'copy.md').write_bytes((self.root/'method.md').read_bytes())
        with self.assertRaises(Rejected):self.guard(resolver=lambda p:self.root/'copy.md').packet(self.binding,'primary')
    def test_27_mutable_asset(self):
        self.records[0]['immutable']=False
        with self.assertRaises(Rejected):self.guard().packet(self.binding,'primary')
    def test_28_dependency_not_allowed(self):
        self.chain();self.allow['primary'].remove('leaf')
        with self.assertRaises(Rejected):self.guard().packet(self.binding,'primary')
    def test_29_reparse_detection_branch(self):
        from unittest.mock import patch
        from types import SimpleNamespace
        original=Path.lstat;leaf=self.root/'method.md';g=self.guard()
        def observed(p,*a,**kw):
            if p==leaf:return SimpleNamespace(st_mode=stat.S_IFREG,st_file_attributes=0x400)
            return original(p,*a,**kw)
        with patch.object(Path,'lstat',observed):
            with self.assertRaises(Rejected):g.packet(self.binding,'primary')
    def test_30_configuration_snapshot(self):
        g=self.guard();before=g.packet(self.binding,'primary')[0]
        self.allow['primary'].clear();self.records[0]['dependencies'].append('historical')
        self.assertEqual(g.packet(self.binding,'primary')[0],before)

def run():
    class Results(unittest.TextTestResult):
        def startTest(self,t):super().startTest(t);self.records=getattr(self,'records',[])
        def addSuccess(self,t):super().addSuccess(t);self.records.append({'id':t.id(),'status':'PASS'})
        def addError(self,t,e):super().addError(t,e);self.records.append({'id':t.id(),'status':'ERROR','reason':self._exc_info_to_string(e,t)})
        def addFailure(self,t,e):super().addFailure(t,e);self.records.append({'id':t.id(),'status':'FAIL','reason':self._exc_info_to_string(e,t)})
    result=unittest.TextTestRunner(verbosity=2,resultclass=Results).run(unittest.defaultTestLoader.loadTestsFromTestCase(PathTests))
    report={'version':VERSION,'tests':result.testsRun,'passed':result.testsRun-len(result.errors)-len(result.failures),'failed':len(result.errors)+len(result.failures),'skipped':len(result.skipped),'records':result.records}
    (O/'test_results').mkdir(exist_ok=True)
    import uuid
    (O/'test_results'/('path-'+uuid.uuid4().hex+'.json')).write_bytes(context.canonical(report))
    if result.wasSuccessful():(O/'PATH_CONTAINMENT_TEST_RESULTS.json').write_bytes(context.canonical(report))
    raise SystemExit(not result.wasSuccessful())
if __name__=='__main__':run()
