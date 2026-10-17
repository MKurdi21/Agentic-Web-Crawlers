# Research Mode

Research question: **Why Are Web AI Agents More Vulnerable Than Standalone LLMs?
A Security Analysis.**

All 112 completed summaries and records are linked in the [catalog](catalog.md).
Verified state: 112 completed, 0 pending, 0 exclusions, 0 failed/deferred.
The final19 request started at 93 and completed all 19 remaining papers through
nine two-paper batches and one final single-paper batch using the existing runner.
Five archived duplicates remain separate. All 186 starting deliverable fingerprints
and 11 protected-input fingerprints are unchanged. Both synthesis files cover 112.
All pairs pass existing checks; final regression tests passed 12 + 4.
Corpus processing is complete; no further dispatch is required.
See [handoff](../docs/RESEARCH_MODE_HANDOFF.md) and [completion report](CORPUS_COMPLETION_REPORT.md).
Previous [Iteration 3 completion](ITERATION3_VALIDATION.md#completion-addendum--2026-10-10)
and [pilot validation](validation.json) remain historical records.

From the repository root in PowerShell:

```powershell
python -m venv research/.venv
research/.venv/Scripts/python.exe -m pip install -r research/requirements.txt
research/.venv/Scripts/python.exe -B scripts/research_mode.py --inventory
research/.venv/Scripts/python.exe -B scripts/research_mode.py --limit 2
```

Omit `--limit 2` to process all remaining eligible papers sequentially. Repeat
`--paper <existing SummaryName>` to select papers; add `--retry-failed` to retry
failures. Requires the existing authenticated `codex` CLI. Model calls consume
the configured account allowance. Do not run multiple Research Mode commands
concurrently.
An account usage limit leaves the current paper pending and stops further model
dispatch. Resume after the provider's reset or restored allowance.

Outputs: `summaries/*.md`, `records/*.json`, `catalog.json`, `inventory.json`, and
`progress.json`. Records wrap the existing summary-schema object with comparison
fields and exact source quotations. Completed files are checked by fingerprint
on resume; changed outputs need renewed processing. Individual failures are
recorded without blocking other papers. Extraction, images, and logs remain in
ignored `evidence/`; originals and historical outputs are never overwritten.
Retained model responses are revalidated on resume without another model call.
If retained JSON or quotations fail checks, inspect and repair that output with
source evidence; the CLI preserves it rather than silently regenerating it.

Reused: twelve authorized corpus roots/scanner, stable manifest names, dual PDF
extraction and selected page rendering, comprehensive summary prompt, Codex
model interface, summary JSON schema and typed claims/page locators. Existing
taxonomy category paths are retained in every source record.

Bypassed: historical Phase 4B entry points, READY/COMMITTED transitions, freezing,
dispatch receipts, independent verifier requirements, adjudication, promotion,
experimental consumption transitions, and recovery orchestration. No historical
control is weakened. The user permanently retired B02â€“B08 reservations for ordinary
Research Mode on2026-10-14; all112 canonical identities are eligible. The separate
[retirement decision](HISTORICAL_HOLDOUT_RETIREMENT.md) preserves their true historical
states and discontinues the experiment without claiming scientific success.

Quality checks validate schema, required headings, source identity, page ranges,
and exact supporting quotations. They do not prove factual entailment or complete
visual coverage. Inspect outputs before using claims in a literature review.
Missing supplements, low-text pages and extraction limitations must remain
explicit. `progress.json` completion means deliverables passed these lightweight
checks, not historical scientific validation.
Very long papers use one model call and may exceed context or allowance limits;
their retained extraction can support staged manual analysis when needed.

Tests: `research/.venv/Scripts/python.exe -B scripts/test_research_mode.py` and
`python -B scripts/test_summary_state.py`.
