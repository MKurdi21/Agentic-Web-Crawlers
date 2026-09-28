# Phase 4 Lane A: holdout validation

**Result: `HOLDOUT_VALIDATION_FAIL`.** The frozen Phase 3 workflow was applied to six untouched reports. The primary pass produced 264 field slots and 233 evidence items. A separate-context Codex verifier reviewed all 209 critical items and the 18 items selected by the frozen lower-risk sample. This is model-based source verification, not independent human source review or trusted-human approval.

The verifier reported 43 critical primary/verifier disagreements, including 42 locator failures, two quantitative errors, and four detected primary false accepts under its strict classification. Two decisive quantitative findings were separately checked by the coordinator against the exact source representations:

- H03 VisualWebArena: the primary `results.quantitative` field labels **16.37%** “best overall”; the source's later Appendix B/Table 5 reports **19.78%** for GPT-4o and explicitly compares it with 16.37%. The 16.37% figure belongs to the main baseline table and requires that qualifier. See the private H03 exact-source page 8 and page 13 text snapshots; source SHA-256 and item ID are in `HOLDOUT_DISAGREEMENTS.csv`.
- H04 AgentDoS: the primary `results.negative` field says **three** of 20 agents yielded no reported vulnerability. Source Table 2 has **four** zero-vulnerability rows: Quivr, Owl, Bisheng, and Taskweaver, consistent with 16 affected agents. The page-15 locator also fails to establish that numeric claim. See the private H04 source-derived layout and Table 2.

The H06 qualitative result is marked `NOT_LOCATABLE` at its supplied page-27 locator. The remaining disagreements remain excluded from supported conclusions pending source adjudication; none is silently treated as supported. No critical error was granted scientific acceptance, and no live scientific state changed. The detected defects mean the frozen workflow did not pass this holdout challenge. Lane B is prohibited by the Phase 4 dependency gate.

No critical false acceptance can be claimed absent. The defensible finding is that **four primary critical false accepts were detected by separate-context model verification**, with the two numeric defects above independently checked by the coordinator. `ground_truth_critical_false_accepts` remains `UNKNOWN` because no qualified human-reviewed ground truth exists.

The methodology cannot now be tuned against these six reports while preserving their status as untouched validation evidence. Any corrected methodology needs a new version and a new untouched holdout for another independent challenge. See `HOLDOUT_VALIDATION_METRICS.json` for named denominators and per-report counts.
