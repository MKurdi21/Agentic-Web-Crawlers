# Durable preemption and recovery

Version: phase4bc-recovery-v1.0.0. This additive Windows toolkit does not change scientific or context rules and contains no real source-delivery implementation.

## Authority and commit
Under a single-writer OS byte lock: persist exclusive intent with run/unit/attempt, exact pins, expected outputs and replay policy; stage and flush/readback bytes; exclusively publish final outputs; exclusively publish immutable receipt linked to preceding receipt; append/fsync hash-linked event; atomically replace same-directory canonical state. A receipt, not an output filename, commits a unit. Recover receipt-before-journal and journal-before-state crashes from the same receipt. No overwrite of accepted output ownership is permitted.

Genesis pins and bindings are immutable trusted inputs. State cannot redefine them. Validate run identity, immutable intent, input digest, output scope, prior receipt, event receipt references, and current state anchor. Missing bytes, altered bytes, receipt gaps/branches or missing committed receipts block. This is integrity against accidental interruption, not authentication against an attacker replacing the entire trusted genesis and all records.

## Lock and failure
RUN_LOCK.json describes PID, Windows creation-time evidence, session, heartbeat and status. The OS lock decides exclusion; timestamps/PIDs alone do not authorize reclaim. Unknown owner liveness blocks. Reused PID with different creation time is recorded separately. ACTIVE_OPERATION.json must exactly equal persisted intent at commit. A failed preflight creates an active durable failure latch. Begin/commit/finish cannot bypass it; only a successful full recovery may clear it.

## Recovery
Every recover-and-continue request requires preflight: journal, canonical state, genesis pins, live bindings, receipt chain, event/state commit anchors, owner lock, active intent, uncommitted files, source-consumption and packet pins. Supplied observations must be independently computed; actual path bindings are rehashed by the engine. Model recollection and prose are not commit evidence. Unknown unregistered outputs receive a logical quarantine inventory and block; partial expected files move into private quarantine before a new attempt. Staging bytes remain preserved with quarantine records. CAN_REPLAY_SAFELY and REQUIRES_CLEAN_RESTART both use new attempts after quarantine; MUST_NOT_REPLAY blocks until authoritative side-effect evidence resolves it. Same unit/input committed receipt returns existing outcome; different input conflicts. No generic exactly-once external side-effect claim.

Missing state conservatively blocks. Truncated JSON state can reconstruct from genesis, valid receipt chain and source-access journal; a parseable invalid state is not silently repaired. Torn non-newline terminal journal records are preserved, hashed and linked to a new segment. Corrupt committed/interior records block; no truncation. Recovery diagnostics and all failed test attempts remain preserved.

## Source and context
Before source access, untouched status additionally requires no substantive bytes reaching any context. After access, consumption is permanent. Same-report continuation requires exact source/method/context/packet pins, committed scientific milestones, fresh clean packet review and unambiguous acceptance. The synthetic continuity booleans test mechanics only: they cannot authorize real continuation. No real source API exists here; future evidence-backed adapter and separate authorization are required. Never feed recovery history, diagnoses, previous outcomes or coordinator prose into workers. Saved or new Codex sessions both undergo identical durable preflight.

## Preemption
Record USAGE_HEADROOM_UNKNOWN when no account telemetry exists; do not infer quota percentages or promise uninterrupted work. Near exhaustion blocks a new expensive scientific unit. Persist PREEMPTED_BY_USAGE_LIMIT when tools remain available; otherwise recover from the last receipt. Distinguish scientific failure, context failure, controller failure, environment blocker, usage preemption, user stop, tool failure and unknown interruption. Natural safe points: pre-access, extraction commit, verification commit, report gate; later authorized rehearsal import/snapshot/restore/rollback boundaries.

## Durability and testing
Flush/fsync/readback, exclusive publication and atomic state replacement are process-crash controls. No arbitrary-power-loss, filesystem, disk/controller, Drive-sync or distributed-lock guarantee. Synthetic SQLite checks run integrity_check and foreign_key_check separately and quarantine corruption without repair. Runtime tests and backups stay NEVER_PACKAGE. CLI offers init, begin, commit, preempt, recover and finish; recover performs quarantine/replay reconciliation. Requests are JSON; no arbitrary scientific source launch.

Documentation: https://learn.chatgpt.com/docs/codex/cli (session resumption), https://learn.chatgpt.com/docs/pricing (usage estimates, not account balance), https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-createsymboliclinkw and https://knowledge.workspace.google.com/admin/drive/drive-faq-for-admins. Local observed results govern environment conclusions.
