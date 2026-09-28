# State drift and consistency report

Severity expresses impact on reconstruction/integration, not a scientific verdict. OBSERVED findings are established from files; code-derived risks are labeled INFERRED and are not evidence of a corruption event. Target-package defects are separate in EXISTING_VS_PROPOSED_ARCHITECTURE.md.

## Observed current-system findings

| ID | Severity | Finding | Evidence / treatment |
| --- | --- | --- | --- |
| D01 | MEDIUM | README historical 48-paper/root-Security-Borderline description conflicts with 112 active source reports in numbered folders | README.md:3,18-38; CORPUS_INVENTORY.csv; TOP_LEVEL_INVENTORY.csv. Preserve as historical; do not repair. |
| D02 | MEDIUM | 96 broken PDF-link occurrences for 48 former source paths in docs/papers.md; papers survive elsewhere | LINK_RECONCILIATION.csv gives every file/line/target; docs/papers.md:23-70. 49 other local links resolve. |
| D03 | MEDIUM | Five duplicate_of pointers use absent historical New paths | docs/paper_inventory.csv:114-118; actual hashes still match canonical sources. |
| D04 | LOW | Two near-version original_path pointers use absent New paths | docs/near_duplicate_candidates.csv:2-3; current matching hashes in inventory rows57-58. |
| D05 | HIGH | AGENTFUZZER filename actually contains AgentVigil preprint; another AgentVigil proceedings PDF and draft exist | Both source PDF p.1 metadata/text/visual inspection; CORPUS_INVENTORY.csv. Preserve aliases; probable same-contribution risk to synthesis counts. |
| D06 | MEDIUM | Toward Secure LLM Agents venue uncertainty is not carried consistently in all historical prose | Root report:107 TOSEM versus docs/metadata_verification.md:96,119 and docs/papers.md:745 warnings. No external resolution attempted. |
| D07 | HIGH | 37 structurally complete drafts have no review attestations; rich self-reported coverage must not become verified completion | reviews.json empty; summary_state.py:115-123; Retrieval ledger.md:3-39. Workflow correctly distinguishes these; finding is an integration hazard/provenance gap, not checkpoint mismatch. |
| D08 | MEDIUM | Two retained older scratch directories are not represented by stage completion; ToolHijacker has extraction but checkpoint pending | Checkpoint pending is correct by its definition. ARTIFACT_INVENTORY.csv; checkpoint.orphan_candidate_directories; CURRENT_STATE_MODEL.md. |
| D09 | INFORMATIONAL | Baseline has36 drafts; current has37, solely Retrieval Barrier addition | AUDIT_MEASUREMENTS.json:baseline_changes. Expected progress, not unexplained drift. |
| D10 | INFORMATIONAL | Saved checkpoint is dated September7 but still matches all current source/draft/final hashes/statuses | AUDIT_MEASUREMENTS.json:checkpoint_differences=[]; no refresh performed. |
| D11 | MEDIUM | Current checkpoint hashes do not prove the 36 recovered drafts used current prompt/source bytes at generation | checkpoint papers[].generation_provenance; no original per-draft run metadata except Retrieval. PROVENANCE_AUDIT.md. |
| D12 | LOW | current_repo.txt is a prior filesystem listing, not a checkpoint; includes stale cache listing | current_repo.txt headings/date rows versus current inventory; no scripts read it as state. |

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

## Final preservation observation

OBSERVED: all pre-existing non-Git research/control files and the original reference ZIP remain byte-identical. Git status outside audit outputs is unchanged. Git-internal metadata did change: the index differs and Codex turn-diff capture files were added/replaced. The audit issued no Git mutation command and intentionally modified no pre-existing file; exact metadata writer attribution is UNKNOWN. Do not interpret this as an all-Git-bytes-unchanged guarantee. Full paths and before/after hashes are in PRESERVATION_CHECK.json. The session also observed PowerShell7.6.5 initially and7.6.6 after recovery; both environment observations are retained.
