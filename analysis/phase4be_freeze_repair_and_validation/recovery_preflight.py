"""Recovery observation only. No candidate mutation, source parsing, or live refresh."""
import sys, os, json, hashlib, importlib, shutil
from pathlib import Path
sys.dont_write_bytecode=True
R=Path.cwd(); O=R/'analysis/phase4be_freeze_repair_and_validation'
sys.path.insert(0,str(R/'analysis/phase4bc_supplement/recovery_protocol'))
import engine as e
def h(p):return e.filehash(p)
def read(p):return e.read(p)
def agg(x):return e.digest(e.canonical(x))
def main():
    original=[p for p in sorted(O.rglob('*')) if p.is_file()]
    inventory=[]
    for p in original:
        rel=p.relative_to(O).as_posix()
        synthetic=rel.startswith('NEVER_PACKAGE/')
        inventory.append({'path':rel,'size':p.stat().st_size,'sha256':h(p),'authority':'SYNTHETIC_DIAGNOSTIC_ONLY' if synthetic else 'UNRECEIPTED_PREPARATION_OBSERVATION_OR_DRAFT','replay_classification':'MUST_NOT_REPLAY' if synthetic else 'REQUIRES_CLEAN_RESTART','preservation':'RETAIN_IN_PLACE_LOGICAL_QUARANTINE_NO_PROMOTION'})
    protected=read(O/'PROTECTED_BASELINE_EXTENDED.json')['files']; drift=[]
    for x in protected:
        p=R/x['path']
        if not p.is_file() or p.stat().st_size!=int(x['size']) or h(p)!=x['sha256']:drift.append(x['path'])
    pins=read(O/'PARENT_EXTERNAL_PINS.json')['files']; failures=[x['path'] for x in pins if not Path(x['path']).is_file() or h(x['path'])!=x['sha256']]
    method=read(R/'analysis/phase4br_remediation/REMEDIATED_WORKFLOW_CONFIGURATION.json');method.pop('methodology_sha256');method.pop('frozen_at')
    ctx=read(R/'analysis/phase4bc_context_isolation/CONTEXT_PACKET_ARCHITECTURE_CONFIGURATION.json');ctx.pop('context_packet_architecture_sha256')
    rec=read(R/'analysis/phase4bc_supplement/RECOVERY_IMPLEMENTATION_MANIFEST.json')
    actual_rec=[{**x,'sha256':h(R/'analysis/phase4bc_supplement'/x['path']),'size':(R/'analysis/phase4bc_supplement'/x['path']).stat().st_size} for x in rec['files']]
    sys.path.insert(0,str(R/'analysis/phase4bc_path_containment/continuity_adapter'))
    import adapter
    cp=adapter.code_pins()
    sys.path.insert(0,str(R/'analysis/phase4bd_real_source_continuity/integration_layer'))
    import bridge
    fingerprints={'methodology':agg(method),'context':agg(ctx),'path':cp['path_containment'],'recovery':agg(actual_rec),'continuity':cp['immutable_code'],'real_source_continuity':bridge.codehash()}
    expected=['ad691060099fff81a3e75de6d4ffdfeb4a8906e006dbfbeefc80a6c601f1d07f','63927844eaac94765a7a804ab128076a88cad6eac2f534b715b08b17c4e21606','41fa409998ec492286c81e01efb8484a4805074f97093ae795b0c11911ce43dd','5f5adf341fac45c68cb23d6e97714ec7324625ca1ee9b3bfa6b8fbe5ab2ac0d0','3494b44b5316a9ed98bbd4d903299e48f347dccd05330b369590e382015b373e','3f33ac37175db0399cebf2447a2129d5091b42e9401b9bcc2fe67f6789e55068']
    fingerprint_pass=list(fingerprints.values())==expected
    runtime=bridge.runtime_integrity()
    routing=[h(R/'analysis/phase4b_validation_final/MODEL_ROUTING_POLICY.json'),h(O/'execution_candidate/MODEL_ROUTING_POLICY.json')]
    routing_pass=all(x=='93dd05d1aeca6ac109385a781d50e37535d72d69fa975ddda89d92f470cef00a' for x in routing)
    sources=[]
    for x in read(R/'analysis/phase4b_validation_final/HOLDOUT_PROCESSING_ORDER.json')['order']:
        sources.append({'holdout_id':x['holdout_id'],'actual_sha256':h(R/x['path']),'expected_sha256':x['source_sha256'],'state':'UNTOUCHED_RESERVED_VALIDATION_EVIDENCE','access_evidence':'NO_ACTUAL_AUTHORITY_RECORDS_SOURCE_DELIVERY_OR_RUNTIME_TREE; HASH_ONLY_NO_PARSE'})
    progress=read(O/'PREPARATION_PROGRESS.json');changes=[]
    for rel,old in progress['current_code_hashes'].items():
        now=h(O/'execution_candidate'/rel);changes.append({'path':rel,'progress_sha256':old,'current_sha256':now,'changed':old!=now})
    tracked=set(progress['current_code_hashes']);new=[p.relative_to(O/'execution_candidate').as_posix() for p in (O/'execution_candidate').rglob('*.py') if p.relative_to(O/'execution_candidate').as_posix() not in tracked]
    checkpoint=read(R/'analysis/checkpoint.json')
    missing=[n for n in ['RECOVERY_STATE.json','GENESIS.json','FREEZE_STATE.json','FREEZE_RECEIPT.json','IMMUTABLE_MANIFEST.json','PREPARATION_COMPLETE_RECEIPT.json','STAGE_A_TO_B02_TRANSITION_RECEIPT.json'] if not (O/n).exists()]
    forbidden=[p.relative_to(O).as_posix() for p in original if not p.relative_to(O).as_posix().startswith('NEVER_PACKAGE/') and (p.name in ['FREEZE_RECEIPT.json','PRE_ACCESS_RECEIPT.json','SOURCE_ACCESS_BEGAN.json'] or 'milestone_receipts' in p.parts)]
    report={'request_id':'234e55b6-5606-4654-8550-93261b4c7fe1','timestamp':e.now(),'reason':'PREEMPTED_BY_USAGE_LIMIT','reason_authority':'USER_REPORTED; no account telemetry','previous_session_identity':'UNKNOWN','new_worker_identity':'/root/phase4be_recovery_preflight','new_process_pid':os.getpid(),'new_process_start':e.process_start(os.getpid()),'quota':'UNKNOWN','tokens':'UNKNOWN','run_id':'NOT_ESTABLISHED_NO_GENESIS','current_stage':'STAGE_A','lifecycle':'PREPARATION_UNENROLLED_DRAFTS','current_holdout':None,'last_durably_committed_milestone':'NONE','last_committed_atomic_unit':'NONE','interrupted_atomic_unit':'UNCOMMITTED_DRAFT_PREPARATION; no persisted intent to identify exact unit','frontier':'NONE; PREPARATION_PROGRESS is observation not commit','recovery_verdict':'RECOVERY_BLOCKED','blockers':['MISSING_ACTUAL_RECOVERY_STATE_AND_GENESIS','UNREGISTERED_UNRECEIPTED_DRAFTS_REQUIRE_PROSPECTIVE_ENROLLMENT_NOT_RETROACTIVE_COMMIT'],'next_permitted_operation':'ESTABLISH_PROSPECTIVE_PREPARATION_RECOVERY_GENESIS_AND_ATOMIC_INTENT_UNDER_SOLE_WRITER_OS_LEASE; reconcile preserved draft hashes before completing unfinished preparation; no quiescence/freeze/source access','protected_count':len(protected),'protected_drift':drift,'external_pin_count':len(pins),'external_pin_failures':failures,'frozen_fingerprints':fingerprints,'all_six_fingerprints_pass':fingerprint_pass,'aggregate_definitions':'methodology configuration excluding methodology_sha256/frozen_at; context excluding context_packet_architecture_sha256; recovery ordered current path,size,sha256 manifest entries; containment/continuity adapter.code_pins actual bytes; real continuity bridge.code_manifest actual bytes; NFC canonical JSON','runtime_aggregate':runtime,'routing_raw_sha256':routing,'routing_pass':routing_pass,'source_hash_checks':sources,'reviews_empty':read(R/'analysis/reviews.json')=={},'checkpoint_live_counts':checkpoint.get('counts',checkpoint.get('status_counts')),'missing_actual_authority_artifacts':missing,'actual_authority_records_found':forbidden,'progress_changes':changes,'new_python_drafts':new,'inventory_count':len(inventory),'synthetic_count':sum(x['authority']=='SYNTHETIC_DIAGNOSTIC_ONLY' for x in inventory),'lane_b_runtime_exists':any((O/n).exists() for n in ['rehearsal_runtime','runtime_state','control_state','freeze_state']),'outputs_reconciled':'ALL preexisting artifacts hash inventoried and retained; diagnostic logical quarantine, no promotion','operations_replayed':[],'duplicate_effects_detected':[],'protocol_limitation':'Inherited engine available but actual Phase4BE genesis/state/intent never initialized; cannot invent receipt chain or claim formal recovery PASS. Journal below records current observations only. No scientific classification.'}
    if drift or failures or not fingerprint_pass or not routing_pass or forbidden:report['blockers'].append('INTEGRITY_OR_AUTHORITY_REQUIRES_REVIEW')
    with e.Engine(O).lock('/root/phase4be_recovery_preflight') as eng:
        e.exclusive(O/'RECOVERY_PREFLIGHT_INVENTORY.json',e.canonical({'files':inventory}))
        e.exclusive(O/'RECOVERY_PREFLIGHT.json',e.canonical(report))
        eng.event('RECOVERY_REQUEST',reason='PREEMPTED_BY_USAGE_LIMIT',request_id=report['request_id'],previous_session_identity='UNKNOWN',quota='UNKNOWN',tokens='UNKNOWN',frontier=report['frontier'],preflight_sha256=h(O/'RECOVERY_PREFLIGHT.json'))
        eng.event('RECOVERY_PREFLIGHT_FAIL',verdict='RECOVERY_BLOCKED',blockers=report['blockers'],exact_next_permitted_operation=report['next_permitted_operation'],preflight_sha256=h(O/'RECOVERY_PREFLIGHT.json'))
        eng.journal()
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
