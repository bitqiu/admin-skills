# Figma Extraction Rules

Use these rules while gathering and interpreting evidence. The goal is representative coverage and defensible synthesis, not exhaustive traversal.

## Evidence map

Start with a compact inventory:

| Evidence class | Look for | What it can establish |
| --- | --- | --- |
| Variables and collections | Names, aliases, scopes, modes, values | Canonical tokens and theme relationships |
| Styles | Paint, text, effect, grid styles | Shared roles when Variables are absent |
| Main components | Properties, variants, anatomy, constraints | Canonical component behavior |
| Instances | Overrides and repeated usage | Real usage patterns and local exceptions |
| Representative pages | Shell, sequences, density, states | Layout and page composition rules |
| Repository code | Theme aliases, shared primitives | Implementation mapping only |

Prefer structured properties over pixel estimates. Screenshots are valuable for hierarchy and composition but weak evidence for exact token values.

## Bounded sampling

1. Inspect the file/page index and locate foundations, libraries, components, and product areas.
2. Inspect Variables, Styles, and main components before sampling pages when access permits.
3. Select representative current pages that maximize distinct patterns: typically one Dashboard, List, Detail, Form, and Settings page, plus a Dialog or Drawer state.
4. Add a page only when it represents a different shell, density, component family, workflow, or responsive mode.
5. Stop broadening the sample when new pages repeat established rules and known conflicts are already represented.

If only one frame is available, document only what it supports. State which system areas remain unknown instead of extrapolating a complete design system.

## Claim classification

### Verified Token

A claim is verified when its value and role come directly from one of these sources:

- A scoped Figma Variable, including its collection and mode
- A named Figma Style
- A published main component or explicit variant property
- An exact property inspected on an authoritative frame when no shared definition exists

Record the original name, value, applicable mode or variant, semantic role, and source. Preserve aliases when Figma uses them rather than replacing every alias with its resolved primitive.

### Derived Rule

A rule is derived only when multiple relevant examples support the same contextual behavior. Record:

- The synthesized rule
- Which pages or components support it
- Scope, exceptions, and confidence
- Exact values where observable

One instance is an observation, not a system-wide rule. A pattern can still be high confidence when three authoritative examples agree, or lower confidence when many legacy instances conflict.

### Unresolved

Use unresolved when evidence is missing, values conflict without a clear authority, or visual measurement is too imprecise. Do not promote it into foundations or component defaults.

## Foundations checklist

### Colors

Identify roles rather than swatch counts:

- Canvas/background, surface, elevated surface
- Primary and secondary actions
- Primary, secondary, muted, inverse, and link text
- Border, divider, focus, and overlay
- Success, warning, error, and info
- Disabled backgrounds, content, and borders

For each canonical color include light/dark or other mode mappings when defined. Preserve existing Variable names; otherwise create a stable semantic name such as `color.text.secondary`. Do not invent a dark mode from light-mode screenshots.

### Typography

Capture family, weight, size, line height, and letter spacing, then map observed styles to roles such as Page Title, Section Title, Body, Secondary Body, Table Header, Table Cell, Helper Text, and Form Label. Note numeric alignment or monospace treatment when material to admin data.

### Spacing

Infer the smallest useful scale rather than listing every measured gap. Then document contextual rules for page padding, section gap, card padding, form rhythm, inline controls, filters, table cells, and overlay content. Treat isolated optical adjustments as exceptions.

### Radius, borders, and effects

Separate control, button, card, dialog, and tag radii when evidence differs. Capture border width and role, divider use, hover/focus borders, and the purpose of Card, Dropdown, Modal, or floating-element shadows. Do not describe elevation solely as a raw shadow string; explain where it belongs.

### Icons

Identify the icon family or source, common sizes and stroke treatment, alignment, color inheritance, and rules for icon-only versus icon-plus-label actions. Mark the library unknown when it cannot be verified.

## Layout checklist

### App shell

Inspect sidebar width in expanded/collapsed states, header height, content origin, scroll ownership, sticky regions, and the hierarchy among shell, page, and raised surfaces.

### Page container

Inspect horizontal and vertical padding, max width, centered versus fluid behavior, alignment anchors, section rhythm, grids, and breakpoints or alternate responsive frames. Do not infer responsive behavior from a single desktop frame.

### Navigation

Capture menu group anatomy, indentation, selected and hover states, badges, expansion behavior, sidebar collapse behavior, breadcrumb use, and where global versus page-local actions live.

## Component checklist

For every material component, document only evidenced variants and cover:

- Purpose and usage boundary
- Anatomy and content constraints
- Variant hierarchy and sizes
- Default, hover, active/selected, focus, disabled, loading, validation, and destructive states as applicable
- Icon placement and label behavior
- Layout relationships with adjacent components
- Known exceptions or missing states

Consider Button, Input, Textarea, Select, DatePicker, Checkbox, Radio, Switch, Search, Tabs, Table, Pagination, Badge, Tag, Tooltip, Dropdown, Breadcrumb, Card, Dialog, Drawer, Form, Empty, Alert, and Notification. The list is a discovery aid, not a mandate to invent absent components.

### Table depth

Capture header and row height, cell padding, numeric/text alignment, borders, truncation or wrapping, sorting/filter indicators, hover and selected behavior, bulk selection, fixed or operation columns, empty/loading states, and pagination placement. Explain the relationship among filters, table actions, selection, and pagination.

### Form depth

Capture label placement and width, required indicators, controls, help/error text, field and section gaps, column layout, form width, validation timing, dependent fields, and action placement. Distinguish full-page forms from dialog or drawer forms.

### Overlays

For Dialog, Drawer, Dropdown, Tooltip, and Notification, capture trigger, placement, sizing, backdrop, elevation, dismissal, action order, overflow, and focus/keyboard behavior only where Figma or adjacent product evidence supports it.

## Page-pattern synthesis

Write page patterns as observed compositions, not universal recipes. A pattern should state:

- Ordered regions and which are optional
- Alignment and spacing relationships
- Primary and secondary action placement
- Where filters, tabs, tables, summaries, and pagination belong
- Overlay or drill-down behavior
- Variants supported by different examples

Look for List, Detail, Form, Dashboard, Settings, Logs, and product-specific patterns. An observed List pattern might be `Breadcrumb -> Page Header -> Statistics -> Tabs -> Filters -> Table -> Pagination`, but use this only when the sampled Figma supports it.

## Conflict handling

Resolve candidate conflicts in this order:

1. Canonical Variable or Style
2. Published main component
3. Newer page or explicitly current design area
4. Frequency across relevant current pages
5. Isolated or evidently historical page

Recency is evidence only when it can be established. Do not label a design historical from appearance alone.

For unresolved conflicts record:

| Field | Required content |
| --- | --- |
| Observed | Conflicting values or behaviors and where each appears |
| Expected Canonical | Existing canonical choice, or `Undetermined` |
| Evidence | Variable/style/component/page references |
| Recommendation | A proposed resolution clearly labeled as a recommendation |

## Evidence references

Use stable, human-usable references where available: Figma file and page name, frame or component name, node ID, and link. Avoid raw node IDs without names. Group references by foundations, components, and representative pages so future updates can resample efficiently.
