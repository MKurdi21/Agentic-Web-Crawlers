# Provenance Model

Track observed_at separately from historic generation time and import events. Current source/prompt hashes do not prove what generated an old summary. The retained Retrieval run/log and partial ledger remain raw authoritative provenance evidence;36 other drafts and48 legacy summaries have unknown per-run provenance. No model/prompt history is backfilled.

Accepted artifact provenance records exact source hash,attempt and stage pins. Declared semver+SHA pins coexist with measured effective code/schema/runtime hashes and the preserved heavy-prompt hash for relevant stages. Events retain acceptance,rejection,lease,run,pin and invalidation history. Raw bytes remain immutable registrations; changes create new records, not overwritten evidence.

Trusted synthetic review receipts hash their actor/time/input/rationale/pins payload into the event history; content changes invalidate them. Production trust is unconfigured and fails closed. The event ledger is append-oriented with update/delete triggers, not a cryptographic defense against a privileged DB administrator. Filesystem flushes, timestamps and hash checks do not certify historical scientific review.
