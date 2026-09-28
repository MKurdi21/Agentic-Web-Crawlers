# Rollback Plan

Phase2 rollback requires no live restoration because live research/control authority was never changed. Keep the private shadow/test material until handoff review; no automatic cleanup of unique evidence. Failed test DBs are diagnostic specimens,not repaired production state.

For future cutover rollback: stop new claims;freeze/import outstanding outboxes as retained historical candidates;record accepted postcutover events and blobs;restore reviewed prior instruction/router/config mapping from exact backups;resume the old state engine only under separate authorization. Do not overwrite newer user-edited finals or reset the recovery baseline. New accepted artifacts survive rollback as preserved records even if not visible through the old workflow.

Backup validation requires separate reopen,application/schema metadata checks,integrity_check,foreign_key_check,semantic/event fingerprint comparison,and independently copied artifact closure. DB-only restoration is not a complete store backup. Any missing/mismatched accepted blob stops rollback validation; automatic repair is prohibited.
