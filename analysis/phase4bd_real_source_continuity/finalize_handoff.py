"""Metadata-only handoff; readiness is gated by review and external receipt."""
from pathlib import Path
import sys,json
O=Path(__file__).resolve().parent;sys.path.insert(0,str(O/'integration_layer'))
from bridge import *
release='--release' in sys.argv
tests=read(O/'test_results/FINAL_TEST_SUMMARY.json');pres=read(O/'PRESERVATION_CHECK.json');assert pres['status']=='PASS'
assert tests['failed']==0 and tests['passed']==198 and tests['skipped']==1
review=read(O/'INDEPENDENT_REAL_SOURCE_CONTINUITY_REVIEW.json')
if release:assert review['final_artifact_review'] in ['PASS','PASS_WITH_EXPLICIT_LIMITATIONS']
classification='READY_TO_RESUME_PHASE4B_AT_B02' if release else 'REAL_SOURCE_INTEGRATION_COMPLETE_NOT_READY_TO_RESUME'
base=read(O/'PHASE4BD_BASELINE.json');fixture=read(O/'REAL_SOURCE_INTEGRATION_FIXTURE.json')
hand={'phase':'PHASE4BD','classification':classification,'edition':'PACKAGED_HANDOFF_EXTERNAL_RECEIPT_REQUIRED','latest_blocker':{'prior_reason':'FROZEN_REAL_REPORT_CONTINUITY_INTEGRATION_UNAVAILABLE','closed':release},'scientific_methodology':{'version':'phase4br-scientific-v3.0.0','sha256':METHOD,'changed':False},'context_architecture':{'version':'phase4bc-context-v1.0.0','sha256':base['frozen_pins']['context_architecture']},'path_containment':{'version':'phase4bc-path-containment-v1.0.0','sha256':base['frozen_pins']['path_containment']},'recovery_protocol':{'version':'phase4bc-recovery-v1.0.0','sha256':base['recovery_sha256']},'real_source_continuity':{'version':VERSION,'sha256':codehash(),'development_source_id':fixture['report_id'],'development_source':'B01 AgentDojo, already consumed','real_source_transport_exercised':True,'packet_acknowledgement_passed':True,'pre_access_receipt_passed':True,'source_access_event_passed':True,'consumption_transition_passed':True,'consumption_irreversible':True,'source_delivery_after_commit_only':True,'fresh_session_recovery_passed':True,'post_source_recovery_passed':True,'duplicate_recovery_idempotent':True,'context_firewall_passed':True,'scope':'Consumed-B01 real transport, minimal development field and process-crash recovery; not scientific accuracy validation or permission to access B02'},'tests':tests,'independent_review':{'mode':'READ_ONLY_MODEL_TECHNICAL_REVIEW','status':review['final_artifact_review'],'human_or_scientific_approval':False},'reserved_holdout':{'selected':7,'untouched':7,'consumed':0,'contamination_events':0,'resume_start':'B02','evidence_limit':pres['evidence_limit']},'live_state':{'source_verified':0,'promoted':0},'lane_b_executed':False,'phase4b_resumed':False,'phase5_started':False,'checkpoint_refreshed':False,'skills_installed':False,'live_migration':False,'preservation':{'status':pres['status'],'protected_files_checked':pres['protected_files_checked'],'git_outside_boundary_matches':pres['git_outside_boundary_matches']},'package':{'path':'analysis/phase4bd_real_source_continuity_package.zip','sha256':'SEE_EXTERNAL_PACKAGE_RECEIPT','receipt':'analysis/phase4bd_real_source_continuity/PACKAGE_RECEIPT.json','validation':'EXTERNAL_RECEIPT_REQUIRED'},'limitations':review['limitations'],'stop_condition':'Stop Phase4BD. Separate authorization required before opening B02, resuming Phase4B, LaneB or Phase5.'}
(O/'FINAL_HANDOFF.json').write_bytes(canonical(hand))
(O/'EXECUTIVE_PHASE4BD.md').write_text(f'''# Phase 4BD

{classification}. The final archive receipt must pass before this handoff is released.

The previously missing real-source continuity chain is exercised using consumed B01 (AgentDojo). Actual PDF bytes reach a fresh deterministic worker only after packet acknowledgement, committed pre-access, source-access event, irreversible consumption and delivery authority. A minimal source-derived field and locator are privately committed. After simulated second-unit preemption, a new coordinator process reconstructs the packet and resumes a fresh worker without conversation memory or duplicate authoritative effects.

Tests: 154 inherited and 45 new (40 core plus five post-freeze firewall acceptance); 198 passed, zero failed, one unchanged native Google Drive symlink skip. The approved platform-independent containment suite passes; the skip is neither relabeled as pass nor silently omitted. A retained real-source demonstration has one access event and one consumption receipt.

Protected files: 16,576 unchanged. B02–B08: seven untouched, zero consumed, zero recorded contamination. Live verified/promoted: 0/0. This evidence is recorded access plus hashes, not an OS-wide audit. Phase 4B and Lane B were not resumed; no migration, checkpoint refresh, promotion or skill installation occurred.

This phase tests engineering transport and recovery, not scientific correctness. Parent methodology and architecture bytes remain unchanged. Environment/OS-sandbox, dependency-root reparse, optimized-Python and startup-timeout limitations are explicit in the independent review. Any future authorization must retain the frozen pins and report-isolated packet controls.
''',encoding='utf-8')
(O/'PHASE4B_RESUME_READINESS_FINAL.md').write_text(f'''# Phase 4B resume preparation

Latest resumed Phase 4B v2 result: NO_GO.

Latest blocker: FROZEN_REAL_REPORT_CONTINUITY_INTEGRATION_UNAVAILABLE.

Phase 4BD real-source integration: PASS for the consumed-B01 development path. Parent scientific methodology: unchanged, phase4br-scientific-v3.0.0, {METHOD}.

Integration: {VERSION}, {codehash()}.

B02–B08: 7 untouched, 0 consumed, 0 recorded contamination. Live source_verified=0, promoted=0.

Final classification: {classification}. Release additionally requires the external package receipt to report PASS. Independent artifact review: {review['final_artifact_review']}.

The native Drive symlink test remains an inherited environment skip. Platform-independent path containment retains its separately approved parent policy. Broader production hardening limits are not scientific findings and remain documented.

No scientific accuracy claim is made. A deterministic PDF worker exercised one minimal development field, not the full holdout workflow. Preparation readiness neither opens B02 nor resumes Phase 4B. A future separately authorized run must establish new current-report approval, exact-byte packet acknowledgement, all frozen/environment pins, irreversible source consumption, fresh contexts, sequential gates and early stopping. Lane B and Phase 5 remain separately gated.
''',encoding='utf-8')
(O/'PACKAGE_CONVENTION.md').write_text('''# Packaging convention

The ZIP is built from a finite explicit allowlist; the independent validator owns a separate expected member set. Both must match the archive manifest. No private development sources, values, PDF files, inherited runtime copies, databases, backups, caches or prior archives are eligible.

The embedded PACKAGE_MANIFEST.json lists all release files except its own hash; membership is that list plus the manifest itself. PACKAGE_RECEIPT.json is external only and hashes the completed ZIP. The packaged FINAL_HANDOFF.json references that external receipt and deliberately contains no circular ZIP hash. After successful independent archive validation, the local external FINAL_HANDOFF.json receives the ZIP hash and an external-final edition marker. Its bytes therefore differ from the packaged handoff in that disclosed metadata only. The receipt records the packaged handoff hash. Durable completion receipts pin both editions through the package receipt and final external handoff.

Readiness is not released until the external receipt passes. Private receipt chains and source-derived values stay local under NEVER_PACKAGE; sanitized metadata proves counts/hashes without embedding originals. Content scanning is a bounded check, not universal detection of every possible paraphrase or encoding.
''',encoding='utf-8')
print(json.dumps({'classification':classification,'tests_passed':tests['passed'],'integration_sha256':codehash(),'release':release}))
