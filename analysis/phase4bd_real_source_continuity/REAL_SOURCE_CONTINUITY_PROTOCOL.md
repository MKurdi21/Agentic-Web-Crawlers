# Real-source continuity protocol

Version: `phase4bd-real-source-continuity-v1.0.0`. Scope: authorized, already-consumed B01 development transport and durable recovery. This is not scientific validation or authorization to open B02. Parent scientific, context, path and recovery versions remain unchanged; their exact pins are in the baseline and integration manifest.

## Authorization and pins

An explicit, hash-pinned registry binds report identity, development identity, source-file identity, exact source hash/path, role and prior consumption. The Phase 4BD registry authorizes only consumed B01 and denies all seven reserved report identities. No title-based resolution or synthetic-only source substitution occurs. Source hashes are checked before transport and again on delivered bytes. Frozen packet assets are resolved by the inherited containment guard. Runtime dependencies require exact inventory and content hashes before their scientific worker imports. The scientific worker is a deterministic fresh subprocess, not a human or separate-context model verifier.

The integration fingerprint covers code, worker contract, tests, schemas and executed parent dependencies. The immutable dependency manifest additionally pins the complete third-party inventory, verified at runtime. Code revisions during implementation invalidate earlier real-test fingerprints; completed inherited suites remain evidence about their unchanged test modules. No prior-phase file is edited.

## Delivery sequence

1. Resolve the authorized report and source; stream-hash the real PDF without interpreting it.
2. Verify methodology, context, containment, recovery and integration pins. Build the exact generic packet and check its binding.
3. Apply the static deny scanner and separate-context model semantic review. The B01 identity exception is limited to two schema fields; historical content in the body is still rejected. Review binds exact packet, task-wrapper and review-protocol hashes. This metadata relies on trusted orchestration and is not human approval.
4. Start a fresh worker. It receives only the generic packet, current identity, declared stage and source-size/hash metadata. Obtain its actual exact-packet acknowledgement before sending any PDF bytes. Commit the acknowledgement as an immutable recovery milestone.
5. Call the unchanged real helper to create its pre-access receipt. Commit the integration pre-access wrapper linking that receipt, acknowledgement, roles, source identity and all pins.
6. Under the OS-held coordinator lock, commit source intent; append and flush the one `SOURCE_ACCESS_BEGAN` event; materialize consumed state; commit the immutable consumption receipt. The event is the irreversible authority if a crash precedes state projection.
7. Call the real helper's `open_source` on B01. It commits its own source-access record before returning real bytes. Validate both helper identity and ordering. On recovery, verify the existing helper event instead of duplicating it. Hash the bytes again.
8. Commit delivery authority linking the helper event, consumption receipt, source hash and authoritative access event. Validate the entire chain and consumed projection before returning bytes to the worker transport.
9. Persist a scientific-unit intent, deliver bytes, parse one development field and its locator, and commit the structured result. An incomplete unit is never a scientific acceptance.

The worker extracts the first nonempty text line of PDF page 1. Its TEXT_SPAN binds the SHA-256 of the NFC-normalized extracted representation and Unicode-code-point offsets in that same representation. The second unit independently recomputes that field from the same source. Both are development-only transport exercises, not full extraction, accuracy estimates, verification of scientific claims, or promotion. Actual values and all source-derived outputs remain private.

## Recovery and replay

Validate canonical state/genesis, receipt chain, packet acknowledgement, pre-access receipt, source intent, access event, consumption and delivery authority before continuation. Missing or conflicting links block. Receipt-backed outputs are authoritative; loose output files are not. A valid access event permanently establishes consumption even if the state snapshot is stale. Failed delivery never restores untouched status.

Same committed unit and input fingerprint returns the registered result without another authoritative unit or consumption event. An uncommitted replayable unit is quarantined by the inherited recovery engine and restarted with a new attempt. Repeated recovery can append recovery diagnostics; it cannot duplicate scientific commits. B01 remains consumed even before a new run opens its bytes because its prior status is consumed.

`cli.py recover RUN` and `cli.py verify RUN` reconstruct from disk in a new coordinator process. They print metadata only. A fresh worker acknowledges the rebuilt exact packet. No previous conversation, recovery explanation, other-paper findings or adjudication is inserted into that worker's input. The inherited continuity key `known_scientific_milestone` means a known transport checkpoint before any scientific commit, and thereafter a verified receipt chain; `fresh_packet_review` means a still-valid exact-byte review, not a newly performed model review.

## Boundaries and limitations

This is application-level ordering and process-crash evidence, not a cross-filesystem transaction, OS sandbox, arbitrary-power-loss guarantee or Drive-synchronization guarantee. The worker inherits local filesystem permissions; direct malicious calls to prior helpers are outside this governed entry point. Hash chains do not authenticate against an actor rewriting every authority file. Reviewer identity is orchestration evidence, not production authentication.

Independent review noted further deployment hardening opportunities: explicit rejection of dependency-root Windows junction/reparse ancestors, ignoring optimized-Python environment flags, and timeout-bounded startup acknowledgement. The tested environment and exact source/dependency paths are recorded; these limitations must remain visible in any later authorization discussion. None permits Phase 4BD to release a reserved source.
