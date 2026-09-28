# Pre-access timing

Future execution order: untouched/hash confirmation; immutable verification; build/bind/render; static scan; separate semantic review; freeze exact packet; durable exclusive receipt; fresh context; exact packet acknowledgement/context ID; approval/binding recheck; durable SOURCE_ACCESS_BEGAN; then interpretation of source bytes. Hashing for identity is allowed before interpretation.

Receipt binds holdout/report/source, immutable code, generic methodology and scientific parent, policy, template, rendered packet, scan/review records, context protocol, timestamp and source_access_started=false. Hash-linked exclusive events reject missing predecessors, wrong report, changed packets, stale approvals and replay. Flush/readback is not proof against arbitrary power loss.

The library tests this mechanism only with SYNTHETIC_TEST identities and caller-supplied synthetic bytes. Phase4BC provides no production source-release operation. B02 dry-run packets and manifests do not constitute a pre-access authorization. No reserved SOURCE_ACCESS_BEGAN event may be created. Future verifier item releases are separately bound and cannot replace the original report receipt.
