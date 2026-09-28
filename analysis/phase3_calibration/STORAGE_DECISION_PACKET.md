# Storage Decision Packet

Status: production path and owners unresolved.

## Options

| Profile | Strength | Material limitation |
|---|---|---|
| SQLite inside synced workspace | Convenient co-location | Sync is not a database-coordination protocol |
| Local non-synced SQLite | Best fit for single authoritative coordinator | Requires explicit backup ownership |
| Local SQLite plus verified Drive exports | Separates authority from distribution | Export scheduling and restore ownership required |
| Client/server database | Supports multiple machines | Adds operating and deployment complexity |

## Recommendation

Use local non-synced authoritative SQLite with controlled, independently verified backup exports to Google Drive. Keep immutable artifacts under a separately reconciled store and back them up with their own manifest. A healthy database does not prove artifact presence, and a database-only backup is incomplete.

SQLite Online Backup can produce a consistent database snapshot when completed, but that does not validate Drive synchronization or arbitrary device failure. Production location, backup owner, recovery operator, schedule, retention, and restore objectives require owner decisions.

Sources: [SQLite Backup API](https://www.sqlite.org/backup.html), [SQLite WAL limitations](https://www.sqlite.org/wal.html), [SQLite PRAGMAs](https://www.sqlite.org/pragma.html), [SQLite foreign keys](https://www.sqlite.org/foreignkeys.html).
