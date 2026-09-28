from pathlib import Path
import json,csv,collections,hashlib,datetime
R=Path(__file__).resolve().parents[2];O=R/'analysis/workspace_audit'
def read(n):return json.loads((O/n).read_text(encoding='utf-8'))
def csvread(n):return list(csv.DictReader((O/n).open(encoding='utf-8')))
def write(n,t):(O/n).write_text(t.strip()+'\n',encoding='utf-8')
def table(headers,rows):return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(str(x).replace('|',';').replace('\n',' ') for x in r)+' |' for r in rows])
S=read('AUDIT_MEASUREMENTS.json');D=read('RECONCILIATION_DETAILS.json');B=read('INITIAL_BASELINE.json');M=csvread('PAPER_PROCESSING_MATRIX.csv');C=csvread('CORPUS_INVENTORY.csv');T=csvread('TOP_LEVEL_INVENTORY.csv')
E='Evidence labels: OBSERVED = directly established; INFERRED = interpretation of observations; UNKNOWN = insufficient evidence; CONFLICTING = sources disagree. CURRENT_SYSTEM refers only to live files outside the reference ZIP and audit outputs. Archive citations use `ZIP!rebuild/...:lines` and refer exclusively to REFERENCE_TARGET_ARCHITECTURE. Recommendations are PROPOSED_INTEGRATION, not executed changes.'
write('EXECUTIVE_SUMMARY.md',f'''# Executive summary

{E}

## What exists

OBSERVED: This is a curated PDF repository with a historical 48-summary literature synthesis and a newer recoverable draft-generation workflow. Current state is derived from stable CSV mappings, filesystem hashes, structural predicates, a baseline, and review declarations; it is not an event ledger or SQLite application. Evidence: `scripts/summary_state.py:82-156`, `analysis/WORKFLOW.md:38-57`, `README.md:3,18-38`.

The audit independently inventoried **117 PDFs / 112 unique SHA-256 values**, with **112 active manifest records**, **5 exact duplicate copies**, **48 legacy summaries**, **37 v2 drafts**, **1 durable evidence run**, **2 older scratch directories**, and **0 manual-review files**. All 112 manifest source paths and all 117 historical inventory current-path hashes reconcile. There are no orphan summary files or evidence directories. Evidence: `CORPUS_INVENTORY.csv`, `PAPER_PROCESSING_MATRIX.csv`, `ARTIFACT_INVENTORY.csv`, `AUDIT_MEASUREMENTS.json`, `RECONCILIATION_DETAILS.json`.

## Real frontier

OBSERVED: The current checkpoint is byte-fingerprint-consistent with live paper artifacts: **37 structural_pass / 75 pending / 0 needs_repair / 0 source_verified / 0 promoted**. Structural pass means required headings/order and 20,000 characters, not scientific correctness (`scripts/summary_state.py:47-70,112-123`). The 37 drafts comprise 36 recovered drafts plus Retrieval Barrier. The latter has a partial review ledger; none has a valid recorded attestation because `analysis/reviews.json` is empty.

By highest observed artifact level: **36 unreviewed drafts**, **1 draft with partial source review**, **1 extraction-only newer attempt (ToolHijacker, also with legacy summary)**, **18 other legacy-only papers**, and **56 papers with no processing artifact found**. Legacy/v2 overlap is 29; 19 legacy files have no v2; 8 v2 files have no legacy output. Exact lists are in the processing matrix and `CURRENT_STATE_MODEL.md`.

## Most important findings

- CONFLICTING: Historical documentation still describes 48 papers in root/Security/Borderline; those directories are now empty. `docs/papers.md` has 96 broken PDF-link occurrences representing 48 former paths; all corresponding papers survive. Five duplicate pointers and two version-candidate pointers use former New paths (`LINK_RECONCILIATION.csv`; `docs/paper_inventory.csv:114-118`; `docs/near_duplicate_candidates.csv:2-3`).
- OBSERVED/INFERRED: Two probable report-version groups need contribution-aware treatment: Mind the Web, and AgentVigil. The file named AGENTFUZZER is actually an AgentVigil preprint; its separate proceedings PDF and both drafts are retained. Identity is established from PDF first-page text/metadata and direct visual inspection; contribution equivalence remains an inference. Thus 112 unique PDF contents is not a verified independent-study count (`DUPLICATE_AND_VERSION_REPORT.md`).
- OBSERVED: Only Retrieval Barrier retains a durable generation log/run record; its partial ledger explicitly withholds attestation. Historical drafts lack provable exact generation inputs. Preserve both summary generations and scratch evidence; do not import a structural pass as a verified result (`PROVENANCE_AUDIT.md`; Retrieval `ledger.md:3-39`).
- OBSERVED: The supported wrapper serializes generation with an exclusive file handle, but direct generator/state invocations bypass it. Shared checkpoint replacements are not a multi-file transaction. Concurrency/sync failure scenarios are code-derived risks, not observed corruption (`scripts/run_summary.ps1:20-36`; `scripts/summary_state.py:73-77,156,178-180`).

## Reference and integration

OBSERVED: The supplied ZIP is a separate proposed plugin/controller package: 121 archive entries, 72 files, 15 skills, 14 JSON schemas, a SQLite schema, generic templates, and two controller/scoring scripts. It was read directly, not installed or executed. SHA-256: `55902ec025685c1f4f2afb37672cc885222eab9952b39eb7ee48429100633e42`. See `REFERENCE_PACKAGE_INVENTORY.csv`.

INFERRED: The reference offers useful separation of stage outputs, attempts, evidence, versions, and synthesis, but its production label exceeds some code guarantees. Completion does not reject expired/reaped attempts or enforce all semantic QA; source/code pinning is incomplete; SQL and filesystem acceptance are not one transaction; several schemas allow empty or weakly constrained records. These are target-package limitations, not live-workspace features (`EXISTING_VS_PROPOSED_ARCHITECTURE.md`).

PROPOSED_INTEGRATION: First preserve bytes, aliases, historical paths, baseline and uncertainty; define a lossless state/artifact crosswalk; validate an isolated importer and strengthen target acceptance before any authority cutover. Retain the current heavy prompt unchanged and register recovered outputs with honest unknown provenance. Do not copy the generic AGENTS, template prompt, controller, or schemas over the live repository. The handoff details a dependency-based strategy rather than implementing one.

## Audit limits and safety

All PDF title pages were text-inspected for identity; four version-edge title pages and two existing evidence images were visually inspected. This is not a full scientific source review. Historical model provenance, exact old execution commands, independent-contribution count, and future taxonomy/scope choices remain explicitly unresolved. They do not prevent preservation/import of raw artifacts, but they block automatic acceptance or final synthesis claims. See `UNRESOLVED_QUESTIONS.md` and `VALIDATION_REPORT.json` for final integrity results.
''')
write('CURRENT_STATE_MODEL.md',f'''# Current state model

{E}

## Authority and identities

OBSERVED: The unit is a manifest row, joined through `SummaryName`; source path, staged target, final target, and `ExistingName` are retained separately. There is no standalone paper ID. Two manifests are byte-identical (SHA-256 `e3bf75767e8232ea73df524b00fa5a492cd83b1846405976a4e23a9e4c39344d`). The builder recovers 48 legacy names from PDF basenames in docs and generates 64 others, appending eight source-hash characters on name collision; rebuilding would depend on path ordering and historical docs (`.codex_build_summary_manifest.ps1:3-48`).

{table(['Concept','Authority','Evidence'],[
('Identity/path routing','analysis/manifest.csv','summary_state.py:82-83,109'),('Source/draft/final content','actual files and SHA-256','summary_state.py:25-29,110-112'),('Current rubric','analysis/PROMPT.md hash','summary_state.py:85-87'),('Review declaration','reviews.json plus exact hashes and notes-file existence','summary_state.py:115-123'),('Recovery origin','baseline.json','summary_state.py:99-102,124-127,151-155'),('Derived progress','script predicates; JSON/Markdown checkpoint are exports','summary_state.py:144-180'),('Generation attempt observation','evidence/<summary-stem>/run.json','summary_state.py:128-135')])}

## Predicates, not enforced event transitions

OBSERVED (`scripts/summary_state.py:47-70,112-123`): missing staged draft -> pending; existing failed shape -> needs_repair; passed shape -> structural_pass. Shape requires 22 numbered Markdown heading matches, normalized lowercase alphanumeric title substrings, first-match order, a Stage 0 heading, a completeness-audit heading, and >=20,000 characters. Stage 0 need not be first and audit need not be last. Body text cannot substitute for headings.

Review is valid only if source and draft exist, draft shape passes, review source/prompt/draft hashes equal observed hashes, reviewed_at and notes_path are truthy, and the resolved notes file exists. A valid review yields source_verified, or promoted when final and draft hashes match. Review-note contents/hash, reviewer identity, date syntax, ledger coverage, images, model and script version are not checked. Missing source raises an issue but may leave structural_pass.

```mermaid
flowchart TD
    F[Observe manifest and current files] --> D{{Draft exists?}}
    D -->|No| P[pending]
    D -->|Yes| S{{Required structure passes?}}
    S -->|No| N[needs_repair]
    S -->|Yes| V{{Hash-bound review predicate valid?}}
    V -->|No| U[structural_pass]
    V -->|Yes| E{{Final hash equals draft?}}
    E -->|No| R[source_verified]
    E -->|Yes| A[promoted]
```

Any observation can regress after edits/deletions. No permanent terminal state or transition event history exists. Pending includes 19 papers with legacy summaries; old finals do not satisfy the new rubric. Generation run states running/generated_requires_source_review/failed_or_interrupted are a separate axis, never substitutes for review status (`generate_summary.ps1:22-31,202-212`).

## Baseline, review, promotion and recovery

OBSERVED: baseline created at {json.loads((R/'analysis/baseline.json').read_text())['created_at']} stores source/draft/final hashes for all 112 rows, with 36 drafts and 48 finals. Missing baseline causes refresh to create one, conflicting with the procedural instruction never silently reset it. Only source changes, not final edits, are automatically flagged against baseline (`summary_state.py:124-127,151-155`; `WORKFLOW.md:46`).

Promotion is procedural: compare final with baseline/last reviewed version, inspect diff, copy reviewed draft, refresh. No promotion API or automated user-edit guard is implemented (`WORKFLOW.md:97-105`). Editing review notes alone would not invalidate the predicate.

OBSERVED: wrapper refuses any existing staged draft and acquires an exclusive generation.lock file handle. A lingering zero-byte filename is not a held lock. Process inspection during this audit found app-server/audit processes, not a live paper-generation worker; no locks were acquired or processes terminated. Crashes can leave stale running metadata, and no lease/reaper exists. No current run is marked failed or running; Retrieval is generated_requires_source_review. Older scratch proves retained extraction, not a still-running process (`run_summary.ps1:12-36`; `WORKFLOW.md:19-36`).

OBSERVED: state writes fixed .tmp filenames then replaces destinations; JSON and Markdown checkpoint writes are separate. Direct state refresh has no lock. Malformed JSON, inaccessible files, bad notes paths or missing run status fields can abort the whole refresh. Wrapper invokes native Python in finally without an explicit exit-code check. No transactional recovery, per-record isolation or retry queue exists (`summary_state.py:73-87,128-180`; `run_summary.ps1:25-36`).

## Reconciliation and frontier

OBSERVED: all current source/draft/final fingerprints and statuses match saved checkpoint, dated 2026-09-07T15:34:25.812097+00:00. Only Retrieval draft differs from baseline (null -> `945561f59ec6a1d41e986254c7f74e413fdd1d039a443d7a7d1cc8b6bffff9ff`). No source/final baseline changes, missing manifest sources, unmapped drafts/finals/evidence, review records, or hash-unmatched archived copies were found (`AUDIT_MEASUREMENTS.json`; `RECONCILIATION_DETAILS.json`).

{table(['Definition','Count'], [('Active manifest source reports',112),('Unique PDF hashes',112),('Legacy summary coverage',48),('V2 structural passes',37),('Valid source review attestations',0),('Promoted under current predicate',0),('New-workflow partial source reviews',1),('Newer extraction-only attempts',1),('No processing artifact found',56)])}

UNKNOWN: completed scientific review outside the retained registry and exact number of independent contributions. Two probable version groups would give 110 candidate contribution groups if collapsed, but this is not an adjudicated total. Do not label the 56 artifact-free records as historically never read.

## Exact paper lists by highest observed artifact level

'''+ '\n\n'.join('### '+state+' ('+str(sum(x['newest_apparent_workflow_state']==state for x in M))+')\n\n'+'\n'.join('- `'+x['summary_name']+'`' for x in M if x['newest_apparent_workflow_state']==state) for state in S['frontier'])+'''

## Test contract

OBSERVED: four existing tests cover placeholder structure passing, body-versus-heading mismatch, order/length, missing-file hash and path escape (`scripts/test_summary_state.py:23-44`). They intentionally prove shape is not science. No tests cover attestation semantics, baseline reset, promotion protection, race recovery or malformed per-paper state. Audit computations reproduce predicates independently; no state refresh or pipeline execution occurred.
''')
write('CURRENT_PIPELINE.md',f'''# Current pipeline and prompt reconstruction

{E}

## End-to-end supported path

OBSERVED: `pwsh -File scripts/run_summary.ps1 -SummaryName <existing-mapped-name.md>` resolves exactly one manifest row, rejects existing draft, obtains an exclusive generation lock, calls generator with source/stage/prompt paths, refreshes state in finally, then disposes lock. `-DryRun` displays metadata before locking. This audit did not invoke it (`scripts/run_summary.ps1:1-36`).

```mermaid
flowchart LR
    M[Stable manifest row] --> W[Runner: reject draft and lock]
    P[PDF plus saved PROMPT] --> X[Dual text extraction and ranked PNGs]
    W --> X
    X --> C[One Codex exec call]
    C --> D[Staged Markdown draft]
    C --> L[Durable log and run metadata]
    D --> H[Shallow generation checks]
    H --> S[Checkpoint derived from files]
    D --> R[Analyst ledger and source revisit]
    R --> A[Hash-bound review declaration]
    A --> F[Deliberate final copy after edit check]
```

## Script contracts

{table(['Script','Inputs and outputs','Execution/lifecycle'],[
('.codex_build_summary_manifest.ps1','docs/papers.md and recursive PDF paths -> .summary_manifest.csv','Recovers names from basename links, slugifies new names, suffixes collisions with 8 hash chars; requires exactly 112 PDFs; writes replacement CSV. Lines 3-48.'),
('.codex_full_summary_worker.ps1','Pdf,Target,PromptPath -> staged Markdown; .summary_work_<stem>_<PID>','Caller-root paths; one ephemeral Codex exec with danger-full-access; discards streams; shallow checks; containment-checked scratch deletion in finally. Lines 1-18,124-159,167-198. Legacy/superseded by supported wrapper, but still callable.'),
('scripts/generate_summary.ps1','Pdf,Target,PromptPath -> draft and analysis/evidence/<stem>','Repository-root target; rejects draft; one read-only-sandbox Codex exec; durable log/run; no lock of its own. Lines 1-31,145-212.'),
('scripts/run_summary.ps1','SummaryName, optional DryRun; manifest + saved prompt','Exclusive handle serializes wrapper generation and state refresh; direct generator/state calls bypass it. Lines 1-36.'),
('scripts/summary_state.py','Manifest,prompt,baseline,reviews,PDFs,drafts,finals,run records -> checkpoint JSON/MD','No arguments, recomputes file predicates; initializes missing baseline; no model calls, no promotion; fixed temporary filenames. Lines 80-184.')])}

OBSERVED dependencies: PowerShell, discoverable `python`, PyMuPDF/fitz, PyPDF2, and discoverable `codex`; no version lock. Generator passes source/work paths as arguments, matching skill guidance about prior concurrent environment-variable contamination. Neither worker pins model, reasoning effort, package, CLI or script version. Current invocation is `codex exec --ephemeral -s read-only -C <root> -o <stage-target>` plus image arguments and standard-input prompt; CLI writes requested output despite model tool-use restriction (`generate_summary.ps1:14-15,34-42,167-175`).

## Extraction and retained evidence

OBSERVED (`generate_summary.ps1:34-138`): for every page, native PyMuPDF and PyPDF2 text are compared by length; only the longer text is retained with page boundaries. Extraction disagreements are not reconciled. A PyPDF2 error string can participate in that comparison. Native text below 80 characters flags OCR need but no OCR runs. Image counts and figure/table/diagram/algorithm/architecture/equation mentions rank pages; at most 56 are rendered whole-page at 1.25 scale. This heuristic is not an object coverage inventory. Embedded attachment count is recorded without extracting attachments. Appendix detection can match references. Current missing-page metadata states unassessed, whereas old metadata used an empty list.

{table(['Workspace','Contents','Identity/lifecycle'],[
('analysis/evidence/retrieval_barrier_comprehensive_summary','21 files: article/accessibility/images, 15 PNGs, run/log/partial ledger','20-page source; selected 1,2,4-14,19,20; run finished 2026-09-07 15:34 UTC requiring source review.'),
('.summary_work_retrieval_barrier_comprehensive_summary_46468','18 files: article/accessibility/images plus 15 PNGs','Same article SHA and all 15 image hashes as durable Retrieval run; old accessibility differs; retains historical evidence.'),
('.summary_work_toolhijacker_comprehensive_summary_46468','17 files: article/accessibility/images plus 14 PNGs','18-page source; selected 1,2,3,5-12,16-18; no v2 draft or new run metadata; unique retained extraction.')])}

Evidence: `ARTIFACT_INVENTORY.csv` hashes; each accessibility.json page_count/visual_pages; Retrieval `run.json`. Retrieval text hash is `0943dbea1e6e5bc5603c43a596fa91bf9d45749e0435e558f6a47818bc415a86`; ToolHijacker text hash is `41a72adbe70f737ee900aaa7fb8308e0d7b2dd90f453e4baac05d5ff7cac555a`.

Creation sequence is run=running -> text/accessibility/PNGs/image list -> composed prompt -> one Codex call/log -> draft structural checks -> completed/failed run -> wrapper checkpoint. Ledger is an analyst-maintained artifact, not produced by that code. Retrieval ledger at lines 3,8-17,35-39 records only partial source review (pp10-11, Figure 9/Table 2), missing review.md and no attestation. Direct visual inspection in this audit confirmed page10 is a retained figure/text page; it did not verify the entire summary.

## Heavy prompt versus enforcement

OBSERVED: `analysis/PROMPT.md` has 1,249 lines, SHA-256 `{D['prompt_sha256']}`. It defines closed-document A author / B observable / C derived / D interpretation / E external distinctions, Stage 0 capability reporting, full object inventory, cumulative extraction before narrative, every substantive visual, equations/experiments, source-grounded revisit, long-document persistent ledgers, 22 final sections, and inventory-denominated completeness. No explicit semantic version is present (`PROMPT.md:61-100,103-262,265-746,749-814,817-1211`).

OBSERVED: wrappers add instructions to avoid tools/external facts and emit final Markdown from the supplied whole text and selected PNGs. They do not persist a pre-narrative ledger or perform later independent source review (`generate_summary.ps1:145-175`; `WORKFLOW.md:89-92`). Generation validates 20,000 characters and required phrase substrings; the state manager improves this to numbered heading/order checks, but neither establishes factual/visual completeness. No exact historical prompt is provable for 36 recovered drafts. Retrieval log contains the current full prompt and is stronger generation-time evidence. Embedded wrappers are additional instruction generations, not a replacement rubric.

## Failures, idempotency and concurrency

OBSERVED: no retry loop, scheduler or quota parser. Quota stopping is procedural (`WORKFLOW.md:19-36`). Supported runner refuses any draft, including partial failed output. Current generator retains evidence and records failed_or_interrupted on caught errors; abrupt death may leave running. Retrying without a draft reuses the stem directory and overwrites run/log/extraction; stale extra PNGs may remain. Thus retention is durable but not immutable attempt history (`generate_summary.ps1:13-31,131-138,173,202-212`).

INFERRED concurrency risks, not observed corruption: bypassing wrapper permits competing output/evidence writes; direct refreshes race on fixed .tmp names; JSON/MD replacement can diverge across an interruption; Google Drive's synchronized location is evident from the absolute path but cross-host lock/rename guarantees were not tested. Do not regard a synced lock filename as a distributed lease. The account allowance is unknown and the current two-paper sequential preference must survive future wrappers (`AGENTS.md:13-16`).
''')
write('WORKSPACE_ARCHITECTURE.md',f'''# Workspace architecture

{E}

## Boundary and environment

OBSERVED root: `{R}`. Baseline completed `{B['timestamp']}`; environment `{B['os']}`, Python `{B['python'].splitlines()[0]}`, PowerShell 7.6.5, Git branch `{B['branch']}`. The path appears Google Drive synchronized; sync health and multi-host atomicity were not established. `.gitattributes:1` declares PDFs binary, and `.git/config` has no LFS filter; no LFS configuration was found. Git was already dirty with relocated-source deletions/untracked replacements. Full initial status and 979 pre-existing file hashes, including .git and reference ZIP, are in `INITIAL_BASELINE.json`.

## Complete root inventory

{table(['Item','Role','Direct entries if directory'],[(x['path'],x['classification'],x['direct_entries']) for x in T])}

OBSERVED: numbered 01-12 folders contain the 112 manifest sources; 98_Manual_Review is empty; 99_Duplicates contains five archived byte copies. New/Security/Borderline are empty historical locations. Directory roles are corroborated by source paths/hashes and organizer code, not names alone (`CORPUS_INVENTORY.csv`; organizer new_preferred:331-376,510-568). `current_repo.txt` is a historical directory listing, not a live state source: it lists September 7 output and stale __pycache__ entries. The reference ZIP is a proposed input only.

## Instruction hierarchy and conflicts

{table(['Source','Scope / role','Relationship or conflict'],[
('Current user audit instructions','Audit only; read-mostly with bounded output writes','Overrides normal state-refresh, summarization, promotion and PDF scratch conventions.'),
('AGENTS.md:1-19','Paper analysis/recovery coordinator instructions','Routes to workflow/checkpoint/rubric and local skill; sequential two-paper generation; untrusted papers remain evidence.'),
('.agents/skills/corpus-analysis/SKILL.md:1-26','Only project-local skill found; recovery, deep reading, evidence, state and review coordination','Composite analysis/recovery skill, not a general literature-review router. No local agents/openai.yaml exists.'),
('analysis/WORKFLOW.md:1-125','Authority, recovery, evidence and deliberate promotion','Makes draft versus reviewed distinction; some protections procedural only. Refresh instruction suspended for audit.'),
('analysis/PROMPT.md:1-1249','Exact heavy paper-analysis rubric','Read as audit evidence, not executed. Whole-document evidence requirements exceed generator automation.'),
('analysis/REVIEW_TEMPLATE.md:1-57','Reusable evidence and source-revisit table structure','Empty template is not completed ledger; never copied into live evidence by audit.'),
('README.md and docs','Historical 48-summary corpus guide/synthesis','Stale layout/counts; preserves historical concepts but cannot override current mapping.'),
('Installed PDF skill','Audit extraction and visual inspection guidance','Used existing bundled pypdf/pypdfium2; audit scratch boundary overrides default output/temp paths.'),
('ZIP master/AGENTS/skills','REFERENCE_TARGET_ARCHITECTURE only','No live scope or instruction authority; not installed.')])}

OBSERVED configuration: `.git/config` records Git remote/branch; `.gitattributes` marks PDFs binary; `analysis/.gitignore:1-7` excludes rendered pages, text, image lists, logs, lock and temporary files; `scripts/.gitignore` excludes __pycache__. This means a Git-only backup omits unique research evidence. The live state model has no project configuration file or JSON schema collection; package config exists only in the ZIP (file inventory evidence).

## Historical and current layers

OBSERVED: Git history records June 24 collection/documentation work and July 22 comprehensive summaries (`RECONCILIATION_DETAILS.json:git_history`). Historical prose files still discuss 48 summaries; organized inventory captures 117 PDF locations. The recovered state baseline tracks 36 drafts, later 37 with Retrieval. Current checkpoint is a filesystem observation, not a source-quality attestation (`CURRENT_STATE_MODEL.md`).

```mermaid
flowchart TB
    PDF[Current numbered PDF corpus] --> MAP[Stable manifest aliases]
    PDF --> OLD[48 legacy summaries]
    OLD --> DOC[Historical 48-paper docs and gap prose]
    MAP --> GEN[Current wrapper and generator]
    GEN --> ST[37 staged drafts]
    GEN --> EV[1 durable evidence run]
    SCR[2 older scratch workspaces] --> EV
    PDF --> STATE[Filesystem-derived state predicates]
    ST --> STATE
    REV[Empty reviews plus recovery baseline] --> STATE
    STATE --> CP[JSON and Markdown checkpoints]
    REF[Separate reference ZIP] -. comparison only .-> HAND[Proposed integration handoff]
    STATE --> HAND
    DOC --> HAND
```

The scratch-to-evidence arrow denotes observed identical Retrieval bytes, not proven copy execution. ToolHijacker scratch is unique and must remain available. Model provenance is rich only in Retrieval's durable log; most artifact links are reconstructed from stable manifest names and hashes (`PROVENANCE_AUDIT.md`).

## Historical synthesis and format comparison

OBSERVED: `docs/papers.md` has 26,933 words/754 lines; matrix 3,080/169; gaps 6,482/364; citation clusters 4,889/298; metadata ledger 3,159/138. These are human-readable synthesis products, not evidence-database outputs. Matrix claims 48-summary scope (`docs/problem_approach_matrix.md:3-7`); gaps explicitly deny global completeness (`docs/gaps_and_research_directions.md:5,9-12,355-364`); metadata distinguishes 33 local-complete, 14 local-plus-historical and one conflict (`docs/metadata_verification.md:98-111`). Those metadata labels do not imply source-reviewed summaries.

OBSERVED: gap prose includes eleven directions, RQs, hypotheses and a six-dimension 1-5 prioritization framework, but explicitly says not to collapse scores mechanically (`docs/gaps_and_research_directions.md:26-364,305-324`). Root report labels a July 22 closed-corpus audit and states search is not a PRISMA reproduction (`agentic_ai_web_agents_literature_search_report.md:5-12,211-215`). Historical URLs are not current external validation. A Toward Secure LLM Agents venue conflict remains between report TOSEM wording and metadata warnings (`report:107`; `metadata_verification.md:96,119`).

{table(['Sample','Legacy','V2 / evidence','Interpretation'],[
('Retrieval Barrier','5,652 words / 513 lines; nine sections','15,886 words / 1,364 lines; Stage0 +22 +audit; durable run and partial ledger','Broader explicit figures/tables/maths/evidence/validity structure; no review attestation. Legacy lines6-509; v2:324-705,726-1002,1222-1364.'),
('WebArena','4,751 words /451 lines','9,029 words /956 lines; rendering limitations disclosed','V2 separates axes of method, metrics, caveats and coverage; claims of visual inspection remain self-report. v2:5-19,840-944.'),
('ToolHijacker','5,094 words /606 lines','No v2; unique 18-page scratch extraction','Legacy-only output with partial newer attempt; not never processed.'),
('WebInject','No legacy','No v2 or evidence','Representative no-processing-artifact source; title page accessible. Processing matrix row webinject_comprehensive_summary.md.'),
('AgentVigil/AGENTFUZZER','No legacy for either','Two v2 drafts of probable related versions','Filename differences cannot establish independent contributions; first-page identity contradicts AGENTFUZZER filename.')])}

INFERRED: richer v2 structure improves explicit traceability opportunities but cannot prove higher scientific correctness. Both generations remain valuable artifacts. Historical documentation should be preserved read-only as 48-paper analysis and taxonomy seeds, not relabeled as complete expanded-corpus synthesis.
''')
write('DUPLICATE_AND_VERSION_REPORT.md',f'''# Duplicate and version report

{E}

## Exact content duplicates

OBSERVED: SHA-256 of every discovered PDF yields 117 files, 112 distinct hashes and five groups of two. All extra copies are archived under 99_Duplicates/Exact; no hash duplicates exist between active canonical paths. No exact pair uses differing filenames. The full paths/hashes are in `CORPUS_INVENTORY.csv`.

{table(['Active source','Archived identical path','SHA-256'],[(g[0],g[1],next(c['sha256'] for c in C if c['path']==g[0])) for g in S['duplicate_groups']])}

CONFLICTING: all five historical inventory `exact_duplicate_of` fields still point to New paths, not their surviving canonical locations (`docs/paper_inventory.csv:114-118`). Byte identity resolves the relationship in this audit without editing those records. The reference's ingest-first hash representative would depend on its new papers-directory scan order (`ZIP!rebuild/scripts/litrevctl.py:131-140`); do not let it silently choose new canonical identities.

## Report-version groups

{table(['Group','Observed evidence','Classification / safe treatment'],[
('Mind the Web (two PDFs)','Same four authors and near-identical title; first-page visual shows ACM ASIA CCS 2026 DOI 10.1145/3779208.3805968 versus arXiv:2510.04965v2 dated 20 Oct 2025; distinct SHA values and abstract wording','PROBABLE_ALTERNATE_VERSION, high identity evidence; preserve separate manifest IDs, no scientific-equivalence adjudication.'),
('AGENTFUZZER filename / AgentVigil filename','First file metadata/title says AgentVigil: Generic Black-Box Red-teaming, arXiv:2505.05849v4 14 Jun 2025; other says AgentVigil: Automatic Black-Box Red-teaming, EMNLP 2025 pp23159-23172; same nine authors','PROBABLE_ALTERNATE_VERSION; stale AGENTFUZZER filename is not another system. Both v2 aliases preserved; inspect semantic deltas before contribution grouping.')])}

Evidence: each corresponding source PDF p.1, text extraction and direct visual inspection during audit; CSV `title_evidence`, `version_relation`, `notes`. Similarity scan over normalized filenames at >=0.87 found these two pairs only; it is a candidate generator, not an exhaustive proof that no other bibliographic relationships exist. Metadata and title-page checks cover all 117 PDFs. No full paper comparison was performed.

{table(['Path','Pages','SHA-256'],[(c['path'],c['pdf_pages'],c['sha256']) for c in C if any(x in c['filename'] for x in ['Mind_the_Web','AGENTFUZZER','AgentVigil'])])}

UNKNOWN: exact independent-study/contribution count. If these two groups each represent one contribution, 112 reports would give 110 candidate groups; do not publish that as adjudicated research-object count. Existing docs only list the Mind-the-Web filename pair (`docs/near_duplicate_candidates.csv:2-3`), so automated folder/hash handling has not resolved the additional AgentVigil relationship.

## Manual review and taxonomy

OBSERVED: 98_Manual_Review has no files, yet two version relationships require semantic review; the directory is not a comprehensive review register. Both organizers classify by ordered filename regexes and assign tags, preserving near-title candidates without auto-merging (`organize_agentic_web_crawlers_new_preferred.py:70-328,510-568`). Original and New-preferring variants disagree on duplicate canonical preference (`original:353-369`; `new_preferred:353-376`). Exact executed flags are unknown. Keep historical aliases, hashes, paths, and version uncertainty during any future import.
''')
write('PROVENANCE_AUDIT.md',f'''# Provenance audit

{E}

The table describes retained generation provenance, not fingerprints newly measured by this audit. An observed current hash must never be backdated as proof of historical input. Evidence: legacy/v2 artifact metadata and headings; `analysis/baseline.json:papers`; `checkpoint.json:papers`; Retrieval run/log/ledger; `scripts/generate_summary.ps1:22-31,202-212`.

'''+table(['Field','Legacy summaries','V2 summaries','Durable evidence workflow','Checkpoints'],[
('Source path','PARTIALLY_RECORDED','PARTIALLY_RECORDED','CONSISTENTLY_RECORDED','CONSISTENTLY_RECORDED'),
('Source generation hash','NOT_RECORDED','PARTIALLY_RECORDED','CONSISTENTLY_RECORDED','CONSISTENTLY_RECORDED (observed now)'),
('Prompt generation version/hash','NOT_RECORDED','PARTIALLY_RECORDED','CONSISTENTLY_RECORDED (hash only)','CONSISTENTLY_RECORDED (current hash only)'),
('Model','NOT_RECORDED','PARTIALLY_RECORDED','PARTIALLY_RECORDED (log)','NOT_RECORDED'),
('Codex/runtime version','NOT_RECORDED','PARTIALLY_RECORDED','PARTIALLY_RECORDED (log)','NOT_RECORDED'),
('Generation timestamp','PARTIALLY_RECORDED (history/mtime bounds)','PARTIALLY_RECORDED','CONSISTENTLY_RECORDED','PARTIALLY_RECORDED (one embedded run)'),
('Extraction method','UNKNOWN','PARTIALLY_RECORDED','CONSISTENTLY_RECORDED (accessibility/code)','NOT_RECORDED'),
('Attempt number','NOT_RECORDED','NOT_RECORDED','NOT_RECORDED','NOT_RECORDED'),
('Retry history','NOT_RECORDED','NOT_RECORDED','NOT_RECORDED','NOT_RECORDED'),
('Script generation version/hash','NOT_RECORDED','NOT_RECORDED','NOT_RECORDED','NOT_RECORDED'),
('Configuration','NOT_RECORDED','PARTIALLY_RECORDED','PARTIALLY_RECORDED (log)','PARTIALLY_RECORDED (batch/concurrency)'),
('Extraction/image input hashes','NOT_RECORDED','NOT_RECORDED','NOT_RECORDED','NOT_RECORDED'),
('Output hash at generation','NOT_RECORDED','NOT_RECORDED','NOT_RECORDED','CONSISTENTLY_RECORDED (observed now)'),
('Validation results','UNKNOWN','PARTIALLY_RECORDED','PARTIALLY_RECORDED','CONSISTENTLY_RECORDED (structure only)'),
('Human/source review','UNKNOWN','PARTIALLY_RECORDED (one partial ledger)','PARTIALLY_RECORDED','CONSISTENTLY_RECORDED (no valid attestations)')])+f'''

“Consistently” for durable evidence refers to its single observed run and implemented contract, not a large sample. Legacy source mapping can now be reconstructed for all 48, but is not embedded historical generation provenance. Older timestamps bound existence rather than prove exact runtime. No human identity or approval should be invented.

## Strongest retained run

OBSERVED: Retrieval `run.json` records source hash `745d721cf4fa003ef45b64d33373cbd42f211f09659c5b572d7601e5ef608fde`, prompt `{D['prompt_sha256']}`, source/target paths, PID25136, start 2026-09-07T15:21:40.4174564Z, finish 15:34:25.7474625Z and generated_requires_source_review. The log records Codex0.153.0, gpt-6-astra, provider openai, medium reasoning, read-only sandbox, session01a07c75-faac-7091-8d47-44861e956780 (`generation.log:5-14`), the full current prompt and 89,825 reported tokens (`:5461-5462`). This does not establish billing cost or account balance.

OBSERVED: ledger explicitly says partial review, pages10-11, with remaining source revisit outstanding (`ledger.md:3,8-17,35-39`). Review registry is empty and review.md absent. V2 self-reported completeness is not an independent attestation. The current run metadata has no draft/script/image hashes, semantic versions, attempt number, package version or immutable acceptance record.

## Preservation and target contrast

OBSERVED: old/new Retrieval article and all 15 PNGs have identical hashes, but old accessibility metadata contains a less cautious missing-page claim. ToolHijacker scratch has no newer retained equivalent. Treat both as historical evidence, not disposable caches. Git ignore rules exclude much of this evidence (`analysis/.gitignore:1-7`).

REFERENCE_TARGET_ARCHITECTURE: target metadata, source locators, artifact relationships and version pins provide a useful model (`ZIP!rebuild/references/provenance.md:5-48`; `db/schema.sql:69-89,179-224`). However controller artifact input_hashes are four run-input hashes, not complete source/image/code fingerprints; skill bundle is a version label, not a content hash (`litrevctl.py:74-88,292-293`). Schema path is stored as schema_version. The controller updates mutable SQL evidence records while retaining bundle files. Preserve imported historical provenance separately from target acceptance metadata and never fabricate missing fields.
''')
