"""Behavioral recovery tests: invented inputs only, all fixtures NEVER_PACKAGE."""
import json
import os
from pathlib import Path
import sqlite3
import tempfile
import unittest
import uuid
from engine import *
ROOT=Path(__file__).resolve().parents[1]
FIX=ROOT/'private_test_storage';FIX.mkdir(exist_ok=True)
PINS={k:digest(k.encode()) for k in PIN_KEYS}

class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.path=Path(tempfile.mkdtemp(prefix='synthetic-',dir=FIX));self.e=Engine(self.path)
        with self.e.lock('test-new'):self.e.init('synthetic-run',PINS)
    def go(self,op,*args,**kw):
        with self.e.lock('test-context'):return getattr(self.e,op)(*args,**kw)
    def begin(self,policy='CAN_REPLAY_SAFELY'):return self.go('begin','unit1',{'invented':'input'},['outputs/result.json'],policy)
    def crash(self,where):
        self.begin()
        with self.assertRaises(Crash):self.go('commit',{'outputs/result.json':b'{"synthetic":true}'},crash_at=where)
    def recover(self,**kw):return self.go('recover',PINS,**kw)
    def test_01_before_unit(self):self.assertEqual(self.recover()['last_committed_milestone'],None)
    def test_02_mid_computation(self):
        old=self.begin();self.recover();new=self.begin();self.assertNotEqual(old['attempt_id'],new['attempt_id'])
    def test_03_output_before_receipt(self):
        self.crash('outputs');self.recover();self.assertFalse((self.path/'outputs/result.json').exists());self.assertEqual(len(list((self.path/'private_quarantine').rglob('result.json'))),1)
    def test_04_receipt_before_state(self):
        self.crash('receipt');s=self.recover();self.assertEqual(s['last_committed_milestone'],'unit1');self.assertEqual(len(self.e.receipts()),1)
    def test_05_duplicate_recover(self):
        self.crash('receipt');a=self.recover();b=self.recover();self.assertEqual(a['last_committed_milestone_receipt_sha256'],b['last_committed_milestone_receipt_sha256'])
    def test_06_stale_lock(self):
        replace(self.path/'RUN_LOCK.json',{'status':'HELD','pid':4294967294,'process_start':'dead'})
        self.recover();self.assertEqual(len(list((self.path/'lock_diagnostics').glob('*.json'))),1)
    def test_07_partial_state_json(self):
        self.crash('receipt');(self.path/'RECOVERY_STATE.json').write_bytes(b'{"partial":')
        self.assertEqual(self.recover()['last_committed_milestone'],'unit1')
    def test_08_partial_sqlite(self):
        p=self.path/'synthetic.db';p.write_bytes(b'SQLite format 3\x00broken')
        self.assertFalse(sqlite_check(p)['passed']);self.assertEqual(p.read_bytes(),b'SQLite format 3\x00broken')
    def test_09_duplicate_registration(self):
        self.crash('receipt');self.recover();r=self.begin();self.assertTrue(r['already_committed']);self.assertEqual(len(self.e.receipts()),1)
    def drift(self,k):
        pins={**PINS,k:'0'*64}
        with self.assertRaises(Blocked):self.go('recover',pins)
    def test_10_source_drift(self):self.drift('source_sha256')
    def test_11_methodology_drift(self):self.drift('methodology_sha256')
    def test_12_packet_drift(self):self.drift('current_packet_sha256')
    def test_13_before_source(self):self.assertFalse(self.recover()['source_access_started'])
    def test_14_after_source(self):
        self.go('source_access_synthetic',{'packet_sha256':PINS['current_packet_sha256'],'semantic_status':'SEMANTIC_CONTEXT_CLEAN'})
        with self.assertRaises(Blocked):self.recover()
        s=self.recover(continuity={k:True for k in ['same_report','unchanged_pins','clean_context','known_scientific_milestone','unambiguous_acceptance','fresh_packet_review']})
        self.assertTrue(s['source_access_started']);self.assertEqual(s['active_holdout_state'],'CONSUMED_VALIDATION_EVIDENCE')
    def test_15_new_session(self):self.assertEqual(self.recover(session_mode='NEW_SESSION')['status'],'RECOVERABLE')
    def test_16_resumed_session(self):self.assertEqual(self.recover(session_mode='RESUMED_SESSION')['status'],'RECOVERABLE')
    def test_17_abandoned_staging(self):
        i=self.begin();p=self.path/'staging'/i['attempt_id']/'partial.tmp';exclusive(p,b'synthetic partial');self.recover();self.assertTrue(p.exists());self.assertTrue((self.path/'quarantine'/f'{i["attempt_id"]}.json').exists())
    def test_18_completed_replay(self):
        self.crash('receipt');self.recover();self.go('finish');self.assertEqual(self.recover()['status'],'RUN_COMPLETE');self.assertTrue(self.begin()['already_committed'])
    def test_19_journal_before_state(self):
        self.crash('journal');self.assertEqual(self.recover()['last_committed_milestone'],'unit1')
    def test_20_torn_tail(self):
        p=self.path/'RECOVERY_EVENTS.jsonl';old=p.read_bytes();p.write_bytes(old+b'{"torn":')
        self.recover();self.assertEqual(p.read_bytes(),old+b'{"torn":');self.assertTrue((self.path/'RECOVERY_EVENTS_0001.jsonl').exists());self.recover()
    def test_21_conflicting_branches(self):
        self.crash('receipt');p=next((self.path/'milestone_receipts').glob('*.json'));r=read(p);r['attempt_id']='competing';exclusive(p.with_name('competing.json'),canonical(r))
        with self.assertRaises(Blocked):self.recover()
    def test_22_altered_committed_output(self):
        self.crash('receipt');(self.path/'outputs/result.json').write_bytes(b'altered')
        with self.assertRaises(Blocked):self.recover()
    def test_23_pid_reuse(self):
        replace(self.path/'RUN_LOCK.json',{'status':'HELD','pid':os.getpid(),'process_start':'different-start'})
        self.recover();self.assertTrue(list((self.path/'lock_diagnostics').glob('*.json')))
    def test_24_concurrent_recovery(self):
        other=Engine(self.path)
        with self.e.lock():
            with self.assertRaises(Blocked):
                with other.lock():other.recover(PINS)
    def test_25_stale_semantic_review(self):
        with self.assertRaises(Blocked):self.go('source_access_synthetic',{'packet_sha256':'0'*64,'semantic_status':'SEMANTIC_CONTEXT_CLEAN'})
        self.assertFalse(self.e.state()['source_access_started'])
    def test_26_must_not_replay(self):
        self.begin('MUST_NOT_REPLAY')
        with self.assertRaises(Blocked):self.recover()
    def test_27_idempotency_conflict(self):
        self.crash('receipt');self.recover()
        with self.assertRaises(Blocked):self.go('begin','unit1',{'changed':True},['outputs/result.json'])
    def test_28_journal_interior_corruption(self):
        p=self.path/'RECOVERY_EVENTS.jsonl';p.write_bytes(p.read_bytes().replace(b'RUN_START',b'RUN_BROKE'))
        with self.assertRaises(Blocked):self.recover()
    def test_29_path_escape(self):
        with self.assertRaises(Blocked):self.go('begin','escape',{},['../escape.txt'])
    def test_30_usage_preempt(self):
        self.begin();self.go('preempt');self.assertEqual(self.e.state()['status'],'PREEMPTED_BY_USAGE_LIMIT');self.recover()
    def test_31_headroom(self):
        with self.assertRaises(Blocked):self.go('begin','unit',{},[],expensive=True,near_exhaustion=True)
    def test_32_binding_hash(self):
        p=self.path/'input.txt';exclusive(p,b'synthetic');s=self.e.state();s['bindings']=[{'path':str(p),'sha256':filehash(p)}];replace(self.path/'RECOVERY_STATE.json',s);p.write_bytes(b'changed')
        with self.assertRaises(Blocked):self.recover()
    def test_33_separate_sqlite_checks(self):
        p=self.path/'synthetic.db'
        with sqlite3.connect(p) as c:c.executescript('CREATE TABLE parent(id INTEGER PRIMARY KEY);CREATE TABLE child(id INTEGER REFERENCES parent(id));INSERT INTO child VALUES(7);')
        r=sqlite_check(p);self.assertEqual(r['integrity_check'],[('ok',)]);self.assertFalse(r['passed']);self.assertTrue(r['foreign_key_check'])
    def test_34_real_source_blocked(self):
        s=self.e.state();s['phase_id']='PHASE4BC-S';replace(self.path/'RECOVERY_STATE.json',s)
        with self.assertRaises(Blocked):self.go('source_access_synthetic',{'packet_sha256':PINS['current_packet_sha256'],'semantic_status':'SEMANTIC_CONTEXT_CLEAN'})
    def test_35_unknown_state(self):
        s=self.e.state();s['status']='MADE_UP';replace(self.path/'RECOVERY_STATE.json',s)
        with self.assertRaises(Blocked):self.e.state()
    def test_36_duplicate_json_keys(self):
        with self.assertRaises(Blocked):loads(b'{"a":1,"a":2}')
    def test_37_mutable_authority_drift(self):
        s=self.e.state();s['source_sha256']='0'*64;replace(self.path/'RECOVERY_STATE.json',s)
        with self.assertRaises(Blocked):self.go('recover',{**PINS,'source_sha256':'0'*64})
    def test_38_foreign_receipt(self):
        self.crash('receipt');p=next((self.path/'milestone_receipts').glob('*.json'));r=read(p);r['run_id']='other-run';p.write_bytes(canonical(r))
        with self.assertRaises(Blocked):self.recover()
    def test_39_failure_latches(self):
        self.drift('methodology_sha256')
        with self.assertRaises(Blocked):self.begin()
        with self.assertRaises(Blocked):self.go('finish')
        self.recover();self.begin()
    def test_40_output_ownership(self):
        self.crash('receipt');self.recover()
        with self.assertRaises(Blocked):self.go('begin','unit2',{},['outputs/result.json'])
        self.assertTrue((self.path/'outputs/result.json').is_file())
    def test_41_deleted_receipt(self):
        self.crash('journal');next((self.path/'milestone_receipts').glob('*.json')).unlink()
        with self.assertRaises(Blocked):self.recover()
    def test_42_active_intent_mutation(self):
        self.begin();p=self.path/'ACTIVE_OPERATION.json';i=read(p);i['expected_outputs']=['outputs/other.json'];p.write_bytes(canonical(i))
        with self.assertRaises(Blocked):self.go('commit',{'outputs/other.json':b'bad'})
    def test_43_unknown_output(self):
        exclusive(self.path/'surprise.json',b'{}')
        with self.assertRaises(Blocked):self.recover()
        self.assertTrue(list((self.path/'private_quarantine').glob('unregistered-*.json')))
    def test_44_windows_alias_ownership(self):
        self.crash('receipt');self.recover();original=(self.path/'outputs/result.json').read_bytes()
        for alias in ['OUTPUTS/result.json','outputs/./result.json','outputs\\result.json','outputs/result.json.','outputs/result.json:stream']:
            with self.assertRaises(Blocked):self.go('begin','unit2',{},[alias])
        self.assertEqual((self.path/'outputs/result.json').read_bytes(),original)
    def test_45_invalid_uncommitted_intent(self):
        self.begin();p=next((self.path/'intents').glob('*.json'));i=read(p);i['attempt_id']='../escape';p.write_bytes(canonical(i))
        with self.assertRaises(Blocked):self.recover()
        self.assertFalse((self.path/'escape').exists())
    def test_46_control_namespace(self):
        h=filehash(self.path/'INITIAL_STATE.json')
        for rel in ['INITIAL_STATE.json','RECOVERY_STATE.json','intents/fake.json','outputs/con.txt']:
            with self.assertRaises(Blocked):self.go('begin','bad',{},[rel])
        self.assertEqual(filehash(self.path/'INITIAL_STATE.json'),h);self.assertFalse((self.path/'intents').exists())

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(RecoveryTests)
    class Recorder(unittest.TextTestResult):
        def startTest(self,t):super().startTest(t);self.records=getattr(self,'records',[])
        def addSuccess(self,t):super().addSuccess(t);self.records.append({'id':t.id(),'status':'PASS'})
        def addFailure(self,t,e):super().addFailure(t,e);self.records.append({'id':t.id(),'status':'FAIL','error':self._exc_info_to_string(e,t)})
        def addError(self,t,e):super().addError(t,e);self.records.append({'id':t.id(),'status':'ERROR','error':self._exc_info_to_string(e,t)})
    r=unittest.TextTestRunner(verbosity=2,resultclass=Recorder).run(suite)
    report={'protocol':VERSION,'timestamp':now(),'tests':r.testsRun,'passed':r.testsRun-len(r.errors)-len(r.failures),'failed':len(r.errors)+len(r.failures),'skipped':len(r.skipped),'records':r.records,'fixture_root':'private_test_storage','synthetic_only':True}
    exclusive(ROOT/'test_results'/('recovery-'+uuid.uuid4().hex+'.json'),canonical(report))
    raise SystemExit(0 if r.wasSuccessful() else 1)
