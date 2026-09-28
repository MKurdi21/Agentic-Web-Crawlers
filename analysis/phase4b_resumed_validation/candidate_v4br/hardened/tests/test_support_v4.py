import copy, json, tempfile, unittest
from pathlib import Path
from support_v4 import SupportFailure, validate_graph, calculate, support_dependencies, proposition_elements,validate_source_bindings
from pre_access import ReceiptFailure, commit_preaccess, open_source, verify_order, digest, canonical

DESIGN=Path(__file__).resolve().parents[2]

def graph():
    s='a'*64;m='b'*64
    return {'schema_version':'4.0.0','paper_report_id':'report_synthetic','source_sha256':s,'source_page_count':2,'methodology_sha256':m,
      'fields':[{'field_id':'results','claim_ids':['c1']}],
      'source_elements':[{'element_id':'e1','kind':'CELL','source_sha256':s,'page':1,'reference':'Synthetic table row A','content_sha256':'c'*64,'numeric_value':'8'}],
      'locators':[{'locator_id':'l1','source_sha256':s,'source_element_ids':['e1']}],
      'reviews':[{'review_id':'rev1','source_sha256':s,'methodology_sha256':m,'identity_class':'TEST_FIXTURE_NOT_A_HUMAN','rationale':'Synthetic only'}],
      'propositions':[{'proposition_id':'p1','text':'Synthetic system score is eight','origin':'SOURCE_REPORTED','inference_rationale':None,'proposition_type':'VALUE','material':True,'required_roles':['VALUE_SUPPORT'],'support_status':'SUPPORTED','verification_status':'MODEL_SOURCE_REVIEWED'}],
      'support_requirements':[{'requirement_id':'q1','proposition_id':'p1','role':'VALUE_SUPPORT','support_set_id':'s1','required_element_ids':['e1']}],
      'support_sets':[{'support_set_id':'s1','locator_ids':['l1'],'entailment_status':'EXACT','combination_rule':'SINGLE','review_id':'rev1'}],
      'entailments':[{'proposition_id':'p1','locator_id':'l1','role':'VALUE_SUPPORT','entailment_status':'EXACT','review_id':'rev1'}],
      'results':[],'comparison_sets':[],'claims':[{'claim_id':'c1','statement':'Synthetic score eight','critical':True,'proposition_ids':['p1'],'support_status':'FULLY_SUPPORTED','comparison':None,'derivation':None}],'source_conflicts':[]}

def comparative():
    g=graph();e=copy.deepcopy(g['source_elements'][0]);e.update(element_id='e2',reference='Synthetic table row B',numeric_value='3');g['source_elements'].append(e)
    l=copy.deepcopy(g['locators'][0]);l.update(locator_id='l2',source_element_ids=['e2']);g['locators'].append(l)
    g['support_sets'][0].update(locator_ids=['l1','l2'],combination_rule='ALL_ELEMENTS')
    g['entailments'].append({**g['entailments'][0],'locator_id':'l2'})
    g['support_requirements'][0]['required_element_ids']=['e1','e2']
    for i,role in enumerate(['METRIC_SUPPORT','CONDITION_SUPPORT','COMPARISON_SET_SUPPORT','RANKING_SUPPORT','SCOPE_SUPPORT'],2):
        pid='p'+str(i);q='q'+str(i)
        g['propositions'].append({**g['propositions'][0],'proposition_id':pid,'text':'Synthetic '+role,'required_roles':[role]})
        g['support_requirements'].append({**g['support_requirements'][0],'requirement_id':q,'proposition_id':pid,'role':role})
        g['entailments'].extend([{**g['entailments'][0],'proposition_id':pid,'role':role,'locator_id':lid} for lid in ['l1','l2']])
        g['claims'][0]['proposition_ids'].append(pid)
    for rid,elem,val in [('r1','e1','8'),('r2','e2','3')]:
        g['results'].append({'result_id':rid,'subject':rid,'metric':'score','unit':'units','condition':'same','dataset':'synthetic','split':'test','configuration':'fixed','value':val,'source_element_id':elem})
    g['comparison_sets']=[{'comparison_set_id':'cs1','result_ids':['r1','r2'],'scope':'LOCAL','coverage':'COMPLETE_WITHIN_DECLARED_SCOPE','scope_element_ids':['e1','e2'],'document_wide_reconciled':False}]
    g['claims'][0]['comparison']={'comparison_set_id':'cs1','target_result_id':'r1','scope':'LOCAL','operation':'MAX','expected':'8','strict':True}
    return g

class SupportV4(unittest.TestCase):
    def test_inference_cannot_alias_source_fact(self):
        g=graph();g['propositions'][0].update(origin='ANALYST_INFERENCE',inference_rationale='Synthetic interpretation')
        self.rejected(g,'INFERENCE_ALIASED_TO_SOURCE_FACT')
    def test_inference_retained_but_not_full_source_support(self):
        g=graph();g['propositions'][0].update(origin='ANALYST_INFERENCE',inference_rationale='Synthetic interpretation',support_status='INFERENCE_GROUNDED');g['claims'][0]['support_status']='PARTIALLY_SUPPORTED'
        self.assertEqual(validate_graph(g)['fully_supported_claims'],0)
    def test_inference_cannot_fully_support_compound(self):
        g=graph();g['propositions'][0].update(origin='ANALYST_INFERENCE',inference_rationale='Synthetic interpretation',support_status='INFERENCE_GROUNDED')
        self.rejected(g,'COMPOUND_FALSE_SUPPORT')
    def test_process_provenance_not_a_page_fact(self):
        g=graph();g['propositions'][0]['origin']='PROCESS_PROVENANCE';self.rejected(g,'NON_PAGE_PROVENANCE_AS_SCIENTIFIC_FACT')
    def test_source_element_hash_checked_independently(self):
        import hashlib
        g=graph();g['source_elements'][0]['content_sha256']=hashlib.sha256(b'synthetic text').hexdigest()
        self.assertTrue(validate_source_bindings(g,'a'*64,{1:'synthetic text'}))
        with self.assertRaisesRegex(SupportFailure,'SOURCE_ELEMENT_DIGEST_MISMATCH'):validate_source_bindings(g,'a'*64,{1:'altered'})
    def rejected(self,g,code):
        with self.assertRaisesRegex(SupportFailure,code):validate_graph(g)
    def test_valid_never_scientific_approval(self):self.assertFalse(validate_graph(graph())['scientific_acceptance'])
    def test_compound_all_material(self):
        g=comparative();g['propositions'][1]['support_status']='UNRESOLVED';self.rejected(g,'COMPOUND_FALSE_SUPPORT')
    def test_context_only_not_exact(self):
        g=graph();g['entailments'][0]['entailment_status']='CONTEXT_ONLY';self.rejected(g,'PROPOSITION_FALSE_SUPPORT')
    def test_single_partial_not_promoted(self):
        g=graph();g['entailments'][0]['entailment_status']='PARTIAL';self.rejected(g,'PROPOSITION_FALSE_SUPPORT')
    def test_compound_set_can_combine_reviewed_parts(self):
        g=comparative()
        for e in g['entailments']:e['entailment_status']='PARTIAL'
        self.assertEqual(validate_graph(g)['fully_supported_claims'],1)
    def test_missing_role(self):
        g=comparative();g['claims'][0]['proposition_ids'].remove('p3');self.rejected(g,'COMPARATIVE_ROLE_MISSING')
    def test_value_supported_rank_unresolved(self):
        g=comparative();g['propositions'][4]['support_status']='UNRESOLVED';self.rejected(g,'COMPOUND_FALSE_SUPPORT')
    def test_comparison_all_rows_bound(self):
        g=comparative()
        for q in g['support_requirements']:q['required_element_ids']=['e1']
        self.rejected(g,'COMPARISON_ELEMENTS_UNBOUND')
    def test_local_cannot_be_global(self):
        g=comparative();g['claims'][0]['comparison']['scope']='DOCUMENT_WIDE';self.rejected(g,'SCOPE_MISMATCH')
    def test_global_needs_reconciliation(self):
        g=comparative();g['claims'][0]['comparison']['scope']='DOCUMENT_WIDE';g['comparison_sets'][0]['scope']='DOCUMENT_WIDE';self.rejected(g,'GLOBAL_SCOPE_UNRECONCILED')
    def test_scope_unresolved(self):
        g=comparative();g['comparison_sets'][0]['coverage']='UNRESOLVED';self.rejected(g,'COMPARISON_INCOMPLETE')
    def test_condition_mismatch(self):
        g=comparative();g['results'][1]['condition']='other';self.rejected(g,'COMPARISON_CONDITION_MISMATCH')
    def test_tie_rejects_unique_best(self):
        g=comparative();g['results'][1]['value']='8';g['source_elements'][1]['numeric_value']='8';self.rejected(g,'TIED_NOT_STRICTLY_BEST')
    def test_nonstrict_tie_supported(self):
        g=comparative();g['results'][1]['value']='8';g['source_elements'][1]['numeric_value']='8';g['claims'][0]['comparison']['strict']=False;validate_graph(g)
    def test_wrong_ranking(self):
        g=comparative();g['results'][1]['value']='9';g['source_elements'][1]['numeric_value']='9';self.rejected(g,'RANKING_FALSE_SUPPORT')
    def test_result_cannot_disagree_with_source_operand(self):
        g=comparative();g['results'][1]['value']='9';self.rejected(g,'RESULT_SOURCE_VALUE_MISMATCH')
    def test_comparative_elements_cannot_borrow_other_roles(self):
        for role,code in [('RANKING_SUPPORT','RANKING_ELEMENTS_WRONG_ROLE'),('COMPARISON_SET_SUPPORT','COMPARISON_SET_ELEMENTS_WRONG_ROLE'),('SCOPE_SUPPORT','SCOPE_ELEMENTS_WRONG_ROLE')]:
            g=comparative();next(q for q in g['support_requirements'] if q['role']==role)['required_element_ids']=['e1'];self.rejected(g,code)
    def test_percentage_cannot_borrow_value_role(self):
        g=graph();g['propositions'][0]['required_roles']=['DERIVATION_INPUT'];g['support_requirements'][0]['role']='DERIVATION_INPUT';g['entailments'][0]['role']='DERIVATION_INPUT'
        g['source_elements'].append({**g['source_elements'][0],'element_id':'den','numeric_value':'200'});g['locators'][0]['source_element_ids'].append('den')
        g['propositions'].append({**g['propositions'][0],'proposition_id':'p2','required_roles':['VALUE_SUPPORT']});g['claims'][0]['proposition_ids'].append('p2')
        g['support_requirements'].append({**g['support_requirements'][0],'requirement_id':'q2','proposition_id':'p2','role':'VALUE_SUPPORT','required_element_ids':['den']})
        g['entailments'].append({**g['entailments'][0],'proposition_id':'p2','role':'VALUE_SUPPORT'})
        g['claims'][0]['derivation']={'operation':'PERCENT','operand_element_ids':['e1'],'expected':'4','denominator':'200','denominator_element_id':'den'};self.rejected(g,'UNBOUND_DENOMINATOR')
    def test_missing_requirement(self):
        g=graph();g['support_requirements']=[];self.rejected(g,'SCHEMA')
    def test_wrong_element_locator(self):
        g=comparative();g['locators'][1]['source_element_ids']=['e1'];self.rejected(g,'PROPOSITION_FALSE_SUPPORT')
    def test_unknown_proposition_edge(self):
        g=graph();g['entailments'][0]['proposition_id']='absent';self.rejected(g,'ENTAILMENT_REFERENCE')
    def test_cross_source(self):
        g=graph();g['source_elements'][0]['source_sha256']='d'*64;self.rejected(g,'CROSS_SOURCE_ELEMENT')
    def test_review_pins(self):
        g=graph();g['reviews'][0]['methodology_sha256']='d'*64;self.rejected(g,'REVIEW_PIN_MISMATCH')
    def test_no_human_alias(self):
        g=graph();g['reviews'][0]['identity_class']='TRUSTED_HUMAN_APPROVAL';self.rejected(g,'SCHEMA')
    def test_conflict_fail_closed(self):
        g=graph();g['source_conflicts']=[{'conflict_id':'x','affected_claim_ids':['c1'],'status':'UNRESOLVED','rationale':'Synthetic conflict'}];self.rejected(g,'SOURCE_CONFLICT_ACCEPTED')
    def test_unresolved_can_be_retained(self):
        g=graph();g['claims'][0]['support_status']='UNRESOLVED';g['propositions'][0]['support_status']='UNRESOLVED';g['support_sets'][0]['entailment_status']='UNRESOLVED';validate_graph(g)
    def test_dependency_queries(self):
        g=comparative();self.assertEqual(len(support_dependencies(g,'l2')),6);self.assertEqual(proposition_elements(g,'p1'),['e1','e2'])
    def test_numeric_operations(self):
        for op,val in [('MAX',8),('MIN',3),('RANK',1),('TIES',1),('COUNT',2),('GREATER',1),('LESS',0),('DIFFERENCE',5)]:self.assertEqual(calculate(op,[8,3]),val)
        self.assertEqual(calculate('PERCENT',[2],denominator=8),25)
    def test_missing_operand(self):
        with self.assertRaisesRegex(SupportFailure,'INVALID_NUMBER'):calculate('MAX',[None,3])
    def test_zero_denominator(self):
        with self.assertRaisesRegex(SupportFailure,'DENOMINATOR_RANGE'):calculate('PERCENT',[0],denominator=0)
    def test_derived_operand_bound(self):
        g=graph();g['claims'][0]['derivation']={'operation':'MAX','operand_element_ids':['e1'],'expected':'8','denominator':None,'denominator_element_id':None};self.rejected(g,'DERIVATION_ROLE_MISSING')
    def test_derived_wrong_number(self):
        g=graph();g['claims'][0]['derivation']={'operation':'MAX','operand_element_ids':['e1'],'expected':'7','denominator':None,'denominator_element_id':None};self.rejected(g,'DERIVED_VALUE_MISMATCH')
    def test_percentage_requires_source_denominator(self):
        g=graph();g['claims'][0]['derivation']={'operation':'PERCENT','operand_element_ids':['e1'],'expected':'4','denominator':'200','denominator_element_id':None}
        self.rejected(g,'DENOMINATOR_SOURCE_REQUIRED')
    def test_percentage_requires_bound_matching_denominator(self):
        g=graph();g['propositions'][0]['required_roles']=['DERIVATION_INPUT'];g['support_requirements'][0]['role']='DERIVATION_INPUT';g['entailments'][0]['role']='DERIVATION_INPUT'
        g['source_elements'].append({**g['source_elements'][0],'element_id':'den','numeric_value':'200'})
        g['claims'][0]['derivation']={'operation':'PERCENT','operand_element_ids':['e1'],'expected':'4','denominator':'200','denominator_element_id':'den'}
        self.rejected(g,'UNBOUND_DENOMINATOR')
        g['support_requirements'][0]['required_element_ids'].append('den');g['locators'][0]['source_element_ids'].append('den');validate_graph(g)
        g['claims'][0]['derivation']['denominator']='100';self.rejected(g,'DENOMINATOR_SOURCE_MISMATCH')
    def test_duplicate_identity(self):
        g=graph();g['source_elements'].append(copy.deepcopy(g['source_elements'][0]));self.rejected(g,'DUPLICATE_ID')
    def test_qualifier_requirement_cannot_disappear(self):
        g=graph();g['propositions'][0]['required_roles'].append('QUALIFIER_SUPPORT');self.rejected(g,'REQUIRED_ROLE_COVERAGE')
    def test_graph_integration_dispatch(self):
        from validate_semantics import validate
        self.assertEqual(validate('scientific_evidence_v4',graph())['schema_version'],'4.0.0')

class ReceiptTests(unittest.TestCase):
    def setUp(self):
        parent=DESIGN/'test_runtime';parent.mkdir(exist_ok=True);self.tmp=tempfile.TemporaryDirectory(dir=parent);self.root=Path(self.tmp.name);self.source=self.root/'synthetic.txt';self.source.write_bytes(b'Synthetic source')
        self.bind={'phase':'TEST','holdout_id':'T1','paper_id':'synthetic','source_file_id':'src1','source_sha256':digest(self.source.read_bytes()),'candidate_manifest_sha256':'a'*64,'methodology_sha256':'b'*64,'protocol_hashes':{'test':'c'*64},'field_catalog_sha256':'d'*64,'holdout_state':'TEST_ONLY','context_protocol_version':'1'}
    def tearDown(self):self.tmp.cleanup()
    def test_valid_durable_order(self):
        r=commit_preaccess(self.root,self.bind,allowed_reports={'T1'});open_source(self.root,self.source,self.bind,allowed_reports={'T1'});self.assertTrue(verify_order(r,json.loads((self.root/'SOURCE_ACCESS_BEGAN.json').read_bytes())))
    def test_access_without_receipt(self):
        with self.assertRaisesRegex(ReceiptFailure,'MISSING_DURABLE_RECEIPT'):open_source(self.root,self.source,self.bind,allowed_reports={'T1'})
    def test_receipt_after_access_fails(self):
        (self.root/'SOURCE_ACCESS_BEGAN.json').write_text('{}')
        with self.assertRaisesRegex(ReceiptFailure,'SOURCE_ACCESS_PRECEDES_RECEIPT'):commit_preaccess(self.root,self.bind,allowed_reports={'T1'})
    def test_config_mismatch(self):
        commit_preaccess(self.root,self.bind,allowed_reports={'T1'});b={**self.bind,'methodology_sha256':'e'*64}
        with self.assertRaisesRegex(ReceiptFailure,'BINDING_MISMATCH'):open_source(self.root,self.source,b,allowed_reports={'T1'})
    def test_source_mismatch(self):
        commit_preaccess(self.root,self.bind,allowed_reports={'T1'});self.source.write_bytes(b'changed')
        with self.assertRaisesRegex(ReceiptFailure,'SOURCE_HASH_MISMATCH'):open_source(self.root,self.source,self.bind,allowed_reports={'T1'})
    def test_reserved_report_denied(self):
        with self.assertRaisesRegex(ReceiptFailure,'RESERVED_REPORT_DENIED'):commit_preaccess(self.root,self.bind,allowed_reports=set())
    def test_receipt_cannot_be_overwritten(self):
        commit_preaccess(self.root,self.bind,allowed_reports={'T1'})
        with self.assertRaises(FileExistsError):commit_preaccess(self.root,self.bind,allowed_reports={'T1'})

if __name__=='__main__':unittest.main()
