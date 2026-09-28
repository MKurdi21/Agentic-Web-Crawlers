# Taxonomy Governance Options

Status: recommendation pending owner approval.

Use independent, multi-label dimensions where the evidence permits: paper role, agent type, environment, attack surface, attack technique, attacker capability, security property, defense mechanism, evaluation type, benchmark type, resource-risk type, and evidence type.

## Governance options

- **Maintainer-controlled:** one owner approves all term and definition changes.
- **Panel-controlled:** designated reviewers approve changes and resolve disagreements.
- **Open proposal with owner approval:** agents or researchers may propose terms, but a named human owner approves releases.

## Recommendation

Use open proposal with owner approval. Every taxonomy release receives a semantic version and SHA-256. Term additions, definition changes, merges, splits, and deprecations require rationale, affected-record queries, recoding impact, reviewer identity, and supersession history. Changing a taxonomy invalidates dependent coding and synthesis, not source artifacts or verified summaries.

Phase 3 development coding is provisional and cannot freeze the production taxonomy.
