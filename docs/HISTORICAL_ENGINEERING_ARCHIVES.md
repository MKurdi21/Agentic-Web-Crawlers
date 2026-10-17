# Historical engineering archives

Archive set: `litrev-retired-engineering-2026-10-16-v1`. Corrected cleanup transaction: `guarded-cleanup-20261017T151000Z-5bfba68b`.

Exactly 3,627 verified untracked ARCHIVE_ENGINEERING originals were moved to a new external quarantine, with complete path/size/SHA-256 journaling. Exactly 794 approved tracked engineering paths were subsequently quarantined and retired from the current Git tree. Current Research Mode dependencies, source papers, summaries, records, evidence and private-review material remain in place. The original 23 archives, 148-file backup, first-attempt quarantine and restoration receipts remain unchanged.

## Archive identities and receipts

[historical_engineering_archives.json](historical_engineering_archives.json) records payload/manifest/restoration hashes, the external original-path mapping identity and the final separation receipt hash. The external corrected-cleanup report records full local locations, MOVE_RESULTS.csv, METADATA_RESULTS.csv and the durable journal. No private absolute paths or excluded private dependency lists are reproduced here.

- analysis/integration_design: `6895b7a0aaf80eb94691ba749b29217d6d05ab4189007d8150a4ce3fdc149854` (723 members)
- analysis/phase3_calibration: `79c1f8cbc3a3134f48e8b9adb59b4a38ec8aaa85f83d56b20f7150d2f30be5b2` (901 members)
- analysis/phase4_rehearsal: `9069b61fdaaeddd0f27a58c8abeef854c9dc720285d9d1cf0bb19c5fd6cbd750` (97 members)
- analysis/phase4b_b02_scientific_validation: `0d82dd63a46772912eebae2595d974260d70f814fc2588f82dd944ecf3a99881` (840 members)
- analysis/phase4b_resumed_v2: `07168ae5c12ea0c51dd7d448ab0b11991efd28a19263f45b345d6f5f74956813` (41 members)
- analysis/phase4b_resumed_validation: `0ab79c539ef5ebc74eecc887f52e42a5a1d1d7ed8d91c971716edfb492381ece` (177 members)
- analysis/phase4b_validation: `30caeb8a0fc511270b50fb1d8af61fdbc837a3962992005ad68d58d6e2631228` (170 members)
- analysis/phase4b_validation_final: `d5055514a56c1fcd1df2d6f1511c99cf6359657cd18eab9cb5a79886af23095d` (62 members)
- analysis/phase4bc_context_isolation: `db6c83a69c2bde6aa911158efb396c559934e6de051d3373daa564df2c3295b0` (100 members)
- analysis/phase4bc_path_containment: `5a03659e353102bf43e90cf0b87868fea0850de9aac1a2ef7124a3d7690a88d4` (83 members)
- analysis/phase4bc_supplement: `47afde2ad66f5a27430e1474cabc902a979c765a00eabf2152811c9187d9186d` (70 members)
- analysis/phase4bd_real_source_continuity: `50b4a600f1edf5c6885b4e8ec198e54b5a09d2488a41be064a126732ebc152bc` (117 members)
- analysis/phase4be_bytecode_cache_reconciliation: `3190e6d4ee8668766a0af7c6e24b2bd2b7c5f3445e820780814e23dbae1ede80` (15 members)
- analysis/phase4be_checkpoint_identity_and_cache_reconciliation: `97a1a7fcd86df202d87a43b009b74dfbf2d5a1c3c9104fde3e96ff2968503624` (36 members)
- analysis/phase4be_checkpoint_reconciliation: `112138ffe7d91513253361be01708716514d4b836b349278af0e644aa57993d3` (40 members)
- analysis/phase4be_freeze_repair_and_validation: `bf02ae9e7d819ff6fc8a59419aa2775053a989632260ef06ecdef542d58bf06a` (157 members)
- analysis/phase4bf_freeze_coordinator_continuity: `da12d8d104f8c7818cf04ee205d35b73556da7c37cf3821e18da830db50a5dd6` (1175 members)
- analysis/phase4bg_b02_preaccess_bootstrap_remediation: `ed2b22a0cc7e729354cead0f58c28e65cb86498b1a38487a54cf3075dec9880a` (1398 members)
- analysis/phase4bg_runtime_binding_remediation: `d155c1363084ce75a71e39a81862b32d1662ff9f00849c32b8c9897fd693dfb2` (153 members)
- analysis/phase4bg_scientific_entry_dependency_remediation: `f218d85ed5bc1c8a5764be0d27c48ab6a6bcffc9897d82b197e6f325a7e6ba01` (203 members)
- analysis/phase4br_remediation: `ddef2c16e1e030ea1ada6fdc36af917018895ea329e0ceb73177b7e502c669d6` (754 members)
- analysis/phase4r_remediation: `c9857b6b762f8bc2cb0f2fa2a730ba9c820bdeb3a6141cc257fbfab6c0470cd2` (594 members)
- analysis/workspace_audit: `2a99d90b970a19c2863766ebada8187febe240829a890a25b6d1613ff7a1aea1` (31 members)

## Restore historical engineering

Restoration requires a separate authorized operation. Verify SEPARATION_RECEIPT.json and MOVE_RESULTS.csv, quarantine identities and every size/SHA-256. Refuse conflicting existing targets; copy exclusively to original repository-relative paths and verify readback. Preserve all existing quarantine transactions, including the tracked-retirement transaction. For archive readback, verify payload and member-manifest hashes, follow the group RESTORE.md, reject unsafe/link/duplicate/collision entries, and extract only into a new empty destination with full original paths. Never overwrite a checkout or replay committed workflow transitions. Old restoration prose describes archive creation, before this cleanup.

## Limitations

All copies share the same Google Drive account and synchronization domain and are not independent disaster-recovery backups. Cloud synchronization completion and storage retention locks are not asserted. Preserve archives and quarantines until a separate retention decision.

All 23 archives preserve selected non-sensitive engineering slices; full execution closures remain BLOCKED_PRIVATE_REVIEW. Excluded private and unresolved dynamic dependencies remain documented externally. B02 remains historically consumed/primary accepted; verifier, adjudication and scientific decision remain NOT_RUN. Byte preservation is not scientific validation or complete reproduction.

The first attempt did not preserve original historical file timestamps. This retry records current pre-move metadata and preserves modification times/modes where supported; no earlier timestamps are invented. Creation times, ACL/owner/xattrs and stable access times are not asserted.

Two exact earlier Research Mode source versions remain unresolved: scripts/research_mode.py SHA-256 `03edf146f94bf30d53d188459ecd61750889830c765818bc72cdf8314461765f` and scripts/test_research_mode.py SHA-256 `d0b48fafa29e1be1a26d60b7cf1e12877e6f16593e02109b55fe241c5d1a7d5d`. Current code must not be described as those historical bytes without a matching receipt/hash.

## Tracked retirement and Git lineage — 2026-10-17

Starting Git commit: `b4f3884b0203b9b623e1d9d51fd87d65f66e25d8`. Dedicated 794-path retirement commit: `8216af5c4b08432c9aeb55558f581127f77f52d0`. Quarantine transaction: `tracked-retirement-20261017-5e06bf9b41c5`; verification receipt: `QUARANTINE_RECEIPT.json` in external assessment `foundation-resume-20261017-4118455e`, SHA-256 `8cbe9317993501f5025a11d4a36db089b9f5bec699de2bae84b2c415cb89a758`. The external `TRACKED_RETIREMENT_MANIFEST.csv` records original Git blob IDs and blob hashes alongside the preserved working-file hashes, archive members and quarantine paths. Git blob bytes may differ from working-file bytes because of historical line-ending conversion; the archives and quarantine preserve the approved working-file bytes.

The earlier 3,627 untracked quarantined files and these 794 tracked retired files total 4,421 approved original removals. The original 23 archive payloads and their mappings remain unchanged. Preceding Git commits remain accessible without history rewriting. Restore only through a separately authorized operation: verify the recorded receipt and manifest hashes, preflight every destination, refuse conflicts, copy exclusively from verified quarantine or extract verified archive members into a fresh empty directory, then verify every path, size and SHA-256. Do not execute archived workflows or replay historical state transitions.

Retain all archives and quarantines indefinitely pending a separate retention decision. Two already-tracked private-review files remain unchanged; the 202 outstanding private-review files were excluded from this series. Neither the current tree nor its history is approved for distribution. The final series receipt and exact final commit identity are external; the proposed annotated foundation tag remains uncreated pending human review.
