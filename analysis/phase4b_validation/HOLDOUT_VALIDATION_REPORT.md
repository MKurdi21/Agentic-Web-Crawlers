# Phase 4B holdout validation

**Lane A2: HOLDOUT_VALIDATION_FAIL.** The frozen per-report gate failed on B01, the first of eight selected reports. B02–B08 were not opened for scientific review; Lane B is `NOT_RUN_GATE_BLOCKED`.

B01 used 44 primary field slots and 131 candidate evidence items. The complete lower-risk set had four items and the frozen algorithm selected three. Three fresh separate-context model verifiers covered all 127 critical items and the three selected lower-risk items. They classified critical items as 44 supported, 78 partially supported, three ambiguous, and two contradicted. They flagged 80 critical primary support decisions for correction or qualification; 83 critical items were not fully supported by model verification. These are model findings, not independently human-adjudicated ground truth.

The unchanged scientific validator rejected the candidate payload with `COMPARATIVE_FALSE_SUPPORT: TARGET_LOCATOR_MISMATCH`. Earlier serialization errors and the original payload are retained privately. The paper itself contains unresolved conflicting tool totals and attack-success figures; neither was silently resolved. Because no valid candidate evidence artifact emerged under the frozen workflow, the coordinator failed the per-report gate and accepted nothing. Thus `critical_errors_left_accepted = 0` describes a fail-closed rejection, **not** successful scientific validation. `ground_truth_critical_false_accepts = UNKNOWN`.

The immutable candidate inputs matched their frozen manifest before and after B01; the pre-access whole-candidate check also passed. No methodology was tuned against B01. No qualified independent human source review occurred. B01 is consumed validation evidence. The seven later reports retain an untouched/not-run state pending any separately designed future protocol.

The actual source and verifier records remain under the private Phase 4B area. This report omits full source text and substantive excerpts so it can be packaged.
