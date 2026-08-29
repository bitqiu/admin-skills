---
name: prd-to-admin-design
description: Create or extend Figma screens for B2B admin products from PRDs or ADMIN_SPEC.md while following DESIGN.md and existing Figma libraries. Use for requirements-to-design work; not for design-system extraction or frontend implementation.
---

# PRD to Admin Design

Turn approved admin requirements into production-ready Figma screens that fit the product's existing design system. Preserve business intent, favor operational clarity, and leave the Figma file more reusable rather than creating a parallel component system.

## Establish the evidence

Before designing, search the relevant project scope for `PRD.md`, `ADMIN_SPEC.md`, and `DESIGN.md`. Read every file that exists, plus any file the user explicitly identifies. Do not silently substitute similarly named documents when an exact source is available.

When the user provides or identifies a Figma file, inspect it before composing new screens. Understand the concrete system through:

- variables, color styles, text styles, and effects;
- components, variants, properties, and naming conventions;
- existing pages and representative admin screens;
- the admin shell, sidebar, header, page header, forms, tables, filters, modals, drawers, pagination, badges, and tags.

Before any Figma tool or MCP operation, load and follow the Figma skills required by the current environment. Treat those skills as the operating protocol and this skill as the product-design workflow. Do not duplicate, bypass, or invent low-level Figma tool instructions here.

If Figma editing is unavailable, do not claim the design was created. Complete any useful read-only analysis, identify the missing capability, and report the blocker.

## Resolve conflicts by source priority

Apply this precedence:

1. The user's current explicit instructions
2. `ADMIN_SPEC.md` or the designated admin PRD
3. `DESIGN.md`
4. Existing Figma components, variables, and styles
5. Existing comparable pages in the project
6. General B2B admin UX conventions

Keep the responsibilities distinct:

- `ADMIN_SPEC.md` or the PRD determines **what to design**: scope, data, actions, permissions, states, and flows.
- `DESIGN.md` determines **how to design it**: visual language, density, layout, interaction, and component rules.
- Figma determines **how the established system is concretely expressed**: exact tokens, component APIs, variants, and composition.

Do not redefine the product requirements or materially rewrite `ADMIN_SPEC.md`. When requirements are genuinely ambiguous, make only reversible layout assumptions and record them; ask before choosing between materially different business behaviors.

## Design workflow

1. Build a requirement inventory. List required pages, roles, fields, filters, columns, actions, dialogs, drawers, statuses, relationships, validation, and exceptional flows. Preserve requirement identifiers when present so coverage can be checked later.
2. Audit the Figma system. Map each needed pattern to an existing component, variant, variable, style, or representative screen. Prefer the current admin shell and layout conventions.
3. Choose the page pattern. Read [admin-page-patterns.md](references/admin-page-patterns.md) for list, detail, dashboard, and settings work. Read [admin-table-patterns.md](references/admin-table-patterns.md) whenever tables or filters are involved. Read [admin-form-patterns.md](references/admin-form-patterns.md) for forms, modals, drawers, validation, or risky operations.
4. Plan reuse before creating. Reuse existing components and variants whenever they satisfy the semantic and interaction need. Add or extend a component only for a real gap. Never create a visually identical but independent replacement.
5. Compose in Figma. Use Auto Layout, meaningful constraints, the established grid, and Hug/Fill/Fixed behavior deliberately. Favor layouts that tolerate realistic content and expected resizing; avoid screenshot-like piles of absolute-positioned layers.
6. Cover the interaction contract. Represent the important state rules and risky flows, even when not every state needs a separate full-page frame.
7. Reconcile against the source inventory, then fix omissions and inconsistencies in Figma before reporting completion.

## Admin design principles

Design for repeated operational work: clarity, high information density, scanning speed, predictable actions, stable geometry, consistent status language, and explicit system feedback.

Do not turn an admin product into a marketing page or mobile app. Avoid decorative expanses, oversized headings, low-density dashboards, excessive gradient cards, and visual novelty that slows comparison or action.

For semantic Figma layer names, prefer structures such as:

- `UserList/PageHeader`
- `UserList/Filters`
- `UserList/Table`
- `UserDetail/Summary`

Avoid names such as `Frame 1234`, `Group 99`, or `Rectangle 3` for meaningful layers.

## State coverage

Define how relevant components behave in default, hover, active, selected, disabled, loading, empty, error, no-permission, partial-data, and destructive-confirmation states. These may be expressed through component variants, focused state specimens, or annotated flows rather than duplicating every page.

## Completion review

Compare the finished Figma work against `ADMIN_SPEC.md` or the designated PRD and correct clear issues directly. Confirm that:

- every required page and detail section exists;
- filters, table columns, actions, statuses, dialogs, and drawers are covered;
- dangerous operations communicate risk, consequence, confirmation, and any required reason;
- existing components, variables, and styles were reused wherever suitable;
- no duplicate component system was introduced;
- the result follows `DESIGN.md` and the established admin shell;
- Auto Layout, constraints, names, and realistic content produce stable layouts;
- important empty, loading, error, permission, partial-data, and destructive states have explicit rules.

## Completion response

Report the Figma file and pages or frames created or changed, the primary existing components reused, any components or variants added, and meaningful assumptions or unresolved blockers. Keep the response focused on design coverage; do not produce backend code or implement React/Vue pages.
