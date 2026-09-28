"""Finalize the Stage A success / Stage B blocked Phase 4BE-C handoff."""
import hashlib
import json
import pathlib
from datetime import datetime,timezone

here=pathlib.Path(__file__).resolve().parent
root=here.parents[1]
phase=root/'analysis'/'phase4be_freeze_repair_and_validation'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(name,obj):(here/name).write_text(json.dumps(obj,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1048576),b''):h.update(block)
    return h.hexdigest()
rec=read(here/'CHECKPOINT_RECONCILIATION_RECEIPT.json')
pre=read(here/'FRESH_PHASE4BE_RECOVERY_PREFLIGHT.json')
cache=read(here/'PYC_CACHE_DRIFT_DIAGNOSTIC.json')
audit=read(here/'B02_B08_ACCESS_AUDIT.json')
stage_a_review=read(here/'INDEPENDENT_CHECKPOINT_REVIEW.json')
write('INDEPENDENT_PHASE4BE_RECOVERY_REVIEW.json',{
  'verdict':'RECOVERY_BLOCKED','model_role':'GPT-6 Sol independent read-only technical review',
  'reported_by':'/root','blocking_issue':'scripts/__pycache__/summary_state.cpython-312.pyc protected drift absent from AUTHORIZED_EXTERNAL_CHANGESET.json',
  'finding':'New pyc is bound to repaired scanner by timestamp, source size, and code object, but Phase4BE-C sections 28 and 33 do not authorize adopting this extra protected drift.',
  'required_next_operation':'Explicit reconciliation authority for cache change, or exact baseline pyc restoration. Do not guess or silently adopt.',
  'source_access_authorized':False,'freeze_authorized':False,'lane_b_authorized':False})
checks={
 'stage_a_receipt_ready':rec['verdict']=='CHECKPOINT_RECONCILED_READY_TO_RESUME_PHASE4BE',
 'stage_a_independent_review_nonblocking':stage_a_review['verdict']=='PASS_WITH_LIMITATIONS',
 'installed_checkpoint_hashes_match_receipt':all(sha(root/p)==h for p,h in rec['installed_corrected_hashes'].items()),
 'scanner_hash_matches_receipt':sha(root/'scripts'/'summary_state.py')==rec['generator_new_sha256'],
 'drifted_forensic_copies_match_receipt':all(sha(here/'forensic'/('DRIFTED_CHECKPOINT.md' if p.endswith('.md') else 'drifted_checkpoint.json'))==h for p,h in rec['forensic_copy_hashes'].items()),
 'cache_byproduct_preserved':sha(here/'forensic'/'CHANGED_SUMMARY_STATE_TEST_BYPRODUCT.pyc')==cache['current_sha256']==sha(root/cache['protected_path']),
 'holdouts_untouched':all(x=='UNTOUCHED_CONFIRMED' for x in audit['states'].values()),
 'source_verified_zero':read(root/'analysis'/'checkpoint.json')['counts'].get('source_verified',0)==0,
 'promoted_zero':read(root/'analysis'/'checkpoint.json')['counts'].get('promoted',0)==0,
 'preflight_single_known_blocker':pre['blockers']==['UNEXPLAINED_PROTECTED_DRIFT'] and pre['protected_unexplained_drift']==[cache['protected_path'].replace('\\','/')],
 'no_phase4be_new_commit':read(phase/'RECOVERY_STATE.json')['last_committed_milestone']=='PREPARATION_SCIENCE_ROUTE_REPAIRS',
 'no_phase4be_source_access':read(phase/'RECOVERY_STATE.json')['source_access_started'] is False,
 'routing_policy_unchanged':sha(phase/'execution_candidate'/'MODEL_ROUTING_POLICY.json')=='93dd05d1aeca6ac109385a781d50e37535d72d69fa975ddda89d92f470cef00a',
 'no_freeze_receipt':not (phase/'FREEZE_RECEIPT.json').exists(),
 'no_lane_b_runtime':not (phase/'runtime_state').exists(),
}
# Verify durable journal chain by parsing the existing 20 records without importing recovery code.
events=[json.loads(x) for x in (phase/'RECOVERY_EVENTS.jsonl').read_text(encoding='utf-8').splitlines() if x]
checks['phase4be_journal_unchanged']=len(events)==20 and events[-1]['event_sha256']==pre['journal_tail_sha256']
write('PRESERVATION_CHECK.json',{'verdict':'BLOCKED_BY_UNRECONCILED_PROTECTED_CACHE_DRIFT' if all(checks.values()) else 'FAIL',
  'preservation_evidence_checks_pass':all(checks.values()),'checks':checks,
  'frozen_parent_fingerprints':pre['frozen_fingerprints'],'parent_pin_count_verified':pre['external_parent_pin_count'],
  'protected_count_verified':pre['protected_count'],
  'authorized_protected_changes':sorted(pre['authorized_phase4be_c_changes']),
  'authorized_protected_change_count':len(pre['authorized_phase4be_c_changes']),
  'unresolved_protected_drift':pre['protected_unexplained_drift'],
  'unresolved_protected_drift_count':len(pre['protected_unexplained_drift']),
  'holdout_source_hashes':pre['holdout_source_hash_checks']})
if not all(checks.values()):raise RuntimeError('Preservation check failed')
handoff={
 'classification':'CHECKPOINT_RECONCILED_PHASE4BE_RECOVERY_BLOCKED',
 'stage_a':'CHECKPOINT_RECONCILED_READY_TO_RESUME_PHASE4BE',
 'stage_b':'RECOVERY_BLOCKED',
 'cause_of_checkpoint_drift':'Original project-root recursive PDF scanner admitted 40 operational/private PDFs at checkpoint time.',
 'writer_status':'WRITER_IDENTITY_UNKNOWN_CAUSAL_GENERATOR_REPRODUCED',
 'drift_reproduced':True,'tracked_papers':112,'canonical_before':152,'canonical_after':112,
 'total_before':157,'total_after':117,'archived_duplicate_extra_copies':5,
 'scientific_status':{'structural_pass':37,'pending':75,'source_verified':0,'promoted':0},
 'B02_B08_state':audit['states'],'B02_scientifically_opened':False,
 'last_durable_phase4be_milestone':'PREPARATION_SCIENCE_ROUTE_REPAIRS',
 'phase4be_resumed':False,'freeze_committed':False,'lane_b_started':False,
 'stage_b_blocker':'Protected bytecode cache changed as a scanner-test byproduct; exact baseline cache bytes unavailable and its drift is not authorized by the Phase4BE-C external changeset.',
 'next_permitted_operation':'Seek explicit reconciliation authority for scripts/__pycache__/summary_state.cpython-312.pyc, or restore exact protected baseline bytes; rerun full Phase4BE recovery preflight before any preparation continuation.',
 'stage_a_review':stage_a_review['verdict'],'stage_b_review':'RECOVERY_BLOCKED',
 'reconciliation_receipt':'CHECKPOINT_RECONCILIATION_RECEIPT.json',
 'recovery_preflight':'FRESH_PHASE4BE_RECOVERY_PREFLIGHT.json',
 'preservation_check':'PRESERVATION_CHECK.json',
}
write('FINAL_HANDOFF.json',handoff)
(here/'EXECUTIVE_PHASE4BE_C.md').write_text('''# Phase 4BE-C checkpoint reconciliation\n\nFinal classification: `CHECKPOINT_RECONCILED_PHASE4BE_RECOVERY_BLOCKED`.\n\nThe original checkpoint generator recursively scanned the entire project. Its saved 152 canonical PDFs comprised 112 registered corpus sources and 40 operational/private PDF copies; five archived exact duplicates brought the total to 157. The drifted pair was preserved byte for byte, and isolated replay of the original generator over its checkpoint-era paths reproduced the recorded scientific state and issue set. The exact invoking writer remains unknown. Six more operational copies appeared after that checkpoint.\n\nThe repaired scanner uses twelve manifest-supported corpus roots and handles `99_Duplicates` separately. Its candidate and installed checkpoints report 112 canonical, five archived duplicates, 37 structural passes, 75 pending, zero source verified, zero promoted, and no issues. All 112 registered source hashes and the five duplicate hashes match. B02–B08 remain untouched in Phase 4BE authority. Independent Stage A technical review returned `PASS_WITH_LIMITATIONS`, and the live checkpoint pair was installed from validated candidates with exact readback.\n\nFresh Phase 4BE recovery preflight checked 17,245 protected baseline files and 189 external parent pins. One additional protected drift blocks continuation: `scripts/__pycache__/summary_state.cpython-312.pyc` was rewritten when the scanner regression test imported the repaired module. Its exact changed bytes are preserved under `forensic/`; the baseline bytes could not be recovered. The cache change is absent from the authorized external changeset. Independent review confirmed that this is a blocking authorization gap under the recovery rules. No Phase 4BE recovery event, preparation commit, freeze, B02 scientific access, or Lane B activity followed.\n\nNext operation requires explicit reconciliation authority for that cache artifact or exact baseline restoration, followed by a new full recovery preflight.\n''',encoding='utf-8')
print(json.dumps({'classification':handoff['classification'],
                  'preservation':'BLOCKED_BY_UNRECONCILED_PROTECTED_CACHE_DRIFT',
                  'blocker':handoff['stage_b_blocker']}))
