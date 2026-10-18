---
name: corpus-analysis
description: Resume and verify the academic PDF analyses in this repository using the saved rubric, stable paper mapping, cumulative evidence, and checkpoints.
---

> Current scope notice — 2026-10-18: the 123-paper Research Mode working extension is complete. The original 112-paper foundation remains frozen at tag `research-foundation-2026-10-17-v1`; completed sources/outputs must not be regenerated. This skill documents the historical analysis workflow and is maintenance-only. Do not execute the refresh/resume instructions below for routine literature work. Read `docs/RESEARCH_FOUNDATION_HANDOFF.md`, `research/README.md` and `docs/DOCUMENTATION_SYNCHRONIZATION_AUDIT.md` first. Phase 4B is discontinued; historical evidence and retirement decisions remain unchanged. The primary proposal concerns task-dependent web-agent traps; the standalone comparison is secondary. Protocol amendments are proposals, not implementation authorization.
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
