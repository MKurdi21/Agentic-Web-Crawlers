# Phase 4B entry criteria

Phase 4B is a **separate execution phase**. Phase 4R does not authorize either Lane A2 or Lane B. Before Phase 4B starts, independently verify:

1. All 43 Phase 4 critical disagreement IDs have source-adjudication records and private source-evidence hashes; none disappears from the resolution matrix.
2. The known-failure gate passes: both confirmed numeric defects and the newly found sample-denominator error are corrected or fail closed; four originally detected false accepts remain unaccepted; 42 original locator failures have 38 source-bound proposals and four fail-closed states; zero unresolved critical item is counted supported.
3. Generalized mechanisms and candidate tests pass, including inherited safety tests. No safety test was deleted or weakened. Review the ten previously supported items newly scope-limited/fail-closed; do not relabel them as regressions without source evidence or silently restore their old support.
4. Root-cause closure and limits are recorded. Development performance on the six consumed reports is not independent validation.
5. `REMEDIATED_WORKFLOW_CONFIGURATION.json` still hashes the exact candidate code, schemas, validators, protocols, automation matrix, taxonomy, and inactive skills. Any validation-relevant change creates a new methodology version.
6. The eight-report `PHASE4B_VALIDATION_HOLDOUT.csv` still hashes to `5dd9b5edd41f93912290058731c6304e24d657470ff1a45835b5522bd10b0536`, all source identities match, and the contamination log remains empty. No holdout scientific content was inspected in Phase 4R.
7. Live and Phase 1–4 protected inputs remain unchanged. Live `source_verified = 0` and `promoted = 0` are independently rechecked without refreshing the checkpoint.

If any gate fails, Phase 4B cannot start until a versioned repair and, when validation independence is affected, a new untouched holdout are prepared. The independent final agent review was unavailable during Phase 4R due a usage limit; Phase 4B should obtain one where available and retain independent scripts/queries regardless.
