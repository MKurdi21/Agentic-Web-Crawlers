"""Install a validated Phase 4BE-C checkpoint pair after all Stage A gates pass."""
import hashlib
import json
import os
import pathlib
import shutil

here=pathlib.Path(__file__).resolve().parent
state=here.parent
def read(name): return json.loads((here/name).read_text(encoding='utf-8-sig'))
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1048576),b''): h.update(block)
    return h.hexdigest()
def write(name,obj): (here/name).write_text(json.dumps(obj,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf-8')
diag=json.loads((state/'phase4be_freeze_repair_and_validation'/'RECOVERY_LATEST_USAGE_BLOCKED_DIAGNOSTIC.json').read_text(encoding='utf-8'))
snap=read('DRIFTED_CHECKPOINT_FORENSIC_SNAPSHOT.json')
tests=read('SCANNER_REGRESSION_TEST_RESULTS.json')
repro=read('CURRENT_GENERATOR_REPRODUCTION.json')
account=read('CORPUS_ACCOUNTING_RECONCILIATION.json')
audit=read('B02_B08_ACCESS_AUDIT.json')
review=read('INDEPENDENT_CHECKPOINT_REVIEW.json')
comparison=read('CHECKPOINT_CANDIDATE_COMPARISON.json')
change=read('CHECKPOINT_SCANNER_CHANGE_RECEIPT.json')
source=state.parent/'scripts'/'summary_state.py'
pairs=[('analysis/CHECKPOINT.md',state/'CHECKPOINT.md',here/'candidate'/'CHECKPOINT.md',here/'forensic'/'DRIFTED_CHECKPOINT.md'),
       ('analysis/checkpoint.json',state/'checkpoint.json',here/'candidate'/'checkpoint.json',here/'forensic'/'drifted_checkpoint.json')]
checks={
 'drifted_live_hashes_match_diagnostic':all(sha(live)==next(x['current_sha256'] for x in diag['protected_drift'] if x['path']==name) for name,live,_,_ in pairs),
 'forensic_copies_match_drift':all(sha(copy)==sha(live) for _,live,_,copy in pairs),
 'candidate_hashes_match_reviewed_comparison':all(sha(candidate)==comparison['candidate_checkpoint_hashes'][name] for name,_,candidate,_ in pairs),
 'generator_hash_matches_receipt':sha(source)==change['new_sha256'],
 'generator_old_hash_matches_forensic_record':change['old_sha256']=='30eab772c1914c3f03538d10a27e224580a2dbf821e8d8cdc041b7a5693896c2',
 'scanner_tests_pass':tests['verdict']=='PASS' and all(tests['tests'].values()),
 'historical_reproduction_pass':repro['semantic_json_equal_ignoring_issue_order'],
 'accounting_pass':all(account[k] for k in ('canonical_minus_tracked_equals_unmapped','total_equals_canonical_plus_duplicates','all_tracked_sources_exist_and_match','all_duplicate_hashes_match')),
 'holdouts_untouched':all(x=='UNTOUCHED_CONFIRMED' for x in audit['states'].values()),
 'independent_review_no_blocker':review['verdict'] in ('PASS','PASS_WITH_LIMITATIONS') and not review['blocking_issues'],
 'scientific_state_unchanged':all(comparison[k] for k in ('scientific_paper_records_equal','status_counts_equal','duplicate_records_equal','prompt_hash_equal')),
 'candidate_expected_counts':tests['candidate_counts']['canonical_pdf_count']==112 and tests['candidate_counts']['total_pdf_count']==117 and tests['candidate_counts']['counts']=={'structural_pass':37,'pending':75},
 'candidate_no_scientific_promotion':not any(k in tests['candidate_counts']['counts'] for k in ('source_verified','promoted')),
}
write('PRE_INSTALL_ACCEPTANCE_GATE.json',{'verdict':'PASS' if all(checks.values()) else 'FAIL','checks':checks})
if not all(checks.values()): raise RuntimeError('Stage A acceptance gate failed; live checkpoint files untouched')
temps=[]
try:
    for _,live,candidate,_ in pairs:
        tmp=live.with_name(live.name+'.phase4bec.tmp')
        shutil.copyfile(candidate,tmp)
        if sha(tmp)!=sha(candidate): raise RuntimeError('Candidate staging hash mismatch')
        temps.append(tmp)
    for (_,live,_,_),tmp in zip(pairs,temps): os.replace(tmp,live)
except Exception:
    for _,live,_,copy in pairs:
        if sha(live)!=sha(copy):
            fallback=live.with_name(live.name+'.phase4bec.rollback.tmp')
            shutil.copyfile(copy,fallback)
            os.replace(fallback,live)
    for tmp in temps:
        if tmp.exists(): tmp.unlink()
    raise
installed={name:sha(live) for name,live,_,_ in pairs}
assert all(installed[name]==sha(candidate) for name,_,candidate,_ in pairs)
candidate_json=json.loads((here/'candidate'/'checkpoint.json').read_text(encoding='utf-8'))
installed_json=json.loads((state/'checkpoint.json').read_text(encoding='utf-8'))
assert candidate_json==installed_json
assert candidate_json['updated_at'] in (state/'CHECKPOINT.md').read_text(encoding='utf-8')
receipt={
 'verdict':'CHECKPOINT_RECONCILED_READY_TO_RESUME_PHASE4BE',
 'original_phase4be_baseline_hashes':comparison['original_phase4be_baseline_checkpoint_hashes'],
 'drifted_hashes':comparison['drifted_checkpoint_hashes'],
 'forensic_copy_hashes':{name:sha(copy) for name,_,_,copy in pairs},
 'generator_old_sha256':change['old_sha256'],'generator_new_sha256':change['new_sha256'],
 'candidate_hashes':comparison['candidate_checkpoint_hashes'],'installed_corrected_hashes':installed,
 'corpus_counts_before':{'canonical':account['scanner_canonical_count'],'total':account['scanner_total_pdf_count'],'duplicates':account['archived_duplicate_count']},
 'corpus_counts_after':{'canonical':candidate_json['canonical_pdf_count'],'total':candidate_json['total_pdf_count'],'duplicates':len(candidate_json['duplicates'])},
 'tracked_paper_count':len(candidate_json['papers']),'excluded_operational_pdf_count_at_drift':account['unmapped_operational_count'],
 'excluded_later_operational_pdf_count':read('POST_CHECKPOINT_PDF_DELTA.json')['count'],
 'legitimate_corpus_changes':[],'B02_B08_state':audit['states'],
 'source_verified':candidate_json['counts'].get('source_verified',0),'promoted':candidate_json['counts'].get('promoted',0),
 'writer_status':'WRITER_IDENTITY_UNKNOWN_CAUSAL_GENERATOR_REPRODUCED',
 'independent_review':review['verdict'],
 'install_method':'candidate files staged and hash-checked; each live path atomically replaced; pair equality verified after both replacements',
}
write('CHECKPOINT_RECONCILIATION_RECEIPT.json',receipt)
print(json.dumps({'verdict':receipt['verdict'],'installed_hashes':installed}))
