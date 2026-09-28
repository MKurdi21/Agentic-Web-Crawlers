# Packet engine interface

Run Python with `-B`. `context_engine.py` uses the standard library. It never parses source PDFs, opens current-report source paths, invokes a shell, follows links, or starts agents.

## Composition

`build_packet(root, registry, allowlists, binding, role)` returns `(packet_bytes, metadata)`. The complete canonical JSON packet is the complete task wrapper; callers must not append narrative. Register every template as an ordinary explicitly allowlisted artifact. Paths are normalized relative to the context architecture root. Each artifact needs `artifact_id`, `path`, `sha256`, `layer`, `role`, `reason`, `permitted_content_category`, and `dependencies`. Roles are `primary`, `verifier`, `both`, `template_primary`, or `template_verifier`; delivery layers are only A/B. Current-report metadata belongs exclusively in the strict binding.

Registry shape is `{artifacts:[...]}`. Allowlists shape is `{primary:[artifact_id,...],verifier:[artifact_id,...]}`. Dependencies must also appear explicitly in the role allowlist; cycles and unknown dependencies fail. Markdown dependencies must be declared; executable context includes, external JSON references, path expansion, traversal and reparse points fail. Text is data: no import or substitution is performed.

Binding fields are exactly `phase`, `holdout_id`, `paper_id`, `source_sha256`, `methodology_sha256`, `context_protocol_version`, and `current_report_source`. Source state must equal `NOT_YET_OPENED`. Context version is `phase4bc-context-v1.0.0`. Actual scientific verifier items are not constructed during this phase; dry-run verifier packets contain the approved generic template and current identity only.

`verify_immutable(root,entries)` checks pinned path/size/hash entries, rejects extra files and reparse directories, and returns the manifest fingerprint. Use a dedicated immutable tree rather than a mixed runtime tree. The coordinator must independently pin the approved manifest and recheck it before release; regenerate-on-drift is prohibited.

## Review and release

`scan_packet(packet,deny)` accepts `{version,patterns:[{id,text,category}]}` and normalizes Unicode, case, whitespace, HTML entities, and common escaped characters. It returns exact packet and deny fingerprints. It does not detect arbitrary encoding, all paraphrases, or scientific truth. This implementation deliberately has no exemption facility: any hit blocks, so an occurrence-specific exception cannot accidentally become a broad suppression.

`review_record(...)` serializes a separately obtained semantic review. It does not conduct review, authenticate model identity, or certify human approval. The orchestrator must retain the actual fresh-context review result and its provenance. Synthetic review fixtures only test binding mechanics.

`release(packet,deny,static_record,semantic_record,builder_context_id=...,expected_binding=...,expected_packet_sha256=...,expected_review_protocol_sha256=...)` recomputes the static result, validates the whole canonical packet shape, checks the separately pinned digest, rejects self-review context IDs, and requires clean exact-hash semantic review under the exact separately pinned review protocol, with nonempty rationale. It returns `PACKET_DRY_RUN_APPROVED`, with `production_source_release_available=false`.

No public real-source release operation exists. This is intentional: readiness is preparation, and a future authorized execution must establish real source delivery and context identity assurance separately. Caller-provided reviewer/context IDs cannot by themselves prove isolation. Host/tool access is not an OS sandbox.

## Synthetic receipt sequence

`SyntheticSession(directory,binding)` accepts only `SYNTHETIC_TEST` with synthetic holdout/report IDs. `receipt` records exact packet, approval, method/source/policy/template/code pins and UTC time. `acknowledge` requires a prior receipt and exact packet, links the previous record, and records a fresh context ID. `deliver` accepts synthetic bytes (never a source path), requires both earlier events, unchanged approval/packet/source binding, then exclusively emits the linked access event before returning bytes. Duplicate events fail. Real B02–B08 bindings are refused at construction.

These events demonstrate synthetic sequencing and file flush/readback. They do not prove arbitrary power-loss durability or make the orchestration caller trustworthy. Private test storage is outside all package allowlists. The actual symlink integration test may be unavailable on the Drive filesystem; its failure/skip must remain reported separately from the deterministic mocked reparse-attribute guard test.

## CLI

`python -B context_engine.py build --root ROOT --registry REGISTRY.json --allowlists ALLOWLISTS.json --binding BINDING.json --role primary --output PACKET.json --metadata METADATA.json`

`python -B context_engine.py scan --packet PACKET.json --deny DENY.json --output SCAN.json`

Outputs use exclusive creation. Review/release/state APIs remain explicit library calls to avoid implicit source release. External orchestration records timestamps and higher-level packet-manifest fields; timestamps never enter deterministic packet bytes.
