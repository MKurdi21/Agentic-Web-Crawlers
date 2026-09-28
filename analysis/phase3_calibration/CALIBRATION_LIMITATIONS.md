# Calibration limitations

Phase 3 is a **development and calibration exercise**. The 12 top-level categories, 13 concrete units, 15 active reports, and 16 physical observations are deliberately selected methodological probes. They are not statistically representative of all 112 reports.

The methodology was allowed to change in response to this development set. Therefore these results are not independent validation, production accuracy, generalization performance, or corpus-wide scientific validation. Phase 4 reserves an untouched six-report challenge set for post-calibration testing. Even a successful Phase 4 holdout would not establish full-corpus accuracy.

Only 143 of 660 field slots received a source-located value; 487 are explicitly `NOT_EXTRACTED` and 30 are `NOT_APPLICABLE`. Numeric claims outside the selected propositions were not exhaustively enumerated. Only PAGE locators were encountered in sanitized scientific records; the remaining locator variants have synthetic controller tests but no scientific calibration result here.

Independent subagents became unavailable during the run. Every selected item received a distinct source-grounded second pass by the coordinator, labeled `NON_INDEPENDENT_SECOND_PASS`. This is neither independent duplicate extraction nor trusted-human approval. Independent model agreement, if later obtained, would still not be human scientific approval.

No production human identity or authorization channel exists. `TRUSTED_HUMAN_APPROVAL` remains unavailable and production transitions that require it fail closed. The report/version dispositions are recommendations only.

The SQLite and artifact tests demonstrate internal behavior under the tested filesystem and failure injections. They do not prove durability against arbitrary power loss, filesystem/controller defects, Google Drive synchronization, or distributed writers.
