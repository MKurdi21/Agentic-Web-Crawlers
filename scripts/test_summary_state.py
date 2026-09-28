"""Focused tests for the checkpoint's limited structural validation contract."""

import tempfile
import unittest
from pathlib import Path

from summary_state import REQUIRED, check_structure, digest, resolve


class StructureTests(unittest.TestCase):
    def check_text(self, text):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "draft.md"
            path.write_text(text, encoding="utf-8")
            return check_structure(path)

    def draft(self):
        return "# Stage 0\n" + "\n".join(
            f"## {i}. {name}\n" + "Evidence placeholder. " * 60
            for i, name in enumerate(REQUIRED, 1)
        ) + "\n# Completeness Audit\n"

    def test_complete_shape_is_only_structural_pass(self):
        self.assertTrue(self.check_text(self.draft())["passed"])

    def test_body_mentions_do_not_replace_heading(self):
        result = self.check_text(self.draft().replace("## 7. Methodology", "7. Methodology"))
        self.assertFalse(result["passed"])
        self.assertIn("7. Methodology", result["missing"])

    def test_order_and_shortness_fail(self):
        text = self.draft().replace("## 7. Methodology", "## TEMP", 1)
        text = text.replace("## 8. Experiments / Analyses", "## 7. Methodology", 1)
        text = text.replace("## TEMP", "## 8. Experiments / Analyses", 1)
        result = self.check_text(text)
        self.assertEqual(result["missing"], [])
        self.assertFalse(result["numbered_sections_in_order"])
        self.assertFalse(result["passed"])
        self.assertFalse(self.check_text("# Stage 0\n# Completeness Audit")["passed"])

    def test_missing_source_and_path_escape(self):
        self.assertIsNone(digest(Path("__nonexistent_source_for_test__.pdf")))
        with self.assertRaises(ValueError):
            resolve("../../outside-repo")


if __name__ == "__main__":
    unittest.main()
