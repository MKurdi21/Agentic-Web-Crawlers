# Path containment and content identity

Packet inclusion is governed by explicit logical identity, canonical containment, immutable content identity, and content classification, not by availability of symlinks.

`ALLOW = path_contained AND artifact_registered AND hash_matches AND classification_allowed`.

Guard accepts registered IDs from role-specific allowlists. Every root and ancestor is checked for link/reparse identity. Lexical NFC/separator normalization permits dot segments but rejects any parent segment, even exit/re-entry, alternate drives, device/UNC aliases, globs, environment substitution and ambiguous names. Containment compares path segments, never a string prefix. Duplicate/case-ambiguous identities fail closed. An in-root unregistered copy remains forbidden.

Strict resolution, lstat/reparse checks and the final opened-handle path precede byte inclusion. Windows uses GetFinalPathNameByHandleW; POSIX uses /proc/self/fd when available and strict resolution plus fstat identity otherwise. Before/after identity, size and modification-time checks detect changes; registered SHA-256 is mandatory. Unknown resolution fails closed. This is not a hostile-OS sandbox or atomic protection against every filesystem race or Drive synchronization behavior.

All transitive dependencies must separately satisfy registration, allowlist, hash and class. Cycles and undeclared includes/imports/references are rejected through the frozen parent reference checker. No broad directory trust or glob expansion exists. HISTORICAL_DEVELOPMENT_ONLY is never eligible merely because it is under a project root. Static and separate semantic packet release controls remain required after composition.

`parent_adapter.build_parent_packet` is the additive production composition entrypoint; no live installation or prior-code change occurred. Current-report binding remains separately schema-validated; generic assets are Layers A/B, not arbitrary source bodies. The report-independent continuity contract receives only exact approved current-report records.

Sources: https://docs.python.org/3/library/os.path.html#os.path.commonpath and https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfinalpathnamebyhandlew . Local executable tests establish this implementation's observations, not platform-wide guarantees.
