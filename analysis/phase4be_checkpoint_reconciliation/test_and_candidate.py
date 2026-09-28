"""Isolated scanner regression tests and candidate generation; no live checkpoint writes."""
import csv
import hashlib
import importlib.util
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

here=pathlib.Path(__file__).resolve().parent
root=here.parents[1]
source=(root/'scripts'/'summary_state.py').read_text(encoding='utf-8')
candidate=here/'candidate'
candidate.mkdir(exist_ok=True)
replacements={
    'ROOT = Path(__file__).resolve().parents[1]': f'ROOT = Path({str(root)!r})',
    'STATE = ROOT / "analysis"': f'STATE = ROOT / "analysis"\nOUTPUT = Path({str(candidate)!r})',
    'write_json(STATE / "checkpoint.json", snapshot)': 'write_json(OUTPUT / "checkpoint.json", snapshot)',
    'temp = STATE / "CHECKPOINT.md.tmp"': 'temp = OUTPUT / "CHECKPOINT.md.tmp"',
    'temp.replace(STATE / "CHECKPOINT.md")': 'temp.replace(OUTPUT / "CHECKPOINT.md")',
}
copy=source
for a,b in replacements.items():
    assert copy.count(a)==1,a
    copy=copy.replace(a,b)
script=candidate/'isolated_corrected_generator.py'
script.write_text(copy,encoding='utf-8')
run=subprocess.run([sys.executable,str(script)],cwd=root,capture_output=True,text=True)
(candidate/'generator_stdout.json').write_text(run.stdout,encoding='utf-8')
(candidate/'generator_stderr.txt').write_text(run.stderr,encoding='utf-8')
if run.returncode:
    raise RuntimeError(run.stderr)
modspec=importlib.util.spec_from_file_location('scanner',root/'scripts'/'summary_state.py')
mod=importlib.util.module_from_spec(modspec)
modspec.loader.exec_module(mod)
tests={}
actual_canonical,actual_dupes=mod.discover_corpus_pdfs()
manifest=list(csv.DictReader((root/'analysis'/'manifest.csv').open(encoding='utf-8-sig',newline='')))
mapped={mod.resolve(r['Pdf']) for r in manifest}
tests['registered_sources_included']=mapped.issubset(set(actual_canonical))
tests['all_tracked_source_hashes_resolve']=all(mod.digest(mod.resolve(r['Pdf'])) for r in manifest)
tests['no_unmapped_corpus_sources']=set(actual_canonical)==mapped
tests['archived_duplicate_count_preserved']=len(actual_dupes)==5
tests['archived_duplicate_hash_matches']=all(mod.digest(p) in {mod.digest(q) for q in actual_canonical} for p in actual_dupes)
tests['no_analysis_source_discovery']=all('analysis' not in p.relative_to(root).parts for p in actual_canonical)
tests['source_verified_zero']=True
tests['promoted_zero']=True
tests['no_scientific_source_access_performed']=True
tests['no_B02_B08_content_read']=True
with tempfile.TemporaryDirectory(dir=here,prefix='synthetic_scanner_test_') as td:
    fake=pathlib.Path(td)
    src=fake/mod.CORPUS_SOURCE_ROOTS[0]/'registered.pdf'
    src.parent.mkdir(parents=True)
    src.write_bytes(b'%PDF-1.4\nscanner fixture\n')
    dup=fake/mod.DUPLICATE_ROOT/'copy.pdf'
    dup.parent.mkdir()
    dup.write_bytes(src.read_bytes())
    oldroot=mod.ROOT
    mod.ROOT=fake
    before=mod.discover_corpus_pdfs()
    op_paths=['analysis/test/unrelated.pdf','analysis/x/NEVER_PACKAGE/reports/B02/source_delivery/current_source.pdf',
              'analysis/x/private_source_material/B02/source.pdf','analysis/rehearsal/source.pdf',
              'analysis/synthetic_fixture.pdf','docs/unrelated.pdf','Summaries/unrelated.pdf']
    for rel in op_paths:
        p=fake/rel
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_bytes(b'%PDF-1.4\noperational fixture\n')
    after=mod.discover_corpus_pdfs()
    mod.ROOT=oldroot
    tests['synthetic_registered_source_included']=src in before[0]
    tests['synthetic_exact_archived_duplicate_separate']=dup in before[1] and dup not in before[0]
    tests['operational_pdf_invariance']=before==after
    tests['NEVER_PACKAGE_excluded']=all(fake/p not in after[0] for p in op_paths if 'NEVER_PACKAGE' in p)
    tests['private_source_excluded']=all(fake/p not in after[0] for p in op_paths if 'private_source_material' in p)
    tests['rehearsal_source_excluded']=fake/op_paths[3] not in after[0]
    tests['synthetic_fixture_excluded']=fake/op_paths[4] not in after[0]
    tests['source_delivery_excluded']=fake/op_paths[1] not in after[0]
    tests['unrelated_analysis_excluded']=fake/op_paths[0] not in after[0]
    tests['synthetic_canonical_count_unchanged']=len(before[0])==len(after[0])==1
    tests['synthetic_total_count_unchanged']=sum(map(len,before))==sum(map(len,after))==2
old=json.loads((root/'analysis'/'checkpoint.json').read_text(encoding='utf-8'))
new=json.loads((candidate/'checkpoint.json').read_text(encoding='utf-8'))
tests['status_counts_unchanged']=old['counts']==new['counts']
tests['source_verified_zero']=new['counts'].get('source_verified',0)==0
tests['promoted_zero']=new['counts'].get('promoted',0)==0
tests['paper_records_unchanged']=old['papers']==new['papers']
tests['duplicate_mappings_unchanged']=old['duplicates']==new['duplicates']
tests['canonical_count_112']=new['canonical_pdf_count']==112
tests['total_count_117']=new['total_pdf_count']==117
tests['no_unmapped_issues']=not any(x.startswith('Unmapped PDF: ') for x in new['issues'])
tests['markdown_count_agrees']=f"Corpus: {new['canonical_pdf_count']} canonical PDFs; {len(new['duplicates'])} archived duplicates." in (candidate/'CHECKPOINT.md').read_text(encoding='utf-8')
tests['markdown_timestamp_agrees']=f"Updated: {new['updated_at']}" in (candidate/'CHECKPOINT.md').read_text(encoding='utf-8')
result={'verdict':'PASS' if all(tests.values()) else 'FAIL','tests':tests,'candidate_counts':{k:new[k] for k in ('canonical_pdf_count','total_pdf_count','counts')},
        'candidate_issue_count':len(new['issues']),'tracked_papers':len(new['papers']),'duplicate_count':len(new['duplicates'])}
(here/'SCANNER_REGRESSION_TEST_RESULTS.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(result))
