"""Deterministically author v2 contracts; writes only the design schemas directory."""
from common import *
S={'type':'string','minLength':1}; ID={**S,'format':'identifier'}; HASH={**S,'format':'sha256'}
def arr(item,minitems=1):return {'type':'array','items':item,'minItems':minitems}
def obj(props,required=None):return {'type':'object','properties':props,'required':list(props) if required is None else required,'additionalProperties':False}
LOCATORS={
 'PAGE':{'page':{'type':'integer','minimum':1}},
 'PAGE_RANGE':{'start':{'type':'integer','minimum':1},'end':{'type':'integer','minimum':1}},
 'SECTION':{'heading':S},'FIGURE':{'identifier_or_caption':S},'TABLE':{'identifier':S},'EQUATION':{'identifier_or_anchor':S},'APPENDIX':{'heading':S},
 'TEXT_SPAN':{'text_sha256':HASH,'start':{'type':'integer','minimum':0},'end':{'type':'integer','minimum':1},'offset_convention':{'const':'UNICODE_CODEPOINT'}},
 'ARTIFACT_URL':{'url':{**S,'format':'http-uri'}},
 'REPOSITORY_FILE':{'repository':S,'revision':S,'path':S},'UNKNOWN':{'reason':S,'missing_context':S}}
LOCATOR={'oneOf':[obj({'type':{'const':k},'source_sha256':HASH,**v}) for k,v in LOCATORS.items()]}
CLAIM=obj({'record_id':ID,'paper_report_id':ID,'claim_type':{'enum':['AUTHOR_CLAIM','OBSERVABLE_EVIDENCE','DERIVED','INTERPRETATION','NEGATIVE_FINDING']},'statement':S,'locator':LOCATOR,'confidence':{'enum':['HIGH','MEDIUM','LOW','UNKNOWN']}})
VERIFY=obj({'record_id':ID,'evidence_id':ID,'evidence_sha256':HASH,'status':{'enum':['UNVERIFIED','SUPPORTED','PARTIALLY_SUPPORTED','CONTRADICTED','AMBIGUOUS','NOT_LOCATABLE','NOT_APPLICABLE']},'rationale':S,'locator':LOCATOR})
BASE={'paper_report_id':ID,'source_sha256':HASH,'schema_version':{'const':'2.0.0'}}
CONTRACTS={
 'normalized_paper':obj({**BASE,'text_sha256':HASH,'inventory':arr(obj({'object_id':ID,'object_type':{'enum':['SECTION','FIGURE','TABLE','EQUATION','APPENDIX','EXPERIMENT','ALGORITHM']},'locator':LOCATOR}))}),
 'summary':obj({**BASE,'narrative':S,'claims':arr(CLAIM),'coverage':obj({'reviewed_object_ids':arr(ID,0),'unreviewed_object_ids':arr(ID,0),'limitations':arr(S,0)})}),
 'evidence':obj({**BASE,'items':arr(CLAIM),'entities':arr(obj({'entity_id':ID,'entity_type':{'enum':['METHOD','SYSTEM','BENCHMARK','DATASET','METRIC','EXPERIMENT','THREAT_MODEL','DEFENSE','ATTACK','LIMITATION']},'description':S,'evidence_ids':arr(ID)}),0)}),
 'verification':obj({**BASE,'items':arr(VERIFY),'protocol_sha256':HASH}),
 'research_object':obj({'schema_version':{'const':'2.0.0'},'record_id':ID,'state':{'enum':['CANDIDATE','CONFIRMED','REJECTED','UNRESOLVED']},'members':arr(ID),'relationship_type':{'enum':['VERSION_OF','SAME_CONTRIBUTION','EXTENDS','REPLICATES','UNRESOLVED']},'evidence_ids':arr(ID),'rationale':S}),
 'taxonomy':obj({'schema_version':{'const':'2.0.0'},'record_id':ID,'version':{**S,'format':'semver'},'terms':arr(obj({'term_id':ID,'definition':S,'inclusion':S,'exclusion':S}))}),
 'paper_taxonomy_coding':obj({**BASE,'taxonomy_id':ID,'taxonomy_version':{**S,'format':'semver'},'codes':arr(obj({'term_id':ID,'evidence_ids':arr(ID),'rationale':S}))}),
 'contradiction':obj({'schema_version':{'const':'2.0.0'},'record_id':ID,'claim_ids':arr(ID,2),'comparison_context':obj({'metric_or_proposition':S,'conditions':S,'comparability_rationale':S}),'interpretation':S}),
 'synthesis':obj({'schema_version':{'const':'2.0.0'},'record_id':ID,'input_ids':arr(ID),'input_fingerprint':HASH,'report_ids':arr(ID),'research_object_ids':arr(ID),'report_count':{'type':'integer','minimum':1},'object_count':{'type':'integer','minimum':1},'coverage':{'enum':['COMPLETE_ELIGIBLE_SCOPE','PARTIAL_AUTHORIZED']},'exclusions':arr(obj({'report_id':ID,'reason':S}),0),'matrix':arr(obj({'row_id':ID,'evidence_ids':arr(ID),'finding':S}))}),
 'gap_candidate':obj({'schema_version':{'const':'2.0.0'},'record_id':ID,'synthesis_ids':arr(ID),'statement':S,'limitations':arr(S),'novelty_status':{'const':'NOT_EXTERNALLY_VALIDATED'}}),
 'research_question':obj({'schema_version':{'const':'2.0.0'},'record_id':ID,'gap_ids':arr(ID),'question':S,'testable_outcome':S,'limitations':arr(S)}),
 'artifact_metadata':obj({'artifact_id':ID,'sha256':HASH,'kind':S,'privacy':{'enum':['NEVER_PACKAGE','SYNTHETIC']},'created_at':{**S,'format':'timestamp'}}),
 'worker_task':obj({'task_id':ID,'attempt_id':ID,'run_id':ID,'worker':ID,'token':S,'generation':{'type':'integer','minimum':1},'expiry':{'type':'number'},'source_sha256':HASH,'paper_report_id':ID,'stage':S,'pins':{'type':'object','minProperties':1},'outbox':S}),
 'worker_result':obj({'task_id':ID,'attempt_id':ID,'run_id':ID,'worker':ID,'token':S,'generation':{'type':'integer','minimum':1},'submission_id':ID,'paper_report_id':ID,'source_sha256':HASH,'kind':{'enum':['normalized_paper','summary','evidence','verification','research_object','taxonomy','paper_taxonomy_coding','contradiction','synthesis','gap_candidate','research_question']},'output_path':S,'output_sha256':HASH})}
def main():
 for name in ('worker_task','worker_result'):
  CONTRACTS[name]['properties']['attempt_number']={'type':'integer','minimum':1}
  if 'attempt_number' not in CONTRACTS[name]['required']:CONTRACTS[name]['required'].append('attempt_number')
 for name,schema in CONTRACTS.items():write_json(DESIGN/'hardened/schemas'/f'{name}.schema.json',{'$schema':'https://json-schema.org/draft/2020-12/schema','$id':f'urn:litrev:v2:{name}',**schema})
if __name__=='__main__':main()
