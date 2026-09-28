# Phase 4B holdout selection protocol

`selection_protocol_version = phase4b-holdout-selection-v1`  
`selection_timestamp = 2026-09-16T22:10:09.012716+00:00`  
`methodology_fingerprint = ab28253c49940db4cd28ba0ea224185c8f3b03289312dba3c64322a33d95f1bb`  
`selection_snapshot_sha256 = 1572346145712e26ad83657b06ec574e60b0e2612c2edf19763d8e9ea64d64c5`  
`holdout_sha256 = 5dd9b5edd41f93912290058731c6304e24d657470ff1a45835b5522bd10b0536`

The eight-report holdout was selected **after** methodology version `phase4r-scientific-v2.0.0` was frozen and before scientific inspection of these reports. Selection used only the Phase 2 report crosswalk and Phase 1 corpus category/title/page-count metadata plus source-hash confirmation. It is a challenge set for quantitative, comparative, negative, availability, security, benchmark, long-horizon, crawler, survey, and multimodal workflow behavior; it is not statistically representative of all 112 reports. These dimensions are selection intentions inferred from bibliographic and structural metadata, not assessed paper findings.

Exclusions: all 15 Phase 3 calibration reports, six consumed Phase 4 reports, exact duplicate physical copies, unresolved version/contribution groups, and any report substantively opened during Phase 4R. Every selected report is an active manifest identity with a distinct verified source hash and no recorded version relation. Synthetic fixtures contain no additional report identity. One report fills each stratum; preferred IDs and rationale are frozen in the CSV.

If a preferred report later proves ineligible through metadata drift **before Phase 4B substantive access**, a new version must select an eligible active report from the same audit category by lexicographically smallest source SHA-256 after applying the same exclusions. Record the replacement and new CSV hash. Never use Phase 4R failure details or apparent likelihood of success to choose a replacement. Once Phase 4B begins, contamination or methodology tuning invalidates untouched status and requires a new validation set.

Phase 4R may confirm identity, source hash, processing state, and pre-existing artifact inventory. It may not extract claims, results, locators, taxonomy codes, summaries, or reuse judgments from these eight sources. No PDF content was opened during selection. The empty `PHASE4B_HOLDOUT_CONTAMINATION_LOG.json` records this boundary; Phase 4B must recheck it before Lane A2.

Selection inputs and exact SHA-256 values are recorded in `PHASE4B_HOLDOUT_SELECTION_RECEIPT.json`. Report identities and source hashes are frozen in `PHASE4B_VALIDATION_HOLDOUT.csv`.
