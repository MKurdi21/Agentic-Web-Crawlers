# Packaging Spec

PACKAGE_MANIFEST.json enumerates exact packageable release files,relative paths,byte sizes and SHA256s. Eligible roots are named top-level design documents/manifests,hardened source/schema/test fixtures,inactive deploy_payload,and explicitly listed sanitized test_results. Never recursively ZIP the design tree. Entire shadow,_deps,caches,databases,nested archives and runtime outboxes/stores are forbidden.

Reject candidates matching forbidden filenames/extensions,known original whole-file hashes,original content samples or embedded base64 material. Original PDFs,summary generations,article/accessibility/page images/logs/raw evidence/control files and reference/audit ZIPs cannot become packageable by renaming. Sanitized exports are newly structured metadata only.

Independent validation reopens every ZIP entry,checks CRC,exact member set,size/SHA,casefold collisions,traversal and forbidden content. Negative tests include a renamed original-like fixture and private path member. Known-source scans have limits and are not arbitrary steganography detection; physical separation,exact allowlisting and constrained exports are primary. Package manifest self-hash is intentionally omitted; final ZIP hash is recorded externally in its receipt.
