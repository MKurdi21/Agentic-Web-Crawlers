# State And Event Model

Work states are PENDING,CLAIMED,RUNNING,RESULT_READY,ACCEPTED,RETRYABLE,FAILED,BLOCKED,HUMAN_REVIEW,SUPERSEDED,INVALIDATED. This release uses direct validated submission from CLAIMED/RUNNING; RESULT_READY is reserved for durable staging and never independently grants acceptance. Claim requires pending/retryable,remaining attempts and accepted prerequisites. Heartbeat requires live current lease/worker/token. Reaping expired active attempts supersedes them and permits bounded retry or terminal failure. Pin/source changes invalidate affected work and dependent pointers.

Attempts retain number,worker,token,lease generation,expiry,outbox,state. Tasks retain current attempt and expected source/pins. Artifacts retain immutable role and origin. Scientific report state is independently preserved during import. No generic SQL decision row enables production or bypasses prerequisites.

Events are append-only and record run/task creation,claim,heartbeat,reaping,acceptance,errors,source/pin invalidation and synthetic review content hashes. Replay receipts are unique per run/task/attempt/submission key. Events that represent unique transitions do not multiply on identical replay/import. Errors can append diagnostic events without rewriting accepted evidence.
