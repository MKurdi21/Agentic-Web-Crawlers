from pathlib import Path
O=Path(__file__).resolve().parent
docs={
'CONTEXT_ARCHITECTURE.md':'''# Context architecture

The earlier stop is CONTEXT_DELIVERY_ARCHITECTURE_FAILURE, not SCIENTIFIC_METHOD_FAILURE. This phase has no scientific results for reserved reports.

Four layers: A contains generic executable scientific methodology; B frozen risk/sampling/acceptance policy; C exact current-report identity and, only in future authorized execution, current evidence; D historical development evidence is coordinator/developer-only. Worker packets permit A+B+C and never D. Registries, denylists, leakage mappings, test fixtures and scan hit details are control-plane material, not worker content.

The deterministic builder admits explicit registered IDs and checked hashes. Templates are allowlisted content, not an escape hatch. No recursive context discovery, broad globs, arbitrary coordinator strings or environment context expansion. Relative paths and every component are checked for traversal/reparse escapes. Referenced dependencies must themselves be explicitly permitted. Scientific/controller code stays out of the prose packet unless registered for a necessary role.

Scientific parent version remains phase4br-scientific-v3.0.0 (schema 4.0.0); parent fingerprint ad691060099fff81a3e75de6d4ffdfeb4a8906e006dbfbeefc80a6c601f1d07f is provenance, not a hash of new sanitized files. Generic-content hashes are new. Context architecture version is phase4bc-context-v1.0.0. Scientific semantic changes block this context-only readiness claim.

Canonical JSON uses NFC strings, sorted keys, UTF-8 and no insignificant whitespace; duplicate/normalized-duplicate keys and non-finite values fail. Text-file hashes bind original exact bytes. Aggregate hashes bind sorted path/size/hash records. Timestamps stay outside deterministic packet bytes. Methodology, policy, templates, binding, final packet and immutable code have distinct fingerprints.

Every exact rendered packet, including its task wrapper, is scanned and separately reviewed. Static scanning is not semantic proof. A separately recorded semantic verdict binds packet and review-protocol hashes. CLEAN is required. A builder-provided clean flag cannot substitute. Review identity authentication is an orchestration evidence boundary, not a software-generated human authorization.

Only synthetic source delivery is implemented in this phase. Real report packets are metadata-only dry runs and cannot unlock a source. Future live-source delivery needs separately authorized implementation/execution and the full receipt/context acknowledgement sequence. No agent is granted production trusted-human approval.
''',
'COORDINATOR_FIREWALL_PROTOCOL.md':'''# Coordinator information firewall

Create each future primary and verifier with fork_history=none. Build the complete task wrapper mechanically from reviewed templates plus current binding; do not append helpful history, lessons, prior errors, running metrics, report results or reviewer persuasion. Hash the exact dispatch, not a different draft. Tool-returned current evidence must preserve report/source/item binding.

Primary receives generic rules and current source only after its gate. Verifier receives a current atomic proposition, locator/support set and necessary current table/operand context, not the primary rationale or unrelated conclusions. Each later report starts clean. Historical diagnostic and packet-review contexts cannot serve as later scientific extractors/verifiers.

Ambient system/developer/repository/skill instructions remain visible in the execution framework; they must be inventoried at future dispatch. A fresh fork excludes conversation history, not shared filesystem access. This implementation is explicit input validation and an orchestration protocol, not an OS sandbox. Do not permit broad filesystem research tools in a validation task by policy; audit actual task inputs/access records. If meaningful isolation cannot be demonstrated, stop before source access.

Contaminated contexts are retired; their findings and context IDs are preserved. Never silently retry a dirty context with a clean label.
''',
'VALIDATION_CONTEXT_DENY_POLICY.md':'''# Deny policy

Default deny: only registered, hash-matching A/B artifacts and strict current binding enter worker packets. Historical layer D is forbidden regardless of filename or encoding. Control data containing forbidden terms is never delivered to workers.

Scan normalized case, Unicode, whitespace, HTML/common JSON escapes, known IDs/titles, distinctive numeric failure patterns, disagreement identifiers, prior metrics, coordinator narratives and prohibited historical paths. Paraphrase detection requires independent semantic inspection of exact rendered bytes. Neither technique proves complete leakage detection.

Any static hit blocks release. No blanket suppression or automatic exemption exists. A potential false positive requires an occurrence-specific, hash-bound disposition by a separate reviewer and a new reviewed release decision; until such an exception path is implemented and tested it remains blocked. UNKNOWN/UNRESOLVED semantic review cannot pass. Current-report scientific evidence in a future verifier can legitimately overlap historical terms; no automatic exemption is allowed.
''',
'PER_REPORT_PRE_ACCESS_RECEIPT_PROTOCOL.md':'''# Pre-access timing

Future execution order: untouched/hash confirmation; immutable verification; build/bind/render; static scan; separate semantic review; freeze exact packet; durable exclusive receipt; fresh context; exact packet acknowledgement/context ID; approval/binding recheck; durable SOURCE_ACCESS_BEGAN; then interpretation of source bytes. Hashing for identity is allowed before interpretation.

Receipt binds holdout/report/source, immutable code, generic methodology and scientific parent, policy, template, rendered packet, scan/review records, context protocol, timestamp and source_access_started=false. Hash-linked exclusive events reject missing predecessors, wrong report, changed packets, stale approvals and replay. Flush/readback is not proof against arbitrary power loss.

The library tests this mechanism only with SYNTHETIC_TEST identities and caller-supplied synthetic bytes. Phase4BC provides no production source-release operation. B02 dry-run packets and manifests do not constitute a pre-access authorization. No reserved SOURCE_ACCESS_BEGAN event may be created. Future verifier item releases are separately bound and cannot replace the original report receipt.
''',
'CONTEXT_ARCHITECTURE_CHANGELOG.md':'''# Context architecture changelog

phase4bc-context-v1.0.0 introduces four-layer separation, clean generic policy presentation, explicit registry/role allowlists, external deny controls, deterministic complete packets, distinct fingerprints, separate semantic review and synthetic-only receipt sequencing. Prior frozen packets and evidence remain unchanged.

This revision removes historical teaching examples and empirical history from worker context; it does not revise scientific thresholds or claim improved extraction accuracy. Semantic mappings and independent review must substantiate preservation. No silent re-freeze is permitted. Later architecture changes require new version, fingerprints, tests and review.
''',
'PHASE4B_RESUME_V2_PLAN.md':'''# Future resumed Phase 4B — not executed

Requires separate user authorization. Verify Phase4BC package/receipt, frozen context architecture, scientific parent and generic/policy/code fingerprints; verify all seven reservations from access records and source hashes only. B01 remains excluded development evidence. This is the seven-report remainder, not the original eight-report cohort or corpus accuracy sample.

Order B02→B03→B04→B05→B06→B07→B08. For each report, construct and independently scan/review exact current-only primary packet, commit durable pre-access receipt, create fresh context without prior history, acknowledge exact bytes/context ID, record access event and only then deliver source. Future real-source release is not implemented by the synthetic-only Phase4BC harness and must be supplied through separately authorized reviewed integration.

Complete all fields, result inventories, proposition/role support, arithmetic, document-wide comparisons, absence/conflict semantics, frozen sampling, fresh-context critical and sampled verification, adjudication and mandatory gate before opening the next. Preserve exact source/protocol pins and immutable equality before/after each report. No tuning against held-out findings. A mandatory failure stops immediately and preserves later sources; use no unopened source for diagnosis.

AI-only success remains PASS_WITH_LIMITATIONS; human ground-truth error counts remain UNKNOWN. No software satisfies trusted-human approval. Lane B stays blocked until the complete eligible sequence passes and separate authorization covers rehearsal. Retain all migration-equivalence/idempotency/replay/stale-source checks, separate SQLite/FK/store gates, paired quiesced backups, restore/rollback and single-writer simulations if reached. No live migration, promotion, checkpoint refresh or skill installation. Phase5 remains separately authorized.
'''
}
for n,t in docs.items():(O/n).write_text(t,encoding='utf-8')
for d in ['context_architecture/packet_templates','context_architecture/deny_rules','context_architecture/historical_forbidden','test_results','private_diagnostic_material']:(O/d).mkdir(parents=True,exist_ok=True)
print('Design reports',len(docs))
