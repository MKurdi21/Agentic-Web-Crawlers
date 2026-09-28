"""Run an isolated copy of the original generator against checkpoint-era paths."""
import json
import pathlib
import subprocess
import sys

here=pathlib.Path(__file__).resolve().parent
root=here.parents[1]
state=root/'analysis'
old=json.loads((state/'checkpoint.json').read_text(encoding='utf-8'))
paths=sorted({r['Pdf'].replace('\\','/') for r in old['papers']} |
             {x['path'] for x in old['duplicates']} |
             {x.removeprefix('Unmapped PDF: ') for x in old['issues'] if x.startswith('Unmapped PDF: ')})
out=here/'reproduction'
out.mkdir(exist_ok=True)
source=(root/'scripts'/'summary_state.py').read_text(encoding='utf-8')
replacements={
    'ROOT = Path(__file__).resolve().parents[1]': f'ROOT = Path({str(root)!r})',
    'STATE = ROOT / "analysis"': f'STATE = ROOT / "analysis"\nOUTPUT = Path({str(out)!r})',
    'now = datetime.now(timezone.utc).isoformat()': f'now = {old["updated_at"]!r}',
    'all_pdfs = sorted(ROOT.rglob("*.pdf"))': f'all_pdfs = [ROOT / p for p in {paths!r}]',
    'write_json(STATE / "checkpoint.json", snapshot)': 'write_json(OUTPUT / "checkpoint.json", snapshot)',
    'temp = STATE / "CHECKPOINT.md.tmp"': 'temp = OUTPUT / "CHECKPOINT.md.tmp"',
    'temp.replace(STATE / "CHECKPOINT.md")': 'temp.replace(OUTPUT / "CHECKPOINT.md")',
}
for a,b in replacements.items():
    if source.count(a)!=1:
        raise RuntimeError(f'Expected one replacement for {a!r}, got {source.count(a)}')
    source=source.replace(a,b)
script=out/'isolated_original_generator.py'
script.write_text(source,encoding='utf-8')
run=subprocess.run([sys.executable,str(script)],cwd=root,capture_output=True,text=True)
(out/'generator_stdout.json').write_text(run.stdout,encoding='utf-8')
(out/'generator_stderr.txt').write_text(run.stderr,encoding='utf-8')
if run.returncode:
    raise RuntimeError(run.stderr)
new=json.loads((out/'checkpoint.json').read_text(encoding='utf-8'))
newissue=set(new['issues'])
oldissue=set(old['issues'])
def comparable(v):
    x=dict(v)
    x['issues']=sorted(x['issues'])
    return x
result={
    'method':'isolated copy of current scripts/summary_state.py, all 157 checkpoint-era paths supplied from saved checkpoint, original updated_at injected, outputs redirected into Phase4BE-C',
    'live_checkpoint_written':False,
    'generator_returncode':run.returncode,
    'historical_path_count':len(paths),
    'historical_paths_all_exist':all((root/p).is_file() for p in paths),
    'reproduced_counts':{k:new[k] for k in ('canonical_pdf_count','total_pdf_count','counts')},
    'drifted_counts':{k:old[k] for k in ('canonical_pdf_count','total_pdf_count','counts')},
    'issue_set_equal':newissue==oldissue,
    'paper_records_equal':new['papers']==old['papers'],
    'duplicate_records_equal':new['duplicates']==old['duplicates'],
    'semantic_json_equal_ignoring_issue_order':comparable(new)==comparable(old),
    'new_issues':sorted(newissue-oldissue),
    'missing_issues':sorted(oldissue-newissue),
    'limitation':'The checkpoint-era path set is reconstructed from the drifted checkpoint. This establishes deterministic generator behavior over the reported files, not OS-level writer identity.'
}
(here/'CURRENT_GENERATOR_REPRODUCTION.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('historical_path_count','historical_paths_all_exist','reproduced_counts','issue_set_equal','paper_records_equal','duplicate_records_equal','semantic_json_equal_ignoring_issue_order')}))
