"""Assemble private B01 development graphs from the recorded source adjudications."""
import json,re,hashlib,copy,collections,sys
from pathlib import Path
O=Path(__file__).resolve().parent;P=O/'private_source_material';OLD=P/'original_phase4b/holdout_validation/B01/private'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(b):return hashlib.sha256(b).hexdigest()
parts=re.split(r'=+ PDF PAGE (\d+) =+', (OLD/'extracted_pages.txt').read_text(encoding='utf-8'))
pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
items=read(OLD/'normalized_evidence_items.json');S=items[0]['source_sha256'];R=items[0]['paper_id']
A={x['original']['primary']['stable_item_id']:x for x in read(P/'adjudication_atoms.json')}

def new_graph(field):
    return {'schema_version':'4.0.0','paper_report_id':R,'source_sha256':S,'source_page_count':26,'methodology_sha256':'0'*64,
      'fields':[{'field_id':field,'claim_ids':[]}],'source_elements':[],'locators':[],'reviews':[{'review_id':'development_review','source_sha256':S,'methodology_sha256':'0'*64,'identity_class':'MODEL_SOURCE_REVIEW','rationale':'B01 consumed development data; coordinator source adjudication; no human ground truth'}],
      'propositions':[],'support_requirements':[],'support_sets':[],'entailments':[],'results':[],'comparison_sets':[],'claims':[],'source_conflicts':[]}

def element(g,page,ref,value=None,kind='TEXT_SPAN'):
    eid='e'+str(len(g['source_elements'])+1);lid='l'+str(len(g['locators'])+1)
    g['source_elements'].append({'element_id':eid,'kind':kind,'source_sha256':S,'page':page,'reference':ref,'content_sha256':sha(pages[page].encode('utf-8')),'numeric_value':None if value is None else str(value)})
    g['locators'].append({'locator_id':lid,'source_sha256':S,'source_element_ids':[eid]});return eid,lid

def proposition(g,text,page,ref,role='VALUE_SUPPORT',status='SUPPORTED',value=None,extra=None,origin='SOURCE_REPORTED'):
    pid='p'+str(len(g['propositions'])+1);eid,lid=element(g,page,ref,value)
    locids=[lid];eids=[eid]
    for pg,r in extra or []:
        e,l=element(g,pg,r);locids.append(l);eids.append(e)
    if origin=='ANALYST_INFERENCE':status='INFERENCE_GROUNDED'
    g['propositions'].append({'proposition_id':pid,'text':text,'origin':origin,'inference_rationale':'Analyst interpretation grounded in the listed source observations; not an author-stated conclusion or direct entailment.' if origin=='ANALYST_INFERENCE' else None,'proposition_type':{'VALUE_SUPPORT':'FACT','METRIC_SUPPORT':'METRIC','CONDITION_SUPPORT':'CONDITION','SCOPE_SUPPORT':'SCOPE','COMPARISON_SET_SUPPORT':'COMPARISON_SET','RANKING_SUPPORT':'RANKING','DERIVATION_INPUT':'VALUE','QUALIFIER_SUPPORT':'QUALIFIER'}.get(role,'FACT'),'material':True,'required_roles':[role],'support_status':status,'verification_status':'MODEL_SOURCE_REVIEWED' if status in ('SUPPORTED','INFERENCE_GROUNDED') else 'UNRESOLVED'})
    sid='s'+str(len(g['support_sets'])+1)
    es='EXACT' if status=='SUPPORTED' else 'PARTIAL' if status=='INFERENCE_GROUNDED' else 'UNRESOLVED'
    g['support_sets'].append({'support_set_id':sid,'locator_ids':locids,'entailment_status':es,'combination_rule':'ALL_ELEMENTS' if len(locids)>1 else 'SINGLE','review_id':'development_review'})
    g['support_requirements'].append({'requirement_id':'q'+str(len(g['support_requirements'])+1),'proposition_id':pid,'role':role,'support_set_id':sid,'required_element_ids':eids})
    for l in locids:g['entailments'].append({'proposition_id':pid,'locator_id':l,'role':role,'entailment_status':('PARTIAL' if len(locids)>1 else 'EXACT') if status=='SUPPORTED' else 'PARTIAL' if status=='INFERENCE_GROUNDED' else 'UNRESOLVED','review_id':'development_review'})
    return pid,eid,lid

def claim(g,text,status=None):
    cid='c'+str(len(g['claims'])+1);ids=[p['proposition_id'] for p in g['propositions']]
    if status is None:status='FULLY_SUPPORTED' if all(p['support_status']=='SUPPORTED' for p in g['propositions']) else 'PARTIALLY_SUPPORTED'
    g['claims'].append({'claim_id':cid,'statement':text,'critical':True,'proposition_ids':ids,'support_status':status,'comparison':None,'derivation':None});g['fields'][0]['claim_ids'].append(cid);return g['claims'][-1]

unresolved_tail={
 'CH043':'Whether no companion report exists is unresolved; the single-page locator did not establish absence.',
 'CH046':'Whether precise attacker information is completely specified across scenarios remains unresolved.',
 'CH059':'Document-wide absence of seed distributions and significance tests remains unresolved.'}
extra_support={'framing.motivation':[(3,'Related benchmark discussion'),(6,'Dynamic/adaptive evaluation')],
 'forward.future_work':[(10,'Section 5 items iv-v')],
 'forward.open_problems':[(9,'Tool isolation and future work'),(10,'Broader tasks')],
 'identity.venue':[],
 'results.quantitative':[(2,'Introduction historical version statement'),(7,'Claude 3.5 released after first version')]}

graphs=[];crosswalk=[]
for i,item in enumerate(items,1):
    iid=item['stable_item_id'];field=item['stable_field_id'];g=new_graph(field);original=item['claim'];ch=A.get(iid);status='STILL_CORRECT'
    if ch:
        n=ch['adjudication']['challenge_id'];atoms=ch['revised_atoms']
        for k,a in enumerate(atoms):
            role=['VALUE_SUPPORT','METRIC_SUPPORT','CONDITION_SUPPORT','SCOPE_SUPPORT'][k] if 'result_id' in original else 'VALUE_SUPPORT'
            origin='ANALYST_INFERENCE' if n=='CH065' or (n=='CH070' and k in (0,2,3)) else 'SOURCE_REPORTED'
            proposition(g,a['text'],a['page'],a['reference'],role,status='UNRESOLVED' if n=='CH010' else 'SUPPORTED',value=original.get('value') if 'result_id' in original and k==0 else None,origin=origin)
        if n in unresolved_tail:proposition(g,unresolved_tail[n],item['locator']['page'],'Original locator does not prove absence',role='QUALIFIER_SUPPORT',status='UNRESOLVED')
        c=claim(g,ch['adjudication']['primary_claim_paraphrase'],'UNRESOLVED' if n=='CH010' else None)
        status='NOW_UNRESOLVED' if n=='CH010' else 'NARROWED' if ch['adjudication']['claim_correctness']=='CLAIM_PARTIAL' else 'STILL_CORRECT' if n=='CH036' else 'IMPROVED'
    elif field=='security.persistence':
        proposition(g,'The current benchmark does not cover persistent multi-task contexts.',9,'Section 4.3 tool isolation limitations')
        proposition(g,'Delayed injection across future tasks is discussed as a hypothetical limitation.',9,'Section 4.3 wait-until-next-task example')
        claim(g,'Persistence is discussed as an uncovered hypothetical limitation, not absent.');status='IMPROVED'
    elif field=='results.comparative':
        # Four distinct comparisons are evaluated in separate graph records below.
        proposition(g,'Four local ranking claims are evaluated separately; no document-wide best is inferred.',20,'Tables 3 and 5',status='UNRESOLVED')
        claim(g,'See four linked table-local comparison graphs.','UNRESOLVED');status='DECOMPOSED_COMPARISONS'
    elif 'derived_tools_total' in original:
        operand_ids=[]
        for row,val in zip(['Workspace','Slack','Travel','Banking'],original['operands']):
            _,eid,_=proposition(g,f'Table 1 {row} tool count is {val}.',6,f'Table 1 row {row}, Tools column','DERIVATION_INPUT',value=val);operand_ids.append(eid)
        c=claim(g,'The sum of the four printed tool counts is 74, not a reconciled canonical total.')
        c['derivation']={'operation':'SUM','operand_element_ids':operand_ids,'expected':'74','denominator':None,'denominator_element_id':None}
    elif 'derived_difference_percentage_points' in original:
        operand_ids=[]
        for label,val in [('Max',57.55),('Important message',57.7)]:
            _,eid,_=proposition(g,f'Table 4 {label} targeted ASR is {val}.',20,f'Table 4 Targeted ASR row, {label} column','DERIVATION_INPUT',value=val);operand_ids.append(eid)
        c=claim(g,'The difference between these printed cells is -0.15 percentage points; the prose interpretation remains unreconciled.')
        c['derivation']={'operation':'DIFFERENCE','operand_element_ids':operand_ids,'expected':'-0.15','denominator':None,'denominator_element_id':None}
    elif field=='results.quantitative' and original.get('status')=='PRESENT':
        for table,metric,val in [(3,'benign utility',69.00),(3,'utility under attack',50.08),(3,'targeted ASR',47.69),(5,'benign utility',69.0),(5,'utility under attack',50.01),(5,'targeted ASR',57.69)]:
            proposition(g,f'Table {table} GPT-4o no-defense {metric} is {val} percent.',20,f'Table {table}, GPT-4o/no-defense, {metric}',value=val)
            proposition(g,f'Metric is {metric}.',6,'Section 3.4','METRIC_SUPPORT')
            proposition(g,'No attack for benign utility; attack-present security cases for the other metrics.',6,'Section 3.4','CONDITION_SUPPORT')
        proposition(g,'Tables 3 and 5 represent distinct reported experiment contexts; no merged ASR is asserted.',20,'Tables 3 and 5 captions','SCOPE_SUPPORT',extra=[(7,'Section 4.1'),(8,'Section 4.3')])
        claim(g,'Six separately attributed measurements, with no cross-experiment harmonization.');status='IMPROVED'
    elif 'gpt4o_targeted_asr_table3' in original:
        for table,key in [(3,'gpt4o_targeted_asr_table3'),(5,'gpt4o_no_defense_targeted_asr_table5')]:
            proposition(g,f'Table {table} GPT-4o/no-defense targeted ASR is {original[key]} percent.',20,f'Table {table} targeted ASR cell',value=original[key])
        proposition(g,'The values are separately attributed to experiments; equivalence of conditions is not asserted.',20,'Tables 3 and 5 captions','SCOPE_SUPPORT',extra=[(7,'Section 4.1'),(8,'Section 4.3')])
        claim(g,'Two table-specific reported values; canonical same-condition value unresolved.');status='IMPROVED'
    elif 'abstract_intro_benign_claim' in original:
        proposition(g,'The introduction states that the best model solves under 66 percent of tasks.',2,'Introduction evaluation paragraph')
        proposition(g,'Table 3 reports Claude 3.5 Sonnet benign utility of 78.22 percent.',20,'Table 3 Claude 3.5 Sonnet, Benign utility',value='78.22')
        proposition(g,'The paper says Claude 3.5 Sonnet was released after the first report version.',7,'Section 4.1 Claude 3.5 discussion','QUALIFIER_SUPPORT')
        claim(g,'Two version-context statements are preserved separately; no single unqualified performance statement.');status='IMPROVED'
    elif 'result_id' in original:
        pg=item['locator']['page'];ref=item['locator'].get('note',item['locator'].get('section','Source paragraph'))
        proposition(g,f"{original['subject']}: {original['metric']} = {original['value']} {original['unit']}.",pg,ref,value=original['value'])
        proposition(g,'Condition: '+original['condition'],pg,ref,'CONDITION_SUPPORT')
        if original['result_id'].startswith('r_t4'):proposition(g,'This is the attack-phrasing experiment, not Table 3 or Table 5.',8,'Section 4.2','SCOPE_SUPPORT')
        claim(g,'Source-reported measurement with original local scope.')
    else:
        val=original.get('value',original)
        text=val if isinstance(val,str) else json.dumps(val,ensure_ascii=False,sort_keys=True)
        pg=item['locator']['page'];ref=item['locator'].get('section',item['locator'].get('note','Original field source'))
        if field=='forward.future_work':
            for t,pg,ref in [('Stronger attacks and defenses are proposed.',9,'Section 5 i'),('Automated task construction is proposed.',9,'Section 5 ii'),('More difficult tasks are proposed.',9,'Section 5 iii'),('Multimodal tasks are proposed.',10,'Section 5 iv'),('Constrained injections are proposed.',10,'Section 5 v')]:proposition(g,t,pg,ref)
            status='IMPROVED'
        else:proposition(g,text,pg,ref,extra=extra_support.get(field,[]))
        claim(g,'Retained source-grounded fact or explicitly attributed report observation.')
    gid='DEV'+str(i).zfill(3);write(P/'development_graphs'/f'{gid}.json',g)
    crosswalk.append({'graph_id':gid,'original_evidence_item_id':iid,'field_id':field,'critical':item['critical'],'challenge_id':ch['adjudication']['challenge_id'] if ch else None,'development_change':status,'graph_path':f'private_source_material/development_graphs/{gid}.json','claim_status':g['claims'][0]['support_status']})
    graphs.append(g)

# Explicitly scoped maxima/minima. Values come from original result inventory;
# all source values were rechecked against rendered page 20 during adjudication.
numeric={x['claim']['result_id']:x for x in items if 'result_id' in x['claim']}
comp_specs=[('T3_BENIGN','r_t3_', 'benign utility','MAX','Claude 3.5 Sonnet'),('T3_ASR','r_t3_','targeted asr','MAX','GPT-4o'),('T5_ASR','r_t5_','targeted asr','MIN','Tool filter'),('T5_BENIGN','r_t5_','benign utility','MAX','Repeat prompt')]
for name,prefix,metric,op,target_name in comp_specs:
    rows=[x for rid,x in numeric.items() if rid.startswith(prefix) and x['claim']['metric']==metric]
    g=new_graph('results.comparative');table=3 if prefix=='r_t3_' else 5
    cond='absence of attacks; 97 user tasks' if metric=='benign utility' else 'Important message baseline; 629 security cases' if table==3 else 'GPT-4o strongest-attack defense experiment'
    elems=[];lids=[];target=None
    for x in rows:
        r=x['claim'];eid,lid=element(g,20,x['locator']['note'],r['value'],'CELL');elems.append(eid);lids.append(lid)
        g['results'].append({'result_id':r['result_id'],'subject':r['subject'],'metric':metric,'unit':'percent','condition':cond,'dataset':'AgentDojo','split':'reported evaluation','configuration':'Table '+str(table),'value':str(r['value']),'source_element_id':eid})
        if r['subject']==target_name:target=r
    assert target
    for role,text,pg,ref in [
        ('VALUE_SUPPORT',f"{target_name} has value {target['value']} percent.",20,next(x['locator']['note'] for x in rows if x['claim']['subject']==target_name)),
        ('METRIC_SUPPORT',f'Metric is {metric}.',6,'Section 3.4'),
        ('CONDITION_SUPPORT',cond,6 if metric=='benign utility' else 7 if table==3 else 8,'Section 3.4' if metric=='benign utility' else 'Section 4.1' if table==3 else 'Section 4.3'),
        ('COMPARISON_SET_SUPPORT',f'All {len(rows)} entries of this metric in Table {table}.',20,f'Table {table} entire metric column/row'),
        ('RANKING_SUPPORT',f'The target equals the {op} of this table-local set.',20,f'Table {table} compared cells'),
        ('SCOPE_SUPPORT',f'Table {table} only; no whole-report superlative.',20,f'Table {table} caption and headers')]:
        pid,eid,lid=proposition(g,text,pg,ref,role)
        if role in ('COMPARISON_SET_SUPPORT','RANKING_SUPPORT'):
            q=g['support_requirements'][-1];s=g['support_sets'][-1];q['required_element_ids']+=elems;s['locator_ids']+=lids;s['combination_rule']='ALL_ELEMENTS'
            for l in lids:g['entailments'].append({'proposition_id':pid,'locator_id':l,'role':role,'entailment_status':'PARTIAL','review_id':'development_review'})
        if role=='VALUE_SUPPORT':
            target_index=next(i for i,r in enumerate(g['results']) if r['result_id']==target['result_id'])
            g['support_requirements'][-1]['required_element_ids'].append(elems[target_index]);g['support_sets'][-1]['locator_ids'].append(lids[target_index]);g['support_sets'][-1]['combination_rule']='ALL_ELEMENTS'
            g['entailments'].append({'proposition_id':pid,'locator_id':lids[target_index],'role':role,'entailment_status':'PARTIAL','review_id':'development_review'})
    scope_e=g['source_elements'][-1]['element_id']
    g['comparison_sets']=[{'comparison_set_id':name,'result_ids':[r['result_id'] for r in g['results']],'scope':'LOCAL','coverage':'COMPLETE_WITHIN_DECLARED_SCOPE','scope_element_ids':[scope_e],'document_wide_reconciled':False}]
    c=claim(g,f'{target_name} is table-local {op} for {metric}.');c['comparison']={'comparison_set_id':name,'target_result_id':target['result_id'],'scope':'LOCAL','operation':op,'expected':str(target['value']),'strict':True}
    write(P/'development_graphs'/f'COMP_{name}.json',g)
    crosswalk.append({'graph_id':'COMP_'+name,'original_evidence_item_id':next(x['stable_item_id'] for x in items if x['stable_field_id']=='results.comparative'),'field_id':'results.comparative','critical':True,'challenge_id':None,'development_change':'DECOMPOSED_COMPARISON','graph_path':f'private_source_material/development_graphs/COMP_{name}.json','claim_status':'FULLY_SUPPORTED'})
write(O/'DEVELOPMENT_ITEM_CROSSWALK.json',{'scope':'DEVELOPMENT_ONLY','original_items':len(items),'graph_count':len(crosswalk),'items':crosswalk})
print(json.dumps({'original_items':len(items),'graphs':len(crosswalk),'changes':dict(collections.Counter(x['development_change'] for x in crosswalk))}))
