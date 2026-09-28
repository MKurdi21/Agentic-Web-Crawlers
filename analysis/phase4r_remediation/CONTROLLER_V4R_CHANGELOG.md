# Candidate v4r changelog and schema migration note

Candidate identity: `litrev-hardened-candidate-v4r`, proposed scientific contract `3.0.0-remediation.1`. Parent is the byte-frozen Phase 4 candidate; the original remains unchanged.

- Added a parallel `scientific_evidence_v3.schema.json` contract for result inventory, table cells, atomic propositions, typed discovery/support locators, compound claims, quantitative provenance, and source-result conflicts. Its `schema_version` is `3.0.0`; historical version 2 evidence remains valid historical input but is **not auto-converted, reinterpreted, or accepted**.
- Added `scientific_v3.py` guards for document-wide comparative reconciliation, deterministic decimal derived values, eligible table-row coverage, sample-versus-failure denominators, compound support, locator entailment, and conflicting source values. These checks fail closed on missing scope, wrong arithmetic, context-only support, and unresolved critical references. They do not certify source transcription.
- Routed `scientific_evidence_v3` through the candidate's five-layer validation entry point. The existing version 2 schemas and behavior remain available for historical compatibility. A future importer needs an explicit v2-to-v3 mapping with preserved original bytes, protocol pins, and review status; no such live migration ran here.
- Corrected candidate-copy workspace-root resolution for `candidate_v4r`, without changing its shadow-only write boundary.
- Added generalized synthetic regression tests and sanitized fixtures. Inherited safety tests remain present. No production approval, live state, or deployed skill was changed.

The new contract is a candidate. A structurally and semantically valid payload is not source-verified. Operational acceptance must still bind an exact task/source/protocol, authoritative current state, and a trusted review policy where required.
