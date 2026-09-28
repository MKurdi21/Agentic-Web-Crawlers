import csv,json,pathlib,hashlib,shutil
from collections import Counter,defaultdict
R=pathlib.Path(__file__).resolve().parent
M=json.loads((R/'CALIBRATION_METRICS.json').read_text(encoding='utf-8'))
records=[]
for p in sorted((R/'calibration_records/sanitized').glob('C*.json')):records.append(json.loads(p.read_text(encoding='utf-8')))

def write(name,text):(R/name).write_text(text.strip()+"\n",encoding='utf-8')

write('UNEXPECTED_FILE_RESOLUTION.md',r'''# Unexpected-file correction

**OBSERVED.** The original Phase 2 residue `analysis/integration_design/shadow/private_source_material/raw/staging_4c7a64d312574b388369b65d14dbfe1f.tmp` remains byte-identical: 36,772 bytes, SHA-256 `63ca4afd25dbd54113e53d633cc578d2ea01f19aef74fd8820bf0073856a1e80`. It matches the historical ACE summary but is neither a valid content-addressed blob nor an allowed control file.

The v3 reconciler classifies it `UNEXPECTED_FILE` with reason `ABANDONED_STAGING_RESIDUE`; Phase 2 is preserved rather than repaired. V3 permits only its bound metadata control file, content-addressed blobs, and active temporary files under `.staging/<run_id>/<submission_id>/`. Root-level `staging_*.tmp` files and unmatched staging files fail closed.

The mandatory valid/control/unexpected/missing/corrupt/orphan scenarios pass. A clean v3 store requires `MISSING_REFERENCED_BLOB == 0`, `HASH_MISMATCH == 0`, and `UNEXPECTED_FILE == 0`. Orphans stay visible and policy-controlled.''')

write('CONTROLLER_V3_CHANGELOG.md',r'''# Controller v3 changelog

- Added database-bound `artifact_store_id`, root binding, and exact metadata-control validation.
- Retained six disjoint classifications: `VALID_REFERENCED_BLOB`, `EXPECTED_CONTROL_FILE`, `ORPHAN_BLOB`, `MISSING_REFERENCED_BLOB`, `HASH_MISMATCH`, and `UNEXPECTED_FILE`.
- Stages publication on the artifact filesystem under `.staging/<run_id>/<submission_id>/candidate.tmp`; flushes, closes, hashes, publishes without overwrite, and registers only the final immutable path.
- Existing hash-addressed bytes are independently rehashed before reuse; conflicting bytes fail with `BLOB_INTEGRITY` and are never overwritten.
- Root-level or unmatched staging residue fails reconciliation. Crash tests prove fail-closed detection before synthetic-only cleanup.
- Reconciliation emits database/store identity, roots, entry classifications, failure reasons, and a scan fingerprint.
- Added eight focused v3 store tests while preserving all inherited safety semantics. Final suite: 58/58 pass; Phase 2 reported 50/50.

No live controller, script, skill, checkpoint, or database was modified.''')

write('CALIBRATION_RESULTS.md',f'''# Phase 3 calibration results

## Denominators

The development set contains **12 top-level categories**, **13 concrete calibration units**, **15 active report identities**, and **16 physical source observations**, including one additional exact duplicate observation. These are separate denominators.

## Measured calibration output

- 660/660 report-field slots received an explicit status.
- 143 source-located sanitized evidence items were produced: 142 critical and 1 noncritical.
- All 143 created items received a separate source-grounded coordinator pass labeled `NON_INDEPENDENT_SECOND_PASS`; zero received independent-model or human verification.
- 143 slots were `CORRECT_COMPLETE`, 487 were explicitly `NOT_EXTRACTED`, and 30 were `NOT_APPLICABLE`.
- All created items use source-hash-bound `PAGE` locators. Other locator types remain technically tested by the controller suite but scientifically unencountered or uncalibrated here.

This bounded result exposes a major operational constraint: the frozen 44-field catalog is substantially broader than the evidence extracted in this run. The missing slots are visible rather than imputed. Consequently, this exercise supports schema and workflow development but does not establish scientific completeness.

## Version and contribution findings

**Mind the Web:** recommend `SAME_CONTRIBUTION_VERSION`, pending trusted-human adjudication. The 13-page and 17-page reports are separate evidence-bearing versions. The inspected results differ: approximately 1,500 versus 2,000 candidates, about 300 versus 400 SFT examples, 61% versus 64% SFT, and 82% versus 85% SFT-plus-DPO. Results must remain version-specific.

**AGENTVIGIL:** recommend `SAME_CONTRIBUTION_VERSION`, pending trusted-human adjudication. Principal Tables 1–3 align in the inspected pair, while the arXiv version adds explicit limitations concerning cost and weak Claude transfer. Separate report identity and version-specific evidence must be retained.

## Material calibration findings

- Historical summary presence is useful for discovery, but no legacy/v2 artifact becomes accepted or source-verified through import.
- Retrieval Barrier remains a partial historical source review; ToolHijacker remains extraction-only historical evidence.
- The crawler-trap paper defers classifier implementation and operational testing; its title must not be interpreted as measured deployed-classifier accuracy.
- Sanitized records represented the selected propositions without a schema-expressiveness failure, but 487 unextracted slots prevent a broad automation claim.
- The untouched Phase 4 holdout remained uninspected scientifically and has zero contamination events.

No live state changed: `source_verified = 0`, `promoted = 0`.''')

write('CALIBRATION_LIMITATIONS.md',r'''# Calibration limitations

Phase 3 is a **development and calibration exercise**. The 12 top-level categories, 13 concrete units, 15 active reports, and 16 physical observations are deliberately selected methodological probes. They are not statistically representative of all 112 reports.

The methodology was allowed to change in response to this development set. Therefore these results are not independent validation, production accuracy, generalization performance, or corpus-wide scientific validation. Phase 4 reserves an untouched six-report challenge set for post-calibration testing. Even a successful Phase 4 holdout would not establish full-corpus accuracy.

Only 143 of 660 field slots received a source-located value; 487 are explicitly `NOT_EXTRACTED` and 30 are `NOT_APPLICABLE`. Numeric claims outside the selected propositions were not exhaustively enumerated. Only PAGE locators were encountered in sanitized scientific records; the remaining locator variants have synthetic controller tests but no scientific calibration result here.

Independent subagents became unavailable during the run. Every selected item received a distinct source-grounded second pass by the coordinator, labeled `NON_INDEPENDENT_SECOND_PASS`. This is neither independent duplicate extraction nor trusted-human approval. Independent model agreement, if later obtained, would still not be human scientific approval.

No production human identity or authorization channel exists. `TRUSTED_HUMAN_APPROVAL` remains unavailable and production transitions that require it fail closed. The report/version dispositions are recommendations only.

The SQLite and artifact tests demonstrate internal behavior under the tested filesystem and failure injections. They do not prove durability against arbitrary power loss, filesystem/controller defects, Google Drive synchronization, or distributed writers.''')

# Field automation matrix.
counts=defaultdict(Counter)
for report in records:
 for f in report['fields']:counts[f['stable_field_id']][f['quality']]+=1
with (R/'FIELD_AUTOMATION_MATRIX.csv').open('w',encoding='utf-8',newline='') as fh:
 w=csv.DictWriter(fh,fieldnames=['stable_field_id','report_slots','extracted','not_extracted','not_applicable','recommended_handling','reason']);w.writeheader()
 for fid in sorted(counts):
  c=counts[fid];ex=c['CORRECT_COMPLETE'];handling='AUTO_EXTRACT_VERIFY' if ex>=12 else 'HUMAN_REVIEW_REQUIRED' if ex else 'NOT_CURRENTLY_RELIABLE'
  w.writerow({'stable_field_id':fid,'report_slots':15,'extracted':ex,'not_extracted':c['NOT_EXTRACTED'],'not_applicable':c['NOT_APPLICABLE'],'recommended_handling':handling,'reason':'Phase 3 development-set coverage; critical fields still require configured review policy.'})

with (R/'EXISTING_ARTIFACT_REUSE_MATRIX.csv').open('w',encoding='utf-8',newline='') as fh:
 fields=['paper_id','calibration_unit_id','existing_processing_state','artifact_scope','reuse_class','source_verification_effect','notes'];w=csv.DictWriter(fh,fieldnames=fields);w.writeheader()
 cases={x['paper_id']:x for x in csv.DictReader((R/'CALIBRATION_CASES.csv').open(encoding='utf-8'))}
 for report in records:
  c=cases[report['paper_id']];state=c['existing_processing_state'];reuse='TARGETED_VERIFICATION_REUSABLE' if state in ('SOURCE_REVIEW_PARTIAL','STRUCTURALLY_VALID') else 'AUTO_PARSE_CANDIDATE' if c['existing_artifacts'] else 'RAW_IMPORT_ONLY'
  w.writerow({'paper_id':report['paper_id'],'calibration_unit_id':report['calibration_unit_id'],'existing_processing_state':state,'artifact_scope':c['existing_artifacts'] or 'NONE','reuse_class':reuse,'source_verification_effect':'NONE','notes':'Reuse requires exact source/artifact hashes and field-level verification; import never promotes.'})

write('VERIFICATION_THRESHOLD_STUDY.md',r'''# Verification-threshold study

## Provisional recommendation

`SOURCE_VERIFIED` should require exact source identity; completed review of all synthesis-critical identity, method, quantitative, security-assumption, limitation, contradiction, and negative-result fields; source-bound locators; protocol and artifact pins; resolved material disagreements; and `TRUSTED_HUMAN_APPROVAL`.

`ACCEPTED_STRUCTURED_EVIDENCE` should require five-layer validation, exact source/protocol pins, an accepted immutable artifact, and the review level assigned to each field's consequence. Noncritical unknowns may remain only when excluded from dependent claims and denominators.

Phase 3 created 142 critical items and one lower-risk item. All received a non-independent second pass. This calibrates mechanics but does not satisfy the proposed human threshold. The automation matrix is intentionally conservative because 487 field slots were not extracted.

The owner must approve production thresholds and configure a real authorization channel. Until then, trusted-human-gated transitions are unavailable.''')

write('RESEARCH_OBJECT_ADJUDICATION_PACKET.md',r'''# Research-object adjudication packet

| Pair | Evidence-based recommendation | Confidence | Production status |
|---|---|---|---|
| Mind the Web reports | `SAME_CONTRIBUTION_VERSION` | Moderate | `UNRESOLVED`; human adjudication required |
| AGENTVIGIL reports | `SAME_CONTRIBUTION_VERSION` | Moderate | `UNRESOLVED`; human adjudication required |

Mind the Web versions differ materially in candidate/training counts and reported SFT/DPO results; retain separate report identities, artifacts, locators, and version-specific claims. AGENTVIGIL shares core tables in the inspected versions, while limitation coverage differs. A research object may link reports without merging their evidence.

No title similarity rule or model recommendation may create a confirmed production object. The designated human authority must record reviewer identity, authority, reviewed source/artifact hashes, policy hash, decision, rationale hash, and supersession history.''')

write('SKILL_CALIBRATION_REPORT.md',r'''# Inactive skill calibration

The five-skill decomposition remains a useful target: compatibility coordination; paper evidence processing; verification/adjudication; taxonomy/synthesis; and gap/RQ methodology. All five copied inactive skills pass the official `quick_validate.py` structural validator.

Static responsibility review found coherent primary boundaries. Paper processing owns extraction; verification owns independent checking and adjudication records; taxonomy/synthesis owns cross-paper coding; gap/RQ owns candidate generation and traceability; compatibility coordination owns migration and state crosswalks. No merge or split is justified by the limited Phase 3 evidence.

Holdout IDs are supplied through an external denylist rather than embedded in reusable skill text. No skill was installed or activated. Model trigger precision and context-cost performance were not independently evaluated because additional agent execution was unavailable; this remains a Phase 4 entry check. A skill or model can recommend a decision but cannot satisfy `TRUSTED_HUMAN_APPROVAL`.''')

unknowns=json.loads((R.parent/'workspace_audit/UNRESOLVED_REGISTER.json').read_text(encoding='utf-8'))
unknown_lines='\n'.join(f"- **{u['id']} — {u['unknown']}**: {u['migration_effect']}." for u in unknowns)
write('POLICY_DECISION_PACKET.md',f'''# Owner policy decision packet

No option below is approved by Phase 3. Recommended defaults support rehearsal only.

| Decision | Recommended rehearsal default | Live-deployment blocker? |
|---|---|---|
| Production DB/artifact location | Local non-synced authority, controlled verified exports | Yes |
| Backup/recovery owner | Named operator with restore drills | Yes |
| Trusted-human identities/channel | Fail closed until authenticated mechanism exists | Yes |
| Verification thresholds | Use the provisional risk-tiered threshold study | Yes |
| Research-object authority | Named human adjudicator | Yes for contribution synthesis |
| Inclusion/synthesis eligibility | Separate knowledge-base inclusion from synthesis eligibility | Yes |
| Partial synthesis | Tiered, denominator-explicit, verified-subset only | Yes |
| Taxonomy governance | Versioned multi-axial taxonomy with human change authority | Yes |
| Gap scoring | Disabled | No for rehearsal |
| External search | Disabled | No for rehearsal |
| Retention/deletion | Preserve through Phase 4; quarantine unexplained orphans | Long-term decision required |

## Carried audit unknowns

{unknown_lines}

The owner should record decisions in a signed/versioned configuration. Phase 3 does not fabricate approval identities or convert recommendations into policy.''')

write('PHASE4_MIGRATION_REHEARSAL_PLAN.md',r'''# Phase 4 non-destructive validation and migration rehearsal

## Entry conditions

Use the frozen v3 schema, semantic validators, locator model, automation matrix, verification protocol/threshold proposal, inactive skills, and research-object rules. Preserve the six-report holdout hash and deny tuning access until Lane A begins. Configure no live authority.

## Lane A — untouched workflow-validation holdout

Run the frozen methodology once on the untouched holdout. Measure structured extraction quality, critical-field correctness, locator performance, verification behavior, schema expressiveness, automation-policy behavior, and unexpected failures. Keep report-, field-, and evidence-item denominators explicit. Do not tune during this lane.

If a serious defect requires change, version the methodology, reclassify the original holdout as development evidence, select and freeze a new untouched set using an approved protocol, and repeat only if independent validation is still required. Never optimize repeatedly against the same holdout while calling it independent.

## Lane B — migration rehearsal

`preservation snapshot → fresh shadow import → independent equivalence validation → policy-configured candidate → representative evidence migration → backup → independent restore → rollback simulation → cutover simulation`

Run Lane B under a new non-authoritative boundary. Recheck SQLite configuration, `integrity_check`, `foreign_key_check`, artifact-store closure, backup fingerprints, exact rollback state, and package isolation. Report Lane A and Lane B separately. Passing rehearsal cannot erase a failed workflow-validation result.

Phase 4 remains non-destructive. It cannot migrate live authority, install skills, promote papers, or authorize production processing.''')

write('DEPLOYMENT_READINESS.md',r'''# Deployment readiness

## Overall result: `CONDITIONAL_GO_TO_PHASE_4_REHEARSAL`

This result authorizes no deployment. It indicates that the v3 candidate may enter an independently controlled, non-destructive Phase 4 holdout validation and migration rehearsal.

| Dimension | Result | Evidence / condition |
|---|---|---|
| Preservation and boundary | PASS | Final protected-hash comparison and package validator |
| Controller regression | PASS | 58/58 tests; inherited safety semantics retained |
| Database integrity | PASS | Both SQLite checks pass after import, reimport, and restored backup |
| Artifact-store integrity | PASS | Missing, mismatch, and unexpected failure scenarios pass; clean stores gate correctly |
| Migration equivalence | PASS | 117 observations, 112 reports/sources, five duplicate extras, zero false promotions |
| Calibration protocol | CONDITIONAL_PASS | 660 slots classified; only 143 extracted and verified by non-independent second pass |
| Holdout protection | PASS | Six reports frozen before science; zero contamination events |
| Human trust/governance | BLOCKED for deployment | No trusted-human authentication channel; fail closed |
| Independent scientific validation | BLOCKED for deployment | Reserved for Phase 4; Phase 3 is development evidence |
| Package isolation | PASS | Exact allowlist plus independent archive inspection |

Live deployment is blocked by owner policies, trusted-human configuration, untouched-holdout validation, and the final non-destructive rehearsal. `GO_TO_LIVE_DEPLOYMENT` is unavailable in Phase 3.''')

write('EXECUTIVE_PHASE3.md',r'''# Phase 3 executive handoff

Phase 3 produced a tested migration candidate without changing live authority. The controller now detects unexpected store files fail closed and stages temporary publications beneath structured `.staging` paths. The final technical suite passes 58/58 tests. First and second shadow imports reconcile 117 PDF observations to 112 source/report identities, five duplicate copies, 174 historical artifact registrations, two unresolved relationships, 13 historical unknowns, and zero accepted, source-verified, or promoted records. The restored backup passes both SQLite checks and verifies all 157 unique referenced artifact hashes.

Scientific work was bounded development calibration: 12 categories, 13 units, 15 reports, and 16 physical observations. All 660 field slots were classified; 143 source-located propositions were created and rechecked, while 487 remained explicitly unextracted and 30 not applicable. The recheck was a `NON_INDEPENDENT_SECOND_PASS`, not independent or human review.

Six holdout reports were frozen before calibration and remained untouched. Readiness is `CONDITIONAL_GO_TO_PHASE_4_REHEARSAL`; no live deployment, migration, skill installation, checkpoint update, paper promotion, or bulk generation occurred.''')

# Copy packageable machine reports; raw runtime remains excluded.
(R/'test_results').mkdir(exist_ok=True)
for src,dst in [
 (R/'candidate_v3/test_results/UNIT_INTEGRATION_RESULTS.json',R/'test_results/UNIT_INTEGRATION_RESULTS.json'),
 (R/'candidate_v3/test_results/COMPATIBILITY_EXPORT.json',R/'test_results/COMPATIBILITY_EXPORT.json'),
 (R/'candidate_v3/test_results/BACKUP_REPORT.json',R/'test_results/BACKUP_REPORT.json')]:
 shutil.copyfile(src,dst)

# Fingerprints for required scientific interfaces.
names=['CALIBRATION_PROTOCOL.md','FIELD_CATALOG.json','HOLDOUT_SELECTION_PROTOCOL.md','PHASE4_VALIDATION_HOLDOUT.csv','HOLDOUT_CONTAMINATION_LOG.json','VERIFICATION_SAMPLE_MANIFEST.json','CALIBRATION_METRICS.json','DEPLOYMENT_READINESS.md']
fps=[]
for n in names:
 p=R/n;fps.append({'path':n,'size':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(R/'PHASE3_FINGERPRINTS.json').write_text(json.dumps({'candidate_name':'litrev-hardened-candidate-v3','candidate_version':'3.0.0-calibration.1','parent_phase2_sha256':'8b63bb35d632496bd98303c6878d9030941538180cf47ca5569ba1448fa54b76','artifacts':fps},indent=2)+"\n",encoding='utf-8')
