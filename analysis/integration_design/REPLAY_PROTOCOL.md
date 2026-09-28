# Replay Protocol

Replay key=(run_id,task_id,attempt_id,submission_id). Its digest covers the canonical envelope and the actual submitted output hash. Same key+digest returns original receipt and does not append acceptance events or scientific upgrades. Same key+different digest rejects as REPLAY_CONFLICT and retains diagnostic evidence. A new submission ID cannot bypass current lease/source/stage/prerequisite checks.

An accepted historical replay remains a historical receipt after downstream invalidation; it does not set valid=1 again. Expired/reaped attempts cannot create new accepted results. Retries create new attempt numbers and lease generations; old tokens cannot heartbeat or win. Partial output preservation is independent of retry permission.

Replay is tested separately from identical historical import. Import idempotency preserves all semantic identity/relationship/count sets and unique events; command exit success alone is insufficient.
