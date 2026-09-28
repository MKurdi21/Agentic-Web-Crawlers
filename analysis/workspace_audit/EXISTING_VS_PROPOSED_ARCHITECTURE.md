# Current system versus reference architecture

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

The compatibility CSV has **43 significant components**: 15 skills, 14 individual schemas and 14 infrastructure/policy components. Classification counts: `{"MISSING": 5, "NEEDS_HUMAN_DECISION": 1, "NOT_NEEDED": 1, "PARTIALLY_IMPLEMENTED": 23, "SIMILAR_BUT_INCOMPATIBLE": 13}`. Each CSV row includes intended responsibility, current equivalent/evidence, behavioral overlap, state/artifact/provenance compatibility, complexity, data-loss risk, treatment and notes. All classifications concern current behavior, not merely target availability.

| Component ID | Reference responsibility | Classification | Recommendation |
| --- | --- | --- | --- |
| skill:literature-review-router | Route all review phases | PARTIALLY_IMPLEMENTED | MERGE |
| skill:review-state-coordinator | State, eligibility, attempts and recovery | SIMILAR_BUT_INCOMPATIBLE | WRAP_CURRENT_IMPLEMENTATION |
| skill:corpus-ingestion | Hash/register/dispose source reports | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| skill:paper-deep-reader | Normalize and deeply summarize one source | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| skill:paper-evidence-extractor | Create source-located structured evidence | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| skill:evidence-verifier | Independent material evidence checking | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| skill:research-object-resolver | Link report versions to contributions | PARTIALLY_IMPLEMENTED | MERGE_CONCEPTS |
| skill:taxonomy-thematic-coder | Evidence-backed controlled coding | SIMILAR_BUT_INCOMPATIBLE | MERGE_CONCEPTS |
| skill:cross-paper-synthesizer | Build contribution-aware verified matrices | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| skill:contradiction-replication-analyzer | Comparable cross-object claims and drivers | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| skill:research-gap-detector | Evidence-supported candidate generation and scores | SIMILAR_BUT_INCOMPATIBLE | POSTPONE_HUMAN_DECISION |
| skill:external-gap-validator | Reproducible external novelty checking | MISSING | POSTPONE_HUMAN_DECISION |
| skill:research-question-generator | Traceable falsifiable RQs | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| skill:literature-review-writer | Thematic verified review prose | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| skill:corpus-auditor | Coverage, provenance, compatibility and claim audit | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| schema:worker_task | Schema: worker_task | MISSING | ADAPT_TO_EXISTING_SEMANTICS |
| schema:worker_result | Schema: worker_result | MISSING | ADAPT_TO_EXISTING_SEMANTICS |
| schema:artifact_metadata | Schema: artifact_metadata | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| schema:corpus_manifest | Schema: corpus_manifest | SIMILAR_BUT_INCOMPATIBLE | WRAP_CURRENT_IMPLEMENTATION |
| schema:normalized_paper | Schema: normalized_paper | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| schema:summary | Schema: summary | SIMILAR_BUT_INCOMPATIBLE | ADAPT_TO_EXISTING_SEMANTICS |
| schema:evidence | Schema: evidence | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| schema:verification | Schema: verification | SIMILAR_BUT_INCOMPATIBLE | ADAPT_TO_EXISTING_SEMANTICS |
| schema:research_object | Schema: research_object | PARTIALLY_IMPLEMENTED | MERGE_CONCEPTS |
| schema:taxonomy | Schema: taxonomy | SIMILAR_BUT_INCOMPATIBLE | MERGE_CONCEPTS |
| schema:paper_taxonomy_coding | Schema: paper_taxonomy_coding | SIMILAR_BUT_INCOMPATIBLE | ADAPT_TO_EXISTING_SEMANTICS |
| schema:contradiction | Schema: contradiction | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| schema:gap_candidate | Schema: gap_candidate | SIMILAR_BUT_INCOMPATIBLE | POSTPONE_HUMAN_DECISION |
| schema:research_question | Schema: research_question | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| infra:sqlite | SQLite authoritative state | SIMILAR_BUT_INCOMPATIBLE | REPLACE_ONLY_AFTER_MIGRATION |
| infra:bundles | Immutable accepted bundles | MISSING | ADAPT_TO_EXISTING_SEMANTICS |
| infra:leases | Leases, retry and stale recovery | SIMILAR_BUT_INCOMPATIBLE | ADAPT_TO_EXISTING_SEMANTICS |
| infra:pins | Semantic version and hash pinning | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| infra:calibration | Calibration and phase gates | MISSING | ADAPT_TO_EXISTING_SEMANTICS |
| infra:gap_score | Deterministic gap scoring | SIMILAR_BUT_INCOMPATIBLE | POSTPONE_HUMAN_DECISION |
| infra:protocol | Versioned review protocol | PARTIALLY_IMPLEMENTED | MERGE_CONCEPTS |
| infra:config | Generic project configuration | NEEDS_HUMAN_DECISION | ADAPT_TO_EXISTING_SEMANTICS |
| infra:template | Generic empty workspace and placeholder prompt | NOT_NEEDED | REJECT_AS_UNNECESSARY |
| infra:instructions | Master instructions / AGENTS / plugin manifest | SIMILAR_BUT_INCOMPATIBLE | MERGE_CONCEPTS |
| infra:qa | Semantic QA gates | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| infra:provenance | Evidence/artifact provenance graph | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| infra:synthesis_control | Corpus-stage artifact registration | PARTIALLY_IMPLEMENTED | ADAPT_TO_EXISTING_SEMANTICS |
| infra:methodology | Methodology source bibliography | PARTIALLY_IMPLEMENTED | POSTPONE_HUMAN_DECISION |

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
