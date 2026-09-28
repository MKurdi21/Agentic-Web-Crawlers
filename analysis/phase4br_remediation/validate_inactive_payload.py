import sys,json,re,hashlib
from pathlib import Path
O=Path(__file__).resolve().parent;C=O/'candidate_v4br';sys.path.insert(0,str(C/'_deps'));import yaml
rows=[]
for p in sorted((C/'deploy_payload/skills').glob('*/SKILL.md')):
    text=p.read_text(encoding='utf-8');head=text.split('---',2)[1];meta=yaml.safe_load(head)
    refs=re.findall(r'\]\(([^)]+)\)',text);bad=[x for x in refs if not x.startswith('https:') and not (p.parent/x).is_file()]
    rows.append({'skill':meta['name'],'frontmatter_valid':bool(meta.get('description')),'references_valid':not bad,'missing_references':bad,'installed':False})
inherited=[]
old=O.parents[1]/'analysis/phase4b_validation/candidate_frozen/hardened/tests'
for p in sorted(old.glob('test_*.py')):
    q=C/'hardened/tests'/p.name;inherited.append({'file':p.name,'unchanged':p.read_bytes()==q.read_bytes(),'sha256':hashlib.sha256(q.read_bytes()).hexdigest()})
out={'skills':rows,'skill_count':len(rows),'checks':'Static frontmatter/reference and inherited-test preservation checks; no live activation or empirical trigger-accuracy claim','inherited_test_files':inherited,'passed':all(x['frontmatter_valid'] and x['references_valid'] for x in rows) and all(x['unchanged'] for x in inherited)}
(O/'test_results').mkdir(exist_ok=True);(O/'test_results/INACTIVE_PAYLOAD_AND_TEST_PRESERVATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
