# Architecture sources

Official pages were inspected during the approved plan revision on2026-09-13. They inform proposed engineering,not CURRENT_SYSTEM facts. No external literature validation occurred.

- [SQLite foreign keys](https://www.sqlite.org/foreignkeys.html): Explicit per-connection enabling and queried verification.
- [SQLite PRAGMAs](https://www.sqlite.org/pragma.html): EXTRA/DELETE; separate integrity_check and foreign_key_check; metadata.
- [SQLite WAL](https://www.sqlite.org/wal.html): Same-host limitation; no distributed sync guarantee.
- [SQLite backup](https://www.sqlite.org/backup.html): Use backup API then independently verify snapshot.
- [JSON Schema2020-12](https://json-schema.org/draft/2020-12/json-schema-validation): Structural and format semantics separated.
- [Official Codex skills](https://learn.chatgpt.com/docs/build-skills): Focused triggers,progressive disclosure,deterministic scripts.
