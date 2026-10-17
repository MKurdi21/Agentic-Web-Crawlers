---
name: corpus-analysis
description: Resume and verify the academic PDF analyses in this repository using the saved rubric, stable paper mapping, cumulative evidence, and checkpoints.
---

# Corpus Analysis

Read `analysis/WORKFLOW.md` and `analysis/CHECKPOINT.md` from the repository
root. Read `analysis/PROMPT.md` before substantive analysis. Refresh the
checkpoint with `python scripts/summary_state.py`.

- Resolve a paper through `analysis/manifest.csv`; retain its summary filename.
  Deduplicate by SHA256, never by similar titles. Distinct versions stay separate.
- Treat existing `.summary_v2` files as drafts requiring source review. Heading
  presence, length, and the draft's own completeness claim do not verify coverage.
- Keep document inventory, numerical facts, visual inspection, and unresolved
  references in `analysis/evidence/<summary-stem>/`. For long works, update a
  cumulative ledger before synthesizing; do not concatenate chunk summaries.
- Label author claims, visible evidence, derived values, and analyst inference.
  A rendered page is not automatically an inspected page. Record actual review.
- Generation uses one paper per invocation and a durable log. Pass PDF and work
  paths as process arguments; per-paper environment variables previously caused
  cross-paper contamination with concurrent workers.
- On recovery, inspect process command lines. Never terminate the application's
  `codex app-server`. Reuse partial evidence before regenerating paid output.
- Promote a draft only after the source audit described in the workflow. Record
  reviewed source, prompt, and draft hashes so later edits invalidate approval.
