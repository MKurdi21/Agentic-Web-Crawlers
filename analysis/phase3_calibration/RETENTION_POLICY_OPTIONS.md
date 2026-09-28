# Retention Policy Options

Status: recommendation pending owner approval.

| Class | Recommended Phase 3 treatment | Proposed production default |
|---|---|---|
| Accepted artifacts | Preserve | Indefinite while cited or authoritative |
| Superseded artifacts | Preserve with supersession link | Retain for reproducibility |
| Stale/rejected results | Preserve | Retain through cutover; later policy-controlled archival |
| Orphan blobs | Inventory; no historical deletion | Quarantine, grace period, coordinator recheck, then authorized collection |
| Event/task history | Preserve | Append-only retention sufficient to reproduce decisions |
| Source snapshots | Preserve when acceptance depends on them | Retain with accepted evidence |
| Backups | Verify and retain by schedule | Owner-defined generations and restore objectives |
| Calibration artifacts | Preserve with protocol pins | Retain as development evidence |

Garbage collection must never delete accepted blobs, required event-linked evidence, retained raw history, active publications, or preserved rejected outputs. Phase 3 performs destructive collection only on synthetic fixtures.
