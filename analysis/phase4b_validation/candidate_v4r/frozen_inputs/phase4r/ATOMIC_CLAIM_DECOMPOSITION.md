# Atomic claim decomposition, version 2

Before verification, split each compound claim into independently testable propositions: identity, quantity, metric, condition, comparison scope, direction, and interpretation. For example, “X achieved the best overall score of V” contains at least a value proposition and a document-wide ranking proposition. Each proposition receives its own support status and one or more source support locators.

A composed claim is fully supported only if **all material propositions** are supported. One correct number cannot validate an incorrect superlative. If any material proposition is partial, contradicted, unlocatable, or unresolved, classify the whole as `PARTIALLY_SUPPORTED_COMPOUND_CLAIM` or a stricter contradiction state and list the failing proposition IDs. The deterministic `compose_claim` check enforces this aggregation; `validate_scientific_payload` also rejects a full-support label that conflicts with its propositions.

Do not replace source review with proposition counting. Reviewers must assess whether the decomposition itself omits a material qualifier, and a verifier must inspect the exact support location rather than relying on topical similarity.
