# Supplemental symlink result

**ENVIRONMENT_BLOCKED / SYMLINK_PRIVILEGE_BLOCKED**. G reports FAT32; local C reports NTFS. Regular-file positive control passed. The unchanged original Python real-file-link operation failed with WinError1314 before the guard could inspect a link. Thus no real-link identity or rejection was demonstrated; invariant remains unsatisfied. The original Drive error1 and local privilege error1314 are distinct. No settings, elevation, junction substitution or permissions changes occurred. Fixture cleanup succeeded.

Independent read-only reviewer confirmed original-method fidelity. Historical Phase4BC remains223 checks:222pass,0fail,1skip. Supplemental test is separately ENVIRONMENT_BLOCKED, not an extra passing test. Modern Python Windows symlink creation was the already-permitted non-elevated path tested; no equivalent evidence is claimed.
