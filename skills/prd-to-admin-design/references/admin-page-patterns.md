# Admin Page Patterns

Use these patterns as decision aids, not rigid templates. Start from the user's workflows and the existing Figma system, then omit sections that do not serve the task.

## List pages

A list page usually combines:

1. Page header with title, context, and the highest-value page action
2. Optional compact metrics when they change prioritization or explain the dataset
3. Tabs when they represent durable subsets or lifecycle states
4. Filter bar and active-filter summary
5. Data table or another dense collection view
6. Pagination or the product's established loading model

Keep the table visually dominant. Do not surround every region with a separate decorative card. Make the filter-to-result relationship obvious and preserve table geometry while loading.

## Detail pages

A detail page usually combines:

1. Breadcrumb or reliable return path
2. Page header with identity, status, primary actions, and overflow actions
3. Compact summary of the facts needed for immediate judgment
4. Tabs only when content groups are substantial and independently revisited
5. Semantic information sections
6. Related entities, records, or transactions
7. Operation logs or audit history when accountability matters

Do not place all fields in one undifferentiated card. Group by business meaning, for example: basic information, account information, financial information, related orders, risk information, and operation history. Keep identity and current status visible near consequential actions.

## Form pages

Use a full page for long, multi-section, high-impact, or independently addressable workflows. A common structure is breadcrumb, page header, semantic sections, fields and validation, then sticky or bottom actions. Read [admin-form-patterns.md](admin-form-patterns.md) before designing the interaction.

## Dashboards

A dashboard usually combines:

1. Time range and comparison context
2. A small set of decision-relevant metrics
3. Charts with units, legends, comparison periods, and meaningful empty states
4. Rankings or breakdowns
5. Operational tables
6. Exceptions and alerts that lead to action

Favor monitoring and investigation over decorative KPI collections. Use color to encode meaning, not to make every metric card unique. Keep timestamps, freshness, and partial-data conditions visible when they affect trust.

## Settings

A settings area usually combines category navigation, scoped form sections, concise descriptions, save state, and a separated danger zone. Make persistence behavior clear: immediate, per-section, or page-level. Preserve unsaved changes across accidental navigation when the product requires it.

## Layout and responsiveness

- Reuse the existing sidebar, header, content width, grid, and page-header behavior.
- Use stable dimensions for toolbars, table headers, action areas, and repeated rows so content or state changes do not shift the workflow.
- Design the primary desktop operating width first unless the requirements specify another priority, then define narrower behavior intentionally.
- Collapse secondary controls before compressing primary data beyond readability.
- Use overflow or alternate views for wide data sets according to the existing product convention; do not hide important columns without an explicit priority rule.

## State expression

Show states where reviewers can evaluate the interaction contract efficiently:

- Put reusable control states in component variants.
- Put collection loading, empty, error, permission, and partial-data states in focused specimens or representative frames.
- Put multi-step destructive flows in connected dialog or drawer frames.
- Annotate behavior only when it cannot be inferred from the visual design and component properties.
