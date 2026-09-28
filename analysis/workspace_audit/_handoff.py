from pathlib import Path
import json,csv,hashlib,collections,datetime
R=Path(__file__).resolve().parents[2];O=R/'analysis/workspace_audit'
def j(n):return json.loads((O/n).read_text(encoding='utf-8-sig'))
def rows(n):return list(csv.DictReader((O/n).open(encoding='utf-8')))
def h(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
B=j('INITIAL_BASELINE.json');S=j('AUDIT_MEASUREMENTS.json');D=j('RECONCILIATION_DETAILS.json');compat=rows('REFERENCE_ARCHITECTURE_COMPATIBILITY.csv');M=rows('PAPER_PROCESSING_MATRIX.csv');E=j('ENVIRONMENT_OBSERVATIONS.json')
text='''# Integration handoff: existing workspace and separate reference architecture

This document is for the next architect, who need not rediscover the repository. It records three separate subjects: **CURRENT_SYSTEM** (pre-audit live implementation), **REFERENCE_TARGET_ARCHITECTURE** (supplied ZIP), and **PROPOSED_INTEGRATION** (recommendations only). The audit generated reports and inventories; it installed nothing, refreshed no checkpoint, generated no paper summary, and created no database.

OBSERVED means direct file/code/hash evidence; INFERRED means interpretation of observations; UNKNOWN means insufficient evidence; CONFLICTING means sources disagree. Exact report-level records are in CORPUS_INVENTORY.csv and PAPER_PROCESSING_MATRIX.csv. References to ZIP members never establish current functionality. Relative source paths resolve from `G:\\My Drive\\Papers\\Agentic Web Crawlers`; ZIP references resolve under its `rebuild/` member root.

## A. What the workspace already has

OBSERVED: 12 numbered PDF collections, a duplicate archive, an empty manual-review location, 48 legacy Markdown summaries, 37 staged v2 drafts, one durable evidence run and two older extraction workspaces. A local corpus-analysis skill and AGENTS route reading/recovery to a saved heavy prompt and workflow. Stable manifests, baseline, empty reviews and script-derived checkpoints supply recoverable paper state. Historical docs contain substantive matrices, taxonomy-like groupings, gap/RQ prose and citation notes. No live SQLite state, generic plugin installation, structured evidence schema collection, outbox/lease engine or contribution graph was found. Evidence: TOP_LEVEL_INVENTORY.csv, ARTIFACT_INVENTORY.csv, CURRENT_STATE_MODEL.md.

## B. What work has already been performed

OBSERVED: Git history has June24 collection/documentation commits and a July22 comprehensive-summary commit; historical documents describe the 48-summary corpus. Current organized inventory contains117 source paths. The recovery baseline from September7 contains36 drafts and48 legacy finals. Retrieval Barrier subsequently adds the37th draft and only durable run log. Its ledger records partial source review, not acceptance. All current source/draft/final fingerprints agree with saved checkpoint. Evidence: RECONCILIATION_DETAILS.json:git_history; baseline.json:papers; AUDIT_MEASUREMENTS.json:baseline_changes/checkpoint_differences; Retrieval ledger.md:3-39.

## C. Current source of truth for each concept

| Concept | Current authority | Import consequence |
|---|---|---|
| Factual paper content | Exact source PDF bytes | Preserve before transformation; text is an aid |
| Routing/identity alias | analysis/manifest.csv SummaryName with Pdf/StageTarget/FinalTarget | Retain joins and aliases even if adding paper_id |
| Content identity | Actual SHA-256 of source/draft/final | Distinguish measured-now fingerprint from generation provenance |
| Progress | summary_state.py predicates over files and review declarations | Checkpoint is a dated export, not authoritative event history |
| Recovery origin | baseline.json hashes | Never reset or replace with current hashes |
| Source-review attestation | reviews.json plus matching hashes/notes existence | Empty registry means no valid recorded approvals |
| Attempt observation | evidence/<stem>/run.json and generation.log | One mutable last-run record, not immutable history |
| Historical synthesis | docs/README/report, scoped to48 summaries | Register historical scope and unknown verification |

Evidence: scripts/summary_state.py:82-156; WORKFLOW.md:38-57; README.md:3,18-38.

## D. Existing paper lifecycle

OBSERVED: organizer moves/classifies sources and writes inventory; manifest builder recovers established names from docs or slugifies filenames. Supported run_summary resolves one SummaryName, refuses an existing draft, opens an exclusive generation lock and invokes generate_summary. Generator extracts text with two libraries, ranks/render pages, composes full prompt/text/accessibility/images and makes one Codex call. It writes staged Markdown/log/run metadata and performs shallow shape checks. Runner refreshes checkpoint. Analyst separately inventories/revisits source, maintains ledger, records review declaration, checks final edits, and deliberately copies verified draft to final. No new-rubric promotion has a valid current attestation. Evidence: CURRENT_PIPELINE.md; scripts/run_summary.ps1:8-36; WORKFLOW.md:61-105.

## E. Existing state/checkpoint semantics

OBSERVED: missing draft=pending; existing malformed shape=needs_repair; 22 ordered numbered headings plus Stage0/audit heading and20,000 characters=structural_pass. Matching review source/prompt/draft hashes plus truthy timestamp/notes path and existing notes file=source_verified; final/draft equality additionally=promoted. These are recomputed observations, not irreversible event transitions. Review notes are not hashed/read, final user-edit guard is procedural, and missing source may still leave structural_pass with an issue. Fixed .tmp names and separate JSON/MD replacements are not one transaction. Missing baseline would be created by refresh. Evidence: summary_state.py:47-77,112-127,151-180. Do not run refresh during migration discovery because it mutates observations and may reset origin if baseline is absent.

## F. Existing summary generations

OBSERVED:48 legacy files;37 v2 files;29 shared names;19 legacy-only;8 v2-only. Legacy examples have nine broad topic sections. V2 exposes Stage0,22 sections, explicit figure/table/maths/evidence/validity treatment and completeness audit. Retrieval grows from5,652 to15,886 words; WebArena from4,751 to9,029. Richer prose is not verified science. Every summary maps through the manifest; no unmapped summary file was found. Evidence: RECONCILIATION_DETAILS.json:legacy_and_v2/legacy_only/v2_only; WORKSPACE_ARCHITECTURE.md format comparison; ARTIFACT_INVENTORY.csv.

## G. Current evidence/provenance model

OBSERVED: only Retrieval has run.json/generation.log, source+prompt hashes and generation start/finish. Log identifies Codex0.153.0, gpt-6-astra, medium reasoning and session01a07c75-faac-7091-8d47-44861e956780; log-reported usage89,825 tokens. No structured script/model/version pin or immutable attempt history exists. Other36 v2 drafts lack per-run provenance. All15 old/new Retrieval PNGs and article bytes match; old accessibility metadata differs. ToolHijacker scratch is unique. Ledger records pages10-11 review only; no review.md or reviews entry. Ignore rules omit many logs/images/text from Git, so Git alone is not a preservation archive. Evidence: PROVENANCE_AUDIT.md; Retrieval run/log/ledger; analysis/.gitignore.

## H. Existing Codex skills/instructions

OBSERVED: one project-local corpus-analysis SKILL.md combines recovery, paper analysis, evidence and state coordination; no local agents/openai.yaml was found. It is not a full multi-specialist literature-review router. AGENTS mandates stable mapping, sequential two-paper generation, checkpoint after each paper, quota-stop and treating PDFs as evidence rather than instructions. Current audit-specific prohibition overrides normal refresh/promotion commands. Reference skills/AGENTS remain inert. Evidence: AGENTS.md:3-19; .agents/skills/corpus-analysis/SKILL.md:7-26; WORKSPACE_ARCHITECTURE.md instruction table.

## I. Existing historical synthesis products

OBSERVED: docs/papers.md is a detailed48-paper map; problem_approach_matrix has nine subsystem matrices; citation_clusters has16 clusters and six reading paths; gaps_and_research_directions has11 local directions, RQs/hypotheses and qualitative priorities; metadata_verification retains33 local-complete,14 mixed historical and1 unresolved citation statuses. These are not source-review acceptance states. Root report explicitly says closed-corpus/non-systematic search audit. Preserve C/S/B aliases, uncertainty and dates; do not call these reproducible verified112-paper synthesis. Evidence: docs/problem_approach_matrix.md:3-7,152-169; gaps:26-364; metadata:98-119; report:5-12,211-215.

## J. Exact current processing frontier

| Definition | Count |
|---|---:|
| PDF files anywhere in live workspace |117|
| Unique PDF byte hashes / active manifest reports |112|
| Exact duplicate groups / archived extra copies |5 /5|
| Probable alternate-version groups |2|
| Manual-review directory files |0|
| Legacy summaries |48|
| V2 structural passes |37|
| Pending new-rubric drafts |75|
| Needs repair / valid source_verified / promoted |0 /0 /0|
| Durable evidence directories / old scratch directories |1 /2|
| Highest observed level: unreviewed draft |36|
| Highest observed level: draft with partial source review |1|
| Highest observed level: extraction-only newer attempt |1|
| Highest observed level: other legacy-only |18|
| No processing artifact found |56|
| Orphan summaries/evidence directories |0|
| Current run records running/failed |0|

OBSERVED: Retrieval Barrier has draft plus partial review; ToolHijacker has old final plus extraction-only newer attempt. Saved next pending names begin ToolHijacker and Unsafe LLM Search; do not automatically start generation from this handoff. Exact lists for all112 records are in PAPER_PROCESSING_MATRIX.csv and CURRENT_STATE_MODEL.md. UNKNOWN: independent contributions;112 unique byte contents could represent110 candidate groups if both probable version pairs are consolidated, but scientific-equivalence review has not occurred. No-processing-artifact is not proof never historically read.

## K. Known inconsistencies

OBSERVED: old README count/layout;96 broken PDF-link occurrences representing48 paths; five duplicate pointers and two near-version pointers using absent New paths; AGENTFUZZER stale filename for an AgentVigil preprint; historical venue conflict; uncertain recovered generation provenance. Checkpoint itself has no source/draft/final hash/status drift. Baseline36->37 is expected Retrieval progress. See STATE_DRIFT_REPORT.md D01-D12 and LINK_RECONCILIATION.csv for exact records; preserve rather than repair.

## L. Components suitable for direct import

PROPOSED_INTEGRATION: losslessly register source bytes, actual hashes, full manifest rows/aliases, both summary generations as raw artifacts, baseline fingerprints, current checkpoint observation, empty reviews, evidence/scratch hashes, and historical docs with scope/date. Import “unknown” historical model/prompt provenance honestly. Raw registration is not automatic schema acceptance or VERIFIED/DONE. Existing final files should remain untouched while drafts are reviewed.

## M. Components requiring compatibility wrappers

PROPOSED_INTEGRATION: stable SummaryName-to-new-ID crosswalk; current predicate export; old stage/final paths and user-edit guard; generator’s no-overwrite/serialized behavior; raw Markdown-to-structured-artifact registration; A/B/C/D claim categories; historical path/duplicate aliases. Existing text can seed normalization but needs object-level coverage metadata before target NORMALIZE acceptance. Evidence: current manifest, summary_state.py:112-127, WORKFLOW.md:61-105 versus target OUTPUTS in litrevctl.py:26-34.

## N. Components probably superseded only after validation

PROPOSED_INTEGRATION: fixed shared-file checkpoint writes and same-stem mutable attempt logging can be superseded by a validated coordinator/attempt model. Retain old state manager as comparison oracle through cutover. Old worker deletion/log-discard behavior and hardcoded112 manifest builder should become historical tools after compatibility validation, not be removed now. Historical synthesis remains archival, even after newer synthesis supersedes its coverage.

## O. Missing capabilities

OBSERVED in CURRENT_SYSTEM: no leased task/result packets, immutable accepted bundles, SQLite authoritative stage history, normalized claim/verification tables, adjudicated contribution graph, versioned evidence-backed taxonomy, automated candidate-specific external-gap validation or calibrated phase gate. Current prose/ledger counterparts mean many target concepts are partial rather than entirely absent. Full classifications are in REFERENCE_ARCHITECTURE_COMPATIBILITY.csv; all43 rows compare behavior.

## P. Major integration risks

INFERRED: counting related versions independently; losing historical aliases/baseline/ignored evidence; upgrading shape to verified acceptance; replacing heavy prompt with placeholder; using new hashes as historical provenance; copying generic configuration that changes resource/search policy; running a synced authoritative database without storage/writer validation; adopting reference stale-completion/schema/transaction weaknesses. Evidence: preservation invariant table and target code findings in EXISTING_VS_PROPOSED_ARCHITECTURE.md. No observed corruption was repaired and no concurrency incident was manufactured.

## Q. Recommended migration order

PROPOSED_INTEGRATION: preserve raw evidence and aliases -> reconcile report identity plus old status meanings -> design raw registration and explicit historical provenance -> strengthen reference acceptance/storage/recovery -> validate isolated import/round-trip equivalence -> calibrate retained-paper adapters/source review -> reviewed authority cutover with rollback -> compatible worker protocol. Structured evidence review, contribution adjudication and taxonomy governance then support new synthesis, candidate scoring policy, separately authorized external validation and RQs/review. The full dependency graph allows source-checking preserved drafts before cutover and avoids forcing a single linear regenerate-everything sequence (MIGRATION_PRESERVATION_MAP.md).

## R. Things the next architect MUST NOT assume

-37 drafts are37 verified papers, or48 legacy summaries satisfy the new rubric.
-Checkpoint timestamps/current hashes prove historical generation inputs.
-Empty manual-review folder means all bibliographic or scientific decisions are resolved.
-112 hashes equal112 independent studies; AGENTFUZZER filename denotes a separate contribution.
-Rendered page means visually inspected, or partial ledger means full review.
-Git tracks every unique evidence artifact.
-Generic SQLite, schemas or15 specialist skills already exist in the live project.
-Target complete is a fully validated atomic transaction across SQL and files.
-Reference config or corpus-wide master instructions override user’s sequential/quota/closed-document constraints.
-Historical local gaps establish global novelty or systematic-search completeness.

Each assumption is contradicted or unsupported by the preceding evidence; none should be silently introduced by an importer.

## S. High-confidence facts versus inference versus unknown

OBSERVED: all file counts/hashes/mappings, empty reviews, actual script predicates, reference package contents and code branches. INFERRED: two contribution-version groups, usefulness of compatibility adapters, and code-derived failure scenarios. UNKNOWN: missing original generation/review history, exact independent contribution count, historical organizer commands, sync guarantees, complete scientific correctness and future scope/scoring choices. UNRESOLVED_QUESTIONS.md lists12 unknowns with examined files, resolving evidence and migration impact. Audit completion does not require inventing those answers.

## T. Reference architecture package inspected

OBSERVED: `G:\\My Drive\\Papers\\Agentic Web Crawlers\\Codex_Literature_Review_Production_Architecture.zip`;73,356 bytes; SHA-256 `55902ec025685c1f4f2afb37672cc885222eab9952b39eb7ee48429100633e42`;121 entries/72 files under rebuild/;15 skills and matching agent metadata,14 JSON schemas, SQL schema, litrevctl.py, gap_score.py, config, workflow/provenance/QA/taxonomy/methodology references, tests and placeholder workspace. All requested content inspected directly with zipfile. No extraction of package members was needed. Reference member hashes: REFERENCE_PACKAGE_INVENTORY.csv.

## U. Which reference components are already present

OBSERVED: conceptual overlap exists in hashing/manifests/duplicates, deep-reading rubric, recovery coordination, source-review requirements, partial evidence ledger, historical matrices/gaps/RQs and source hierarchy. They are partly implemented or differently implemented. None of this establishes target schema acceptance, immutable bundle state or SQL authority. Exact live evidence is supplied per compatibility CSV row; freshly created audit helpers are not counted as historical features.

## V. Which reference components are absent

OBSERVED: leased worker_task/worker_result contracts, accepted immutable bundles, formal calibration phase and current reproducible external-gap validation have no live implementation counterpart. Several other capabilities have meaningful prose/record equivalents, so classifying them all MISSING would erase reusable work. Compatibility totals:23 PARTIALLY_IMPLEMENTED,13 SIMILAR_BUT_INCOMPATIBLE,5 MISSING,1 NEEDS_HUMAN_DECISION,1 NOT_NEEDED. These counts group functional components and schemas, not independent software services.

## W. Semantic conflicts

Identity: stable summary aliases versus P IDs and contribution IDs. Completion: whole-draft shape/hash declaration versus six DONE stages and material evidence. Authority: recomputed filesystem state versus SQL. Versioning: current prompt hash versus four pins and labels, with target code pinning incomplete. Acceptance: mutable paths versus attempted immutable copies, with target SQL/file rollback gap. Retry: explicit retained partial work/no loop versus leases/reap/attempt counts, with target late-result acceptance weakness. Verification: whole-draft attestation versus item status, while target semantic coverage is not fully enforced. Taxonomy: filename regex tags versus defined evidence-backed terms. Versions: exact duplicate archive and separate reports versus research-object grouping. Evidence: CURRENT_STATE_MODEL.md and target litrevctl.py:74-95,131-140,233-316.

Target-specific safety gaps matter: complete does not reject expired/reaped attempts or compare old packet versions with current run; required source/paper matching and human-review flags are not comprehensively enforced; filesystem copies precede SQL commit; schemas allow empty locators/verification or untyped code arrays; phase gates rely partly on decisions; synthesis registration is not a complete automated synthesis implementation. See EXISTING_VS_PROPOSED_ARCHITECTURE.md for exact lines and severity. Full target runtime tests were not executed; AST/JSON/constraint inspection is recorded in REFERENCE_STATIC_CHECKS.json.

## X. Reusable existing work

PROPOSED_INTEGRATION: preserve all117 source files,112 manifest aliases,48 legacy summaries,37 drafts,56 evidence/scratch files (21+18+17), original/current source paths and hashes, baseline/current fingerprints, the empty review state, partial review ledger, full Retrieval log, and all historical synthesis. Their values differ: sources are factual evidence; drafts are reusable unreviewed analyses; logs are generation evidence; historical prose is a bounded synthesis seed. No bulk regeneration is justified merely by new schema requirements. See ARTIFACT_INVENTORY.csv for exact paths/hashes and PROVENANCE_AUDIT.md for provenance gaps.

## Y. Unsafe direct-copy operations

Do not copy target root AGENTS/MASTER into current control; install15 skills over local corpus-analysis; replace the actual heavy prompt with template; move PDFs into generic papers/; copy schemas into live analysis; overwrite config/manifest/checkpoint; execute init/ingest/update-inputs against live workspace; initialize review.sqlite3; run gap_score --write over historical data; replace scripts before the compatibility crosswalk exists. Such operations are not this audit’s recommendations or authorization. Only a separately designed, reviewed integration may change the live system.

## Z. Recommended integration strategy

PROPOSED_INTEGRATION: adopt the reference as a design vocabulary and selectively strengthen its controller, not as an installation-ready replacement. Begin with a preservation/import layer that can round-trip all old identities, baseline distinctions and raw artifacts without changing their meaning. Keep unknown provenance explicit. Calibrate normalization/extraction/review adapters on existing representative drafts including Retrieval, ToolHijacker and a version pair. Resolve contribution grouping before denominators and taxonomy before expanded synthesis. Cut state authority over only after isolated acceptance, stale-task, source-change, review, collision and rollback checks prove compatibility; keep rollback to preserved originals. Project-specific protocol, storage, scoring and external-research decisions remain visible, not guessed. Stop here: this audit does not implement any of those steps.

## Validation and package navigation

Start with EXECUTIVE_SUMMARY.md for a short overview; use this handoff for design, the compatibility CSV for component decisions, the preservation map for invariants/dependencies, and CURRENT_STATE_MODEL/CURRENT_PIPELINE for behavioral detail. VALIDATION_REPORT.json and PRESERVATION_CHECK.json record final coverage and byte-integrity checks. The convenience archive contains only final audit reports/inventories/validation evidence, not the source PDFs, summaries, page images, raw paper text, original logs, reference ZIP, scratch extraction or helper scripts.
'''
# Normalize accidental tightly spaced Markdown bullets without altering source artifacts.
text=text.replace('\n+-','\n- ')
text='\n'.join('- '+s[1:] if s.startswith('-') and not s.startswith('- ') else s for s in text.splitlines())
(O/'INTEGRATION_HANDOFF.md').write_text(text.strip()+'\n',encoding='utf-8')
control={p.relative_to(R).as_posix():h(p) for p in [R/'AGENTS.md',R/'analysis/PROMPT.md',R/'analysis/WORKFLOW.md',R/'analysis/manifest.csv',R/'.summary_manifest.csv',R/'analysis/checkpoint.json',R/'analysis/CHECKPOINT.md',R/'analysis/baseline.json',R/'analysis/reviews.json',R/'analysis/REVIEW_TEMPLATE.md',R/'docs/paper_inventory.csv',R/'docs/near_duplicate_candidates.csv']}
scripts={p.relative_to(R).as_posix():h(p) for p in [*R.glob('*.ps1'),*R.glob('*.py'),*(R/'scripts').glob('*.py'),*(R/'scripts').glob('*.ps1')]}
skills={p.relative_to(R).as_posix():h(p) for p in (R/'.agents').rglob('*') if p.is_file()}
snapshot={'schema_version':'workspace-audit-1','audit_timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'initial_baseline_completed_at':B['timestamp'],'workspace_root':str(R),'environment':{'initial_os':B['os'],'initial_python':B['python'],'initial_powershell':'7.6.5','final_observation':E,'git_work_tree':True,'git_branch':B['branch'],'git_lfs_configuration_present':D['git_lfs_config_present'],'synchronized_filesystem':'INFERRED from G:/My Drive path; operational guarantees UNKNOWN'},'corpus_counts':{'pdf_files':117,'unique_pdf_sha256':112,'active_canonical_reports':112,'probable_version_groups':2,'independent_research_objects':None,'manual_review_files':0},'duplicate_counts':{'groups':5,'extra_archived_copies':5,'active_exact_duplicate_pairs':0},'summary_counts':{'legacy':48,'v2':37,'overlap':29,'legacy_only':19,'v2_only':8,'unmapped':0},'evidence_run_counts':{'durable':1,'scratch':2,'unmapped':0,'running_or_failed_current_records':0},'status_counts':{'pending':75,'needs_repair':0,'structural_pass':37,'source_verified':0,'promoted':0},'processing_frontier':S['frontier'],'control_file_hashes':control,'prompt_hash':D['prompt_sha256'],'script_hashes':scripts,'skill_hashes':skills,'unresolved_issue_count':12,'observed_finding_groups':12,'checkpoint_fingerprint_or_status_discrepancies':0,'reference_architecture':{'present':True,'path':str(R/'Codex_Literature_Review_Production_Architecture.zip'),'sha256':h(R/'Codex_Literature_Review_Production_Architecture.zip'),'size_bytes':73356,'archive_member_count':121,'file_count':72,'top_level_structure':['rebuild/'],'skills_count':15,'schemas_count':14,'inspected':True,'inspection_method':'zipfile direct member reads; no extraction or package execution','compatibility_summary':dict(collections.Counter(r['classification'] for r in compat))},'audit_output_file_list':[],'limitations':['Infrastructure audit, not scientific source verification','No definitive independent-contribution count','No external literature validation','Reference runtime/database tests not executed'],'boundary':'Original reference ZIP is pre-existing input; member contents excluded from live implementation counts'}
(O/'WORKSPACE_SNAPSHOT.json').write_text(json.dumps(snapshot,indent=2),encoding='utf-8')
print('Handoff and snapshot written')
