# Reconstruction and refactor decisions

Repository inspection found 112 mapped canonical PDFs in twelve scanner roots,
five duplicate archives, 48 older published summaries, and 37 structurally passing
drafts. Draft presence is not source verification. The root README's older
48-paper overview is historical; current inventory is `research/inventory.json`.

| Area | Existing component | Research Mode decision |
|---|---|---|
| A: PDF processing | Dual PyMuPDF/PyPDF2 extraction and selected-page rendering in `scripts/generate_summary.ps1` | Reuse the embedded extraction block verbatim, writing new local evidence |
| B: structured extraction | Integration-design `summary.schema.json` with typed claims, confidence and source locators | Reuse unchanged inside a record envelope; keep research comparison fields separate |
| C: source quality | Saved comprehensive prompt, evidence directories, structural checks, hash-bound reviews | Reuse prompt and source identity; check exact source quotations and physical pages; disclose review limits |
| D: catalog/comparison | Stable `analysis/manifest.csv`, taxonomy folders, `docs/paper_inventory.csv`, older 48-paper matrices | Keep names/categories/tags; create a separate current catalog and progress file |
| E: holdout validation | Ordered B02–B08 experiment and consumption receipts | Exclude all seven identities; do not run or modify the experiment |
| F: freezing/authorization | Historical READY/COMMITTED freezes, dispatch and acceptance controls | Keep historical entry points outside this CLI |
| G: recovery/scientific verification | Historical coordinator, verifier and adjudication protocols | Preserve records; use ordinary per-paper resumption for research outputs |

The ordinary `scripts/run_summary.ps1` already invokes the model without the
experimental READY/COMMITTED machinery. Its practical restrictions are refusal
to overwrite staged drafts, generation into the historical staging/evidence
locations, automatic legacy checkpoint refresh, and a separate source-review and
promotion workflow. It does **not** itself protect reserved holdouts. Therefore
Research Mode needs a separate safe selection/output path, not repairs to frozen
orchestration.

The current experiment's actual blocker is
`VERIFIER_DISPATCH_COMPLETION_CONTRACT_INCOMPATIBLE`, recorded in
`analysis/phase4b_b02_scientific_validation/primary_wire_recovery_v25_retry1/FINAL_HANDOFF.json`.
B02 is consumed with primary accepted, but verifier/adjudication are not run.
That historical result is preserved, not treated as ordinary processing progress.

Implementation plan used: add one sequential CLI, retain the existing scanner,
extraction, prompt, model interface and schema; use new outputs; exclude holdouts
before extraction; log individual failures; validate five eligible pilot papers;
document commands and limitations. No existing frozen implementation was edited.

Initial unrelated changes to AGENTS.md, checkpoint timestamps, and experimental
directories were retained. The current checkpoint pair passed its versioned
semantic policy. A Windows UTF-8 read failure and rejection of valid short table
quotations were reproduced, repaired and covered by focused tests.
