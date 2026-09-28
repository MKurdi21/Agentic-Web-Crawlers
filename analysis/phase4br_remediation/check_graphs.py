import sys,json
from pathlib import Path
O=Path(__file__).resolve().parent
sys.path[:0]=[str(O/'candidate_v4br/_deps'),str(O/'candidate_v4br/hardened/scripts')]
from support_v4 import validate_graph
rows=[]
for f in sorted((O/'private_source_material/development_graphs').glob('*.json')):
    try:result=validate_graph(json.loads(f.read_text(encoding='utf-8')));rows.append({'file':f.name,'passed':True,'result':result})
    except Exception as e:rows.append({'file':f.name,'passed':False,'error':str(e)})
print(json.dumps({'passed':sum(x['passed'] for x in rows),'failed':[x for x in rows if not x['passed']]}))
