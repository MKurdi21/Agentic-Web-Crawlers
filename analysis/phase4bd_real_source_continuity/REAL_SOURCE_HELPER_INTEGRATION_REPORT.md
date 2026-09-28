# Real-source helper integration

The unchanged parent `analysis/phase4br_remediation/candidate_v4br/hardened/scripts/pre_access.py` validates a report allowlist, required pre-access bindings and actual source hash. It durably creates a pre-access record and then an access record before returning bytes. Its ordering check alone does not validate all report bindings. It does not acknowledge the worker packet, update the canonical recovery consumption state, or register scientific milestones. Called alone, it can return source bytes without the recovery layer's consumption commitment.

Phase 4BD wraps that actual helper; it does not substitute a synthetic source driver or edit the parent. The wrapper verifies every helper pre-access binding, both access-event report and source identity, exact packet acknowledgement and review, and all protocol pins. Its access/consumption commitment and delivery-authority receipt precede transport to a fresh worker. Partial helper records are reconciled against the authoritative chain; wrong-identity events fail before adoption.

The authorization registry contains only consumed B01. The source hash is `26a3f0426ee1d533e4dd9f62d1343a7a1d231fe718cfaf3a362cc7de829ae913`. Source paths/identities are metadata in the fixture; source-derived field bytes are confined to private development test storage. No B02–B08 source is parsed or passed to a worker.

The integration closes a transport/state gap only when final tests and review pass. It does not certify that future full scientific extraction is accurate or that a future holdout run has been authorized.
