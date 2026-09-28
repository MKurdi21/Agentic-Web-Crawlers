# Backup Verification

backup_shadow.backup holds the coordinator lock and snapshots source identity,schema and all ordered semantic rows. It uses SQLite backup API through the same bootstrap,closes the destination,hashes it,and independently opens it read-only. Compare exact semantic snapshot before restoring a second DB copy and checking integrity/FKs again.

Copy referenced artifact hashes into a separate shadow backup store; real artifact bytes remain under private_source_material/backups. Independently verify those copied hashes against restored DB references. Record UUID,schema version/hash,time,event count,snapshot SHA,backup SHA,and check results. No raw DB or backup is packaged.

The backup is a verified candidate snapshot,not proof of Drive synchronization durability. Relocating immutable original registry paths to a new live deployment requires an explicitly reviewed location adapter; that future live operation is not executed. Backup reports disclose that boundary.
