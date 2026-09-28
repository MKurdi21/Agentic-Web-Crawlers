# Versioning And Invalidation

Every run carries semver plus full SHA pins for code,runtime,worker protocol,source,normalization,prompt,summary/evidence schemas,verification,research-object,taxonomy,synthesis,gap/external policy. Tasks retain only stage-relevant declared pins plus measured effective code/schema/runtime and relevant heavy-prompt hash. Acceptance compares the saved task against current authoritative run configuration and measured implementation bytes, not only worker echo.

NORMALIZE consumes source/normalization; SUMMARIZE source/prompt/summary schema; EXTRACT source/prompt/evidence schema; VERIFY source/verification; RESOLVE_OBJECT source/object policy; CODE_TAXONOMY source/taxonomy. Common code/runtime/protocol changes invalidate all affected tasks. A taxonomy-only change does not invalidate normalization or summaries. Prompt changes invalidate summary/extraction and dependent verification,not already retained raw historical prose.

Invalidation traverses explicit task prerequisites and marks accepted pointers invalid while preserving blobs/events. Current structured records derived from invalidated artifacts cease to be eligible. Source A results never attach to B. Future schema migrations must preserve original pins and require explicit versioned migration adapters; changing user_version or schema hashes to bypass validation is prohibited.
