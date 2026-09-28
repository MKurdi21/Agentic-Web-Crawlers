"""Assemble Phase 4BE-C Stage A evidence and acceptance inputs, without installing candidates."""
import csv
import hashlib
import json
from datetime import datetime,timezone
from pathlib import Path

here=Path(__file__).resolve().parent
root=here.parents[1]
state=root/'analysis'
def read(path): return json.loads(path.read_text(encoding='utf-8-sig'))
def write(name,obj):
    content = obj if name.endswith('.md') else json.dumps(obj,indent=2,ensure_ascii=False,sort_keys=True)+'\n'
    (here/name).write_text(content,encoding='utf-8')
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1048576),b''): h.update(block)
    return h.hexdigest()
old=read(state/'checkpoint.json')
new=read(here/'candidate'/'checkpoint.json')
diag=read(state/'phase4be_freeze_repair_and_validation'/'RECOVERY_LATEST_USAGE_BLOCKED_DIAGNOSTIC.json')
snap=read(here/'DRIFTED_CHECKPOINT_FORENSIC_SNAPSHOT.json')
repro=read(here/'CURRENT_GENERATOR_REPRODUCTION.json')
account=read(here/'CORPUS_ACCOUNTING_RECONCILIATION.json')
audit=read(here/'B02_B08_ACCESS_AUDIT.json')
tests=read(here/'SCANNER_REGRESSION_TEST_RESULTS.json')
policy=read(here/'CORPUS_BOUNDARY_POLICY.json')
baseline=read(state/'phase4be_freeze_repair_and_validation'/'PROTECTED_BASELINE_EXTENDED.json')
baseline_index={x['path']:x for x in baseline['files']}
assert sha(state/'CHECKPOINT.md')==snap['files'][0]['sha256']
assert sha(state/'checkpoint.json')==snap['files'][1]['sha256']
assert all(x['sha256']==x['copied_sha256'] for x in snap['files'])
assert tests['verdict']=='PASS'
assert repro['semantic_json_equal_ignoring_issue_order']
assert account['canonical_minus_tracked_equals_unmapped']
assert account['total_equals_canonical_plus_duplicates']
assert account['all_tracked_sources_exist_and_match']
assert all(x=='UNTOUCHED_CONFIRMED' for x in audit['states'].values())
phase_tree=state/'phase4be_freeze_repair_and_validation'/'NEVER_PACKAGE'
old_issue_paths={x.removeprefix('Unmapped PDF: ') for x in old['issues'] if x.startswith('Unmapped PDF: ')}
added=[]
for p in phase_tree.rglob('*.pdf'):
    rel=p.relative_to(root).as_posix()
    if rel not in old_issue_paths:
        added.append(dict(path=rel,sha256=sha(p),size=p.stat().st_size,
                          mtime_utc=datetime.fromtimestamp(p.stat().st_mtime,timezone.utc).isoformat(),
                          under_NEVER_PACKAGE=True,corpus_source=False))
added.sort(key=lambda x:x['path'])
write('POST_CHECKPOINT_PDF_DELTA.json',dict(checkpoint_updated_at=old['updated_at'],
     added_operational_pdfs=added,count=len(added),
     note='Six copies after saved checkpoint explain present tree count 163 versus checkpoint 157; physical paths were checked, with source content unopened.'))
script=root/'scripts'/'summary_state.py'
old_script_hash='30eab772c1914c3f03538d10a27e224580a2dbf821e8d8cdc041b7a5693896c2'
old_script_size=9614
new_script_hash=sha(script)
write('CHECKPOINT_SCANNER_CHANGE_RECEIPT.json',dict(path='scripts/summary_state.py',
     old_sha256=old_script_hash,old_size=old_script_size,new_sha256=new_script_hash,new_size=script.stat().st_size,
     reason='Project-root recursive PDF discovery admitted Phase 4/4BE operational and private copies as canonical corpus.',
     diff_summary=['Added twelve manifest-derived positive corpus source roots and a separate 99_Duplicates root.',
                   'Discovery now visits only those roots and fails closed if a manifest source is outside them.',
                   'Scientific status, source review, promotion and checkpoint rendering logic unchanged.'],
     test_results='SCANNER_REGRESSION_TEST_RESULTS.json',test_verdict=tests['verdict']))
write('AUTHORIZED_EXTERNAL_CHANGESET.json',dict(changes=[dict(path='scripts/summary_state.py',old_sha256=old_script_hash,
     new_sha256=new_script_hash,reason='Authorized Phase4BE-C scanner scope repair',
     phase4be_c_receipt='CHECKPOINT_SCANNER_CHANGE_RECEIPT.json',tests=['SCANNER_REGRESSION_TEST_RESULTS.json'])],
     limitation='Live checkpoint replacements are conditional on Stage A acceptance and will be recorded separately.'))
before_issues=set(old['issues']); after_issues=set(new['issues'])
comparison=dict(original_phase4be_baseline_checkpoint_hashes={x['path']:x['baseline_sha256'] for x in diag['protected_drift']},
    drifted_checkpoint_hashes={x['path']:x['current_sha256'] for x in diag['protected_drift']},
    candidate_checkpoint_hashes={p:sha(here/'candidate'/Path(p).name) for p in ('analysis/CHECKPOINT.md','analysis/checkpoint.json')},
    scientific_paper_records_equal=old['papers']==new['papers'],status_counts_equal=old['counts']==new['counts'],
    duplicate_records_equal=old['duplicates']==new['duplicates'],prompt_hash_equal=old['prompt_sha256']==new['prompt_sha256'],
    canonical_before=old['canonical_pdf_count'],canonical_after=new['canonical_pdf_count'],
    total_before=old['total_pdf_count'],total_after=new['total_pdf_count'],
    removed_issues=sorted(before_issues-after_issues),added_issues=sorted(after_issues-before_issues),
    semantic_difference_classes={'canonical_and_total_count':'EXPECTED_SCANNER_SCOPE_CORRECTION',
       'forty_unmapped_issues':'EXPECTED_SCANNER_SCOPE_CORRECTION','updated_at':'TIMESTAMP_ONLY',
       'paper_records':'UNCHANGED','scientific_status':'UNCHANGED','duplicate_mapping':'UNCHANGED'},
    unresolved_scientific_difference=False,
    historical_baseline_note='The baseline preserved hashes and sizes, not a known full checkpoint byte copy; scientific state is compared to the exact drifted files and durable Phase4BE live-status receipts.')
write('CHECKPOINT_CANDIDATE_COMPARISON.json',comparison)
write('CORPUS_BOUNDARY_POLICY.md',f"""# Corpus source boundary

The manifest names 112 registered sources in exactly twelve numbered top-level research directories. Direct counts in those directories equal the manifest counts, and every registered source SHA-256 still matches the checkpoint. Those twelve paths are the only canonical discovery roots. `99_Duplicates` is counted separately as archived extra copies and all five hashes match registered sources.

The explicit roots are recorded in `CORPUS_BOUNDARY_POLICY.json`. `98_Manual_Review` does not contain a registered source and is not an approved root. A future corpus expansion must update the reviewed source policy and manifest deliberately. Ordinary execution of `python scripts/summary_state.py` now uses this boundary. PDFs under `analysis/`, `docs/`, `scripts/`, drafts, summaries, rehearsal, test, and source-delivery trees have no corpus authority from their extension.

The repair changes discovery and count scope only. It preserves all 112 paper records, their status, five duplicate mappings, source review criteria, and promotion criteria.
""")
write('CHECKPOINT_GENERATOR_ANALYSIS.md',f"""# Checkpoint generator analysis

Before repair, `scripts/summary_state.py` used `ROOT.rglob('*.pdf')` from the project root, then treated every path except one containing `99_Duplicates` as canonical. It added an `Unmapped PDF` issue for every canonical path outside `manifest.csv`. Thus operational PDFs under `analysis/` inflated the canonical count. The old generator wrote `analysis/checkpoint.json` and `analysis/CHECKPOINT.md` in one invocation, each through its own temporary file and atomic rename; the pair was not a single atomic transaction. The shared `now` value appears in both outputs. It would create `analysis/baseline.json` only if absent; that file already exists.

The 2026-09-28T00:14:51.262910+00:00 drifted timestamp is the generator's shared update value. The saved checkpoint enumerated 157 paths; isolated replay against those exact paths reproduces 152 canonical, five duplicate extra copies, 40 unmapped issues, all 112 paper records, and the full normalized JSON semantics. Issue order depends on set iteration. Six later operational PDFs are now present, so a present-time old-generator run would report 158 canonical and 163 total. The observed timestamps and hashes do not identify the OS process that ran the generator.

After repair, discovery traverses twelve approved roots and `99_Duplicates` separately. The manifest must stay within approved roots. Status calculation, review validity, duplicate hash checks, and Markdown rendering are unchanged.
""")
write('WRITER_ATTRIBUTION_REPORT.md',f"""# Writer attribution

Verdict: `WRITER_IDENTITY_UNKNOWN_CAUSAL_GENERATOR_REPRODUCED`.

The exact drifted checkpoint is consistent with one invocation of the original `summary_state.py`: its timestamp and output structure match, and a redirected replay over the checkpoint-era 157 paths reproduces the normalized JSON, paper records, duplicates, issue set, and counts. The two file mtimes are near each other, and both files carry the same logical update timestamp. No command log or OS process record establishes who invoked it. The `RECOVERY_LATEST_USAGE_BLOCKED_DIAGNOSTIC.json` explicitly records origin unknown and no authorized Phase4BE commit. This conclusion attributes the causal generator, not a human or process identity.
""")
write('EXECUTIVE_PHASE4BE_C.md',f"""# Phase 4BE-C checkpoint reconciliation

The checkpoint inflation has a reproducible scanner cause. The drifted files are preserved exactly under `forensic/`. Their 152 canonical and 157 total PDF counts include 112 manifest sources, five archived duplicate copies, and 40 operational PDFs. The 40 issues are 31 Phase4BE `NEVER_PACKAGE` source-delivery/test copies and nine older private rehearsal/validation copies. Six more operational copies appeared after the checkpoint timestamp. No legitimate corpus addition or removal was observed; all 112 registered source hashes match and the twelve approved corpus roots contain exactly those 112 PDFs.

The repaired generator produces an isolated 112 canonical / 117 total candidate with 37 structural passes, 75 pending, zero source verified, zero promoted, unchanged paper and duplicate records, and no issues. Synthetic and real-root regression checks pass. B02–B08 have no durable source-access transition; one older private B02 file matches frozen B02 bytes but is not a Phase4BE scientific delivery. Exact invoking writer remains unknown.

Live checkpoint replacement is pending Stage A independent review and final acceptance. Phase4BE recovery and B02 scientific access have not begun.
""")
print(json.dumps(dict(six_post_checkpoint=len(added),script_hash=new_script_hash,candidate=comparison['candidate_checkpoint_hashes'],all_tests_pass=tests['verdict']=='PASS')))
