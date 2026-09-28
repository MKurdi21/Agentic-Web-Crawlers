# Recovery authority boundaries

The coordinator uses the frozen recovery Engine exclusively under `durable_run/`.
Its state, events, genesis, intents, and milestone receipts are authoritative for
coordinator operations. Unreceipted report inventories and public exports outside
that directory are not inferred to be coordinator Engine outputs.

Root `RECOVERY_STATE.json` and `RECOVERY_EVENTS.jsonl` are disposable byte exports
of their `durable_run/` counterparts. They never establish authority, continuity,
consumption, or permission for source delivery. Recovery reads and verifies the
authoritative directory and its immutable bindings before regenerating exports.

The coordinator source-access-started flag remains false: report-local frozen
Engines and Phase4BD continuity records establish each report's irreversible
consumption and source-delivery authority. Never infer report consumption from
the root export or coordinator flag. Reconcile the report-local ACK, pre-access,
access event, consumption state, and atomic receipt before any continuation.

No source is delivered by coordinator initialization. An uninitialized root is
not permission to bypass report-local pre-access and durable consumption gates.
