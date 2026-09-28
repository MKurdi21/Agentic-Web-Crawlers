# Phase 4BR recovery checkpoint

The authorized task is the attachment at C:\Users\moham\.codex\attachments\bb9df859-22d0-41c8-b619-1cab91b577df\pasted-text.txt. Resume Phase 4BR only. Do not open B02-B08, run Lane B, refresh the live checkpoint, install skills, migrate, or promote. Writes stay in this directory and the approved sibling archive.

## Completed, not yet final

- setup_phase.py verified six prior ZIP hashes/CRCs and captured 8,993 protected paths in PROTECTED_FILES_INITIAL.csv. Original prior artifacts remain inputs, never rewritten.
- 61 immutable candidate files were copied to candidate_v4br. Private original B01 evidence preserved with hashes.
- pre_access.py commits durable receipt before source bytes are made available. Initial B01 development-adjudication receipt exists under private_source_material/access/adjudication. It is historical; never overwrite/backdate it.
- adjudicate_b01.py produced exactly 80 records in B01_SUPPORT_ADJUDICATION.json/CSV and private exact-source records. Provisional distribution: 58 locator-only, 20 both-partial, 1 unresolved, 1 primary-correct.
- IMPORTANT: Always use encoding='utf-8' when reading JSON. Default Windows cp1252 decoding creates false mojibake. CH036 stored author name has correct U+00E8; verifier flag is wrong.
- 15 benign-utility items retain correct cell values but had attack conditions/security denominators. Correct conditions to no attack and 97 user tasks; do not classify these as merely locator defects.
- source-adjudicated compound facts are decomposed with source locations. CH010 remains unresolved absence. CH043/046/059 retain unresolved qualifiers. Dataset DOI needs its dataset scope.
- build_development.py assembled private graphs for all 131 original items and four local comparative graphs (135 graphs). check_graphs.py found all 135 structurally/semantically valid, but this is preliminary, not a final development gate or scientific truth proof.
- New code: support_v4.py, pre_access.py, validation_guard.py; new schema scientific_evidence_v4.schema.json. Existing scientific v3 schema/test semantics are preserved.
- Last full run: 142/142 tests passed (86 inherited, 56 new). Earlier two packaging test errors were missing INITIAL_BASELINE.json, fixed by supplying actual protected hashes; failure report retained. Subsequently added validate_source_bindings and one test; rerun full suite after remaining fixes.
- Synthetic inherited tests create synthetic DBs and unit backup fixtures under candidate shadow. These are not Lane B/live-data migration/backup rehearsal. No Lane B runtime was created.
- 12 synthetic generalized fixtures live in b01_failure_fixtures; prior sanitized fixtures copied to phase4_failure_fixtures.

## Resource stop and review

User explicitly authorized one read-only final reviewer. /root/phase4br_final_review gave one finding then hit a usage limit. Do not claim completed independent review. It found: build_development.py presents CH070 analyst inferences as FACT/VALUE_SUPPORT + EXACT + FULLY_SUPPORTED; prose labels are insufficient. Add explicit structured provenance/origin, keep analyst inference distinct from direct source facts, and test the distinction. Similar CH065 implicit questions and other inference/procedural assertions need scrutiny. The receipt event follows physical hash reading but precedes returning bytes; describe this accurately, not as an OS sandbox or event-before-physical-read guarantee.

## Required next work

1. Resolve reviewer finding in schema, graph builder, semantic validator, tests, and adjudication mappings. Do not just alter wording.
2. Review all remaining source/locator semantics, especially compound unchallenged records and investigator inferences. Existing graph validation does not prove source truth. Exact source data and whole table values stay private.
3. Make source-binding validation part of the explicit development gate. Graph page content hashes bind extracted page bytes; precise reference strings identify source elements. Document granularity/entailment limitations.
4. Write generalized protocol documents and inactive skill amendments: proposition/support model, roles, comparative protocol, receipt protocol, verifier protocol, schema migration notes, skill remediation report, root cause taxonomy.
5. Freeze behavior inputs and new methodology (proposed phase4br-scientific-v3.0.0 with schema 4.0.0). Preserve original v2 identifier/hash separately. No silent re-freeze after final rerun.
6. Record a new durable pre-access receipt for the FINAL development rerun under a new directory after methodology freeze; do not replace historical adjudication receipt.
7. Run final B01-only development evaluation. Account all 80 challenges, 131 original items, 127 original critical items, four table-local rankings, known failures corrected or fail-closed. Preserve unresolved absence/source conflicts. Ground truth remains UNKNOWN.
8. Independently reconcile regression cohort of 45 original verifier-SUPPORTED items (44 critical +1 noncritical). Do not treat verifier opinion as ground truth. Four compound local rankings need deterministic graph checks; persistence NOT_STATED is an additional original error outside the 80 and was corrected to a hypothetical uncovered setting.
9. Rerun full inherited/new tests. No original tests removed/weakened. Document synthetic-only unit DB/backup tests separately from prohibited Lane B.
10. Finish or truthfully label unavailable the single independent read-only final review.
11. Recheck B02-B08 only metadata/hashes, produce resume manifest and plan beginning B02. They remain untouched; no resume authorized.
12. Rehash all 8,993 protected baseline paths; reconcile original 5,737 live set and all prior phases. This takes several minutes. Check Git drift and live scientific state read-only. No checkpoint refresh.
13. Create all user-requested reports, metrics, final handoff, preservation check, exact allowlist package. Exclude private sources, all development graphs with full table values, runtime/deps/caches/DBs/backups, prior archives. Independently validate ZIP contents/hash. Avoid package/hash circularity using a documented external receipt.
14. Return actual classification only after gates; no readiness claim currently exists. Stop before B02 and Lane B.

## Source observations to preserve

- Table 1 rows sum to 74, caption says 70, page 4 prose says 74, page 24 card says 70: unresolved canonical tool total.
- Table 3 GPT-4o ASR 47.69 vs Table 5 57.69 are experiment-attributed facts; differing tables alone do not prove same-condition contradiction.
- Table 4 Max targeted 57.55 vs Important message 57.7 yields -0.15 percentage points, at odds with broad prose improvement. Retain conflict, not silent repair.
- Page 2 under-66% benign statement versus later Claude3.5 result has report-version context on page 7.
- Tool-filter prose 7.5 vs Table 5 6.84 remain separately attributed.
- Inspected B01 rendered pages include 1, 6, 8, 20, 21, 24; exact source text consulted for relevant body/appendix sections. Do not claim every rendered page was visually reviewed.

## Completion supersedes earlier pending notes
Phase4BR completed. FINAL_HANDOFF.json and PACKAGE_RECEIPT.json are authoritative. 151 tests passed; methodology frozen; 80 adjudications and B01 development gates complete. Final independent review was unavailable after correction review because of reviewer quota. B02-B08 remain untouched. Do not resume without separate authorization.

