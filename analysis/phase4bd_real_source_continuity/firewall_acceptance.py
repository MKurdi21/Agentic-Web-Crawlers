"""Post-freeze firewall acceptance checks; no scientific source is opened."""
from pathlib import Path
import sys,json,copy
O=Path(__file__).resolve().parent;sys.path.insert(0,str(O/'integration_layer'))
from bridge import *
entry=next(iter(read(O/'DEVELOPMENT_AUTHORIZATION.json')['reports'].values()))
data,_=packet(entry);approved=read(O/'test_results/PACKET_SEMANTIC_REVIEW.json')
challenges={'prior_B01_findings':'B01 prior scientific finding (invented challenge)',
 'Phase4_findings':'PHASE4_REHEARSAL findings (invented challenge)',
 'recovery_summary':'Recovery summary from a previous operation (invented challenge)',
 'coordinator_historical_notes':'coordinator scientific summary (invented challenge)',
 'previous_holdout_findings':'previous holdout found a result (invented challenge)'}
records=[]
for name,text in challenges.items():
 body=c.loads(data);body['context'][0]['content']+='\n'+text;changed=c.canonical(body)
 blocked=False;reason=None
 try:review_valid(changed,approved,entry)
 except Exception as ex:blocked=True;reason=str(ex)
 assert blocked,name
 records.append({'id':name,'status':'PASS','disposition':'BLOCK','reason':reason,'packet_sha256':digest(changed),'synthetic_injection':True})
report={'tests':5,'passed':5,'failed':0,'skipped':0,'integration_sha256':codehash(),'test_script_sha256':filehash(Path(__file__)),'source_access':False,'records':records,'scope':'Exact approved-packet binding and deny controls; not a universal semantic paraphrase detection benchmark'}
exclusive(O/'test_results/FIREWALL_ACCEPTANCE.json',canonical(report));print(json.dumps({k:report[k] for k in ['tests','passed','failed','source_access']}))
