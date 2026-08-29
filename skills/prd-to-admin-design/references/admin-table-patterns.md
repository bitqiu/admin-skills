# Admin Table and Filter Patterns

Tables are operational tools. Optimize them for scanning, comparison, selection, and safe action rather than visual decoration.

## Define the table contract

For every required field, decide:

- whether it needs a visible column, secondary line, tooltip, detail view, or no list representation;
- business priority and behavior at narrower widths;
- width mode: fixed, bounded flexible, or content-driven;
- alignment, formatting, truncation, wrapping, and sortability;
- whether the value can be missing, stale, restricted, or partially loaded.

Use realistic long values while designing. Check these common types:

| Data | Recommended treatment |
|---|---|
| IDs | Monospace only if the system uses it; truncate predictably and offer copy/access to the full value |
| User or merchant | Primary identity plus only the most useful secondary identifier |
| Status | Existing semantic badge/tag; do not rely on color alone |
| Money | Right-align, include currency and precision rules, distinguish negative values |
| Number | Right-align when comparison matters |
| Date/time | Use one timezone and format convention; expose full precision when operationally necessary |
| Long text | Bound the column, use purposeful wrapping or truncation, and provide access to the full content |
| Boolean | Use explicit domain language when `Yes/No` would be ambiguous |

## Selection and actions

- Add row selection only when meaningful bulk actions exist.
- When selected, show the selection count, applicable bulk actions, and a clear way to exit selection.
- Do not spread many buttons across each row. Show the primary frequent row action, then place secondary actions in a More menu.
- Keep destructive actions visually and spatially distinct from routine actions.
- Define disabled or hidden behavior for actions blocked by status or permissions; prefer an explanation when the reason is not obvious.

## Pagination and data state

Follow the existing product's pagination model. Where applicable, show total count, current range/page, page-size control, and disabled boundary controls. Preserve filters, sorting, and selection according to the product requirements.

Design explicit rules for:

- loading without layout collapse;
- empty results caused by filters versus a genuinely empty dataset;
- request errors with a relevant recovery action;
- no permission without leaking restricted data;
- partial or stale data with visible trust cues.

## Choose filters by field type

| Field type | Preferred control |
|---|---|
| Keyword | Search field or input with a clear searchable scope |
| Status | Select, segmented control, or tabs based on count and persistence |
| Date/time | Date range picker with timezone and boundary semantics |
| Enum | Select; use multi-select only when the query supports union behavior |
| Boolean | Select or switch when the on/off effect is immediate and unambiguous |
| Entity | Searchable select with disambiguating secondary information |

Keep frequently used, high-value filters visible. When filters are numerous, separate basic filters from advanced filters and preserve active advanced criteria through visible chips, a count, or the established product convention.

## Filter interaction contract

Clarify whether filtering applies immediately or on submit. Define reset behavior, default values, URL or navigation persistence when relevant, and the relationship between tabs and filters. Ensure active filters remain discoverable even when advanced controls are collapsed.
