# Frozen model routing

Runtime identity: MODEL_RUNTIME_IDENTITY_UNVERIFIED. Requested models: GPT-6 Sol / GPT-6 Astra. No guessed token or cost figures.

Use Sol for work that is primarily deterministic, procedural,
structural, computational, or orchestration-heavy.

Sol owns:

- coordinator state;
- recovery state;
- frozen-hash validation;
- code fingerprints;
- source identity;
- source SHA-256;
- real-source transport;
- packet construction;
- packet acknowledgements;
- pre-access receipts;
- SOURCE_ACCESS_BEGAN;
- consumption transitions;
- path containment;
- context firewall setup;
- field-slot initialization;
- source structure mapping;
- section/table/figure inventories;
- explicit metadata extraction;
- bibliography-independent factual metadata;
- result inventory construction;
- proposition decomposition;
- support-requirement construction;
- candidate locator collection;
- table-cell extraction where mechanically clear;
- deterministic arithmetic;
- counts;
- percentages;
- ranking computations;
- comparison-set enumeration;
- consistency checks;
- schema validation;
- manifest generation;
- state transitions;
- recovery;
- idempotency;
- test execution;
- metrics;
- packaging;
- Lane B, if later authorized by successful Lane A2;
- SQLite/migration/snapshot/backup/restore/rollback/cutover rehearsal.

Do not spend Astra on these tasks unless a predefined escalation
criterion explicitly requires scientific interpretation.

Reserve Astra for tasks requiring substantial scientific judgment.

Astra owns or adjudicates:

- actual scientific contribution interpretation;
- whether claimed contributions are genuinely supported by source;
- threat-model interpretation;
- attacker goals/capabilities/knowledge/access;
- defense assumptions;
- experimental-design interpretation;
- nuanced methodological limitations;
- negative results;
- causal/interpretive claims;
- ambiguous result scope;
- conflicting main-text/table/appendix evidence;
- comparative claims;
- superlative claims;
- cross-condition ranking claims;
- difficult table interpretation;
- appendix-versus-main-text reconciliation;
- material compound claims;
- claims requiring synthesis across multiple source locations;
- unresolved critical claims after Sol extraction;
- scientific adjudication of critical evidence-support relationships.

Astra must not be used merely to duplicate deterministic Sol work.

Freeze these criteria BEFORE B02.

An item MUST be escalated to Astra when ANY of the following applies:

A. CRITICAL SCIENTIFIC CLAIM

The item concerns:

- core contribution;
- primary experimental conclusion;
- threat model;
- attack mechanism;
- defense effectiveness;
- main quantitative conclusion;
- material limitation;
- negative finding;
- benchmark interpretation.

B. COMPARATIVE CLAIM

Contains or implies:

- best;
- highest;
- lowest;
- strongest;
- weakest;
- overall;
- maximum;
- minimum;
- outperforms;
- underperforms;
- improves;
- degrades;
- more/less effective;
- state of the art.

C. MULTI-LOCATION SUPPORT

Correct interpretation requires reconciling:

- more than one table;
- table + appendix;
- text + figure;
- main paper + supplementary section;
- multiple experimental conditions.

D. AMBIGUITY

Sol cannot establish one interpretation with strong source support.

E. SOURCE CONFLICT

Different source locations appear inconsistent.

F. COMPLEX DERIVATION

The operands themselves require scientific interpretation,
even if final arithmetic is deterministic.

G. COMPOUND CRITICAL CLAIM

A critical claim contains multiple material propositions.

H. SCOPE QUESTION

It is unclear whether a result applies to:

- one condition;
- one model;
- one dataset;
- one benchmark;
- one subset;
- or the complete experimental setting.

I. SOL CONFIDENCE FAILURE

Sol explicitly records:

`SCIENTIFIC_INTERPRETATION_UNCERTAIN`

Do NOT invent a numeric confidence threshold unless one is already
defined in the frozen methodology.

If scientific interpretation is so globally coupled that isolated
claim review would remove necessary context, Astra may receive the
current paper/source in a clean scientific worker context.

This decision must be based on the frozen escalation criteria,
not on the scientific result.

Record:

`ASTRA_WHOLE_REPORT_ESCALATION`

with a reason code.

Examples of valid reason codes:

`GLOBAL_EXPERIMENTAL_CONTEXT_REQUIRED`

`MULTI_SECTION_THREAT_MODEL`

`DOCUMENT_WIDE_COMPARATIVE_RECONCILIATION`

`MAIN_APPENDIX_RESULT_CONFLICT`

Do not escalate simply because Astra is available.

For critical verification, do not show Astra persuasive Sol rationale.

Astra may receive:

- exact current source;
- frozen methodology;
- atomic proposition;
- proposed support locator/set;
- required support roles;
- necessary source context.

Do NOT provide:

- Sol's chain of reasoning;
- persuasive explanation;
- prior holdout results;
- historical Phase 4 failures;
- B01 scientific findings;
- coordinator interpretation.

Astra should independently determine whether the proposition is
supported.

This remains AI verification, NOT independent human review.

For every scientific item store:

- item ID;
- report ID;
- criticality;
- initial processor;
- Astra escalation yes/no;
- escalation reason code;
- verifier model role;
- final disposition.

Create:

`MODEL_ROUTING_LEDGER.jsonl`

At run completion report:

- Sol-only item count;
- Astra-reviewed item count;
- Astra whole-report escalation count;
- critical Astra-review count;
- lower-risk Astra sample count.

Do not infer token/cost figures if runtime does not expose them.

If token usage is available, record actual values.

Once B02 is opened:

DO NOT change:

- escalation criteria;
- sampling algorithm;
- criticality definition;
- Astra routing rules;
- Sol routing rules;

based on B02–B08 scientific results.

If the routing policy itself proves defective:

STOP.

Do not repair it on the active holdout.

Return:

`MODEL_ROUTING_POLICY_FAILURE`

and preserve later reports untouched.

Use frozen sampling:

`sha256-lexicographic-v1`

sample size:

`min(N, max(3, ceil(0.25 × N)))`

Freeze sample before verification.

Do not change sample after seeing results.

Use Astra for sampled lower-risk scientific verification only where
scientific judgment is actually required.

Mechanical checks remain Sol/deterministic.