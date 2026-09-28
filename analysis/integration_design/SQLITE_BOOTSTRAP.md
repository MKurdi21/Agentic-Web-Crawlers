# Sqlite Bootstrap

db.connect is the only sqlite3.connect site. Existing opens use mode=rw or mode=ro; no accidental creation. Creation and backup_target are explicit and require absent destination. Connection-local PRAGMAs are set outside transactions,queried and compared; persistent application/user identity is initialized only for new destinations. Required metadata is NON_AUTHORITATIVE_SHADOW,UUID and exact schema SHA.

Foreign keys must read back1. A missing row,unsupported PRAGMA,wrong journal mode,synchronous mismatch,wrong application ID or user version is a failure. Do not rewrite existing metadata to pass verification. Read-only opens verify identity and then query_only. integrity_check and foreign_key_check are both required because the first does not detect FK violations.

Tests deliberately misconfigure only synthetic fixtures to verify rejection. All normal commands fail closed on unsupported settings; no FULL fallback is allowed. EXTRA is the chosen shadow DELETE profile; actual filesystem/device guarantees remain outside this test evidence.
