# Executive Design

The package implements a NON_AUTHORITATIVE_SHADOW controller and lossless historical registration. It does not install or replace the live workflow. The audit starting point is 117 physical PDFs,112 reports,5 extra duplicate copies,48 legacy summaries,37 v2 structural drafts,0 verified,0 promoted,1 durable run,2 scratch workspaces and2 probable version groups. Independent SQL/filesystem reconciliation is in test_results/COMPATIBILITY_EXPORT.json; semantic second-import comparison is in IDEMPOTENCY_REPORT.json.

CURRENT_SYSTEM uses manifest aliases and filesystem-derived predicates. REFERENCE_TARGET_ARCHITECTURE proposed SQLite/leases/structured stages but admitted stale results and weak acceptance. PROPOSED_INTEGRATION preserves existing bytes and meanings before any authority change. The implementation separates raw registration, immutable artifact acceptance, and scientific adjudication. Human-required transitions have no live trust backend. Existing drafts remain unverified.

Read final test_results/COMPLETION_REPORT.json for actual gates and limitations; absence or failure is not a release approval. This is a migration-candidate shadow architecture, not production/deployment readiness. Live cutover, actual calibration review, trust configuration, contribution adjudication and sync durability remain unresolved.
