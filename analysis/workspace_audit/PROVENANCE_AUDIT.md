# Provenance audit

Evidence labels: OBSERVED = directly established; INFERRED = interpretation of observations; UNKNOWN = insufficient evidence; CONFLICTING = sources disagree. CURRENT_SYSTEM refers only to live files outside the reference ZIP and audit outputs. Archive citations use `ZIP!rebuild/...:lines` and refer exclusively to REFERENCE_TARGET_ARCHITECTURE. Recommendations are PROPOSED_INTEGRATION, not executed changes.

The table describes retained generation provenance, not fingerprints newly measured by this audit. An observed current hash must never be backdated as proof of historical input. Evidence: legacy/v2 artifact metadata and headings; `analysis/baseline.json:papers`; `checkpoint.json:papers`; Retrieval run/log/ledger; `scripts/generate_summary.ps1:22-31,202-212`.

| Field | Legacy summaries | V2 summaries | Durable evidence workflow | Checkpoints |
| --- | --- | --- | --- | --- |
| Source path | PARTIALLY_RECORDED | PARTIALLY_RECORDED | CONSISTENTLY_RECORDED | CONSISTENTLY_RECORDED |
| Source generation hash | NOT_RECORDED | PARTIALLY_RECORDED | CONSISTENTLY_RECORDED | CONSISTENTLY_RECORDED (observed now) |
| Prompt generation version/hash | NOT_RECORDED | PARTIALLY_RECORDED | CONSISTENTLY_RECORDED (hash only) | CONSISTENTLY_RECORDED (current hash only) |
| Model | NOT_RECORDED | PARTIALLY_RECORDED | PARTIALLY_RECORDED (log) | NOT_RECORDED |
| Codex/runtime version | NOT_RECORDED | PARTIALLY_RECORDED | PARTIALLY_RECORDED (log) | NOT_RECORDED |
| Generation timestamp | PARTIALLY_RECORDED (history/mtime bounds) | PARTIALLY_RECORDED | CONSISTENTLY_RECORDED | PARTIALLY_RECORDED (one embedded run) |
| Extraction method | UNKNOWN | PARTIALLY_RECORDED | CONSISTENTLY_RECORDED (accessibility/code) | NOT_RECORDED |
| Attempt number | NOT_RECORDED | NOT_RECORDED | NOT_RECORDED | NOT_RECORDED |
| Retry history | NOT_RECORDED | NOT_RECORDED | NOT_RECORDED | NOT_RECORDED |
| Script generation version/hash | NOT_RECORDED | NOT_RECORDED | NOT_RECORDED | NOT_RECORDED |
| Configuration | NOT_RECORDED | PARTIALLY_RECORDED | PARTIALLY_RECORDED (log) | PARTIALLY_RECORDED (batch/concurrency) |
| Extraction/image input hashes | NOT_RECORDED | NOT_RECORDED | NOT_RECORDED | NOT_RECORDED |
| Output hash at generation | NOT_RECORDED | NOT_RECORDED | NOT_RECORDED | CONSISTENTLY_RECORDED (observed now) |
| Validation results | UNKNOWN | PARTIALLY_RECORDED | PARTIALLY_RECORDED | CONSISTENTLY_RECORDED (structure only) |
| Human/source review | UNKNOWN | PARTIALLY_RECORDED (one partial ledger) | PARTIALLY_RECORDED | CONSISTENTLY_RECORDED (no valid attestations) |

“Consistently” for durable evidence refers to its single observed run and implemented contract, not a large sample. Legacy source mapping can now be reconstructed for all 48, but is not embedded historical generation provenance. Older timestamps bound existence rather than prove exact runtime. No human identity or approval should be invented.

## Strongest retained run

OBSERVED: Retrieval `run.json` records source hash `745d721cf4fa003ef45b64d33373cbd42f211f09659c5b572d7601e5ef608fde`, prompt `21dd3b9e6cd783df7c7ff7c40543a620c4d4cbbb54990dc560a33f3b5a557988`, source/target paths, PID25136, start 2026-09-07T15:21:40.4174564Z, finish 15:34:25.7474625Z and generated_requires_source_review. The log records Codex0.153.0, gpt-6-astra, provider openai, medium reasoning, read-only sandbox, session01a07c75-faac-7091-8d47-44861e956780 (`generation.log:5-14`), the full current prompt and 89,825 reported tokens (`:5461-5462`). This does not establish billing cost or account balance.

OBSERVED: ledger explicitly says partial review, pages10-11, with remaining source revisit outstanding (`ledger.md:3,8-17,35-39`). Review registry is empty and review.md absent. V2 self-reported completeness is not an independent attestation. The current run metadata has no draft/script/image hashes, semantic versions, attempt number, package version or immutable acceptance record.

## Preservation and target contrast

OBSERVED: old/new Retrieval article and all 15 PNGs have identical hashes, but old accessibility metadata contains a less cautious missing-page claim. ToolHijacker scratch has no newer retained equivalent. Treat both as historical evidence, not disposable caches. Git ignore rules exclude much of this evidence (`analysis/.gitignore:1-7`).

REFERENCE_TARGET_ARCHITECTURE: target metadata, source locators, artifact relationships and version pins provide a useful model (`ZIP!rebuild/references/provenance.md:5-48`; `db/schema.sql:69-89,179-224`). However controller artifact input_hashes are four run-input hashes, not complete source/image/code fingerprints; skill bundle is a version label, not a content hash (`litrevctl.py:74-88,292-293`). Schema path is stored as schema_version. The controller updates mutable SQL evidence records while retaining bundle files. Preserve imported historical provenance separately from target acceptance metadata and never fabricate missing fields.
