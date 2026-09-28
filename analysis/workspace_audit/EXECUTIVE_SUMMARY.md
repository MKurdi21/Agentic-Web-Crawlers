# Executive summary

Evidence labels: OBSERVED = directly established; INFERRED = interpretation of observations; UNKNOWN = insufficient evidence; CONFLICTING = sources disagree. CURRENT_SYSTEM refers only to live files outside the reference ZIP and audit outputs. Archive citations use `ZIP!rebuild/...:lines` and refer exclusively to REFERENCE_TARGET_ARCHITECTURE. Recommendations are PROPOSED_INTEGRATION, not executed changes.

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

## Final preservation observation

OBSERVED: all pre-existing non-Git research/control files and the original reference ZIP remain byte-identical. Git status outside audit outputs is unchanged. Git-internal metadata did change: the index differs and Codex turn-diff capture files were added/replaced. The audit issued no Git mutation command and intentionally modified no pre-existing file; exact metadata writer attribution is UNKNOWN. Do not interpret this as an all-Git-bytes-unchanged guarantee. Full paths and before/after hashes are in PRESERVATION_CHECK.json. The session also observed PowerShell7.6.5 initially and7.6.6 after recovery; both environment observations are retained.
