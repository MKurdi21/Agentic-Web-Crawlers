"""Retained consumed-B01 transport receipts; public output is metadata only."""
from pathlib import Path
import sys,json,subprocess,os,uuid
O=Path(__file__).resolve().parent;sys.path.insert(0,str(O/'integration_layer'))
from bridge import *
AUTH=O/'DEVELOPMENT_AUTHORIZATION.json';REVIEW=O/'test_results/PACKET_SEMANTIC_REVIEW.json'
entry_id=next(iter(read(AUTH)['reports']))
root=O/'private_development_source_material'/('retained-'+uuid.uuid4().hex)
a=RealContinuity(root).create(AUTH,entry_id,REVIEW)
ack=a.prepare();a.preaccess();first=a.unit('EXTRACTION');a.unit('VERIFICATION','VERIFY','during_unit');a.close_worker()
before=a.e.state();assert before['status']=='PREEMPTED_BY_USAGE_LIMIT' and before['source_access_started']
command=[sys.executable,'-B',str(O/'integration_layer/cli.py')]
p=subprocess.run(command+['verify',str(root)],capture_output=True,check=True,timeout=240);fresh=json.loads(p.stdout)
assert fresh['pid']!=os.getpid() and fresh['consumed']
n=len(a.e.receipts());p2=subprocess.run(command+['recover',str(root)],capture_output=True,check=True,timeout=180);again=json.loads(p2.stdout)
assert len(a.e.receipts())==n and again['consumed']
second=read(a.e.root/'outputs/verification.json');assert first['value']==second['value'] and first['locator']==second['locator']
events=a.e.journal();access=[x for x in events if x['event_type']=='SOURCE_ACCESS_BEGAN'];assert len(access)==1
receipts=a.e.receipts();ids=[r['atomic_unit_id'] for _,r in receipts];assert len(ids)==len(set(ids))
assert ids.count('PACKET_ACK')==ids.count('PRE_ACCESS')==ids.count('CONSUMPTION')==ids.count('EXTRACTION')==ids.count('VERIFICATION')==1
with a.e.lock('development-complete'):a.e.finish()
report={'status':'PASS','integration_sha256':codehash(),'private_run':root.relative_to(O).as_posix(),'report_id':entry_id,'source_sha256':a.entry['source_sha256'],'primary_worker_context_id':ack['primary_context_id'],'original_coordinator_pid':os.getpid(),'fresh_coordinator':fresh,'repeat_recovery_coordinator':again,'source_access_events':len(access),'consumption_receipts':ids.count('CONSUMPTION'),'packet_ack_receipts':ids.count('PACKET_ACK'),'extraction_commits':ids.count('EXTRACTION'),'verification_commits':ids.count('VERIFICATION'),'unit_ids':ids,'milestone_receipts':[{'sha256':h,'unit':r['atomic_unit_id']} for h,r in receipts],'private_output_hashes':{n:filehash(a.e.root/'outputs'/n) for n in ['extraction.json','verification.json']},'same_value_and_locator':True,'no_scientific_validation':True,'reserved_reports_opened':0,'source_delivery_after_consumption':True,'usage_preemption':'SIMULATED_INVENTED_EVENT_NOT_ACCOUNT_BALANCE','packet_reconstructed_from_disk':True,'worker_conversation_history':'NONE'}
exclusive(O/'test_results/RETAINED_REAL_E2E.json',canonical(report))
print(json.dumps({k:report[k] for k in ['status','source_access_events','extraction_commits','verification_commits','reserved_reports_opened']}))
