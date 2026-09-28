# Corpus source boundary

The manifest names 112 registered sources in exactly twelve numbered top-level research directories. Direct counts in those directories equal the manifest counts, and every registered source SHA-256 still matches the checkpoint. Those twelve paths are the only canonical discovery roots. `99_Duplicates` is counted separately as archived extra copies and all five hashes match registered sources.

The explicit roots are recorded in `CORPUS_BOUNDARY_POLICY.json`. `98_Manual_Review` does not contain a registered source and is not an approved root. A future corpus expansion must update the reviewed source policy and manifest deliberately. Ordinary execution of `python scripts/summary_state.py` now uses this boundary. PDFs under `analysis/`, `docs/`, `scripts/`, drafts, summaries, rehearsal, test, and source-delivery trees have no corpus authority from their extension.

The repair changes discovery and count scope only. It preserves all 112 paper records, their status, five duplicate mappings, source review criteria, and promotion criteria.
