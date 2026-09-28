# Deterministic lower-risk verification sample


Selection algorithm version: `sha256-lexicographic-v1`.

Freeze this algorithm before substantive extraction. Determine membership only after the complete eligible lower-risk evidence set exists for a current validation unit.

For each item, use canonical UTF-8, Unicode NFC normalization, lowercase hexadecimal SHA-256 values, and literal zero-byte separators:

```text
stable_item_id =
    "ei_" + SHA256(
        source_sha256
        || "\x00"
        || stable_field_id
        || "\x00"
        || canonical_claim_json
        || "\x00"
        || canonical_locator_json
    )

selection_digest =
    SHA256(
        protocol_sha256
        || "\x00"
        || validation_unit_id
        || "\x00"
        || paper_id
        || "\x00"
        || stable_field_id
        || "\x00"
        || stable_item_id
    )
```

Canonical JSON recursively sorts object keys, emits UTF-8 with normalized strings, retains schema-required nulls, and has no insignificant whitespace. Exact duplicate claim-and-locator records collapse to one candidate item. Row order, extraction order, filesystem order, timestamps, runtime randomness, and language-runtime hashes are forbidden inputs.

For each concrete unit:

```text
N = eligible lower-risk evidence-item count
sample_size = min(N, max(3, ceil(0.25 * N)))
```

Sort by lowercase `selection_digest`, then `stable_item_id`, and select the first `sample_size`. Generate `VERIFICATION_SAMPLE_MANIFEST.json` before lower-risk verification. Record the eligible count, sample size, item IDs, selection digests, protocol hash, field-catalog hash, candidate-set hash, algorithm version, and generation time.

A changed protocol hash creates a new sample version. Never combine samples across protocol versions without separate denominators and explicit disclosure.

The validation_unit_id is the current holdout identifier supplied in the binding. This is the inherited calibration_unit_id hash input slot; its position and bytes are unchanged. Use the frozen scientific protocol SHA-256, not a packet hash, as protocol_sha256.
