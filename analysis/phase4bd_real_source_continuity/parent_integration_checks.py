from pathlib import Path
import sys,json
O=Path(__file__).resolve().parent;sys.path.insert(0,str(O/'integration_layer'))
from bridge import *
root=C/'context_architecture';registry=c.load(root/'registry.json');allow=c.load(root/'allowlists.json')
binding={'phase':'SYNTHETIC','holdout_id':'SYNTHETIC_CURRENT','paper_id':'SYNTHETIC_REPORT','source_sha256':'1'*64,'methodology_sha256':METHOD,'context_protocol_version':c.VERSION,'current_report_source':'NOT_YET_OPENED'}
records=[]
for role in ['primary','verifier']:
 hardened,meta=build_parent_packet(root,registry,allow,binding,role);original,_=c.build_packet(root,registry,allow,binding,role);assert hardened==original
 records.append({'role':role,'byte_identical_parent_packet':True,'packet_sha256':digest(hardened),'status':'PASS'})
exclusive(O/'test_results/INHERITED_PARENT_INTEGRATION.json',canonical({'suite':'parent_integration','tests':2,'passed':2,'failed':0,'skipped':0,'records':records,'real_sources_opened':False}))
print('Parent integration: 2 PASS')
