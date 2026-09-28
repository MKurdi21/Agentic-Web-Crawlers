import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).parent))
from adapter import *
PRIVATE=BASE/'private_test_storage';PRIVATE.mkdir(exist_ok=True)
REVIEW=BASE/'test_results/EXACT_PACKET_SEMANTIC_REVIEW.json'
class ContinuityTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(dir=PRIVATE);self.addCleanup(self.temp.cleanup)
        self.run=Path(self.temp.name)/'run';self.a=Continuity(self.run).create(REVIEW)
    def access(self):self.a.access('fresh-primary-1')
    def assert_unique(self):
        chain=self.a.e.receipts();ids=[r['atomic_unit_id'] for _,r in chain];self.assertEqual(len(ids),len(set(ids)))
    def test_01_before_source(self):
        s=Continuity(self.run).recover('new-session');self.assertFalse(s['source_access_started']);self.assertEqual(s['active_holdout_state'],'UNTOUCHED_RESERVED_VALIDATION_EVIDENCE')
    def test_02_immediately_after_source(self):
        self.access();s=Continuity(self.run).recover('new-session');self.assertTrue(s['source_access_started']);self.assertEqual(s['active_holdout_state'],'CONSUMED_VALIDATION_EVIDENCE')
    def test_03_extraction_before_commit(self):
        self.access();self.a.unit('primary','lost-session','before_commit');a=Continuity(self.run);a.recover('new-primary');r=a.unit('primary','new-primary');self.assertEqual(r['value'],0.7);self.assert_unique()
    def test_04_after_primary_commit(self):
        self.access();self.a.unit('primary','first','after_commit');a=Continuity(self.run);a.recover('new-primary');r=a.unit('primary','replay');self.assertEqual(r['value'],0.7);self.assert_unique()
    def test_05_during_verifier(self):
        self.access();self.a.unit('primary','first');self.a.unit('verifier','lost-verifier','before_commit');a=Continuity(self.run);a.recover('fresh-verifier');self.assertEqual(a.unit('verifier','fresh-verifier')['outcome'],'SUPPORTED');self.assert_unique()
    def test_06_after_verifier_commit(self):
        self.access();self.a.unit('primary','first');self.a.unit('verifier','verify','after_commit');a=Continuity(self.run);a.recover('new');a.unit('verifier','replay');self.assert_unique()
    def test_07_duplicate_recover(self):
        self.access();self.a.unit('primary','first');a=Continuity(self.run);x=a.recover('new');y=a.recover('new');self.assertEqual(x['last_committed_milestone_receipt_sha256'],y['last_committed_milestone_receipt_sha256']);self.assert_unique()
    def test_08_new_session_end_to_end(self):
        self.access();self.a.unit('primary','initial');self.a.unit('verifier','old','before_worker');a=Continuity(self.run);a.recover('entirely-new','NEW_SESSION');a.unit('verifier','entirely-new');self.assert_unique()
        contexts=[read(p) for p in (self.run/'context_receipts').glob('*.json')];self.assertTrue(all(x['fork_history']=='none' and x['new_process'] for x in contexts))
    def test_09_same_session(self):
        self.access();self.a.unit('primary','session','before_commit');self.a.recover('session','RESUMED_SESSION');self.a.unit('primary','session');self.assert_unique()
    def test_10_context_firewall(self):
        p=self.run/'assets/method.md';p.write_text(ASSETS['method.md']+' coordinator recovery diagnosis SYNTHETIC_PRIOR_FAILURE_LESSON')
        with self.assertRaises(Exception):Continuity(self.run).recover('new')
    def test_11_packet_mutation(self):
        p=self.run/'assets/primary.md';p.write_text('Different unapproved packet')
        with self.assertRaises(Exception):self.a.recover('new')
    def test_12_source_drift(self):
        (self.run/'source.json').write_text('{}')
        with self.assertRaises(Exception):self.a.recover('new')
    def test_13_stale_semantic_review(self):
        p=self.run/'reviews.json';v=read(p);v['primary']['packet_sha256']='0'*64;p.write_bytes(canonical(v))
        with self.assertRaises(Exception):self.a.recover('new')
    def test_14_missing_receipt(self):
        self.access();(self.run/'context_session/01_PRE_ACCESS_RECEIPT.json').unlink()
        with self.assertRaises(Exception):self.a.recover('new')
    def test_15_committed_primary_corruption(self):
        self.access();self.a.unit('primary','first');(self.a.e.root/'outputs/primary.json').write_text('{}')
        with self.assertRaises(Exception):self.a.recover('new')
    def test_16_unknown_worker_narrative(self):
        from worker import execute
        with self.assertRaises(c.GuardError):execute({'coordinator_summary':'SYNTHETIC_PRIOR_FAILURE_LESSON'})
    def test_17_source_consumption_never_reverts(self):
        self.access();self.a.unit('primary','lost','before_commit');self.a.recover('new');self.assertTrue(self.a.e.state()['source_access_started'])
    def test_18_injected_fingerprint(self):
        p=self.run/'frozen.json';v=read(p);v['pins']['path_containment']='0'*64;p.write_bytes(canonical(v))
        with self.assertRaises(Exception):self.a.recover('new')
    def test_19_no_worker_before_access(self):
        with self.assertRaises(c.GuardError):self.a.worker('primary','new')
    def test_20_ambiguous_access_boundary(self):
        packets=self.a.packets()
        with self.a.e.lock('synthetic'):
            self.a.e.source_access_synthetic({'packet_sha256':c.digest(packets['primary']),'semantic_status':'SEMANTIC_CONTEXT_CLEAN'})
        with self.assertRaises(Blocked):self.a.recover('new')
    def test_21_transplanted_source_receipt_chain(self):
        self.access();session=self.run/'context_session';p=session/'01_PRE_ACCESS_RECEIPT.json';r=read(p);r['packet_sha256']='0'*64;p.write_bytes(canonical(r))
        p=session/'02_CONTEXT_ACK.json';a=read(p);a['previous_sha256']=c.fingerprint(r);a['packet_sha256']='0'*64;p.write_bytes(canonical(a))
        p=session/'03_SOURCE_ACCESS_BEGAN.json';d=read(p);d['previous_sha256']=c.fingerprint(a);p.write_bytes(canonical(d))
        with self.assertRaises(c.GuardError):self.a.recover('new')
    def test_22_torn_terminal_journal(self):
        self.access();p=self.a.e.root/'RECOVERY_EVENTS.jsonl';original=p.read_bytes();p.write_bytes(original+b'{"torn":')
        self.assertTrue(Continuity(self.run).recover('new')['source_access_started']);self.assertEqual(p.read_bytes(),original+b'{"torn":')
    def test_23_malformed_state_projection(self):
        self.access();self.a.unit('primary','one');(self.a.e.root/'RECOVERY_STATE.json').write_bytes(b'{"partial":')
        s=Continuity(self.run).recover('new');self.assertTrue(s['source_access_started']);self.assertEqual(s['last_committed_milestone'],'PRIMARY')
    def test_24_executed_recovery_dependencies_pinned(self):
        import inspect
        self.assertEqual(filehash(Path(inspect.getfile(Engine))),filehash(BASE/'inherited_recovery/recovery_protocol/engine.py'))
        from unittest.mock import patch
        original=filehash
        def changed(p):
            if str(p).endswith('MILESTONE_RECEIPT.schema.json'):return '0'*64
            return original(p)
        with patch('adapter.filehash',changed):
            with self.assertRaises(c.GuardError):self.a.recover('new')
    def test_25_coordinator_metadata_not_delivered(self):
        self.access()
        from unittest.mock import patch
        original=subprocess.run;seen=[]
        def capture(*a,**kw):seen.append(c.loads(kw['input']));return original(*a,**kw)
        with patch('adapter.subprocess.run',capture):self.a.unit('primary','arbitrary coordinator history with prior failure')
        self.assertNotIn('session_id',seen[0]);self.assertNotIn('arbitrary coordinator',str(seen[0]))
    def test_26_cached_replay_checks_drift(self):
        self.access();self.a.unit('primary','first');(self.run/'source.json').write_text('{}')
        with self.assertRaises(c.GuardError):self.a.unit('primary','replay')
    def test_27_generic_contract_not_fixed_report(self):
        from context_contract import reconstruct_worker_context
        self.access();frozen,packets=self.a.verify_inputs();s=self.run/'context_session'
        b=binding();b['paper_id']='SYNTHETIC_REPORT_Y';b['holdout_id']='SYNTHETIC_Y'
        body=c.loads(packets['primary']);body['binding']=b;p=c.canonical(body)
        decision=self.a.release('primary',packets['primary']);decision={**decision,'binding_sha256':c.fingerprint(b),'packet_sha256':c.digest(p)} # synthetic mechanics fixture only
        r=c.load(s/'01_PRE_ACCESS_RECEIPT.json');r['binding']=b;r['packet_sha256']=c.digest(p);r['release_sha256']=c.fingerprint(decision)
        a=c.load(s/'02_CONTEXT_ACK.json');a['packet_sha256']=r['packet_sha256'];a['previous_sha256']=c.fingerprint(r)
        d=c.load(s/'03_SOURCE_ACCESS_BEGAN.json');d['previous_sha256']=c.fingerprint(a)
        envelope=reconstruct_worker_context(packet=p,expected_binding=b,source_bytes=SOURCE,stage='primary',primary_item=None,approved_packet_sha256=c.digest(p),source_consumed=True,preaccess=r,ack=a,access=d,release_decision=decision,expected_release_sha256=r['release_sha256'],expected_code_sha256=r['immutable_code_sha256'],expected_policy_sha256=r['policy_sha256'],expected_template_sha256=r['template_sha256'],expected_access_namespace='SYNTHETIC_TEST_ONLY')
        self.assertEqual(c.loads(c.loads(envelope)['packet'])['binding']['paper_id'],'SYNTHETIC_REPORT_Y')

    def test_28_primary_packet_receipt_mismatch(self):
        self.access();frozen,packets=self.a.verify_inputs();s=self.run/'context_session'
        body=c.loads(packets['primary']);body['context'][0]['content']+=' Extra generic text.'
        p=c.canonical(body);r=c.load(s/'01_PRE_ACCESS_RECEIPT.json');decision=self.a.release('primary',packets['primary'])
        with self.assertRaises(c.GuardError):
            reconstruct_worker_context(packet=p,expected_binding=binding(),source_bytes=SOURCE,stage='primary',primary_item=None,approved_packet_sha256=c.digest(p),source_consumed=True,preaccess=r,ack=c.load(s/'02_CONTEXT_ACK.json'),access=c.load(s/'03_SOURCE_ACCESS_BEGAN.json'),release_decision=decision,expected_release_sha256=r['release_sha256'],expected_code_sha256=r['immutable_code_sha256'],expected_policy_sha256=r['policy_sha256'],expected_template_sha256=r['template_sha256'],expected_access_namespace='SYNTHETIC_TEST_ONLY')

if __name__=='__main__':
    class Result(unittest.TextTestResult):
        def startTest(self,t):super().startTest(t);self.records=getattr(self,'records',[])
        def addSuccess(self,t):super().addSuccess(t);self.records.append({'id':t.id(),'status':'PASS'})
        def addError(self,t,e):super().addError(t,e);self.records.append({'id':t.id(),'status':'ERROR','reason':self._exc_info_to_string(e,t)})
        def addFailure(self,t,e):super().addFailure(t,e);self.records.append({'id':t.id(),'status':'FAIL','reason':self._exc_info_to_string(e,t)})
    r=unittest.TextTestRunner(verbosity=2,resultclass=Result).run(unittest.defaultTestLoader.loadTestsFromTestCase(ContinuityTests))
    report={'version':VERSION,'tests':r.testsRun,'passed':r.testsRun-len(r.errors)-len(r.failures),'failed':len(r.errors)+len(r.failures),'skipped':len(r.skipped),'records':r.records,'claims':'Synthetic mechanics only; no holdout scientific validation','process_sessions':'Fresh subprocess per scientific unit; same/new coordinator identity tests. No claim about actual Codex service resume.'}
    (BASE/'test_results'/('continuity-'+uuid.uuid4().hex+'.json')).write_bytes(canonical(report))
    if r.wasSuccessful():(BASE/'CONTINUITY_TEST_RESULTS.json').write_bytes(canonical(report))
    raise SystemExit(not r.wasSuccessful())
