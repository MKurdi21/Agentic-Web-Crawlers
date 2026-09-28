# Fingerprint correction before Phase 4B

The initial Phase 4R freeze accidentally included generated Python `__pycache__` bytecode in candidate/test tree hashes. The bytecode was removed inside the Phase 4R boundary and the fingerprint was recomputed over source files only. No validation-relevant source, schema, protocol, or scientific conclusion changed. This occurred before any Phase 4B substantive access.

Initial bookkeeping fingerprint: `b9c2c3bd07bd8bcfe841c71a5286150af05dbacdd4f898d799da6893af2c2446`.
Corrected source-only methodology fingerprint: `ab28253c49940db4cd28ba0ea224185c8f3b03289312dba3c64322a33d95f1bb`.

The metadata-only holdout is re-frozen against the corrected fingerprint; its identities remain the same and no selected PDF content was opened.
