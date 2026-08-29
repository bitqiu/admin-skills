# DESIGN.md Schema

Create a practical design-system document at the project root. Use this structure by default; add product-specific subsections when evidence warrants them, and explicitly mark unsupported areas rather than inventing rules.

Begin with:

```markdown
# Design System

> Evidence status: Updated from [Figma file] on YYYY-MM-DD.
> Scope: [pages, modes, and product areas inspected].
> Preview themes: Light [Verified/Derived]; Dark [Verified/Proposed].
```

Use tables for exact mappings and prose for semantic rules. Each consequential claim must be identifiable as **Verified Token**, **Derived Rule**, or **Unresolved**. This can be expressed in a `Status` column or a compact label next to the rule; do not add repetitive labels to every sentence when a whole table shares one status.

## 1. Design Principles

Summarize the observed visual language and operating priorities of the admin product: density, hierarchy, predictability, action emphasis, surface usage, and information presentation. Derive these principles from evidence and avoid aspirational brand language that the designs do not demonstrate.

## 2. Foundations

### Colors

For canonical tokens use columns such as:

| Token | Figma name | Mode | Value | Role | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- |

Cover supported background/surface layers, actions, text, borders/dividers, semantic feedback, focus, overlay, and disabled roles. State usage restrictions where confusion is likely.

### Typography

Document exact font properties and a role mapping for Page Title, Section Title, Body, Secondary Body, Table Header, Table Cell, Helper Text, and Form Label when present. Include fallbacks only if the repository defines them; otherwise identify the mapping gap.

### Spacing

List the canonical or observed scale, followed by contextual Derived Rules for page padding, section gaps, card padding, forms, filters, inline controls, and table cells. Keep one-off optical values out of the canonical scale.

### Radius

Map Input, Button, Card, Dialog, Tag, and other evidenced categories. Consolidate equal values under one token without implying all shapes share one usage rule.

### Borders

Document widths, semantic colors, dividers, focused/validation borders, and contexts where borders replace elevation.

### Shadows

Document Card, Dropdown, Modal, and floating-element effects only where present. Pair exact effect values with placement rules.

### Icons

Document source/library, common sizes, alignment, color behavior, and label pairing. Mark unknown sources explicitly.

## 3. Layout

### App Shell

Describe shell regions, dimensions, content origin, scrolling, and background hierarchy.

### Sidebar

Describe expanded/collapsed widths, menu groups, indentation, selected/hover behavior, and collapse rules.

### Header

Describe height, global actions, breadcrumbs or context, and sticky behavior.

### Page Container

Describe padding, max width or fluid behavior, alignment anchors, and vertical rhythm.

### Grid

Describe columns and common content splits only when evidenced.

### Responsive Behavior

Describe verified breakpoints or layout variants. Separate inferred recommendations from observed responsive designs.

## 4. Components

Give each evidenced component its own subsection. For every component cover purpose, variants, sizes, anatomy, content, states, and composition rules. Exact dimensions alone are insufficient.

For Button include hierarchy, variants, sizes, icon usage, destructive use, loading, and disabled behavior.

For Table include header/row height, padding, alignment, borders, hover/selection, sorting, operation columns, bulk actions, loading/empty states, and pagination relationship.

For Form include label/field/help/error anatomy, field and section spacing, width and columns, validation, and action placement. Distinguish page, dialog, and drawer forms.

Cover only components supported by evidence, using this inventory as a prompt: Input, Textarea, Select, DatePicker, Checkbox, Radio, Switch, Search, Tabs, Pagination, Badge, Tag, Tooltip, Dropdown, Breadcrumb, Card, Dialog, Drawer, Empty, Alert, and Notification.

## 5. Page Patterns

Create subsections for observed patterns such as List, Detail, Form, Dashboard, Settings, and Logs. For each include:

- Ordered region sequence
- Required versus optional regions
- Alignment and spacing
- Action placement
- Component relationships
- Known variants and references

Do not retain an empty generic pattern as if it were established. Write `Not established from sampled evidence` when a named pattern is important but unsupported.

## 6. Interaction Patterns

Document navigation, selection and bulk actions, filtering/search, save/cancel behavior, drill-down, overlays, confirmation, feedback, and keyboard behavior supported by the evidence.

## 7. States

Document loading, skeleton, empty, no-results, error, success, warning, disabled, permission-restricted, and offline states that appear in the source. Distinguish absent evidence from a rule that a state should not exist.

## 8. Data Display

Document number/date formatting, truncation, status encoding, alignment, density, summaries, charts, audit trails, and data hierarchy. Include color-independent status cues where observed or implemented.

## 9. Do / Don't

Write paired, concrete guardrails tied to observed patterns. Example form: `Do keep row-level actions in the operation column; don't mix them into status cells.` Do not fill this section with generic design advice.

## 10. Code Mapping

When project code exists, map design tokens and components to implementation names and locations:

| Design token/component | Code token/component | Location | Alignment | Notes |
| --- | --- | --- | --- | --- |

Use `Aligned`, `Partial`, `Missing`, or `Conflict` for Alignment. Do not invent mappings when repository evidence is unavailable.

## 11. Design Inconsistencies

Use one row per unresolved issue:

| Observed | Expected Canonical | Evidence | Recommendation |
| --- | --- | --- | --- |

Recommendations are proposals, not verified source rules. Preserve open issues across incremental updates until evidence resolves them.

## 12. Figma References

Record the Figma file, pages, foundation sources, main components, and representative frames inspected. Prefer named links or named node IDs. Also record material exclusions or access limitations so a future update knows what was not sampled.

## Preview relationship

`preview.html` and `preview-dark.html` are visual renderings of this document, not independent style explorations. Record whether each theme is verified from Figma or derived. If dark mode is proposed because Figma does not define one, identify the proposed token mapping and constraints in the relevant Foundations sections and in `Design Inconsistencies` or an explicit theme note.

Token names, exact values, component dimensions, and state behavior in the previews must agree with this document. When a preview demonstrates a recommendation rather than observed behavior, label that specimen so readers cannot mistake it for source evidence.

## Quality bar

The document is complete when another coding agent can answer, without reopening the full Figma file:

- Which semantic token to use for a given role
- How the app shell and page container are structured
- How core admin components behave across relevant states
- How to compose representative List, Detail, Form, or Dashboard pages
- Which claims are exact Figma definitions versus derived synthesis
- Where Figma and current code align or diverge
- Which unresolved inconsistencies still require design confirmation
- Whether the light and dark previews represent verified or proposed theme behavior

Favor compact tables and decisive rules over exhaustive property dumps. Keep exact values, evidence, and exceptions close enough that readers can verify a claim without searching the whole document.
