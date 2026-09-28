import tempfile,unittest
from pathlib import Path
from validation_guard import manifest,verify_manifest,verify_packet
class GuardTests(unittest.TestCase):
    def test_mutable_runtime_excluded(self):
        parent=Path(__file__).resolve().parents[2]/'test_runtime';parent.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=parent) as d:
            p=Path(d);(p/'code.py').write_text('synthetic');m=manifest(p);(p/'shadow').mkdir();(p/'shadow/state.db').write_bytes(b'synthetic');self.assertTrue(verify_manifest(p,m))
    def test_new_code_and_changed_bytes_rejected(self):
        parent=Path(__file__).resolve().parents[2]/'test_runtime';parent.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=parent) as d:
            p=Path(d);(p/'code.py').write_text('synthetic');m=manifest(p);(p/'code.py').write_text('changed')
            with self.assertRaisesRegex(ValueError,'METHODOLOGY_DRIFT'):verify_manifest(p,m)
    def test_fresh_packet(self):
        p={'report_id':'T1','frozen_protocol_hash':'a'*64,'fork_history':'none','previous_holdout_scientific_content_included':False,'coordinator_summary_included':False,'input_hashes':['b'*64]}
        self.assertTrue(verify_packet(p,current_report='T1',frozen_protocol_hash='a'*64,allowed_input_hashes=['b'*64]))
    def test_history_is_contamination(self):
        p={'report_id':'T1','frozen_protocol_hash':'a'*64,'fork_history':'all','previous_holdout_scientific_content_included':True,'coordinator_summary_included':False,'input_hashes':[]}
        with self.assertRaisesRegex(ValueError,'VALIDATION_CONTEXT_CONTAMINATION'):verify_packet(p,current_report='T1',frozen_protocol_hash='a'*64,allowed_input_hashes=[])
