# Phase 4B: untouched workflow validation, then non-destructive rehearsal

Phase 4B requires a separate explicit execution instruction. It begins by verifying the Phase 4R package, methodology fingerprint, source hashes, holdout CSV hash, contamination log, and protected-file baseline. The six former Phase 4 holdout reports are consumed development data; they must not be represented as independent validation.

## Lane A2 — new untouched holdout

Apply the exact frozen `phase4r-scientific-v2.0.0` candidate to the eight metadata-selected reports in `PHASE4B_VALIDATION_HOLDOUT.csv`. Open substantive source content only in Phase 4B. Use the v3 structured evidence schema, result inventory, atomic claims, typed support locators, derived-value provenance, five-layer validator, automation matrix, verification protocol, and inactive skill architecture. Check source tables and layout visually. Independently verify every critical claim and the frozen lower-risk sample; record source-bound disagreements, false accepts **detected**, locator failures, quantitative errors, and unresolved items with named denominators. Do not call another Codex agent an independent human reviewer. Without qualified independent human source review, the maximum scientific result is `HOLDOUT_VALIDATION_PASS_WITH_LIMITATIONS` and ground-truth critical false accepts remain `UNKNOWN`.

No methodology tuning is permitted against the holdout. A serious defect that requires a change consumes the holdout as development evidence, invalidates its independent-validation status, and requires a new version and untouched set. An unresolved critical item fails closed. No model or fixture can grant production trusted-human approval or set live `SOURCE_VERIFIED`/`PROMOTED`.

Lane B may begin only after Lane A2 returns `HOLDOUT_VALIDATION_PASS` or `HOLDOUT_VALIDATION_PASS_WITH_LIMITATIONS` with no mandatory blocker. A Lane A2 failure stops Phase 4B before migration rehearsal.

## Lane B — non-destructive migration rehearsal

Use a fresh non-authoritative runtime. Capture preservation and input snapshots, import the live workspace read-only, independently reconcile 117 physical PDF observations, 112 reports/source hashes, five duplicate extras, historical summaries and evidence, zero source-verified and zero promoted papers, and repeat the import to prove semantic idempotency. Exercise stale/late results, replay conflicts, source mutation, selective invalidation, trusted-review fail-closed behavior, and artifact-store reconciliation. Unresolved research-object relationships remain provisional.

Quiesce all logical writers for a cross-store snapshot. Capture a monotonic event watermark and accepted-pointer/registry set; back up SQLite and copy the exact artifact closure under the same snapshot ID. Test acceptance committing before the watermark and attempting after quiescence starts. Restore database and artifact closure as a pair, verify receipt/watermark/manifest/accepted pointers and blob hashes, and run `PRAGMA integrity_check` and `PRAGMA foreign_key_check` separately. Then perform matching-pair rollback and single-writer cutover simulation under Phase 4B-only markers. No live authority changes.

Report Lane A2 and Lane B separately. A technical rehearsal pass cannot erase a scientific validation failure. Preserve the package allowlist, private-source exclusion, original-file hashes, policy-status tracking, and AI-only conditional-readiness ceiling from the Phase 4 plan. Production deployment, promotion, skill installation, and Phase 5 still require separate owner authorization.
