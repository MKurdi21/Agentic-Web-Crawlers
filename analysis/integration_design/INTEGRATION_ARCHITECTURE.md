# Integration Architecture

Components: common.py enforces the fixed design/shadow boundary and OS coordinator lock; db.py is the only connection constructor; artifact_store.py publishes immutable bytes; validate_semantics.py implements parsing/schema/formats/semantic/cross-record checks; litrevctl_v2.py coordinates leases, authoritative revalidation, events and disposable views. migrate_shadow.py imports; verify_equivalence.py independently reconciles; backup_shadow.py tests backup closure. Package creation is a separate allowlist workflow.

All current-data DBs live under shadow/. Copied historical content lives exclusively under shadow/private_source_material/ and is NEVER_PACKAGE. Data-bearing runtime trees are excluded in their entirety. Packageable exports contain selected paths,aliases,hashes,statuses and counts, not original content. No .agents hierarchy, active AGENTS.md or plugin manifest is created.

The OS lock serializes cooperating coordinators; SQLite transactions serialize DB writes. Neither protects against arbitrary direct DB editors or other-host filesystem writers. Runtime/source fingerprints and artifact hash checks detect relevant drift. The SQLite and filesystem integrity models are separate. Loss of an accepted blob is critical, even when SQLite integrity_check returns ok.
