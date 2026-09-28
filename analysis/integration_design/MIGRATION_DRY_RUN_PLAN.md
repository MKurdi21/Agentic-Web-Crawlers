# Migration Dry Run Plan

Run migrate_shadow.py against shadow/current.sqlite3 only. Preflight all sources/artifacts against audit hashes and legacy predicates before a transaction. Run verify_equivalence.py independently. Repeat identical import and independently compare source/observation/report/artifact/accepted/relationship/review/event/record/unknown counts and semantic fingerprint. No unexpected growth is allowed.

Expected counts:112 sources,117 observations,112 reports,174 raw registrations,0 accepted worker artifacts,2 unresolved relationships,0 reviews,1 unique import event,0 structured scientific records,13 retained unknowns. Summary subsets are48legacy/37v2; legacy states75pending/37structural. Exact raw artifact count follows ARTIFACT_INVENTORY.csv and is not the count of unique CAS byte blobs.

After schema creation,each import and final comparison,require integrity_check exactly ok and zero foreign_key_check rows. Reconcile all raw registered paths/hashes independently. Stop on drift and preserve diagnostics; do not clean,rebaseline or repair live data. Read-only state comparison must never call summary_state.main.
