from pathlib import Path
import json,csv,collections,hashlib,datetime
R=Path(__file__).resolve().parents[2];O=R/'analysis/workspace_audit'
def write(n,t):(O/n).write_text(t.strip()+'\n',encoding='utf-8')
def table(h,rs):return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x).replace('|',';').replace('\n',' ') for x in r)+' |' for r in rs])
rows=[]
def add(cid,name,ref,current,paths,cl,overlap,state,artifact,provenance,complexity,risk,treatment,evidence,notes):
    rows.append(dict(component_id=cid,reference_component=name,reference_path=ref,current_equivalent=current,current_paths=paths,classification=cl,behavioral_overlap=overlap,state_compatibility=state,artifact_compatibility=artifact,provenance_compatibility=provenance,migration_complexity=complexity,data_loss_risk=risk,recommended_treatment=treatment,evidence=evidence,notes=notes))
skills=[
('literature-review-router','Route all review phases','corpus-analysis recovery routing','AGENTS.md; .agents/skills/corpus-analysis/SKILL.md','PARTIALLY_IMPLEMENTED','Recovery and paper analysis only; no synthesis-phase dispatcher','MERGE','AGENTS.md:3-10; corpus-analysis/SKILL.md:7-26','Keep audit/closed-document boundaries and two-paper sequential preference.'),
('review-state-coordinator','State, eligibility, attempts and recovery','summary_state plus wrapper','scripts/summary_state.py; scripts/run_summary.ps1','SIMILAR_BUT_INCOMPATIBLE','Filesystem-derived predicates versus authoritative stage/attempt database','WRAP_CURRENT_IMPLEMENTATION','summary_state.py:82-180; run_summary.ps1:8-36','Map observed statuses without inventing stage DONE or review events.'),
('corpus-ingestion','Hash/register/dispose source reports','Manifest and organizer inventory','analysis/manifest.csv; docs/paper_inventory.csv; organize_agentic_web_crawlers_new_preferred.py','PARTIALLY_IMPLEMENTED','Hashes, duplicates and aliases exist; no stable independent paper_id or inclusion-decision ledger','ADAPT_TO_EXISTING_SEMANTICS','manifest.csv:1-113; organizer:510-568','Generic ingest only scans papers/, chooses first hash occurrence, creates P IDs; preserve canonical preference.'),
('paper-deep-reader','Normalize and deeply summarize one source','Heavy rubric and generator','analysis/PROMPT.md; scripts/generate_summary.ps1','PARTIALLY_IMPLEMENTED','Full rubric and draft generation exist; structured summary/normalization contract absent','ADAPT_TO_EXISTING_SEMANTICS','PROMPT.md:170-814,817-1211; generate_summary.ps1:34-200','Preserve exact rubric and separate cumulative ledger requirement from single-call behavior.'),
('paper-evidence-extractor','Create source-located structured evidence','Partial ledger and summary evidence sections','analysis/REVIEW_TEMPLATE.md; analysis/evidence/retrieval_barrier_comprehensive_summary/ledger.md','PARTIALLY_IMPLEMENTED','Evidence concepts exist in prose; no normalized claim IDs or evidence JSON','ADAPT_TO_EXISTING_SEMANTICS','REVIEW_TEMPLATE.md:7-57; ledger.md:3-39','Convert only source-supported records; keep A/B/C/D distinctions and missing coverage.'),
('evidence-verifier','Independent material evidence checking','Hash-bound reviewer declaration and source-revisit procedure','analysis/WORKFLOW.md; analysis/reviews.json','PARTIALLY_IMPLEMENTED','Source revisit required; predicate checks only whole-draft hashes and notes existence','ADAPT_TO_EXISTING_SEMANTICS','WORKFLOW.md:61-80,97-100; summary_state.py:115-123','Zero valid attestations; reference item verification is not equivalent to historical approval.'),
('research-object-resolver','Link report versions to contributions','Hash duplicates and unresolved version candidates','docs/near_duplicate_candidates.csv; docs/paper_inventory.csv','PARTIALLY_IMPLEMENTED','Version hints exist, no adjudicated research objects or contribution graph','MERGE_CONCEPTS','near_duplicate_candidates.csv:2-3; CORPUS_INVENTORY.csv version_relation','Two probable groups including AgentVigil; preserve source-level records.'),
('taxonomy-thematic-coder','Evidence-backed controlled coding','Filename categories/tags and thematic prose','organize_agentic_web_crawlers_new_preferred.py; docs/problem_approach_matrix.md','SIMILAR_BUT_INCOMPATIBLE','Regex organization is not evidence-backed code assignment','MERGE_CONCEPTS','organizer:70-328; docs/problem_approach_matrix.md:3-7,9-126','Import folder/tag values as historical hints, not validated taxonomy.'),
('cross-paper-synthesizer','Build contribution-aware verified matrices','Historical 48-paper prose matrices','docs/problem_approach_matrix.md; docs/citation_clusters_and_reading_order.md','PARTIALLY_IMPLEMENTED','Human-readable synthesis exists; no reproducible verified record inputs','ADAPT_TO_EXISTING_SEMANTICS','problem_approach_matrix.md:3-7,128-169; citation_clusters:3-9','Preserve historical scope and denominators; expanded synthesis requires review.'),
('contradiction-replication-analyzer','Comparable cross-object claims and drivers','Narrative contradictions and reproducibility caveats','docs/metadata_verification.md; docs/gaps_and_research_directions.md','PARTIALLY_IMPLEMENTED','Narrative examples exist; no adjudicated machine-readable pair graph','ADAPT_TO_EXISTING_SEMANTICS','metadata_verification.md:96,119; gaps_and_research_directions.md:26-304','Separate venue metadata disputes from experimental contradiction evidence.'),
('research-gap-detector','Evidence-supported candidate generation and scores','Eleven gap directions and qualitative priority scheme','docs/gaps_and_research_directions.md','SIMILAR_BUT_INCOMPATIBLE','Gap/RQ prose exists but explicitly discourages mechanical score collapse','POSTPONE_HUMAN_DECISION','gaps_and_research_directions.md:26-364,305-324','Retain old framework; adopt generic weighted score only after project calibration.'),
('external-gap-validator','Reproducible external novelty checking','Historical external links only','docs/metadata_verification.md; agentic_ai_web_agents_literature_search_report.md','MISSING','No current documented candidate-by-candidate query/outcome workflow','POSTPONE_HUMAN_DECISION','metadata_verification.md:7-24,138; report:5-12,211-215','Future scope decision; closed-document audit does not authorize external validation execution.'),
('research-question-generator','Traceable falsifiable RQs','RQs/hypotheses in gap document','docs/gaps_and_research_directions.md','PARTIALLY_IMPLEMENTED','Existing testable proposals lack normalized RQ-gap-evidence IDs','ADAPT_TO_EXISTING_SEMANTICS','gaps_and_research_directions.md:55-60,343-353','Preserve wording and provisional novelty status.'),
('literature-review-writer','Thematic verified review prose','README, report, docs synthesis','README.md; docs/papers.md; agentic_ai_web_agents_literature_search_report.md','PARTIALLY_IMPLEMENTED','Thematic writing exists; summary-grounded 48-paper scope differs from verified evidence DB','ADAPT_TO_EXISTING_SEMANTICS','README.md:142-166; report:194-215','Historical prose is reusable source material, not new corpus-wide accepted synthesis.'),
('corpus-auditor','Coverage, provenance, compatibility and claim audit','State checks and current audit deliverables','scripts/summary_state.py; analysis/workspace_audit','PARTIALLY_IMPLEMENTED','Basic file/state checks existed; this forensic audit is newly produced, not historical implementation','ADAPT_TO_EXISTING_SEMANTICS','summary_state.py:89-149; INITIAL_BASELINE.json','Do not count newly authored audit helpers as pre-existing features.')]
for slug,purpose,current,paths,cl,overlap,treatment,ev,notes in skills:
    add('skill:'+slug,purpose,'rebuild/skills/'+slug+'/SKILL.md; rebuild/skills/'+slug+'/agents/openai.yaml',current,paths,cl,overlap,'REQUIRES_EXPLICIT_CROSSWALK','PRESERVE_RAW_AND_ADD_ADAPTER','DO_NOT_BACKFILL_UNKNOWN_PROVENANCE','HIGH' if cl in ['SIMILAR_BUT_INCOMPATIBLE','MISSING'] else 'MEDIUM','HIGH' if 'state' in slug or 'resolver' in slug or 'verif' in slug else 'MEDIUM',treatment,ev+'; ZIP!rebuild/skills/'+slug+'/SKILL.md',notes)
schema_map={
'worker_task':('No task packets','scripts/run_summary.ps1','MISSING','Sequential path arguments are not leased worker contracts','ADAPT_TO_EXISTING_SEMANTICS'),
'worker_result':('No structured worker results','scripts/generate_summary.ps1','MISSING','Draft/log/exception are not signed or token-bound result bundles','ADAPT_TO_EXISTING_SEMANTICS'),
'artifact_metadata':('Checkpoint/run hashes','analysis/checkpoint.json; analysis/evidence/retrieval_barrier_comprehensive_summary/run.json','PARTIALLY_IMPLEMENTED','New metadata must distinguish observed-now hashes from generation provenance','ADAPT_TO_EXISTING_SEMANTICS'),
'corpus_manifest':('Stable CSV manifests','analysis/manifest.csv; docs/paper_inventory.csv','SIMILAR_BUT_INCOMPATIBLE','P-number identity/disposition schema cannot replace SummaryName joins directly','WRAP_CURRENT_IMPLEMENTATION'),
'normalized_paper':('Accessibility JSON and article.txt','analysis/evidence/retrieval_barrier_comprehensive_summary','PARTIALLY_IMPLEMENTED','Retained extraction lacks schema-complete sections/visual object inventory','ADAPT_TO_EXISTING_SEMANTICS'),
'summary':('Legacy and v2 Markdown','Summaries; .summary_v2','SIMILAR_BUT_INCOMPATIBLE','Prose lacks required structured fields; do not regenerate solely for JSON shape','ADAPT_TO_EXISTING_SEMANTICS'),
'evidence':('Partial prose ledger','analysis/REVIEW_TEMPLATE.md; analysis/evidence/retrieval_barrier_comprehensive_summary/ledger.md','PARTIALLY_IMPLEMENTED','Item provenance and A/B/C/D need explicit mapping; required locator array may contain empty object','ADAPT_TO_EXISTING_SEMANTICS'),
'verification':('Whole-draft attestations','analysis/reviews.json; scripts/summary_state.py','SIMILAR_BUT_INCOMPATIBLE','No entries currently; per-item statuses and verified coverage differ','ADAPT_TO_EXISTING_SEMANTICS'),
'research_object':('Near-version pointers','docs/near_duplicate_candidates.csv','PARTIALLY_IMPLEMENTED','Bibliographic candidates cannot become resolved contributions automatically','MERGE_CONCEPTS'),
'taxonomy':('Regex categories and tags','organize_agentic_web_crawlers_new_preferred.py','SIMILAR_BUT_INCOMPATIBLE','No versioned defined terms or taxonomy governance','MERGE_CONCEPTS'),
'paper_taxonomy_coding':('Folder membership','docs/paper_inventory.csv','SIMILAR_BUT_INCOMPATIBLE','Folder/tag values are not verified item-supported codes','ADAPT_TO_EXISTING_SEMANTICS'),
'contradiction':('Narrative caveats','docs/gaps_and_research_directions.md; docs/metadata_verification.md','PARTIALLY_IMPLEMENTED','Structured comparable claim pairs need new evidence linkage','ADAPT_TO_EXISTING_SEMANTICS'),
'gap_candidate':('Gap prose and priority framework','docs/gaps_and_research_directions.md','SIMILAR_BUT_INCOMPATIBLE','Weighted 0-4 score differs from existing qualitative 1-5 framework','POSTPONE_HUMAN_DECISION'),
'research_question':('Existing RQ/hypothesis prose','docs/gaps_and_research_directions.md','PARTIALLY_IMPLEMENTED','Retain questions; add support IDs only after gap validation','ADAPT_TO_EXISTING_SEMANTICS')}
for slug,(current,paths,cl,note,tr) in schema_map.items():
    add('schema:'+slug,'Schema: '+slug,'rebuild/schemas/'+slug+'.schema.json',current,paths,cl,note,'NOT_A_DIRECT_STATE_IMPORT','REQUIRES_FIELD_AND_MEANING_MAPPING','RAW_ORIGINALS_RETAINED','MEDIUM','HIGH' if slug in ['corpus_manifest','verification','research_object','evidence'] else 'MEDIUM',tr,paths+'; ZIP!rebuild/schemas/'+slug+'.schema.json', 'Schema examined in full; parse validity is not scientific validation.')
infra=[
('sqlite','SQLite authoritative state','rebuild/db/schema.sql; rebuild/scripts/litrevctl.py','Derived JSON/CSV plus filesystem','scripts/summary_state.py','SIMILAR_BUT_INCOMPATIBLE','WAL/SQL stage state differs from file-observation predicates','REPLACE_ONLY_AFTER_MIGRATION','HIGH','HIGH','ZIP!db/schema.sql:1-3,94-149; summary_state.py:82-180','Choose non-synced database location or verified single-host arrangement before future cutover; no DB created.'),
('bundles','Immutable accepted bundles','rebuild/scripts/litrevctl.py:260-302','Mutable stage/evidence paths','scripts/generate_summary.ps1','MISSING','Target copies to unique attempt dir then commits SQL; files are not transactionally rolled back','ADAPT_TO_EXISTING_SEMANTICS','HIGH','HIGH','ZIP!litrevctl.py:289-302; generate_summary.ps1:13-31,173,202-212','Keep source snapshots and raw legacy registrations distinct from accepted stage outputs.'),
('leases','Leases, retry and stale recovery','rebuild/scripts/litrevctl.py:217-230,305-316','Exclusive wrapper file handle','scripts/run_summary.ps1','SIMILAR_BUT_INCOMPATIBLE','Serial OS lock is not a lease; target complete lacks lease-expiry/current-attempt rejection','ADAPT_TO_EXISTING_SEMANTICS','HIGH','HIGH','ZIP!litrevctl.py:260-274,305-316; run_summary.ps1:20-36','Strengthen controller before parallel adoption; preserve two-paper sequential default.'),
('pins','Semantic version and hash pinning','rebuild/scripts/litrevctl.py:60-95,347-383','Prompt hash and review source/draft hashes','analysis/baseline.json; analysis/reviews.json','PARTIALLY_IMPLEMENTED','Target four input hashes and bundle version; no actual code hash pin or all-schema pins','ADAPT_TO_EXISTING_SEMANTICS','HIGH','HIGH','ZIP!litrevctl.py:74-95,292-293,347-383; summary_state.py:115-127','Changing labels alone does not necessarily update per-paper fingerprints; source content not task-pinned.'),
('calibration','Calibration and phase gates','rebuild/MASTER_CODEX_INSTRUCTION.md; rebuild/scripts/litrevctl.py:388-410','No recorded calibration phase','analysis/WORKFLOW.md','MISSING','Target checks acceptance decision for PRODUCTION, not actual sample acceptance; enqueue/claim lack phase enforcement','ADAPT_TO_EXISTING_SEMANTICS','MEDIUM','MEDIUM','ZIP!MASTER:24-52; litrevctl.py:180-230,388-410','Calibrate adapters on retained representative papers, not blanket regeneration.'),
('gap_score','Deterministic gap scoring','rebuild/scripts/gap_score.py; rebuild/config/gap_scoring.json','Qualitative prioritization','docs/gaps_and_research_directions.md','SIMILAR_BUT_INCOMPATIBLE','Eight weighted dimensions/penalties/caps versus existing nonmechanical priorities','POSTPONE_HUMAN_DECISION','MEDIUM','MEDIUM','ZIP!gap_score.py:13-44; docs/gaps_and_research_directions.md:305-324','Numeric scoring is optional policy; script does not automatically reject filled gaps as reference prose requests.'),
('protocol','Versioned review protocol','rebuild/workspace-template/protocol/review_protocol.md','Heavy rubric and historical search limits','analysis/PROMPT.md; agentic_ai_web_agents_literature_search_report.md','PARTIALLY_IMPLEMENTED','Generic protocol has placeholders for inclusion/synthesis units; cannot claim systematic sampling','MERGE_CONCEPTS','MEDIUM','HIGH','ZIP!workspace-template/protocol/review_protocol.md:5-30; report:211-215','Project scientific scope is a future decision, preserve actual corpus history.'),
('config','Generic project configuration','rebuild/config/project.example.json; rebuild/workspace-template/config.json','Procedural batch settings','AGENTS.md; analysis/checkpoint.json','NEEDS_HUMAN_DECISION','Target max_parallel_workers4/calibration10/external true differ from current sequential2 and closed-document task','ADAPT_TO_EXISTING_SEMANTICS','MEDIUM','MEDIUM','ZIP!config/project.example.json:2-19; AGENTS.md:13-16','Controller hardcodes stages; several config fields are declarative rather than enforced.'),
('template','Generic empty workspace and placeholder prompt','rebuild/workspace-template/','Existing active corpus and exact rubric','analysis/PROMPT.md; analysis/manifest.csv','NOT_NEEDED','Scaffold for a new project would overwrite/obscure live semantics','REJECT_AS_UNNECESSARY','LOW','HIGH','ZIP!workspace-template/prompts/heavy_summary_prompt.md:1-3; PROMPT.md:1-1249','Never copy template over repository; isolated test workspace may use adapted scaffolding later.'),
('instructions','Master instructions / AGENTS / plugin manifest','rebuild/MASTER_CODEX_INSTRUCTION.md; rebuild/AGENTS.md; rebuild/.codex-plugin/plugin.json','Local instruction hierarchy','AGENTS.md; .agents/skills/corpus-analysis/SKILL.md','SIMILAR_BUT_INCOMPATIBLE','Target auto-init/full-corpus orchestration conflicts with current preserved workflow and audit boundary','MERGE_CONCEPTS','MEDIUM','HIGH','ZIP!MASTER:9-18; AGENTS.md:3-16','Target instructions are inert reference content in this audit.'),
('qa','Semantic QA gates','rebuild/references/qa-gates.md; rebuild/tests/test_static.py','Rubric, review workflow and 4 shape tests','analysis/PROMPT.md; scripts/test_summary_state.py','PARTIALLY_IMPLEMENTED','Source-check requirements overlap; both codebases enforce less than prose guarantees','ADAPT_TO_EXISTING_SEMANTICS','HIGH','HIGH','ZIP!references/qa-gates.md:3-56; test_static.py:5-12; test_summary_state.py:23-44','Need acceptance/recovery tests before adoption; target tests only schemas/skill presence.'),
('provenance','Evidence/artifact provenance graph','rebuild/references/provenance.md; rebuild/db/schema.sql:179-224','Hashes, partial ledger and log','analysis/evidence; analysis/checkpoint.json','PARTIALLY_IMPLEMENTED','Whole-artifact provenance exists only partly; item edges/verification absent','ADAPT_TO_EXISTING_SEMANTICS','HIGH','HIGH','ZIP!provenance.md:5-48; CURRENT_STATE_MODEL.md; PROVENANCE_AUDIT.md','Target SQL verification does not persist checked_locators separately; accepted JSON must be retained.'),
('synthesis_control','Corpus-stage artifact registration','rebuild/scripts/litrevctl.py:332-344','Manually maintained historical Markdown','docs; README.md','PARTIALLY_IMPLEMENTED','Target registers files but does not implement matrix/gap/RQ generation or their SQL table imports','ADAPT_TO_EXISTING_SEMANTICS','HIGH','MEDIUM','ZIP!litrevctl.py:15,332-344; docs/problem_approach_matrix.md:3-7','Do not claim fully automated synthesis from enum/table presence.'),
('methodology','Methodology source bibliography','rebuild/references/methodology-sources.md','Historical citation/metadata notes','docs/metadata_verification.md','PARTIALLY_IMPLEMENTED','Both retain sources; target bibliography is not project methodological adoption','POSTPONE_HUMAN_DECISION','LOW','LOW','ZIP!references/methodology-sources.md:1-17; metadata_verification.md:7-24','Read URLs as supplied historical claims only; no browsing or standard-compliance claim.')]
for cid,name,ref,cur,paths,cl,overlap,tr,complexity,risk,ev,note in infra:
    add('infra:'+cid,name,ref,cur,paths,cl,overlap,'REQUIRES_SEMANTIC_RECONCILIATION','PRESERVE_CURRENT_ARTIFACTS','DO_NOT_SYNTHESIZE_MISSING_HISTORY',complexity,risk,tr,ev,note)
with (O/'REFERENCE_ARCHITECTURE_COMPATIBILITY.csv').open('w',encoding='utf-8',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
counts=dict(collections.Counter(r['classification'] for r in rows))
write('EXISTING_VS_PROPOSED_ARCHITECTURE.md',f'''# Current system versus reference architecture

## Strict evidence boundary

OBSERVED: CURRENT_SYSTEM is the pre-audit live repository. REFERENCE_TARGET_ARCHITECTURE is the added ZIP; no archive member was installed, no package script executed, no database initialized. PROPOSED_INTEGRATION consists only of recommendations below. File-name resemblance is not behavioral equivalence.

Reference: `Codex_Literature_Review_Production_Architecture.zip`, 73,356 bytes, SHA-256 `55902ec025685c1f4f2afb37672cc885222eab9952b39eb7ee48429100633e42`; 121 entries including 49 directories, 72 files; root rebuild/ contains skills, schemas, db, scripts, tests, config, references, workspace-template and plugin metadata. All 15 skills, 15 agent YAML files, 14 schemas, both scripts, SQL, instructions, configuration, references, tests and template contents were read. `REFERENCE_PACKAGE_INVENTORY.csv` records member hashes and scope.

## Behavioral subsystem comparison

| Subsystem | CURRENT_SYSTEM | REFERENCE_TARGET_ARCHITECTURE | PROPOSED_INTEGRATION |
|---|---|---|---|
| State authority | Manifest routes identities; actual file hashes + structure + review predicate derive checkpoint | SQLite review_runs/paper_stage_state/tasks/artifacts are authority; snapshot is export | First preserve predicate outputs and baseline distinctions, then validate lossless adapter before authority cutover |
| Paper identity | SummaryName is practical join key; two CSV mappings; folder-based duplicate archive | P0001-style paper IDs; hash/path records; dispositions; separate research objects | Keep legacy aliases, all report hashes and paths; do not deduplicate versions as byte duplicates |
| Stages | Extraction + one summary call, then optional cumulative source review/attestation and final copy | NORMALIZE -> SUMMARIZE -> EXTRACT -> VERIFY -> RESOLVE_OBJECT -> CODE_TAXONOMY | Current pre-narrative ledger requirement must survive; do not relabel draft existence as all stages DONE |
| Artifacts | Legacy/v2 Markdown, text/PNGs/accessibility, one log/run/partial ledger | Human+structured summary, evidence+verification JSON and accepted bundles | Register raw historical artifacts first with provenance gaps; separately derive new structured records |
| Concurrency | Exclusive wrapper lock, bypassable direct scripts, shared mutable JSON/CSV | Coordinator claims/leases disjoint outboxes and imports SQL transactions | Retain sequential two-paper preference until controller acceptance/recovery gaps are addressed |
| Versioning | Current prompt/source/draft hashes; baseline and one generation log | Four run-input hashes plus version labels and stage fingerprints | Pin actual code/schema/source inputs and preserve honest unknown historical provenance |
| Taxonomy/research objects | Filename regex tags/folders, prose categories, two probable version groups | Controlled dimension IDs, evidence-linked codes, research-object membership | Import organization as hints, resolve relationships with evidence, govern new terms explicitly |
| Synthesis | 48-summary matrices, caveats, gaps, RQs and priorities in Markdown | Verified contribution-aware matrices, contradictions, gap validation/RQs/review phases | Preserve old prose with its denominator; enable reproducible synthesis only after source review |

Current evidence: `scripts/summary_state.py:82-180`, `run_summary.ps1:8-36`, `generate_summary.ps1:34-212`, `WORKFLOW.md:61-105`, `docs/problem_approach_matrix.md:3-7`, `docs/gaps_and_research_directions.md:305-324`. Target evidence: `ZIP!rebuild/db/schema.sql:12-224`, `scripts/litrevctl.py:14-34,74-95,131-140,199-302`, `references/workflow.md:11-48`, `references/taxonomy-and-synthesis.md:3-16`.

## Component coverage

The compatibility CSV has **{len(rows)} significant components**: 15 skills, 14 individual schemas and 14 infrastructure/policy components. Classification counts: `{json.dumps(counts,sort_keys=True)}`. Each CSV row includes intended responsibility, current equivalent/evidence, behavioral overlap, state/artifact/provenance compatibility, complexity, data-loss risk, treatment and notes. All classifications concern current behavior, not merely target availability.

'''+table(['Component ID','Reference responsibility','Classification','Recommendation'],[(r['component_id'],r['reference_component'],r['classification'],r['recommended_treatment']) for r in rows])+'''

## Target design versus target implementation: blockers to direct adoption

These are OBSERVED code properties and INFERRED failure implications in the reference package, not defects introduced into the live workspace. No exploit, database or migration was executed.

1. **HIGH — late/stale completion and pins.** complete checks attempt ID, token, attempt number and equality of result versions to saved packet. It does not require a live CLAIMED/RUNNING attempt, reject expired/reaped attempts, compare packet versions with current run pins, or enforce worker identity (`ZIP!rebuild/scripts/litrevctl.py:260-274`). After reaping or update-inputs, an older packet may still reach acceptance if otherwise valid. Add explicit current-attempt/stage-fingerprint/lease checks before adopting retries.
2. **HIGH — semantic acceptance is weaker than schema/hash checks.** Output paper_id and source_sha256 are not checked against task/source; complete ignores verification requires_human_review and coverage findings when overall result says SUCCEEDED (`:275-302`). Source hash is not included as a pinned task field; artifact input hashes comprise four run inputs (`:199-214,292-293`). Source edits after ingestion and cross-paper records need explicit rejection.
3. **HIGH — acceptance is not atomic across SQL and files.** Canonical directories and copied files are created before import_stage and SQL commit; exceptions leave filesystem residue. No cleanup/transaction recovery path is present (`:289-302`). Disjoint directories reduce collisions but do not make filesystem writes transactional. Duplicate output types/basenames and declared relative paths are not fully constrained (`:275-291`).
4. **HIGH — schema limits.** Evidence statement has no minLength and locators allow empty objects; verification allows zero evidence_verifications; taxonomy codes and research-object members lack item schemas. Several arrays/objects are intentionally broad. Controller schema validation uses Draft202012Validator without FormatChecker (`:98-102`). Parsed-schema constraint evidence is in `REFERENCE_STATIC_CHECKS.json`; full jsonschema runtime tests were not run because that dependency is absent in the audit runtime.
5. **HIGH — verification/phase gates are largely procedural.** VERIFY import updates statuses/statement and stores corrected_values in verification rows, but does not update evidence numerical_values or store checked_locators as SQL provenance; accepted JSON is therefore important (`:243-246`). PRODUCTION phase only requires a decision row, not completed calibration evidence; enqueue/claim do not enforce phase (`:180-230,388-410`). SYNTHESIS phase checks DONE/fingerprints, not unresolved material verification status. audit flags UNVERIFIED material as error, but unsupported/ambiguous/unreadable material only as warnings (`:425-428`).
6. **MEDIUM — incomplete version pinning/invalidation.** Fingerprints use skill_bundle_version plus selected content hashes, not actual script/skill hashes or all schemas (`:74-88`). config hash is stored but assert_inputs_unchanged checks only four inputs (`:91-95`). Version-only changes can leave stage fingerprints unchanged; update-inputs changes files before SQL commit and does not cancel all outstanding task packets (`:347-383`). Required stages are hardcoded despite config fields (`:14-34`).
7. **MEDIUM — SQL evidence replacement and scope.** EXTRACT uses globally keyed evidence_id and INSERT OR REPLACE; verification updates by evidence_id without explicit paper/run guard; object IDs likewise have global keys (`db/schema.sql:154-224`; `litrevctl.py:233-257`). Require unique scoped IDs and immutable historical artifact preservation. SQL replacement is not an append-only scientific audit trail.
8. **MEDIUM — synthesis is not a completed automation backend.** corpus-stage registration copies a file and updates stage state, with schema optional NONE; it does not import contradiction/gap/RQ tables or enforce stage-specific semantic support (`:332-344`). Presence of SQL tables and skill instructions is not an implemented generator. Tests cover schema and skill presence only (`tests/test_static.py:5-12`).
9. **MEDIUM — gap policy differs.** gap_score computes 25*weighted scores, penalties and caps 69/59/49/39, but does not automatically reject/reframe externally filled gaps as prose requests (`scripts/gap_score.py:13-44`; `references/gap-scoring.md:29-37`). Existing gap document uses a different nonmechanical priority framework; weights need project judgment, not blind adoption.
10. **MEDIUM — synchronization assumptions.** Target schema selects WAL and NORMAL (`db/schema.sql:1-3`). This audit did not establish Google Drive cross-host SQLite safety. Do not replace the current file observations with a live synced database without choosing and validating an operational location and writer ownership.

## Target policy and instruction mismatch

The reference template prompt is a three-line placeholder, not the current 1,249-line rubric. Template config defaults four workers, calibration10 and external_gap_validation=true; live instructions say two papers sequentially and stop on quota errors. Master instructions auto-initialize/ingest, while this task prohibits both. Generic agents/openai.yaml files are UI labels/default prompts rather than enforced capabilities. Methodology references list external URLs but do not establish project compliance with those methodologies. All remain inert reference material (`ZIP!rebuild/workspace-template/*`; `MASTER_CODEX_INSTRUCTION.md:9-18`; `references/methodology-sources.md:1-17`; current `AGENTS.md:13-16`).
''')
write('MIGRATION_PRESERVATION_MAP.md','''# Preservation map and migration dependencies

All treatments below are PROPOSED_INTEGRATION. No migration was performed. They follow observed current authority, retained artifact quality and target behavior; exact source evidence appears in each row and the compatibility CSV.

## Existing components

'''+table(['Current component','Treatment','Reason / evidence'],[
('117 PDFs and folder paths','PRESERVE_AS_IS','Keep all hashes and report variants; CORPUS_INVENTORY.csv; source-only content remains factual authority.'),
('Root AGENTS and corpus-analysis skill','WRAP_FOR_COMPATIBILITY','Retain rubric routing, sequential batch preference, quota stopping and review rules; AGENTS.md:3-19; SKILL.md:7-26.'),
('Heavy PROMPT.md','PRESERVE_READ_ONLY','Exact user rubric/hash is an invariant; generic placeholder must not replace it; PROVENANCE_AUDIT.md.'),
('Both manifests','IMPORT_STATE','Preserve SummaryName and all original path/target fields; manifests identical; builder depends on historical naming.'),
('checkpoint.json and CHECKPOINT.md','PRESERVE_READ_ONLY','Keep dated observations and import predicates separately; not generation provenance or permanent acceptance.'),
('baseline.json','IMPORT_STATE','Only recovery-era fingerprints; needed to detect pre-existing final edits; summary_state.py:124-127; WORKFLOW.md:102-105.'),
('reviews.json','IMPORT_STATE','Empty is a meaningful observation; no approvals may be synthesized. Preserve format for any later live additions.'),
('48 legacy summaries','PRESERVE_READ_ONLY','Existing published generation and 48-paper synthesis evidence; register raw artifacts without implying new-rubric approval.'),
('37 v2 drafts','REGENERATE_ONLY_IF_NECESSARY','Reusable drafts all pass shape but lack attestations; review/repair selectively rather than blanket paid regeneration.'),
('Durable evidence run','PRESERVE_AS_IS','Only retained full log/run plus partial ledger; review is unfinished; ledger.md:3-39.'),
('Two old scratch directories','PRESERVE_READ_ONLY','ToolHijacker extraction unique; Retrieval identical images/text but distinct accessibility history; do not garbage-collect before verified import.'),
('Current PowerShell generation wrapper','WRAP_FOR_COMPATIBILITY','Preserve no-overwrite semantics and serialized generation until target acceptance is validated.'),
('Legacy worker and manifest builder','RETIRE_AFTER_VALIDATION','Historical behavior explains provenance; do not delete or rerun during migration. Archive once replacements preserve recovery semantics.'),
('Python state manager','SUPERSEDE_AFTER_MIGRATION','Use as read-only comparison oracle through cutover; preserve its weaker structural/review semantics explicitly.'),
('Historical gap analysis and matrices','PRESERVE_READ_ONLY','48-summary scope, local candidates and qualitative priorities remain historical; adapt concepts, not evidence acceptance.'),
('Organizer scripts and inventory','PRESERVE_READ_ONLY','Original/New-preferred variants retain different canonical policies and historical source paths; reruns replace inventory.'),
('Duplicate/version folders','PRESERVE_AS_IS','Exact bytes already classified; probable versions remain independent source reports until adjudicated.'),
('Empty manual-review folder','HUMAN_DECISION_REQUIRED','Empty directory does not mean all version/metadata decisions resolved; distinguish disposition from evidence review.'),
('Git state and ignored artifacts','PRESERVE_AS_IS','Initial Git changes predate audit; Git ignore omits logs/text/PNGs. Full-file baseline required.'),
('Reference ZIP','PRESERVE_READ_ONLY','Immutable reference input; package contents are not live features; reference package SHA recorded.')])+'''

## Reference components

Every reusable target component has an explicit treatment in `REFERENCE_ARCHITECTURE_COMPATIBILITY.csv`. No generic executable is recommended for unconditional direct adoption. Adapt source/evidence/schema contracts, wrap current state/generation until verified cutover, merge identity/taxonomy/protocol concepts, replace state only after a lossless migration, reject the empty workspace template as unnecessary for the live tree, and postpone scientific scope/scoring/external-validation policy pending human decisions. These recommendations follow target acceptance gaps documented in `EXISTING_VS_PROPOSED_ARCHITECTURE.md`, not an assumption that SQLite itself solves provenance.

## Migration invariants

'''+table(['Invariant','Location','Confidence','Why / accidental loss mechanism'],[
('Exact source bytes and report distinctions','PDFs, inventory hashes','HIGH','Title-based deduplication would erase distinct versions; 112 hashes is not independent study count.'),
('Stable SummaryName aliases and target paths','Two manifests, baseline/review keys, evidence stems','HIGH','Generic P-number ingest or rebuilding slugs can break joins and orphan old outputs.'),
('Baseline versus current fingerprints','baseline.json and checkpoint.json','HIGH','Resetting baseline erases recovery origin and user-edit comparison basis.'),
('Unreviewed versus reviewed status','reviews.json, script predicate, partial ledger','HIGH','Marking all drafts DONE/verified manufactures scientific approval.'),
('Both prose generations','Summaries and .summary_v2','HIGH','Overwriting finals would lose user-visible accepted legacy content before review.'),
('Exact rubric and provenance uncertainty','PROMPT.md, Retrieval run/log, old missing records','HIGH','Replacing prompt or backfilling current hashes falsely attributes historical inputs.'),
('Partial source revisit evidence','Retrieval ledger and scratch','HIGH','Cache cleanup loses paid extraction and unfinished review boundary.'),
('Historical collection scope and aliases','docs, report, C/S/B IDs, paper_inventory','HIGH','Relabeling as expanded corpus/systematic review corrupts denominators and novelty status.'),
('Version relationships without premature merging','Mind-the-Web and AgentVigil sources','HIGH for identity; MEDIUM for contribution relationship','Hash duplicate grouping alone misses double-counting; collapsing before delta review loses report-specific methods/results.'),
('Two-paper sequential/quota-stop preference','AGENTS.md and WORKFLOW.md','HIGH','Generic four-worker default could violate user resource expectations.'),
('Uncommitted user reorganization','INITIAL_BASELINE.json git_status and file hashes','HIGH','Reset/clean/move-based migration would discard user changes.')])+'''

## Dependency graph: safe future sequence

```mermaid
flowchart TD
    A[Preserve immutable raw bytes and baseline] --> B[Reconcile aliases paths hashes and report versions]
    A --> C[Specify old predicates review meaning and unknown provenance]
    B --> D[Design lossless historical artifact registration]
    C --> D
    D --> E[Validate isolated import and round-trip equivalence]
    F[Choose DB location and strengthen target acceptance and recovery] --> E
    E --> G[Calibrate retained-paper adapters and review boundaries]
    G --> H[Authorize authority cutover with rollback]
    H --> I[Adapt wrapper and worker attempts]
    D --> J[Preserve and source-check existing drafts and ledgers]
    J --> K[Structured evidence with verified locators]
    G --> K
    B --> L[Adjudicate contribution relationships]
    K --> L
    K --> N[Govern taxonomy with historical seeds]
    L --> S[Verified contribution-aware synthesis]
    N --> S
    S --> Q[Gap candidates and chosen scoring policy]
    Q --> V[Separately authorized external validation]
    V --> W[RQs and final review with limitations]
```

Dependencies are not a claim that every paper must be regenerated. B precedes all imports because SummaryName joins and historical paths carry identity. C precedes acceptance because structural_pass has no item verification meaning. D preserves raw evidence before code/schema transformation. F precedes cutover because target late-result acceptance and SQL/file non-atomicity can invalidate imported history. J can proceed from preserved artifacts without waiting for an authority switch, but no existing review is upgraded automatically. L must precede synthesis denominators; N needs source evidence rather than folder membership. External search is a separate future authorization, not part of this audit. Evidence: current `summary_state.py:109-135`, `WORKFLOW.md:61-105`; target `litrevctl.py:199-302,347-410`; historical `docs/gaps_and_research_directions.md:355-364`.

## Unsafe direct-copy operations

Do not copy ZIP AGENTS or master instructions into the live root; do not install its skills over `.agents/skills/corpus-analysis`; do not copy its workspace template, placeholder prompt, config, schemas, controller scripts or db into current paths. Such copying could auto-initialize conflicting authority, discard rubric/names, reclassify raw drafts as accepted, or change resource/search policy. Preserve the original reference ZIP and build a separately reviewed compatibility layer instead. No SQLite or migration action was performed.
''')
write('STATE_DRIFT_REPORT.md','''# State drift and consistency report

Severity expresses impact on reconstruction/integration, not a scientific verdict. OBSERVED findings are established from files; code-derived risks are labeled INFERRED and are not evidence of a corruption event. Target-package defects are separate in EXISTING_VS_PROPOSED_ARCHITECTURE.md.

## Observed current-system findings

'''+table(['ID','Severity','Finding','Evidence / treatment'],[
('D01','MEDIUM','README historical 48-paper/root-Security-Borderline description conflicts with 112 active source reports in numbered folders','README.md:3,18-38; CORPUS_INVENTORY.csv; TOP_LEVEL_INVENTORY.csv. Preserve as historical; do not repair.'),
('D02','MEDIUM','96 broken PDF-link occurrences for 48 former source paths in docs/papers.md; papers survive elsewhere','LINK_RECONCILIATION.csv gives every file/line/target; docs/papers.md:23-70. 49 other local links resolve.'),
('D03','MEDIUM','Five duplicate_of pointers use absent historical New paths','docs/paper_inventory.csv:114-118; actual hashes still match canonical sources.'),
('D04','LOW','Two near-version original_path pointers use absent New paths','docs/near_duplicate_candidates.csv:2-3; current matching hashes in inventory rows57-58.'),
('D05','HIGH','AGENTFUZZER filename actually contains AgentVigil preprint; another AgentVigil proceedings PDF and draft exist','Both source PDF p.1 metadata/text/visual inspection; CORPUS_INVENTORY.csv. Preserve aliases; probable same-contribution risk to synthesis counts.'),
('D06','MEDIUM','Toward Secure LLM Agents venue uncertainty is not carried consistently in all historical prose','Root report:107 TOSEM versus docs/metadata_verification.md:96,119 and docs/papers.md:745 warnings. No external resolution attempted.'),
('D07','HIGH','37 structurally complete drafts have no review attestations; rich self-reported coverage must not become verified completion','reviews.json empty; summary_state.py:115-123; Retrieval ledger.md:3-39. Workflow correctly distinguishes these; finding is an integration hazard/provenance gap, not checkpoint mismatch.'),
('D08','MEDIUM','Two retained older scratch directories are not represented by stage completion; ToolHijacker has extraction but checkpoint pending','Checkpoint pending is correct by its definition. ARTIFACT_INVENTORY.csv; checkpoint.orphan_candidate_directories; CURRENT_STATE_MODEL.md.'),
('D09','INFORMATIONAL','Baseline has36 drafts; current has37, solely Retrieval Barrier addition','AUDIT_MEASUREMENTS.json:baseline_changes. Expected progress, not unexplained drift.'),
('D10','INFORMATIONAL','Saved checkpoint is dated September7 but still matches all current source/draft/final hashes/statuses','AUDIT_MEASUREMENTS.json:checkpoint_differences=[]; no refresh performed.'),
('D11','MEDIUM','Current checkpoint hashes do not prove the 36 recovered drafts used current prompt/source bytes at generation','checkpoint papers[].generation_provenance; no original per-draft run metadata except Retrieval. PROVENANCE_AUDIT.md.'),
('D12','LOW','current_repo.txt is a prior filesystem listing, not a checkpoint; includes stale cache listing','current_repo.txt headings/date rows versus current inventory; no scripts read it as state.')])+'''

## Reconciliation with no discrepancy

OBSERVED: 112/112 manifest sources exist; manifests are byte-identical; every source/draft/final fingerprint agrees with checkpoint; baseline sources and finals unchanged; 117/117 docs inventory current paths and hashes match; 5/5 archived hashes have active matches; 48/48 legacy summaries and 37/37 v2 summaries map; 1/1 evidence directory and 2/2 scratch directories map; reviews has0 records. No missing or orphan summaries, extra canonical byte duplicates, or unexplained run/output mismatches were found. Exact per-paper outcomes: PAPER_PROCESSING_MATRIX.csv; exact measurements: AUDIT_MEASUREMENTS.json and RECONCILIATION_DETAILS.json.

OBSERVED: no current durable run has running/failed status; Retrieval status generated_requires_source_review matches its draft. Process snapshot found no live generation worker. The old scratch directories are historical interrupted-work candidates; no exact crash termination record survives. A lock filename alone cannot establish a held handle.

## Code-derived risks, not observed corruption

| Risk | Severity | Evidence |
|---|---|---|
| Two direct state refreshes race on fixed temporary names; JSON and MD are not updated as one transaction | HIGH | summary_state.py:73-77,156,178-180; no state lock |
| Direct generator/legacy worker bypass wrapper lock; target paths and evidence stem may collide | HIGH | run_summary.ps1:20-36 versus generate_summary.ps1:13-31 |
| Missing baseline is recreated; final user-edit protection is procedural only | HIGH | summary_state.py:124-127,151-155; WORKFLOW.md:102-105 |
| Review notes can change without invalidating approval; notes content/identity not checked | HIGH | summary_state.py:115-123 |
| Same-stem retries overwrite run/log/extraction; crash can leave stale running and extra PNGs | MEDIUM | generate_summary.ps1:13-31,131-138,173,202-212 |
| Synced filesystem does not demonstrate cross-host lock/atomicity guarantees | MEDIUM | G:/My Drive root plus local FileShare.None and replace calls; no sync incident observed |
| Filename-only organizer link parser likely misses angle-wrapped links | LOW | organizer new_preferred.py:399-444; docs/papers.md:23. INFERRED mechanism; actual historical flags unknown |

No CRITICAL observed corruption was found. The twelve numbered finding groups include expected progress and provenance hazards; they must not be reported as twelve corrupt state records. No inconsistency was repaired.
''')
unknowns=[
('U01','Exact generating prompts/models/runtime for36 recovered drafts and48 legacy outputs','Per-paper logs absent; timestamps/current hashes cannot recreate history','Summaries; .summary_v2; checkpoint; baseline; current_repo.txt; worker scripts','Original run logs/immutable generation metadata','Blocks automatic provenance certification, not raw preservation/import'),
('U02','Whether historical source review occurred outside retained registry','reviews is empty and only one partial ledger survives','reviews.json; WORKFLOW; evidence; summaries','Dated source-review notes tied to exact source/draft hashes','Blocks treating existing outputs as independently verified'),
('U03','Independent contribution count and exact version deltas','Title pages establish two probable groups; full method/result comparison outside audit scope','Four Mind-the-Web/AgentVigil source title pages; inventory; near-duplicate CSV','Report-level delta review and explicit research-object adjudication','Blocks definitive synthesis denominator, not preservation'),
('U04','Exact organizer variant/flags and interrupted-worker history','Two organizer variants and no complete invocation log','Organizer scripts; docs inventories; Git history; scratch; WORKFLOW','Historical shell/run log or user record','Does not block hash-based mapping; retain uncertainty'),
('U05','Google Drive sync health, other-host writers and distributed atomicity','Local code/process view does not establish other machines or sync protocol','Root path; file baseline; process snapshot; locking/write code','Deployment decision plus controlled sync/storage tests','Blocks selecting live SQLite location and distributed writer guarantees'),
('U06','Final project inclusion criteria, synthesis units and taxonomy governance','Current curated corpus and historical prose do not specify a formal current review protocol','README; root report; docs; target protocol/config template','Project-specific protocol decisions','Blocks final scope/taxonomy adoption; raw import can proceed'),
('U07','Whether generic gap weights and external-validation policy fit project','Current nonmechanical rubric differs and audit is closed-document','docs/gaps:305-324; target gap_score/config/references','Explicit policy/calibration choice and separately authorized external research','Blocks automatic weighted ranking/global novelty claims'),
('U08','Toward Secure LLM Agents final publication metadata','Local/historical sources disagree','docs/metadata_verification.md:96,119; report:107; source title page','Authoritative publication check in later authorized phase','Blocks confident venue assertion only'),
('U09','Scientific completeness/accuracy of37 structural passes','Structural and image-existence checks are not a full source review','All draft structure; representative summaries; partial ledger; four existing tests','Inventory-denominated source review per paper','Blocks verified acceptance/synthesis, not reuse of drafts'),
('U10','Full reference controller runtime correctness','Read-only code/schema audit did not execute package or create test database; jsonschema unavailable in audit runtime','All reference code/schemas/tests; REFERENCE_STATIC_CHECKS.json','Isolated acceptance/rollback/stale-task/phase/schema tests after design','Blocks direct production adoption, not architecture comparison'),
('U11','Original corpus search reproducibility and external gap coverage','Historical report explicitly not systematic/PRISMA replay','report:5-12,211-215; metadata ledger','Search logs, inclusion decisions, dates and candidate-specific validation','Blocks claiming exhaustive literature coverage'),
('U12','Absence of all further bibliographic relationships','Hash+title/metadata screening is not full semantic comparison of every pair','117 title-page text checks; normalized filename candidates; PDF inventory','Broader bibliographic/author/identifier review where needed','Does not block preserving112 report IDs; blocks asserting110 definitive objects')]
with (O/'UNRESOLVED_REGISTER.json').open('w',encoding='utf-8') as f:json.dump([dict(zip(['id','unknown','why','examined','resolving_evidence','migration_effect'],u)) for u in unknowns],f,indent=2)
write('UNRESOLVED_QUESTIONS.md','''# Unresolved questions and conflicts

UNKNOWN is retained as a first-class result, not filled with plausible history. These questions do not prevent completion of the infrastructure audit. The final column distinguishes preservation from acceptance/cutover blockers. No answer was invented or external research performed.

'''+table(['ID','Unknown','Why unresolved','Evidence examined','Would resolve it','Migration impact'],unknowns)+'''

CONFLICTING instruction sources were handled explicitly: user audit forbids checkpoint refresh despite AGENTS/skill normal workflow; user output boundary overrides PDF skill temp conventions; reference auto-init/default parallelism/external-search guidance remains inert. User explicitly allowed the sibling handoff ZIP as the only output-boundary exception. No additional approval was needed for this read-only audit.
''')
print(json.dumps({'components':len(rows),'classifications':counts,'unknowns':len(unknowns)}))
