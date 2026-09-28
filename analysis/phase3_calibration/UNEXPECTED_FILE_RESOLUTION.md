# Unexpected-file correction

**OBSERVED.** The original Phase 2 residue `analysis/integration_design/shadow/private_source_material/raw/staging_4c7a64d312574b388369b65d14dbfe1f.tmp` remains byte-identical: 36,772 bytes, SHA-256 `63ca4afd25dbd54113e53d633cc578d2ea01f19aef74fd8820bf0073856a1e80`. It matches the historical ACE summary but is neither a valid content-addressed blob nor an allowed control file.

The v3 reconciler classifies it `UNEXPECTED_FILE` with reason `ABANDONED_STAGING_RESIDUE`; Phase 2 is preserved rather than repaired. V3 permits only its bound metadata control file, content-addressed blobs, and active temporary files under `.staging/<run_id>/<submission_id>/`. Root-level `staging_*.tmp` files and unmatched staging files fail closed.

The mandatory valid/control/unexpected/missing/corrupt/orphan scenarios pass. A clean v3 store requires `MISSING_REFERENCED_BLOB == 0`, `HASH_MISMATCH == 0`, and `UNEXPECTED_FILE == 0`. Orphans stay visible and policy-controlled.
