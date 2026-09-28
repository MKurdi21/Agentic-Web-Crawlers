# Per-report pre-access receipt protocol — 1.0.0

Construct a fresh report-specific context packet from the frozen methodology and current-report inputs only. Verify immutable-code equality and current source identity using metadata/hash access. Write PRE_ACCESS_RECEIPT.json with exclusive creation, flush/fsync, close and byte readback before substantive interpretation. Required bindings: phase, holdout/report ID, paper ID, source-file ID/hash, immutable candidate manifest hash, methodology hash, protocol hashes, field-catalog hash, holdout state, context protocol version, creation time, and substantive_source_access_started=false.

The source-access helper refuses absent/mismatched receipts and unapproved report IDs. It reads bytes to confirm the source hash, writes a separate SOURCE_ACCESS_BEGAN event bound to the receipt, then releases bytes to analysis. Physical hashing reads precede that event; substantive interpretation must not. Never backdate, overwrite or reconstruct a pre-access receipt. Sequence 1 must precede sequence 2; timestamp ordering is supplementary.

Validation must explicitly authorize one current report after the prior report gate passes. No next-report source read, rendered page, extraction or verifier task before its receipt. Sequential stopping and fresh-context construction remain mandatory.

This is application-level enforcement with auditable receipts, not an OS sandbox, human proof, or arbitrary power-loss guarantee. Direct tool access outside the helper must be prevented by orchestration and independently audited. If isolation cannot be established, stop before another reserved report is opened.
