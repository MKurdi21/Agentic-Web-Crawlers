# Controller v3 changelog

- Added database-bound `artifact_store_id`, root binding, and exact metadata-control validation.
- Retained six disjoint classifications: `VALID_REFERENCED_BLOB`, `EXPECTED_CONTROL_FILE`, `ORPHAN_BLOB`, `MISSING_REFERENCED_BLOB`, `HASH_MISMATCH`, and `UNEXPECTED_FILE`.
- Stages publication on the artifact filesystem under `.staging/<run_id>/<submission_id>/candidate.tmp`; flushes, closes, hashes, publishes without overwrite, and registers only the final immutable path.
- Existing hash-addressed bytes are independently rehashed before reuse; conflicting bytes fail with `BLOB_INTEGRITY` and are never overwritten.
- Root-level or unmatched staging residue fails reconciliation. Crash tests prove fail-closed detection before synthetic-only cleanup.
- Reconciliation emits database/store identity, roots, entry classifications, failure reasons, and a scan fingerprint.
- Added eight focused v3 store tests while preserving all inherited safety semantics. Final suite: 58/58 pass; Phase 2 reported 50/50.

No live controller, script, skill, checkpoint, or database was modified.
