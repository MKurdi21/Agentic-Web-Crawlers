import tempfile
import unittest
import csv
import json
from pathlib import Path
from unittest.mock import patch
import research_mode as rm


class ResearchTests(unittest.TestCase):
    def test_retired_holdouts_are_canonical_and_eligible(self):
        inv = rm.inventory()
        self.assertEqual(inv['canonical_count'], 112)
        self.assertEqual(inv['archived_duplicate_count'], 5)
        self.assertTrue(all(row['excluded_holdout'] is None for row in inv['papers']))

    def test_retired_excluded_progress_becomes_pending(self):
        row = {'summary_name': 'retired.md', 'excluded_holdout': None}
        with tempfile.TemporaryDirectory() as folder, patch.object(rm, 'OUT', Path(folder)), \
             patch.object(rm, 'inventory', return_value={'papers': [row], 'canonical_count': 1, 'archived_duplicate_count': 0}), \
             patch.object(rm, 'save_progress') as save, patch('sys.argv', ['research_mode.py', '--inventory']):
            (Path(folder) / 'progress.json').write_text(json.dumps({'papers': {'retired.md': {'status': 'excluded'}}}))
            rm.main()
            self.assertEqual(save.call_args.args[1]['papers']['retired.md']['status'], 'pending')

    def test_manifest_cannot_escape_output_directory(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / rm.CORPUS_SOURCE_ROOTS[0] / 'paper.pdf'
            source.parent.mkdir()
            source.write_bytes(b'fixture')
            (root / 'analysis').mkdir()
            (root / 'docs').mkdir()
            order = root / 'order.json'
            order.write_text(json.dumps({'order': []}), encoding='utf-8')
            with (root / 'analysis/manifest.csv').open('w', newline='', encoding='utf-8') as stream:
                writer = csv.DictWriter(stream, fieldnames=['Pdf', 'SummaryName'])
                writer.writeheader()
                writer.writerow({'Pdf': source.relative_to(root).as_posix(), 'SummaryName': '../../escape.md'})
            (root / 'docs/paper_inventory.csv').write_text('current_path,tags\n', encoding='utf-8')
            with patch.object(rm, 'ROOT', root), patch.object(rm, 'ORDER', order), \
                 patch.object(rm, 'discover_corpus_pdfs', return_value=([source], [])):
                with self.assertRaisesRegex(ValueError, 'summary filename'):
                    rm.inventory()

    def payload(self):
        row = {'summary_name': 'test.md', 'source_sha256': 'a' * 64}
        quote = 'Agents read untrusted content and can execute actions.'
        claims = [{'record_id': str(i), 'paper_report_id': 'test.md',
                   'claim_type': 'AUTHOR_CLAIM', 'statement': quote,
                   'locator': {'type': 'PAGE_RANGE', 'source_sha256': 'a' * 64, 'start': 1, 'end': 1},
                   'confidence': 'MEDIUM'} for i in range(8)]
        narrative = '# Stage 0\n' + '\n'.join(f'## {i}. {h}' for i, h in enumerate(rm.REQUIRED, 1))
        narrative += '\n# Completeness Audit\n' + 'Source-grounded discussion. ' * 800
        payload = {'summary': {'paper_report_id': 'test.md', 'source_sha256': 'a' * 64,
                   'schema_version': '2.0.0', 'narrative': narrative, 'claims': claims,
                   'coverage': {'reviewed_object_ids': [], 'unreviewed_object_ids': [], 'limitations': []}},
                   'research': {k: 'Test value' for k in ('title', 'research_question_relevance', 'attack_surface', 'method', 'limitations')},
                   'support': [{'claim_id': str(i), 'page': 1, 'quote': quote} for i in range(8)]}
        return row, payload, quote

    def test_grounding_rejects_invented_quotes_and_pages(self):
        row, payload, quote = self.payload()
        with tempfile.TemporaryDirectory() as folder:
            work = Path(folder)
            (work / 'article.txt').write_text('===== PAGE 1 OF 1 =====\n' + quote, encoding='utf-8')
            self.assertEqual(rm.quality(payload, row, work)['source_quote_checks'], 'passed')
            payload['support'][0]['quote'] = 'A fabricated statement without any source evidence.'
            with self.assertRaisesRegex(ValueError, 'quotation'):
                rm.quality(payload, row, work)
            payload['support'][0]['quote'] = quote
            payload['summary']['claims'][0]['locator']['end'] = 2
            with self.assertRaisesRegex(ValueError, 'locator'):
                rm.quality(payload, row, work)

    def test_short_exact_table_cells_are_valid_support(self):
        row, payload, quote = self.payload()
        with tempfile.TemporaryDirectory() as folder:
            work = Path(folder)
            (work / 'article.txt').write_text('===== PAGE 1 OF 1 =====\n' + quote + '\nAct 62.3 30.1', encoding='utf-8')
            payload['support'].append({'claim_id': '0', 'page': 1, 'quote': 'Act 62.3 30.1'})
            self.assertEqual(rm.quality(payload, row, work)['source_quote_checks'], 'passed')

    def test_quality_rejects_out_of_order_sections(self):
        row, payload, quote = self.payload()
        payload['summary']['narrative'] = payload['summary']['narrative'].replace('## 7.', '## TEMP.').replace('## 8.', '## 7.').replace('## TEMP.', '## 8.')
        with tempfile.TemporaryDirectory() as folder:
            work = Path(folder)
            (work / 'article.txt').write_text('===== PAGE 1 OF 1 =====\n' + quote, encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'structure'):
                rm.quality(payload, row, work)

    def test_failed_paper_does_not_block_next(self):
        rows = [{'summary_name': x + '.md', 'excluded_holdout': None, 'source_sha256': 'a'} for x in ('bad', 'good')]
        with tempfile.TemporaryDirectory() as folder, patch.object(rm, 'OUT', Path(folder)), \
             patch.object(rm, 'inventory', return_value={'papers': rows}), \
             patch.object(rm, 'save_progress'), \
             patch.object(rm, 'process', side_effect=[ValueError('bad paper'), {'status': 'completed'}]) as proc, \
             patch('sys.argv', ['research_mode.py']):
            rm.main()
            self.assertEqual(proc.call_count, 2)

    def test_global_usage_limit_stops_dispatch(self):
        rows = [{'summary_name': x + '.md', 'excluded_holdout': None, 'source_sha256': 'a'} for x in ('first', 'next')]
        with tempfile.TemporaryDirectory() as folder, patch.object(rm, 'OUT', Path(folder)), \
             patch.object(rm, 'inventory', return_value={'papers': rows}), \
             patch.object(rm, 'save_progress'), \
             patch.object(rm, 'process', side_effect=RuntimeError('OPERATIONAL_USAGE_LIMIT: provider limit')) as proc, \
             patch('sys.argv', ['research_mode.py']):
            rm.main()
            self.assertEqual(proc.call_count, 1)

    def test_utf8_source_reads(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / 'article.txt'
            p.write_text('Research “agent” → action', encoding='utf-8')
            self.assertEqual(rm.read(p), 'Research “agent” → action')

    def test_containment_rejects_operational_and_escape(self):
        for p in ['analysis/fixture.pdf', '../outside.pdf']:
            with self.assertRaises(ValueError):
                rm.contained(p)

    def test_holdout_rejected_before_source_access(self):
        row = {'pdf': '08_Defenses_Guards_Containment/test.pdf', 'excluded_holdout': 'B02'}
        with patch.object(rm, 'digest', side_effect=AssertionError('source accessed')):
            with self.assertRaisesRegex(ValueError, 'holdout'):
                rm.process(row)

    def test_changed_completed_outputs_resume(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(rm, 'OUT', Path(folder)):
            row = {'summary_name': 'a.md', 'source_sha256': 'abc'}
            state = {'status': 'completed', 'source_sha256': 'abc',
                     'summary_sha256': 'missing', 'record_sha256': 'missing'}
            self.assertFalse(rm.completed_valid(row, state))


if __name__ == '__main__':
    unittest.main()
