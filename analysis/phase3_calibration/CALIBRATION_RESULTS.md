# Phase 3 calibration results

## Denominators

The development set contains **12 top-level categories**, **13 concrete calibration units**, **15 active report identities**, and **16 physical source observations**, including one additional exact duplicate observation. These are separate denominators.

## Measured calibration output

- 660/660 report-field slots received an explicit status.
- 143 source-located sanitized evidence items were produced: 142 critical and 1 noncritical.
- All 143 created items received a separate source-grounded coordinator pass labeled `NON_INDEPENDENT_SECOND_PASS`; zero received independent-model or human verification.
- 143 slots were `CORRECT_COMPLETE`, 487 were explicitly `NOT_EXTRACTED`, and 30 were `NOT_APPLICABLE`.
- All created items use source-hash-bound `PAGE` locators. Other locator types remain technically tested by the controller suite but scientifically unencountered or uncalibrated here.

This bounded result exposes a major operational constraint: the frozen 44-field catalog is substantially broader than the evidence extracted in this run. The missing slots are visible rather than imputed. Consequently, this exercise supports schema and workflow development but does not establish scientific completeness.

## Version and contribution findings

**Mind the Web:** recommend `SAME_CONTRIBUTION_VERSION`, pending trusted-human adjudication. The 13-page and 17-page reports are separate evidence-bearing versions. The inspected results differ: approximately 1,500 versus 2,000 candidates, about 300 versus 400 SFT examples, 61% versus 64% SFT, and 82% versus 85% SFT-plus-DPO. Results must remain version-specific.

**AGENTVIGIL:** recommend `SAME_CONTRIBUTION_VERSION`, pending trusted-human adjudication. Principal Tables 1–3 align in the inspected pair, while the arXiv version adds explicit limitations concerning cost and weak Claude transfer. Separate report identity and version-specific evidence must be retained.

## Material calibration findings

- Historical summary presence is useful for discovery, but no legacy/v2 artifact becomes accepted or source-verified through import.
- Retrieval Barrier remains a partial historical source review; ToolHijacker remains extraction-only historical evidence.
- The crawler-trap paper defers classifier implementation and operational testing; its title must not be interpreted as measured deployed-classifier accuracy.
- Sanitized records represented the selected propositions without a schema-expressiveness failure, but 487 unextracted slots prevent a broad automation claim.
- The untouched Phase 4 holdout remained uninspected scientifically and has zero contamination events.

No live state changed: `source_verified = 0`, `promoted = 0`.
