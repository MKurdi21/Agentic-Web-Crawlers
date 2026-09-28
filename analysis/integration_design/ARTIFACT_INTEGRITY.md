# Artifact Integrity

Database consistency and artifact consistency are different gates. artifact_store.reconcile enumerates files and independently hashes registry paths,reporting VALID_REFERENCED_BLOB,ORPHAN_BLOB,MISSING_REFERENCED_BLOB,HASH_MISMATCH,UNEXPECTED_FILE. Missing/mismatched accepted content is critical even if SQLite returns ok. Recovery refuses to rebuild views on such failure.

GC is dry-run by default and executable deletion is restricted to shadow/synthetic. It requires the coordinator lock,grace period,no artifact registration,and no retention reference. Raw historical registrations,accepted outputs,rejected/stale content and retained backup references are preserved. Private historical material is never deleted during Phase2. Temporary orphan files remain inventory items rather than silently discarded evidence.

Store directories are partitioned by database-path identity to keep independent tests from sharing acceptance candidates. Content is still deduplicated within a store. Publication verifies existing hash locations byte-for-byte. An integrity error records evidence and stops acceptance instead of overwriting suspicious bytes.
