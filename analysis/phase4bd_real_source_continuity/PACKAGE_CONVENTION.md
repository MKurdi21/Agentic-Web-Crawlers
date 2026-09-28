# Packaging convention

The ZIP is built from a finite explicit allowlist; the independent validator owns a separate expected member set. Both must match the archive manifest. No private development sources, values, PDF files, inherited runtime copies, databases, backups, caches or prior archives are eligible.

The embedded PACKAGE_MANIFEST.json lists all release files except its own hash; membership is that list plus the manifest itself. PACKAGE_RECEIPT.json is external only and hashes the completed ZIP. The packaged FINAL_HANDOFF.json references that external receipt and deliberately contains no circular ZIP hash. After successful independent archive validation, the local external FINAL_HANDOFF.json receives the ZIP hash and an external-final edition marker. Its bytes therefore differ from the packaged handoff in that disclosed metadata only. The receipt records the packaged handoff hash. Durable completion receipts pin both editions through the package receipt and final external handoff.

Readiness is not released until the external receipt passes. Private receipt chains and source-derived values stay local under NEVER_PACKAGE; sanitized metadata proves counts/hashes without embedding originals. Content scanning is a bounded check, not universal detection of every possible paraphrase or encoding.
