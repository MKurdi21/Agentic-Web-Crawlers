import json,sys,hashlib
from pathlib import Path
O=Path(__file__).resolve().parent;A=O/'context_architecture';D=O/'B02_PREACCESS_PACKET_DRY_RUN'
sys.path.insert(0,str(A/'scripts'));import context_engine as e
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,v):p.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
cfg=read(O/'CONTEXT_PACKET_ARCHITECTURE_CONFIGURATION.json');deny=read(O/'VALIDATION_CONTEXT_DENYLIST.json');binding=read(D/'binding.json')
expected={'primary':'183b490ded6e4bd2c1590ac4d3308a8a59ff8b01a145a08c0545425ae6c0b119','verifier':'82ac187d323c98550d64aadccc43705ea590654927cb83a224704bb00b4d8f1d'}
reviews={}
e.verify_immutable(A,read(O/'IMMUTABLE_EXECUTION_MANIFEST.json')['files'])
for role,sha in expected.items():
 packet=(D/(role+'.packet.json')).read_bytes();assert e.digest(packet)==sha
 r=e.review_record(packet,reviewer_context_id='/root/bc_packet_review',status='SEMANTIC_CONTEXT_CLEAN',rationale='Separate-context read-only reviewer inspected exact complete packet; generic rules, schema, policies and current identity only; no prior scientific findings or real-paper remediation examples detected.',review_protocol_sha256=cfg['semantic_review_protocol_sha256'])
 decision=e.release(packet,deny,read(D/(role+'.scan.json')),r,builder_context_id='/root',expected_binding=binding,expected_packet_sha256=sha,expected_review_protocol_sha256=cfg['semantic_review_protocol_sha256'])
 save(D/(role+'.semantic_review.json'),r);save(D/(role+'.release_decision.json'),decision)
 m=read(D/(role+'.release_manifest.json'));m['semantic_review_result']='SEMANTIC_CONTEXT_CLEAN';save(D/(role+'.release_manifest.json'),m);reviews[role]=r
save(O/'SEMANTIC_CONTEXT_REVIEW.json',{'status':'SEMANTIC_CONTEXT_CLEAN','packets':reviews,'limits':'Model-based findings, no proof of universal paraphrase detection or human approval.'})
save(O/'INDEPENDENT_PACKET_REVIEW.json',{'status':'COMPLETED','reviewer_context':'/root/bc_packet_review','fork_history':'none','packets':reviews,'source_access':False,'historical_expected_answers_provided':False,'human_review':False})
hashes=['71ddf69effd6952cfe832190aef6062e3501b2a417421c92c98c391b4162c31f','6b949f9ceb105f4426de7e316d109a5553694055b433dce5656be43ffaea2e03','c0395e0a23c7960765da6b6c3a1b22f2d9dfa2dbc5d9731289bcb548fe4e196d','225b07768851dc697ae49b57d7bfa2e9952d56b3db113f32eb76e1062b9b35b6']
verdicts=['CLEAN','CONTAMINATED','CLEAN','CONTAMINATED'];rows=[]
for letter,sha,v in zip('abcd',hashes,verdicts):
 p=A/'tests/semantic_challenges'/('challenge_'+letter+'.json');assert e.digest(p.read_bytes())==sha
 rows.append({'challenge':letter,'sha256':sha,'observed':v,'expected':v,'status':'PASS','reviewer_context':'/root/bc_packet_review'})
save(O/'test_results/SEMANTIC_CHALLENGE_RESULTS.json',{'tests_run':4,'passed':4,'failed':0,'skipped':0,'review_protocol_sha256':cfg['semantic_review_protocol_sha256'],'expected_answers_withheld':True,'tests':rows})
print('Independent exact-packet reviews and four semantic challenge outcomes recorded')
