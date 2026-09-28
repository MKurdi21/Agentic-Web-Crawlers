# Phase 4 validation holdout selection protocol

```text
holdout_selection_protocol_version = phase3-holdout-selection-v1
selection_timestamp = 2026-09-14T14:28:28.259Z
selection_snapshot_sha256 = a315f1428f8bf244bc08653f2a6f9810ac79f9b6bcdd56e7d7b633cf1d049785
holdout_status = FROZEN_UNTOUCHED
```

## Purpose and methodological boundary

The Phase 4 validation holdout is an untouched challenge set for evaluating the frozen post-Phase-3 workflow outside the reports used to develop it. It is not intended to estimate statistically representative accuracy for all 112 active report identities.

Selection uses only audit metadata, corpus categories, manifest membership, processing state, bibliographic identity already recorded by the audit, page count, artifact-presence flags, and source hashes. No PDF content, summary content, evidence workspace, claim, result, method, locator, taxonomy code, or reuse quality was inspected to select the holdout.

The selected reports must not be scientifically analyzed during Phase 3. Phase 3 calibration findings cannot be used to change this selection.

## Frozen selection inputs

The selection snapshot is derived from these pre-existing metadata sources:

| Input | SHA-256 |
|---|---|
| `analysis/integration_design/test_results/COMPATIBILITY_EXPORT.json` | `6af7bf1d9bfe4364a421460c2c66c0aaeead7fbf0404650e03f80ceb7fc91785` |
| `analysis/manifest.csv` | `e3bf75767e8232ea73df524b00fa5a492cd83b1846405976a4e23a9e4c39344d` |
| `analysis/workspace_audit/CORPUS_INVENTORY.csv` | `0f70484b7207a9b2b22c64e14f9df27b5ea6d21e6cb0d17da71911d173383dbc` |
| `analysis/workspace_audit/DUPLICATE_AND_VERSION_REPORT.md` | `931b4640166940f02eec1cd0d812638d72761104c0742d408b06361eefcfd6da` |
| `analysis/workspace_audit/PAPER_PROCESSING_MATRIX.csv` | `645e7ea7906cbe9079265d5aadb2d28f51b1233d805011b212ddad600e0b219c` |

To compute `selection_snapshot_sha256`, normalize each input path to forward slashes, pair it with its lowercase hexadecimal SHA-256 using a literal zero byte, sort by normalized path, join records with a single LF byte, encode as UTF-8 without a byte-order mark, and hash the resulting bytes with SHA-256.

## Eligibility and exclusions

A report is eligible only when it:

1. Is an `ACTIVE_MANIFEST` report identity in the frozen audit metadata.
2. Has a current source hash matching the frozen audit hash.
3. Is absent from the 15 active Phase 3 calibration report identities.
4. Is not a known exact duplicate physical observation.
5. Has no recorded unresolved contribution or version relationship.
6. Has not been substantively inspected for Phase 3 before holdout freeze.
7. Fills no more than one selection stratum.

The Phase 3 calibration denylist is:

```text
report_f65b70426e7cad20f3bca498
report_e1a4d04452c57f69534e5603
report_4a25815942a0fae3db98433d
report_5f96daa6c80a1d5839a1d991
report_a4988586b3a9b60e43f89eda
report_97ce3e361031031820f35361
report_05dbe40340050b30d7fb7462
report_29316d7f064e35b04ddd17fa
report_17b162af40f95b9ba51cb157
report_23e9445a563eb86c07c0ac0b
report_d0c5b16dc9dbc30b0d49815f
report_c16f40cd135ffcbb595294e7
report_db40269d76c4e5b83043918b
report_da6cfb0488d945c042abd882
report_a772a6285ca222fd2e193e7f
```

## Strata and ordered preferred candidates

The first eligible report in each ordered list is selected. Each frozen list contains the plan's preferred identity. If that identity later proves ineligible because of baseline drift, select the eligible report with the lexicographically smallest lowercase source SHA-256 from the same audit category and record a new holdout version. Do not use scientific findings as a fallback criterion.

| Holdout ID | Selection stratum | Ordered preferred candidate |
|---|---|---|
| H01 | Attack/security plus multimodal interaction | `report_930591b4e381bdca32354589` — Attacking Vision-Language Computer Agents via Pop-ups |
| H02 | Defense | `report_c73e0d842744a9a2abde5d88` — PlanGuard |
| H03 | Benchmark/environment with structurally complex presentation | `report_7d2cce4b8b43e8ee55c33c36` — VisualWebArena |
| H04 | Resource exhaustion or availability | `report_5b76dc0b8a92199dbda22672` — Autonomy Comes with Costs |
| H05 | Web-agent architecture or long-horizon behavior | `report_021fa210d97cccf60f48987d` — WebVoyager |
| H06 | Traditional crawling with difficult or older source structure | `report_88cc32894edf81646c04e0ba` — IRLbot |

Stratum descriptions are corpus- and structural-metadata labels. They are not new scientific coding of the reports.

## Eligibility result

All six preferred reports passed the eligibility checks at freeze time:

- Their exact current PDF SHA-256 values equal their audit SHA-256 values.
- Each source hash occurs once in `CORPUS_INVENTORY.csv`.
- Each row is `ACTIVE_MANIFEST` with empty `duplicate_of` and `version_relation` fields.
- None of the six report IDs occurs in the Phase 3 calibration denylist.
- No evidence workspace was recorded for any selected report.
- Existing processing state was used only as metadata; existing summaries and drafts were not opened.

## Holdout access control

Allowed Phase 3 operations are limited to:

```text
identity confirmation
source hash confirmation
existing-artifact inventory
processing-state confirmation
structural metadata needed for selection
```

Forbidden Phase 3 operations include:

```text
claim extraction
scientific summary evaluation
structured evidence extraction
verification
locator-quality evaluation
research-gap analysis
taxonomy coding beyond existing metadata
methodology/results inspection for calibration
reuse-quality assessment
```

Every Phase 3 scientific task must apply the six `paper_report_id` values in `PHASE4_VALIDATION_HOLDOUT.csv` as a denylist. A forbidden operation must fail closed and append an event to `HOLDOUT_CONTAMINATION_LOG.json`.

## Contamination and replacement

If accidental substantive inspection occurs:

1. Mark the affected report `HOLDOUT_CONTAMINATED`.
2. Record the actor, timestamp, operation, material exposed, exposure extent, and affected methodological dimensions.
3. Preserve the original holdout row and contamination event.
4. Select an untouched replacement from the same audit category using the frozen fallback rule when possible.
5. Increment the protocol or holdout roster version, freeze a new CSV, and record its SHA-256 without overwriting the prior version.
6. Classify the contaminated report as development evidence and never represent it as untouched validation evidence.

If no eligible replacement exists, preserve the reduced holdout and document the corpus constraint. No report may be tuned against and then restored to independent-validation status.

## Phase 4 use

Phase 4 Lane A applies the final frozen post-Phase-3 methodology to this untouched roster without tuning during the lane. A serious defect that requires methodology changes invalidates this roster for subsequent independent validation: version the methodology, classify the inspected roster as development evidence, and select a new untouched validation set if independent validation remains required.

The holdout results will be reported separately from Phase 4 migration rehearsal results and will not be represented as full-corpus performance guarantees.
