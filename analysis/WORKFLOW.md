# Paper Analysis Workflow

## Objective and Sources

Apply [PROMPT.md](PROMPT.md) to every canonical paper and save the verified
analysis under `Summaries/`. This prompt is a byte-for-byte copy of the user's
attachment `3d267782-cf7c-48fb-ad21-395bda471775/pasted-text.txt`; its SHA256 is
recorded in `checkpoint.json`. No external research is authorized by this
closed-document analysis request.

`manifest.csv` preserves the recovered 112-paper mapping, including the 48
established summary names. It was copied from `.summary_manifest.csv`.
Canonical PDFs are outside `99_Duplicates/`; currently there are 117 PDFs total,
112 canonical entries and five archived duplicates. Verify hashes before
excluding duplicates. Two different Mind the Web versions remain separate.
The state refresh reports new, missing, and colliding entries; investigate and
extend the manifest deliberately when the corpus changes.

## Recovery and Resource Use

1. Read `CHECKPOINT.md`, then run `python scripts/summary_state.py` from the root.
2. Inspect running generation process command lines and evidence directories.
   An unavailable old tool session does not alone prove a process has stopped.
3. Resume the next incomplete evidence record or pending paper. Existing drafts
   should receive source review instead of automatic regeneration.
4. The user selected two papers per batch on 2026-09-07. Run them sequentially,
   with one generation process at a time and a checkpoint after each paper.
   Each runner invocation handles one paper and refreshes state on exit.
5. On quota/rate failure, retain logs, text, images, and partial output. Do not
   retry in a loop. Record the interruption and resume after the constraint ends.
6. Refresh the checkpoint after each paper and before a handoff.

The account's remaining allowance and reset time are not available to these
scripts. Reduced concurrency lowers the request rate, not the total token cost.
Local inventory, hashing, extraction, and validation do not invoke a model.
No background scheduler or automatic unlimited queue is installed.

## Files and Authority

| File | Purpose |
|---|---|
| `PROMPT.md` | Exact analysis requirements; read before writing |
| `manifest.csv` | Stable PDF-to-summary mapping |
| `checkpoint.json` | Generated current hashes, structural results, counts and issues |
| `CHECKPOINT.md` | Generated readable progress and next work |
| `baseline.json` | Initial recovery fingerprints; never silently reset |
| `reviews.json` | Source-review attestations tied to exact hashes |
| `evidence/<summary-stem>/` | Extraction, images, ledgers, logs, review notes |
| `.summary_v2/` | Draft staging; not approved publication |
| `Summaries/` | Existing published summaries and verified replacements |

The checkpoint is regenerated from actual files. `pending` means no staged
draft; `structural_pass` means only the expected headings and minimum length
were found; `needs_repair` means those checks failed; `source_verified` requires
a matching review attestation; `promoted` additionally requires matching final
content. Changed fingerprints invalidate prior attestations. Old summaries in
`Summaries/` do not count as completed new-rubric analyses.

## Per-Paper Analysis

1. Confirm PDF identity and hash. Record accessible pages, appendices, missing
   supplements, extraction problems, and document type.
2. Inventory all substantive sections, subsections, figures and panels, tables,
   equations, algorithms, experiments, claims, limitations, and appendices.
   Keep original numbering and precise page locators.
3. Maintain `ledger.md` in the evidence directory before synthesis. Include
   terminology, numerical facts with conditions and units, claim/evidence links,
   experiments, uncertainties, cross-references, and coverage status per object.
   [REVIEW_TEMPLATE.md](REVIEW_TEMPLATE.md) supplies the reusable table structure.
4. Inspect every substantive visual; render additional pages or crops as needed.
   Compare native extraction and visual evidence; OCR only where useful and
   record disagreements. Do not claim absent supplementary files were read.
5. Draft Stage 0, all 22 sections, and an inventory-based completeness audit.
   Keep [A]/[B]/[C]/[D] distinctions; show operands for derived numbers.
6. Revisit the original source for every major claim and important number.
   Recheck model, dataset, condition, unit, uncertainty, and caveats. Verify every
   inventory item is represented, explicitly compressed, or marked inaccessible.
7. Correct the draft, record the audit in `review.md`, and attest only when the
   requirements above are met. The agent can perform this review within the
   user's authorization; no additional user approval is required.

Use cumulative analysis for documents too large for reliable single-pass work.
In particular, the 125-page Defeating Prompt Injections by Design, 81-page Hidden
in Memory, and 74-page Web Crawling need careful staged evidence handling.
Never interpret a single long output as proof these stages were performed.

## Generation and Verification Commands

`pwsh -File scripts/run_summary.ps1 -SummaryName <filename.md>` generates one
pending draft using the saved prompt. It retains evidence and logs and refuses
to overwrite a staged draft. This helper produces a draft; the cumulative
ledger and source review still require the analyst's attention.

`python scripts/summary_state.py` performs local checks and refreshes both
checkpoints. It never starts generation or promotes a file.

After source review, put an entry in `reviews.json` keyed by `SummaryName` with
`source_sha256`, `prompt_sha256`, `draft_sha256`, `reviewed_at`, and `notes_path`
pointing to the completed evidence review. Take hashes from a fresh checkpoint.
Attestations are declarations by the reviewer, not automated correctness proofs.

Before promotion, confirm the final file has not changed from `baseline.json`
(or the last reviewed version), inspect the diff, copy the verified draft to
its `FinalTarget`, and refresh state. Preserve any user edits. Promotion is
deliberate and does not require another approval from the user.

Only after analyses are verified should corpus docs be audited against them.
Update counts, links, categories, numerical claims, comparisons, and limitations
with traceable summary references. Do not treat unreviewed drafts as established
facts. Commit related changes in meaningful groups when committing is requested;
inspect user reorganization changes and never revert them.

## Recovered Limitations

At recovery, 36 drafts existed; their source-review status was unknown. The
previous two-paper retrieval-barrier/ToolHijacker batch was interrupted with
extraction directories remaining and no completed draft. The older worker
discarded logs and usually deleted evidence; its successful heading checks
cannot establish visual or numerical accuracy. Existing scratch evidence is
preserved for reuse. Earlier generations selected up to 56 scored visual pages,
did not perform OCR, and had no durable extraction ledger. Review these gaps
explicitly for recovered drafts.

The extraction field `appendix_pages_detected` is heuristic and can match an
in-text appendix reference. Verify actual appendix boundaries in the PDF.
Some extracted text contains NUL characters; use `rg -a` when searching it and
recheck affected notation visually.
