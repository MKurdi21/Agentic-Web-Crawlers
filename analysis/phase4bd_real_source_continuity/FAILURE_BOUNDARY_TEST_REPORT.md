# Failure boundaries

The completed real-source suite covers all required A–G boundaries using consumed B01. Tests 01–03 reject before acknowledgement, before pre-access, and before access respectively. Test 04 commits irreversible consumption then aborts before helper delivery. Tests 05–06 interrupt during delivery and after output generation but before unit commit; recovery quarantines incomplete attempts. Test 07 returns a committed unit without replay. Tests 21–22 recover an event-before-projection crash and a deliberately stale untouched projection without undoing consumption.

Tests 13–20, 27, 30–38 reject identity, protocol, stage and authority-chain problems. Tests 34–35 include malformed-but-committed/receipt-linked records, not only changes caught by a file hash. Private test corruption is invented or confined to copied development runtime; no prior phase or source is altered.

These are process-level fault injections, not arbitrary-power-loss tests. A committed access event before failed delivery intentionally leaves B01 consumed. Source-derived results and diagnostic scratch remain NEVER_PACKAGE. See REAL_SOURCE_CONTINUITY_TEST_RESULTS.json for exact test IDs and integration fingerprint.
