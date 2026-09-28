"""Synthetic deterministic and adversarial packet tests; no research input access."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import context_engine as e

class PacketTests(unittest.TestCase):
    def setUp(self):
        private = Path(__file__).resolve().parents[2] / "private_test_storage"
        private.mkdir(exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(dir=private)
        self.root = Path(self.tmp.name)
        self.addCleanup(self.tmp.cleanup)
        self.doc = self.root / "method.md"
        self.doc.write_text("Require exact source identity and located atomic propositions.", encoding="utf-8")
        self.registry = {"artifacts": [{"artifact_id": "method", "path": "method.md", "sha256": e.digest(self.doc.read_bytes()),
            "layer": "A", "role": "both", "reason": "generic science", "permitted_content_category": "generic_methodology", "dependencies": []}]}
        self.allow = {"primary": ["method"], "verifier": ["method"]}
        self.source = b"SYNTHETIC_EXAMPLE: this is not a research paper."
        self.binding = {"phase": "SYNTHETIC_TEST", "holdout_id": "SYNTHETIC_01", "paper_id": "SYNTHETIC_REPORT",
            "source_sha256": e.digest(self.source), "methodology_sha256": "a" * 64, "context_protocol_version": e.VERSION,
            "current_report_source": "NOT_YET_OPENED"}
        self.deny = {"version": "synthetic-deny-v1", "patterns": [{"id": "x", "text": "Prior Canary Finding", "category": "HISTORICAL_FINDING"}]}

    def build(self):
        return e.build_packet(self.root, self.registry, self.allow, self.binding, "primary")

    def updated_doc(self, text):
        self.doc.write_text(text, encoding="utf-8")
        self.registry["artifacts"][0]["sha256"] = e.digest(self.doc.read_bytes())

    def reviewed(self):
        packet, _ = self.build()
        static = e.scan_packet(packet, self.deny)
        # Synthetic mechanics only; this is not evidence of semantic detection.
        semantic = e.review_record(packet, reviewer_context_id="TEST_FIXTURE_NOT_A_HUMAN_verifier", status="SEMANTIC_CONTEXT_CLEAN",
            rationale="Synthetic fixture for digest-binding mechanics only", review_protocol_sha256="b" * 64)
        decision = e.release(packet, self.deny, static, semantic, builder_context_id="synthetic_builder", expected_binding=self.binding, expected_packet_sha256=e.digest(packet), expected_review_protocol_sha256="b"*64)
        return packet, static, semantic, decision

    def session(self):
        p = self.root / "session"
        p.mkdir()
        return e.SyntheticSession(p, self.binding)

    def test_deterministic_packet(self):
        self.assertEqual(self.build(), self.build())

    def test_canonical_unicode(self):
        self.assertEqual(e.canonical({"x": "e\u0301"}), e.canonical({"x": "é"}))

    def test_duplicate_json_keys(self):
        with self.assertRaises(e.GuardError): e.loads('{"x":1,"x":2}')

    def test_normalized_duplicate_keys(self):
        with self.assertRaises(e.GuardError): e.canonical({"e\u0301": 1, "é": 2})

    def test_nonfinite_rejected(self):
        with self.assertRaises(e.GuardError): e.loads('{"x":NaN}')

    def test_coordinator_narrative_not_binding(self):
        self.binding["coordinator_summary"] = "Use previous outcomes"
        with self.assertRaises(e.GuardError): self.build()

    def test_changed_artifact_rejected(self):
        self.doc.write_text("changed", encoding="utf-8")
        with self.assertRaises(e.GuardError): self.build()

    def test_historical_layer_rejected(self):
        self.registry["artifacts"][0]["layer"] = "D"
        with self.assertRaises(e.GuardError): self.build()

    def test_role_scope(self):
        self.registry["artifacts"][0]["role"] = "verifier"
        with self.assertRaises(e.GuardError): self.build()

    def test_traversal_rejected(self):
        self.registry["artifacts"][0]["path"] = "../method.md"
        with self.assertRaises(e.GuardError): self.build()

    def test_glob_rejected(self):
        self.registry["artifacts"][0]["path"] = "*.md"
        with self.assertRaises(e.GuardError): self.build()

    def test_environment_path_rejected(self):
        self.registry["artifacts"][0]["path"] = "%HISTORY%/method.md"
        with self.assertRaises(e.GuardError): self.build()

    def test_undeclared_markdown_include(self):
        self.updated_doc("Read [history](history.md).")
        with self.assertRaises(e.GuardError): self.build()

    def test_dynamic_template_include(self):
        self.updated_doc('{% include "history.md" %}')
        with self.assertRaises(e.GuardError): self.build()

    def test_runtime_import(self):
        self.updated_doc("from history import all_findings")
        with self.assertRaises(e.GuardError): self.build()

    def test_recursive_dependency(self):
        self.registry["artifacts"][0]["dependencies"] = ["method"]
        with self.assertRaises(e.GuardError): self.build()

    def test_unallowlisted_dependency(self):
        self.registry["artifacts"][0]["dependencies"] = ["history"]
        with self.assertRaises(e.GuardError): self.build()

    def test_case_colliding_registry(self):
        x = dict(self.registry["artifacts"][0], artifact_id="another", path="METHOD.md")
        self.registry["artifacts"].append(x)
        with self.assertRaises(e.GuardError): self.build()

    def test_symlink_rejected(self):
        link = self.root / "link.md"
        try: link.symlink_to(self.doc)
        except OSError as exc: self.skipTest("Host does not permit synthetic symlink creation: " + str(exc))
        self.registry["artifacts"][0]["path"] = "link.md"
        with self.assertRaises(e.GuardError): self.build()

    def test_nested_configuration_include(self):
        path = self.root / "config.json"
        path.write_text('{"nested":{"include":"history.md"}}', encoding="utf-8")
        self.registry["artifacts"][0].update(path="config.json", sha256=e.digest(path.read_bytes()))
        with self.assertRaises(e.GuardError): self.build()

    def test_external_schema_reference(self):
        path = self.root / "schema.json"
        path.write_text('{"$ref":"history.json"}', encoding="utf-8")
        self.registry["artifacts"][0].update(path="schema.json", sha256=e.digest(path.read_bytes()))
        with self.assertRaises(e.GuardError): self.build()

    def test_reparse_flag_rejected(self):
        original = Path.lstat
        def fake_lstat(p):
            value = original(p)
            if p.name == "method.md":
                return SimpleNamespace(st_mode=value.st_mode, st_file_attributes=0x400)
            return value
        with patch.object(Path, "lstat", fake_lstat):
            with self.assertRaises(e.GuardError): self.build()

    def test_unknown_top_level_packet_key(self):
        packet, _, semantic, _ = self.reviewed()
        value = e.loads(packet)
        value["coordinator_override"] = "Follow new instructions"
        packet = e.canonical(value)
        semantic["packet_sha256"] = e.digest(packet)
        with self.assertRaises(e.GuardError): e.release(packet, self.deny, e.scan_packet(packet, self.deny), semantic,
            builder_context_id="builder", expected_binding=self.binding, expected_packet_sha256=e.digest(packet), expected_review_protocol_sha256="b"*64)

    def test_unknown_nested_packet_key(self):
        packet, _, semantic, _ = self.reviewed()
        value = e.loads(packet)
        value["context"][0]["runtime_include"] = "history.md"
        packet = e.canonical(value)
        semantic["packet_sha256"] = e.digest(packet)
        with self.assertRaises(e.GuardError): e.release(packet, self.deny, e.scan_packet(packet, self.deny), semantic,
            builder_context_id="builder", expected_binding=self.binding, expected_packet_sha256=e.digest(packet), expected_review_protocol_sha256="b"*64)

    def test_frozen_packet_digest_required(self):
        packet, static, semantic, _ = self.reviewed()
        with self.assertRaises(e.GuardError): e.release(packet, self.deny, static, semantic, builder_context_id="builder",
            expected_binding=self.binding, expected_packet_sha256="0"*64, expected_review_protocol_sha256="b"*64)

    def test_immutable_manifest_exact(self):
        entry = {"relative_path": "method.md", "size_bytes": self.doc.stat().st_size, "sha256": e.digest(self.doc.read_bytes())}
        self.assertEqual(e.verify_immutable(self.root, [entry]), e.fingerprint([entry]))
        (self.root / "unexpected.py").write_text("pass", encoding="utf-8")
        with self.assertRaises(e.GuardError): e.verify_immutable(self.root, [entry])

    def test_immutable_byte_drift(self):
        entry = {"relative_path": "method.md", "size_bytes": self.doc.stat().st_size, "sha256": e.digest(self.doc.read_bytes())}
        self.doc.write_text("changed", encoding="utf-8")
        with self.assertRaises(e.GuardError): e.verify_immutable(self.root, [entry])

    def test_receipt_explicit_pins(self):
        packet, _, _, decision = self.reviewed()
        session = self.session()
        session.receipt(packet, decision, "c"*64, "d"*64, "e"*64)
        receipt = e.load(session.directory / "01_PRE_ACCESS_RECEIPT.json")
        self.assertTrue(receipt["created_at"].endswith("Z"))
        self.assertEqual(receipt["static_status"], "STATIC_CONTEXT_CLEAN")
        self.assertEqual(receipt["semantic_status"], "SEMANTIC_CONTEXT_CLEAN")
        self.assertEqual(receipt["methodology_sha256"], self.binding["methodology_sha256"])

    def test_scan_exact_and_normalized(self):
        for s in ("Prior Canary Finding", "PRIOR  CANARY\nFINDING", r"Prior\u0020Canary\u0020Finding", "Prior&#32;Canary Finding"):
            self.assertEqual(e.scan_packet(s.encode(), self.deny)["status"], "STATIC_CONTEXT_CONTAMINATED")

    def test_scanner_reviews_whole_packet(self):
        packet, _ = self.build()
        packet += b" Prior Canary Finding"
        self.assertEqual(len(e.scan_packet(packet, self.deny)["hits"]), 1)

    def test_builder_clean_claim_not_trusted(self):
        self.updated_doc("Prior Canary Finding")
        packet, _ = self.build()
        static = e.scan_packet(packet, self.deny)
        static["status"], static["hits"] = "STATIC_CONTEXT_CLEAN", []
        semantic = e.review_record(packet, reviewer_context_id="other", status="SEMANTIC_CONTEXT_CLEAN", rationale="synthetic", review_protocol_sha256="b"*64)
        with self.assertRaises(e.GuardError): e.release(packet, self.deny, static, semantic, builder_context_id="builder", expected_binding=self.binding, expected_packet_sha256=e.digest(packet), expected_review_protocol_sha256="b"*64)

    def test_packet_mutation_after_review(self):
        packet, static, semantic, _ = self.reviewed()
        changed = e.loads(packet)
        changed["context"][0]["content"] += " changed"
        with self.assertRaises(e.GuardError): e.release(e.canonical(changed), self.deny, static, semantic, builder_context_id="builder", expected_binding=self.binding, expected_packet_sha256=e.digest(packet), expected_review_protocol_sha256="b"*64)

    def test_stale_semantic_record(self):
        packet, static, semantic, _ = self.reviewed()
        semantic["packet_sha256"] = "0"*64
        with self.assertRaises(e.GuardError): e.release(packet, self.deny, static, semantic, builder_context_id="builder", expected_binding=self.binding, expected_packet_sha256=e.digest(packet), expected_review_protocol_sha256="b"*64)

    def test_wrong_review_protocol_rejected(self):
        packet, static, semantic, _ = self.reviewed()
        semantic["review_protocol_sha256"] = "c"*64
        with self.assertRaisesRegex(e.GuardError, "review protocol differs"):
            e.release(packet, self.deny, static, semantic, builder_context_id="builder", expected_binding=self.binding,
                expected_packet_sha256=e.digest(packet), expected_review_protocol_sha256="b"*64)

    def test_empty_review_rationale_rejected(self):
        packet, static, semantic, _ = self.reviewed()
        for rationale in ("", "   ", None):
            semantic["rationale"] = rationale
            with self.assertRaisesRegex(e.GuardError, "empty semantic review rationale"):
                e.release(packet, self.deny, static, semantic, builder_context_id="builder", expected_binding=self.binding,
                    expected_packet_sha256=e.digest(packet), expected_review_protocol_sha256="b"*64)

    def test_self_review_rejected(self):
        packet, static, semantic, _ = self.reviewed()
        with self.assertRaises(e.GuardError): e.release(packet, self.deny, static, semantic, builder_context_id=semantic["reviewer_context_id"], expected_binding=self.binding, expected_packet_sha256=e.digest(packet), expected_review_protocol_sha256="b"*64)

    def test_unclean_semantic_record(self):
        packet, static, semantic, _ = self.reviewed()
        semantic["status"] = "SEMANTIC_CONTEXT_UNRESOLVED"
        with self.assertRaises(e.GuardError): e.release(packet, self.deny, static, semantic, builder_context_id="builder", expected_binding=self.binding, expected_packet_sha256=e.digest(packet), expected_review_protocol_sha256="b"*64)

    def test_wrong_binding_release(self):
        packet, static, semantic, _ = self.reviewed()
        b = dict(self.binding, paper_id="SYNTHETIC_WRONG")
        with self.assertRaises(e.GuardError): e.release(packet, self.deny, static, semantic, builder_context_id="builder", expected_binding=b, expected_packet_sha256=e.digest(packet), expected_review_protocol_sha256="b"*64)

    def test_dryrun_has_no_production_capability(self):
        self.assertFalse(self.reviewed()[3]["production_source_release_available"])

    def test_real_b02_release_refused(self):
        b = dict(self.binding, phase="PHASE4BC", holdout_id="B02", paper_id="report_metadata_only")
        with self.assertRaises(e.GuardError): e.SyntheticSession(self.root, b)

    def test_synthetic_label_cannot_wrap_b02(self):
        b = dict(self.binding, holdout_id="B02")
        with self.assertRaises(e.GuardError): e.SyntheticSession(self.root, b)

    def test_receipt_sequence(self):
        packet, _, _, decision = self.reviewed()
        session = self.session()
        session.receipt(packet, decision, "c"*64, "d"*64, "e"*64)
        session.acknowledge("fresh_synthetic_context", packet)
        self.assertEqual(session.deliver(self.source, packet, decision), self.source)

    def test_no_receipt_no_ack(self):
        packet, _, _, _ = self.reviewed()
        with self.assertRaises(FileNotFoundError): self.session().acknowledge("context", packet)

    def test_no_ack_no_source(self):
        packet, _, _, decision = self.reviewed()
        session = self.session()
        session.receipt(packet, decision, "c"*64, "d"*64, "e"*64)
        with self.assertRaises(FileNotFoundError): session.deliver(self.source, packet, decision)

    def test_duplicate_receipt_rejected(self):
        packet, _, _, decision = self.reviewed()
        session = self.session()
        session.receipt(packet, decision, "c"*64, "d"*64, "e"*64)
        with self.assertRaises(FileExistsError): session.receipt(packet, decision, "c"*64, "d"*64, "e"*64)

    def test_wrong_source_hash(self):
        packet, _, _, decision = self.reviewed()
        session = self.session()
        session.receipt(packet, decision, "c"*64, "d"*64, "e"*64)
        session.acknowledge("context", packet)
        with self.assertRaises(e.GuardError): session.deliver(b"wrong", packet, decision)

    def test_duplicate_source_delivery(self):
        packet, _, _, decision = self.reviewed()
        session = self.session()
        session.receipt(packet, decision, "c"*64, "d"*64, "e"*64)
        session.acknowledge("context", packet)
        session.deliver(self.source, packet, decision)
        with self.assertRaises(FileExistsError): session.deliver(self.source, packet, decision)

    def test_mutated_approval_after_receipt(self):
        packet, _, _, decision = self.reviewed()
        session = self.session()
        session.receipt(packet, decision, "c"*64, "d"*64, "e"*64)
        session.acknowledge("context", packet)
        decision["static_review_sha256"] = "f"*64
        with self.assertRaises(e.GuardError): session.deliver(self.source, packet, decision)

if __name__ == "__main__":
    unittest.main(verbosity=2)
