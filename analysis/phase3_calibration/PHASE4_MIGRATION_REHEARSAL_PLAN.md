# Phase 4 non-destructive validation and migration rehearsal

## Entry conditions

Use the frozen v3 schema, semantic validators, locator model, automation matrix, verification protocol/threshold proposal, inactive skills, and research-object rules. Preserve the six-report holdout hash and deny tuning access until Lane A begins. Configure no live authority.

## Lane A — untouched workflow-validation holdout

Run the frozen methodology once on the untouched holdout. Measure structured extraction quality, critical-field correctness, locator performance, verification behavior, schema expressiveness, automation-policy behavior, and unexpected failures. Keep report-, field-, and evidence-item denominators explicit. Do not tune during this lane.

If a serious defect requires change, version the methodology, reclassify the original holdout as development evidence, select and freeze a new untouched set using an approved protocol, and repeat only if independent validation is still required. Never optimize repeatedly against the same holdout while calling it independent.

## Lane B — migration rehearsal

`preservation snapshot → fresh shadow import → independent equivalence validation → policy-configured candidate → representative evidence migration → backup → independent restore → rollback simulation → cutover simulation`

Run Lane B under a new non-authoritative boundary. Recheck SQLite configuration, `integrity_check`, `foreign_key_check`, artifact-store closure, backup fingerprints, exact rollback state, and package isolation. Report Lane A and Lane B separately. Passing rehearsal cannot erase a failed workflow-validation result.

Phase 4 remains non-destructive. It cannot migrate live authority, install skills, promote papers, or authorize production processing.
