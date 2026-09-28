"""Proposition-specific support graph validation. Never grants scientific approval."""
import json, re
import hashlib
from decimal import Decimal, InvalidOperation
from pathlib import Path
from jsonschema import Draft202012Validator

ROLES={'VALUE_SUPPORT','METRIC_SUPPORT','CONDITION_SUPPORT','COMPARISON_SET_SUPPORT','RANKING_SUPPORT','SCOPE_SUPPORT','DERIVATION_INPUT','QUALIFIER_SUPPORT','NEGATIVE_RESULT_SUPPORT','LIMITATION_SUPPORT'}
class SupportFailure(ValueError):
    def __init__(self,code,detail=''):self.code=code;super().__init__(code+': '+detail)
def require(ok,code,detail=''):
    if not ok:raise SupportFailure(code,detail)
def num(x):
    require(not isinstance(x,bool) and x is not None,'INVALID_NUMBER')
    try:v=Decimal(str(x))
    except InvalidOperation:raise SupportFailure('INVALID_NUMBER')
    require(v.is_finite(),'INVALID_NUMBER');return v
def calculate(operation,values,*,target_index=0,denominator=None):
    require(bool(values),'MISSING_OPERANDS');v=list(map(num,values))
    if operation=='MAX':return max(v)
    if operation=='MIN':return min(v)
    if operation=='SUM':return sum(v,Decimal(0))
    if operation=='COUNT':return Decimal(len(v))
    if operation=='COUNT_ZERO':return Decimal(sum(x==0 for x in v))
    if operation=='COUNT_NONZERO':return Decimal(sum(x!=0 for x in v))
    if operation=='RANK':
        require(0<=target_index<len(v),'TARGET_INDEX');return Decimal(1+sum(x>v[target_index] for x in v))
    if operation=='TIES':
        require(0<=target_index<len(v),'TARGET_INDEX');return Decimal(sum(x==v[target_index] for x in v))
    if operation in ('GREATER','LESS','DIFFERENCE','RATIO'):
        require(len(v)==2,'TWO_OPERANDS_REQUIRED')
        if operation=='GREATER':return Decimal(v[0]>v[1])
        if operation=='LESS':return Decimal(v[0]<v[1])
        if operation=='DIFFERENCE':return v[0]-v[1]
        require(v[1]!=0,'ZERO_DENOMINATOR');return v[0]/v[1]
    if operation=='PERCENT':
        require(len(v)==1 and denominator is not None,'DENOMINATOR_REQUIRED');d=num(denominator)
        require(d>0 and 0<=v[0]<=d,'DENOMINATOR_RANGE');return Decimal(100)*v[0]/d
    raise SupportFailure('UNKNOWN_OPERATION',operation)
def index(rows,key):
    require(len(rows)==len({x[key] for x in rows}),'DUPLICATE_ID',key)
    return {x[key]:x for x in rows}

def validate_graph(p,schema_path=None):
    if schema_path is None:schema_path=Path(__file__).resolve().parents[1]/'schemas/scientific_evidence_v4.schema.json'
    schema=json.loads(Path(schema_path).read_text(encoding='utf-8'))
    errs=list(Draft202012Validator(schema).iter_errors(p));require(not errs,'SCHEMA',errs[0].message if errs else '')
    elems=index(p['source_elements'],'element_id');locs=index(p['locators'],'locator_id');sets=index(p['support_sets'],'support_set_id')
    props=index(p['propositions'],'proposition_id');claims=index(p['claims'],'claim_id');reqs=index(p['support_requirements'],'requirement_id')
    results=index(p['results'],'result_id');comparisons=index(p['comparison_sets'],'comparison_set_id');reviews=index(p['reviews'],'review_id')
    fields=index(p['fields'],'field_id')
    for f in fields.values():require(set(f['claim_ids'])<=claims.keys(),'FIELD_CLAIM_REFERENCE')
    require(set(claims)=={c for f in fields.values() for c in f['claim_ids']},'ORPHAN_CLAIM')
    for e in elems.values():
        require(e['source_sha256']==p['source_sha256'],'CROSS_SOURCE_ELEMENT')
        require(1<=e['page']<=p['source_page_count'],'PAGE_BOUNDS')
    for l in locs.values():
        require(set(l['source_element_ids'])<=elems.keys(),'LOCATOR_ELEMENT_REFERENCE')
        require(l['source_sha256']==p['source_sha256'],'CROSS_SOURCE_LOCATOR')
    for r in reviews.values():
        require(r['source_sha256']==p['source_sha256'] and r['methodology_sha256']==p['methodology_sha256'],'REVIEW_PIN_MISMATCH')
        require(r['identity_class'] not in ('TRUSTED_HUMAN_APPROVAL','HUMAN_REVIEW'),'SOFTWARE_HUMAN_APPROVAL')
    edges={}
    for e in p['entailments']:
        key=(e['proposition_id'],e['locator_id'],e['role']);require(key not in edges,'DUPLICATE_ENTAILMENT');edges[key]=e
        require(e['proposition_id'] in props and e['locator_id'] in locs and e['review_id'] in reviews,'ENTAILMENT_REFERENCE')
    for s in sets.values():
        require(set(s['locator_ids'])<=locs.keys() and s['review_id'] in reviews,'SUPPORT_SET_REFERENCE')
    by_prop={pid:[] for pid in props}
    for q in reqs.values():
        require(q['proposition_id'] in props and q['support_set_id'] in sets,'REQUIREMENT_REFERENCE')
        require(set(q['required_element_ids'])<=elems.keys(),'REQUIRED_ELEMENT_REFERENCE');by_prop[q['proposition_id']].append(q)
    full_props=set();failed_requirements=[]
    for pid,prop in props.items():
        if prop['origin']=='ANALYST_INFERENCE':
            require(prop['inference_rationale'] is not None,'INFERENCE_RATIONALE_MISSING',pid)
            require(prop['support_status']!='SUPPORTED','INFERENCE_ALIASED_TO_SOURCE_FACT',pid)
        else:
            require(prop['inference_rationale'] is None,'UNEXPECTED_INFERENCE_RATIONALE',pid)
        if prop['origin'] in ('PROCESS_PROVENANCE','ARTIFACT_METADATA'):
            require(prop['support_status']!='SUPPORTED','NON_PAGE_PROVENANCE_AS_SCIENTIFIC_FACT',pid)
        requirements=by_prop[pid]
        require(bool(requirements),'PROPOSITION_REQUIREMENTS_MISSING',pid)
        require(set(prop['required_roles'])=={q['role'] for q in requirements},'REQUIRED_ROLE_COVERAGE',pid)
        good=True;inference_basis=True
        for q in requirements:
            s=sets[q['support_set_id']];cover={eid for lid in s['locator_ids'] for eid in locs[lid]['source_element_ids']}
            relations=[edges.get((pid,lid,q['role'])) for lid in s['locator_ids']]
            ok=(s['entailment_status']=='EXACT' and set(q['required_element_ids'])<=cover and
                all(e is not None and e['entailment_status'] in ('EXACT','PARTIAL') for e in relations))
            # Combining parts needs a reviewed ALL_ELEMENTS set; context-only never contributes.
            if any(e and e['entailment_status']=='PARTIAL' for e in relations):ok=ok and s['combination_rule']=='ALL_ELEMENTS' and len(s['locator_ids'])>1
            inference_basis=inference_basis and s['entailment_status'] in ('EXACT','PARTIAL') and set(q['required_element_ids'])<=cover and all(e is not None and e['entailment_status'] in ('EXACT','PARTIAL') for e in relations)
            if not ok:failed_requirements.append(q['requirement_id']);good=False
        if prop['support_status']=='SUPPORTED':
            require(good and prop['verification_status']=='MODEL_SOURCE_REVIEWED','PROPOSITION_FALSE_SUPPORT',pid);full_props.add(pid)
        if prop['support_status']=='INFERENCE_GROUNDED':
            require(prop['origin']=='ANALYST_INFERENCE' and prop['verification_status']=='MODEL_SOURCE_REVIEWED','INFERENCE_ORIGIN_REQUIRED',pid)
            require(inference_basis,'INFERENCE_BASIS_MISSING',pid)
    for r in results.values():
        require(r['source_element_id'] in elems,'RESULT_ELEMENT_REFERENCE');num(r['value'])
        source_value=elems[r['source_element_id']]['numeric_value']
        require(source_value is not None and num(source_value)==num(r['value']),'RESULT_SOURCE_VALUE_MISMATCH')
    for comp in comparisons.values():require(set(comp['result_ids'])<=results.keys() and set(comp['scope_element_ids'])<=elems.keys(),'COMPARISON_REFERENCE')
    for claim in claims.values():
        ids=claim['proposition_ids'];require(bool(ids) and set(ids)<=props.keys(),'CLAIM_PROPOSITION_REFERENCE')
        material=[pid for pid in ids if props[pid]['material']]
        require(bool(material),'NO_MATERIAL_PROPOSITION')
        full=claim['support_status']=='FULLY_SUPPORTED'
        require(not full or all(pid in full_props for pid in material),'COMPOUND_FALSE_SUPPORT',claim['claim_id'])
        roles={role for pid in material for role in props[pid]['required_roles']}
        comp=claim['comparison']
        if comp is not None:
            require(comp['comparison_set_id'] in comparisons,'COMPARISON_SET_MISSING')
            cs=comparisons[comp['comparison_set_id']];rows=[results[r] for r in cs['result_ids']]
            if full:
                require({'VALUE_SUPPORT','METRIC_SUPPORT','CONDITION_SUPPORT','COMPARISON_SET_SUPPORT','RANKING_SUPPORT','SCOPE_SUPPORT'}<=roles,'COMPARATIVE_ROLE_MISSING')
                require(cs['coverage']=='COMPLETE_WITHIN_DECLARED_SCOPE','COMPARISON_INCOMPLETE')
                require(bool(cs['scope_element_ids']),'SCOPE_EVIDENCE_MISSING')
                require(comp['scope']==cs['scope'],'SCOPE_MISMATCH')
                if comp['scope']=='DOCUMENT_WIDE':require(cs['document_wide_reconciled'],'GLOBAL_SCOPE_UNRECONCILED')
                context_keys=('metric','unit','condition','dataset','split','configuration')
                require(all(all(row[k]==rows[0][k] for k in context_keys) for row in rows),'COMPARISON_CONDITION_MISMATCH')
                require(comp['target_result_id'] in cs['result_ids'],'TARGET_MISSING')
                target=results[comp['target_result_id']];v=calculate(comp['operation'],[r['value'] for r in rows])
                require(v==num(comp['expected']) and num(target['value'])==v,'RANKING_FALSE_SUPPORT')
                if comp['strict']:require(sum(num(r['value'])==v for r in rows)==1,'TIED_NOT_STRICTLY_BEST')
                required={e for pid in material for q in by_prop[pid] for e in q['required_element_ids']}
                require({r['source_element_id'] for r in rows} | set(cs['scope_element_ids']) <= required,'COMPARISON_ELEMENTS_UNBOUND')
                role_bound=lambda role:{e for pid in material for q in by_prop[pid] if q['role']==role for e in q['required_element_ids']}
                row_elements={r['source_element_id'] for r in rows}
                require(row_elements<=role_bound('RANKING_SUPPORT'),'RANKING_ELEMENTS_WRONG_ROLE')
                require(row_elements<=role_bound('COMPARISON_SET_SUPPORT'),'COMPARISON_SET_ELEMENTS_WRONG_ROLE')
                require(set(cs['scope_element_ids'])<=role_bound('SCOPE_SUPPORT'),'SCOPE_ELEMENTS_WRONG_ROLE')
                require(target['source_element_id'] in role_bound('VALUE_SUPPORT'),'TARGET_VALUE_WRONG_ROLE')
        d=claim['derivation']
        if d is not None:
            require(set(d['operand_element_ids'])<=elems.keys(),'OPERAND_REFERENCE')
            require(all(elems[e]['numeric_value'] is not None for e in d['operand_element_ids']),'OPERAND_VALUE_MISSING')
            if d['operation']=='PERCENT':
                de=d['denominator_element_id']
                require(de in elems and elems[de]['numeric_value'] is not None,'DENOMINATOR_SOURCE_REQUIRED')
                require(num(elems[de]['numeric_value'])==num(d['denominator']),'DENOMINATOR_SOURCE_MISMATCH')
            else:require(d['denominator_element_id'] is None and d['denominator'] is None,'UNEXPECTED_DENOMINATOR')
            actual=calculate(d['operation'],[elems[e]['numeric_value'] for e in d['operand_element_ids']],denominator=d['denominator'])
            require(actual==num(d['expected']),'DERIVED_VALUE_MISMATCH')
            if full:
                require('DERIVATION_INPUT' in roles,'DERIVATION_ROLE_MISSING')
                bound={e for pid in material if pid in full_props for q in by_prop[pid] if q['role']=='DERIVATION_INPUT' for e in q['required_element_ids']}
                require(set(d['operand_element_ids'])<=bound,'UNBOUND_OPERANDS')
                if d['operation']=='PERCENT':require(d['denominator_element_id'] in bound,'UNBOUND_DENOMINATOR')
        for conflict in p['source_conflicts']:
            require(set(conflict['affected_claim_ids'])<=claims.keys(),'CONFLICT_CLAIM_REFERENCE')
            require(not(full and claim['claim_id'] in conflict['affected_claim_ids'] and conflict['status']=='UNRESOLVED'),'SOURCE_CONFLICT_ACCEPTED')
    return {'status':'STRUCTURALLY_AND_SEMANTICALLY_VALID','scientific_acceptance':False,'fully_supported_claims':sum(c['support_status']=='FULLY_SUPPORTED' for c in claims.values()),'failed_requirements':failed_requirements}

def support_dependencies(p,locator_id):
    sets={s['support_set_id'] for s in p['support_sets'] if locator_id in s['locator_ids']}
    return sorted({q['proposition_id'] for q in p['support_requirements'] if q['support_set_id'] in sets})

def proposition_elements(p,proposition_id):
    return sorted({eid for q in p['support_requirements'] if q['proposition_id']==proposition_id for eid in q['required_element_ids']})

def validate_source_bindings(p,source_sha256,page_texts):
    """Check exact extraction-page bytes separately from model entailment judgments."""
    require(p['source_sha256']==source_sha256,'SOURCE_BYTES_MISMATCH')
    for e in p['source_elements']:
        require(e['page'] in page_texts,'SOURCE_PAGE_MISSING')
        actual=hashlib.sha256(page_texts[e['page']].encode('utf-8')).hexdigest()
        require(actual==e['content_sha256'],'SOURCE_ELEMENT_DIGEST_MISMATCH',e['element_id'])
    return True
