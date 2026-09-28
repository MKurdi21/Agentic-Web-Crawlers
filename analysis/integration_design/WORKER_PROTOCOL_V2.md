# Worker Protocol V2

Tasks contain task/attempt/run IDs,worker,token,generation,expiry,source hash,report,stage,pins and disjoint outbox. Results contain the corresponding identity envelope,submission ID,kind,output path and full byte hash. Worker output paths must resolve inside that attempt's outbox without symlink/junction escape. Workers do not write shared SQLite or CAS. Controller CLI offers no model generation or deployment command.

Replay identity is (run_id,task_id,attempt_id,submission_id); the digest covers the canonical envelope plus actual output hash. Identical replay returns the original receipt without fresh acceptance; changed payload under the same key is a critical conflict. Historical receipt replay never restores an invalidated pointer. Lease expiry is checked at acceptance,not merely at reap. Generation and current-attempt checks reject superseded/retried workers.

Source mutation after dispatch records a new source observation and invalidates the current task; old outputs may be retained as rejected historical evidence but cannot win for the new source. The source-byte hash,not mutable path alone,is the provenance identity. Human-required outputs need a current trusted receipt bound to exact output/source/pins; no live trust backend is available.
