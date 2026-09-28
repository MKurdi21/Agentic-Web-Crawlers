# Migration Spec

Import preflight compares every audit PDF and artifact hash with current files; checks unique manifest aliases and read-only legacy structure predicates; requires the audited empty review registry. On drift, stop without repairing or silently rebasing. PDF bytes stay external; path/hash observations identify them. Stable report IDs are report_ plus the first24 hex characters of SHA256 of the unchanged SummaryName, with uniqueness enforced by SQL. Any collision is a hard failure.

Register all174 audit artifact rows as RAW_REGISTERED_HISTORICAL_ARTIFACT, preserving original path/kind and measured hash. Copy their bytes into private raw CAS before immutable registration. Preserve baseline,checkpoint,reviews as dated history references; content-addressed controls remain private. Preserve2 unresolved relationship candidates and13 audit unknowns. No worker acceptance, confirmed objects or scientific decisions are fabricated.

The first import transaction creates identities/observations/reports/artifact registrations/history/relationships/unknowns and one unique import event. Repeating the identical input fingerprint is a semantic no-op. Private orphan bytes from failed imports remain recoverable; metadata does not claim registration if the transaction rolled back. Exports round-trip manifest fields internally and expose only allowlisted metadata externally.
