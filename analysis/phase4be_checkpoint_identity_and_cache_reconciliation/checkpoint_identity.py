"""Phase 4BE-E read-only Git provenance and semantic checkpoint identity checks."""
import copy
import hashlib
import json
import pathlib
import re
import subprocess
import sys

sys.dont_write_bytecode=True
here=pathlib.Path(__file__).resolve().parent
root=here.parents[1]
c=root/'analysis'/'phase4be_checkpoint_reconciliation'
live=root/'analysis'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def out(name,obj):
    (here/name).write_text(obj if name.endswith('.md') else json.dumps(obj,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf-8')
def git(*args):return subprocess.check_output(['git',*args],cwd=root).decode('utf-8',errors='replace').strip()
def canonical(snapshot):
    if not isinstance(snapshot,dict) or 'updated_at' not in snapshot:raise ValueError('missing updated_at')
    x=copy.deepcopy(snapshot)
    del x['updated_at']
    return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
def markdown_stable(text):
    if len(re.findall(r'(?m)^Updated: .*$',text))!=1:raise ValueError('updated line ambiguity')
    return re.sub(r'(?m)^Updated: .*$', 'Updated: <volatile>',text)
old=read(c/'candidate'/'checkpoint.json')
cur=read(live/'checkpoint.json')
oldmd=(c/'candidate'/'CHECKPOINT.md').read_text(encoding='utf-8')
curmd=(live/'CHECKPOINT.md').read_text(encoding='utf-8')
old_sem=hashlib.sha256(canonical(old)).hexdigest()
cur_sem=hashlib.sha256(canonical(cur)).hexdigest()
semantic_equal=old_sem==cur_sem
md_equal=markdown_stable(oldmd)==markdown_stable(curmd)
assert semantic_equal and md_equal
assert sha(root/'scripts'/'summary_state.py')=='7d92cd0953e45a71747bfe3f5533b092e855821ded9515ff0fa9e2a0a9c0d7ea'
commit='2c27edb55ba37ba3315f7d769719a301cb24c6cb'
paths=['analysis/CHECKPOINT.md','analysis/checkpoint.json','scripts/summary_state.py']
blob={p:{'commit_blob_id':git('rev-parse',f'{commit}:{p}'),'head_blob_id':git('rev-parse',f'HEAD:{p}'),
         'index_blob_id':git('rev-parse',f':{p}'),'current_raw_sha256':sha(root/p),
         'current_lf_normalized_sha256':hashlib.sha256((root/p).read_bytes().replace(b'\r\n',b'\n')).hexdigest(),
         'committed_blob_sha256':hashlib.sha256(subprocess.check_output(['git','show',f'{commit}:{p}'],cwd=root)).hexdigest()}
      for p in paths}
assert all(v['commit_blob_id']==v['head_blob_id']==v['index_blob_id'] for v in blob.values())
assert all(v['current_lf_normalized_sha256']==v['committed_blob_sha256'] for v in blob.values())
status=subprocess.check_output(['git','status','--porcelain=v1','--',*paths],cwd=root).decode().strip()
assert not status
first=git('log','--all','--diff-filter=A','--date=iso-strict','--format=%H|%ad|%cd|%s','--','analysis/CHECKPOINT.md','analysis/checkpoint.json').splitlines()
assert len(first)==1 and first[0].startswith(commit)
meta={
 'classification':'COMMITTED_CURRENT_CONTENT_GENERATOR_WRITER_UNKNOWN',
 'first_commit':commit,'first_commit_metadata':first[0],
 'pr_merge_commit':'1e2baf16dd7b6ae7056a28639df2762f97dd1de4',
 'pr_merge_metadata':git('show','-s','--date=iso-strict','--format=%H|%ad|%cd|%s','1e2baf1'),
 'pr':'#11 review/11-analysis-workflow','current_branch':git('branch','--show-current'),
 'working_tree_status_for_target_paths':status,'git_core_autocrlf':git('config','--get','core.autocrlf'),
 'commit_blob_evidence':blob,'checkpoint_generation_timestamp_utc':cur['updated_at'],
 'checkpoint_mtime_utc':{p:__import__('datetime').datetime.fromtimestamp((root/p).stat().st_mtime,__import__('datetime').timezone.utc).isoformat() for p in paths[:2]},
 'active_git_hooks':sorted(p.name for p in (root/'.git'/'hooks').iterdir() if p.is_file() and not p.name.endswith('.sample')),
 'generator_calling_script':'scripts/run_summary.ps1 invokes summary_state.py in finally block; no evidence this script ran for this refresh',
 'exact_generator_process_identity':'UNKNOWN','precise_causation':'Commit contains current checkpoint content; timestamp precedes commit by about 24 seconds. The exact generation command/session remains unproven.',
 'phase4be_c_candidate_updated_at':old['updated_at'],'current_updated_at':cur['updated_at'],
}
out('GIT_CHECKPOINT_PROVENANCE.json',meta)
out('GIT_CHECKPOINT_PROVENANCE_REPORT.md',f'''# Git checkpoint provenance\n\nCommit `{commit}` (`analysis: add corpus mapping and recovery workflow`) first added both checkpoint files and `scripts/summary_state.py` at 2026-09-28 10:35:13 EDT. The current checkpoint update timestamp is {cur['updated_at']}, about 24 seconds before that commit. PR #11 merged `review/11-analysis-workflow` later as `{meta['pr_merge_commit']}`. Both current checkpoint blobs equal that first commit, the current index, and HEAD. `core.autocrlf=true` explains why the worktree raw SHA-256 differs from the committed LF-normalized blob bytes. The target paths are clean, and there are no active Git hooks.\n\nThis proves the current content was committed during the Git/PR work. It does not identify the process that generated the timestamped files. No hook or command record was found that establishes the exact generator invocation. Writer status: `WRITER_UNKNOWN_SEMANTIC_REGENERATION_PROVEN` if isolated authorized-generator reproduction passes.\n''')
diff={
 'classification':'SEMANTICALLY_IDENTICAL_TIMESTAMP_ONLY' if semantic_equal and md_equal else 'SEMANTIC_DIFFERENCE_PRESENT',
 'phase4be_c_raw_hashes':{'analysis/CHECKPOINT.md':sha(c/'candidate'/'CHECKPOINT.md'),'analysis/checkpoint.json':sha(c/'candidate'/'checkpoint.json')},
 'current_raw_hashes':{'analysis/CHECKPOINT.md':sha(live/'CHECKPOINT.md'),'analysis/checkpoint.json':sha(live/'checkpoint.json')},
 'phase4be_c_updated_at':old['updated_at'],'current_updated_at':cur['updated_at'],
 'semantic_hash_phase4be_c':old_sem,'semantic_hash_current':cur_sem,
 'approved_volatile_json_fields':['updated_at'],'approved_volatile_markdown_rendering':['Updated: line'],
 'all_other_json_fields_equal':{k:v for k,v in old.items() if k!='updated_at'}=={k:v for k,v in cur.items() if k!='updated_at'},
 'markdown_equal_except_updated_line':md_equal,'paper_records_equal':old['papers']==cur['papers'],
 'status_counts_equal':old['counts']==cur['counts'],'issues_equal':old['issues']==cur['issues'],
 'duplicates_equal':old['duplicates']==cur['duplicates'],
 'generator_sha256':sha(root/'scripts'/'summary_state.py'),
}
out('CHECKPOINT_SEMANTIC_DIFF.json',diff)
spec={'version':'phase4be-checkpoint-semantic-identity-v1.0.0',
 'canonicalization':'checkpoint-semantic-c14n-v1',
 'machine_authority':'analysis/checkpoint.json parsed with unique keys, remove exactly top-level updated_at, recursively retain every other value, JSON UTF-8 ensure_ascii=false sort_keys=true separators=(comma,colon), allow_nan=false, SHA-256',
 'approved_volatile_json_fields':['updated_at'],'rendered_authority':'analysis/CHECKPOINT.md must equal the trusted generator rendering after normalizing exactly one Updated: line; that line must exactly equal Updated: <JSON updated_at> with no suffix or duplicate; raw SHA always recorded',
 'generator_sha256':'7d92cd0953e45a71747bfe3f5533b092e855821ded9515ff0fa9e2a0a9c0d7ea',
 'baseline_semantic_sha256':old_sem,'source_model':'12 approved corpus roots, 99_Duplicates separate, 112 mapped sources',
 'block_on':['semantic hash change','generator hash change','source hash or manifest drift','rendered Markdown substantive drift','malformed JSON','unknown volatile field','failed isolated reproduction'],
 'allow_on':['raw checkpoint hash change only with approved timestamp change and matching semantic hash, Markdown rendering, generator and isolated reproduction'],
}
spec_hash=hashlib.sha256(json.dumps(spec,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
spec['policy_sha256']=spec_hash
out('CHECKPOINT_SEMANTIC_IDENTITY_SPEC.json',spec)
out('CHECKPOINT_SEMANTIC_IDENTITY_SPEC.md',f'''# Stable checkpoint identity\n\nVersion: `{spec['version']}`. Policy SHA-256: `{spec_hash}`. The JSON checkpoint is machine authority. Parse it strictly, remove only top-level `updated_at`, serialize the entire remaining object as deterministic UTF-8 JSON, and hash it. The current and Phase 4BE-C semantic hash is `{old_sem}`. All remaining fields, including every paper and source hash, remain protected.\n\nRecord raw SHA-256 for provenance. Accept a raw checkpoint change only when the authorized generator hash matches, isolated reproduction has the same semantic hash, and CHECKPOINT.md matches trusted generator rendering after normalizing exactly one `Updated:` line. The line must exactly equal `Updated: ` followed by the JSON timestamp, with no suffix or duplicate. A changed substantive Markdown line blocks. A changed source, issue, duplicate, status, or unknown field blocks.\n''')
print(json.dumps({'commit':commit,'semantic_hash':old_sem,'policy_hash':spec_hash,'semantic_equal':semantic_equal,'markdown_equal':md_equal}))
