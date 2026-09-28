import json
from pathlib import Path
O=Path(__file__).resolve().parent
def obj(props):return {'type':'object','properties':props,'required':list(props),'additionalProperties':False}
def arr(items,minimum=0):return {'type':'array','items':items,'minItems':minimum}
def enum(*x):return {'enum':list(x)}
text={'type':'string','minLength':1};identifier={**text,'pattern':'^[A-Za-z0-9][A-Za-z0-9_.:-]*$'};sha={**text,'pattern':'^[0-9a-f]{64}$'}
number={'type':['number','string'],'pattern':'^-?[0-9]+(?:\\.[0-9]+)?$'};nullable_number={'anyOf':[number,{'type':'null'}]}
boolean={'type':'boolean'};ids={**arr(identifier,1),'uniqueItems':True}
roles=enum('VALUE_SUPPORT','METRIC_SUPPORT','CONDITION_SUPPORT','COMPARISON_SET_SUPPORT','RANKING_SUPPORT','SCOPE_SUPPORT','DERIVATION_INPUT','QUALIFIER_SUPPORT','NEGATIVE_RESULT_SUPPORT','LIMITATION_SUPPORT')
entailment=enum('EXACT','PARTIAL','CONTEXT_ONLY','CONTRADICTORY','IRRELEVANT','UNRESOLVED')
schema=obj({
 'schema_version':{'const':'4.0.0'},'paper_report_id':identifier,'source_sha256':sha,'source_page_count':{'type':'integer','minimum':1},'methodology_sha256':sha,
 'fields':arr(obj({'field_id':identifier,'claim_ids':ids}),1),
 'source_elements':arr(obj({'element_id':identifier,'kind':enum('TEXT_SPAN','TABLE','ROW','CELL','CAPTION','FIGURE','EQUATION','APPENDIX_SECTION','DERIVED_COMPUTATION'),'source_sha256':sha,'page':{'type':'integer','minimum':1},'reference':text,'content_sha256':sha,'numeric_value':nullable_number})),
 'locators':arr(obj({'locator_id':identifier,'source_sha256':sha,'source_element_ids':ids})),
 'reviews':arr(obj({'review_id':identifier,'source_sha256':sha,'methodology_sha256':sha,'identity_class':enum('MODEL_SOURCE_REVIEW','SEPARATE_CONTEXT_MODEL_VERIFICATION','TEST_FIXTURE_NOT_A_HUMAN'),'rationale':text})),
 'propositions':arr(obj({'proposition_id':identifier,'text':text,'origin':enum('SOURCE_REPORTED','ANALYST_INFERENCE','ARTIFACT_METADATA','PROCESS_PROVENANCE'),'inference_rationale':{'anyOf':[text,{'type':'null'}]},'proposition_type':enum('VALUE','METRIC','CONDITION','COMPARISON_SET','RANKING','SCOPE','QUALIFIER','NEGATIVE_RESULT','LIMITATION','FACT'),'material':boolean,'required_roles':{**arr(roles,1),'uniqueItems':True},'support_status':enum('SUPPORTED','INFERENCE_GROUNDED','PARTIALLY_SUPPORTED','CONTRADICTED','UNRESOLVED'),'verification_status':enum('UNREVIEWED','MODEL_SOURCE_REVIEWED','UNRESOLVED')}),1),
 'support_requirements':arr(obj({'requirement_id':identifier,'proposition_id':identifier,'role':roles,'support_set_id':identifier,'required_element_ids':ids}),1),
 'support_sets':arr(obj({'support_set_id':identifier,'locator_ids':ids,'entailment_status':entailment,'combination_rule':enum('SINGLE','ALL_ELEMENTS'),'review_id':identifier}),1),
 'entailments':arr(obj({'proposition_id':identifier,'locator_id':identifier,'role':roles,'entailment_status':entailment,'review_id':identifier}),1),
 'results':arr(obj({'result_id':identifier,'subject':text,'metric':text,'unit':text,'condition':text,'dataset':text,'split':text,'configuration':text,'value':number,'source_element_id':identifier})),
 'comparison_sets':arr(obj({'comparison_set_id':identifier,'result_ids':ids,'scope':enum('LOCAL','DOCUMENT_WIDE'),'coverage':enum('COMPLETE_WITHIN_DECLARED_SCOPE','INCOMPLETE','UNRESOLVED'),'scope_element_ids':ids,'document_wide_reconciled':boolean})),
 'claims':arr(obj({'claim_id':identifier,'statement':text,'critical':boolean,'proposition_ids':ids,'support_status':enum('FULLY_SUPPORTED','PARTIALLY_SUPPORTED','CONTRADICTED','UNRESOLVED'),
  'comparison':{'anyOf':[{'type':'null'},obj({'comparison_set_id':identifier,'target_result_id':identifier,'scope':enum('LOCAL','DOCUMENT_WIDE'),'operation':enum('MAX','MIN'),'expected':number,'strict':boolean})]},
  'derivation':{'anyOf':[{'type':'null'},obj({'operation':enum('MAX','MIN','SUM','COUNT','COUNT_ZERO','COUNT_NONZERO','DIFFERENCE','RATIO','PERCENT'),'operand_element_ids':ids,'expected':number,'denominator':nullable_number,'denominator_element_id':{'anyOf':[identifier,{'type':'null'}]}})]}}),1),
 'source_conflicts':arr(obj({'conflict_id':identifier,'affected_claim_ids':ids,'status':enum('UNRESOLVED','RESOLVED_WITH_RECORDED_EVIDENCE'),'rationale':text}))
})
schema={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'urn:litrev:scientific-evidence:4.0.0',**schema}
p=O/'candidate_v4br/hardened/schemas/scientific_evidence_v4.schema.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(schema,indent=2)+'\n')
