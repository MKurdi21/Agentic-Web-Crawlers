# Package isolation and receipt policy

The convenience ZIP is constructed from explicit root filenames, the frozen immutable candidate inventory, named sanitized test reports, and synthetic fixture JSON. Never recurse over the entire design tree. Exclude private source snapshots, full text, summaries, page images, copied tables, private development graphs, runtime databases/blobs/backups, dependencies/cache directories, credentials and prior archives.

PACKAGE_MANIFEST.json contains exact path/size/hash inventory. Its own bytes are an explicitly named self-member; it does not hash itself. HANDOFF_SNAPSHOT.json is an immutable package-time handoff. FINAL_HANDOFF.json, PACKAGE_RECEIPT.json and INDEPENDENT_FINAL_REVIEW.json are external completion receipts so the ZIP hash never requires a circular self-hash. The external final handoff is authoritative for completed archive validation/readiness.

The independent validator reopens the archive, checks CRC and every hash/member, rejects traversal, case collisions, duplicates, private/runtime paths, known protected source hashes and binary/article signatures. It does not import builder functions. Content scanning has limits; constrained output generation and physical private separation are primary controls. Metadata references to private paths are allowed; the referenced bytes are not packaged.
