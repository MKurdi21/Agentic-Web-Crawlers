import sys,json,copy,csv
from pathlib import Path
O=Path(__file__).resolve().parent
sys.path[:0]=[str(O/'candidate_v4br/_deps'),str(O/'candidate_v4br/hardened/scripts'),str(O/'candidate_v4br/hardened/tests')]
from test_support_v4 import graph,comparative
F=O/'b01_failure_fixtures';F.mkdir(exist_ok=True)
cases=[]
def add(id,title,pos,neg,code):cases.append({'fixture_id':id,'name':title,'source_material':'SYNTHETIC_NOT_PAPER_BYTES','positive':pos,'negative':neg,'expected_error':code})
g=comparative();n=copy.deepcopy(g);n['propositions'][1]['support_status']='UNRESOLVED';add('F01','All material propositions required',g,n,'COMPOUND_FALSE_SUPPORT')
g=graph();n=copy.deepcopy(g);n['entailments'][0]['entailment_status']='CONTEXT_ONLY';add('F02','Context is not support',g,n,'PROPOSITION_FALSE_SUPPORT')
g=comparative();n=copy.deepcopy(g);n['locators'][1]['source_element_ids']=['e1'];add('F03','Compound set requires all elements',g,n,'PROPOSITION_FALSE_SUPPORT')
g=comparative();n=copy.deepcopy(g);n['results'][1]['condition']='attack-versus-benign';add('F04','Condition and denominator coherence',g,n,'COMPARISON_CONDITION_MISMATCH')
g=comparative();n=copy.deepcopy(g);n['comparison_sets'][0]['coverage']='UNRESOLVED';add('F05','Unproven scope fails closed',g,n,'COMPARISON_INCOMPLETE')
g=graph();n=copy.deepcopy(g);n['support_sets'][0]['entailment_status']='UNRESOLVED';add('F06','Unproven absence not supported',g,n,'PROPOSITION_FALSE_SUPPORT')
g=graph();g['propositions'][0]['text']='Synthetic Unicode name: \u00e8';n=copy.deepcopy(g);n['reviews'][0]['source_sha256']='f'*64;add('F07','Unicode survives pinned serialization',g,n,'REVIEW_PIN_MISMATCH')
g=graph();n=copy.deepcopy(g);n['source_elements'][0]['page']=3;add('F08','Wrong page rejected',g,n,'PAGE_BOUNDS')
g=graph();n=copy.deepcopy(g);n['source_conflicts']=[{'conflict_id':'conflict','affected_claim_ids':['c1'],'status':'UNRESOLVED','rationale':'Synthetic unreconciled source conflict'}];add('F09','Unresolved conflict cannot be fully supported',g,n,'SOURCE_CONFLICT_ACCEPTED')
g=comparative();n=copy.deepcopy(g);n['claims'][0]['proposition_ids'].remove('p5');add('F10','Value alone does not prove rank',g,n,'COMPARATIVE_ROLE_MISSING')
g=comparative();n=copy.deepcopy(g);n['comparison_sets'][0]['scope']='DOCUMENT_WIDE';n['claims'][0]['comparison']['scope']='DOCUMENT_WIDE';add('F11','Local result cannot become global',g,n,'GLOBAL_SCOPE_UNRECONCILED')
g=comparative();n=copy.deepcopy(g);n['results'][1]['value']='999';add('F12','Numeric value bound to source operand',g,n,'RESULT_SOURCE_VALUE_MISMATCH')
for x in cases:(F/(x['fixture_id']+'.json')).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
(F/'INDEX.json').write_text(json.dumps({'fixtures':[{'fixture_id':x['fixture_id'],'name':x['name']} for x in cases],'scope':'12 generalized classes; no original paper tables or excerpts'},indent=2)+'\n',encoding='utf-8')
# Inherited packaging tests require a real protected-hash inventory at this path.
rows=list(csv.DictReader((O/'PROTECTED_FILES_INITIAL.csv').open(encoding='utf-8')))
T=O/'candidate_v4br/test_results';T.mkdir(exist_ok=True)
old=T/'UNIT_INTEGRATION_RESULTS.json'
if old.exists():(T/'INITIAL_RUN_FAILURES.json').write_bytes(old.read_bytes())
(T/'INITIAL_BASELINE.json').write_text(json.dumps({'files':{x['path']:{'sha256':x['sha256']} for x in rows}}),encoding='utf-8')
