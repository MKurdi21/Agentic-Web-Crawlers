# Table evidence model, version 2

Each table observation binds `table_id`, caption, PDF page, row label, column label, cell value, unit, footnote, merged-header context, condition, source hash, and support-locator ID. Preserve explicit missing values and table notes. A cell's value without its row/column and experimental condition is not a complete scientific observation.

Derived claims list ordered input cell keys and the operation. A count of zero rows must enumerate the complete eligible row set, not only zero rows. A comparison must include competing values under commensurate conditions. Page-spanning tables and detached captions require compound locators and rendered-page inspection. Source text extraction helps locate content but does not establish table alignment on its own.

The version 3 candidate schema records table cells, result inventory, atomic propositions, locator assessments, and quantitative claims. It is a parallel, migration-candidate contract; historical version 2 artifacts remain unchanged and unpromoted.
