---
name: figma-to-design-md
description: Analyze an existing Figma admin or operations product and create or incrementally maintain the project-root DESIGN.md with matching light and dark HTML previews. Use when asked to extract design rules, tokens, components, layouts, page patterns, or visual catalogs from Figma; do not use as a substitute for implementing Figma screens or redesigning the source file.
---

# Figma to DESIGN.md

Translate the design language implicit in an existing Figma admin system into a durable `DESIGN.md` and corresponding visual previews that another coding agent can use without reopening the entire file. Capture semantic tokens, component behavior, layout rules, page composition, and evidence quality rather than dumping raw properties.

## Read first

Read [references/extraction-rules.md](references/extraction-rules.md) before inspecting Figma. Read [references/design-md-schema.md](references/design-md-schema.md) and [references/preview-contract.md](references/preview-contract.md) before creating or editing output files.

Use the available Figma integration and follow any prerequisite instructions for its tools. If structured Figma data is unavailable, work from supplied screenshots or exports and clearly downgrade claim confidence; never present visual estimates as verified tokens.

## Scope

- Write or update `DESIGN.md`, `preview.html`, and `preview-dark.html` together at the project root. Resolve the project root from repository context; use the current workspace root when no repository root exists.
- Treat the three files as one deliverable. Their token names, values, component geometry, page patterns, and evidence labels must agree.
- Analyze the existing product. Do not redesign Figma, silently normalize its source, or implement application pages unless the user separately asks for that work.
- Do not infer a complete system from one user-linked frame when related evidence can reasonably be inspected.
- Do not crawl an unbounded large file. Inventory first, then inspect representative foundations, components, and page types until additional frames stop changing the conclusions.

## Workflow

### 1. Establish the baseline

Read any existing root `DESIGN.md`, `preview.html`, and `preview-dark.html` before opening Figma. Treat correct, still-supported rules and preview specimens as protected content. Note token names, component guidance, code mappings, unresolved inconsistencies, Figma references, and preview coverage so the update can be incremental.

Inspect relevant repository theme files, shared UI components, and layout primitives only when they help maintain `Code Mapping` or resolve a Figma-to-code discrepancy. Figma remains the design evidence; shipped code is implementation evidence and must not be mislabeled as a Figma definition.

### 2. Build a bounded evidence set

Inventory the relevant Figma pages or sections before deep inspection. When available, include:

- Variables, collections, modes, and styles
- Main components, variants, and representative instances
- Layout constraints, auto layout, grids, and responsive variants
- Representative pages such as Dashboard, List, Detail, Form, Settings, Dialog, and Drawer

Choose examples by coverage, recency, reuse, and component authority. Inspect enough instances to distinguish a reusable rule from a local exception. Record file/page/frame or component names and node identifiers or links as evidence.

### 3. Extract the system

Analyze:

- Foundations: semantic colors, typography roles, spacing scale and contextual gaps, radius, borders, effects, and icons
- Layout: app shell, navigation, sidebar, header, page container, alignment, grid, density, and responsive behavior
- Components: variants, hierarchy, size, anatomy, content rules, states, and composition; give tables and forms extra depth
- Page patterns: recurring sequences and relationships for list, detail, form, dashboard, settings, logs, and any product-specific page type actually supported by evidence
- Interaction and data display: navigation behavior, overlays, feedback, validation, loading, empty/error states, tables, filters, pagination, summaries, and operation placement

Name roles semantically. Prefer a canonical Figma Variable or Style name when one exists. For example, map a primary action fill to `color.action.primary`; do not reduce it to an unexplained hex value.

### 4. Separate facts from synthesis

Classify every consequential claim:

- **Verified Token**: directly defined by a Figma Variable, Style, canonical component, or exact inspected property. Include the exact value and source.
- **Derived Rule**: inferred from multiple consistent examples. Include the rule, evidence set, and confidence or scope.
- **Unresolved**: conflicting or insufficient evidence. Keep it out of canonical guidance and record it in `Design Inconsistencies` or the relevant gap.

Do not turn a repeated number into a rule without context. Convert evidence into implementation guidance, such as: "First-level admin pages use 24px horizontal padding; standard cards use 20px internal padding; compact filter bars use 16px."

### 5. Resolve conflicts deliberately

Use this precedence unless stronger evidence or explicit user direction says otherwise:

1. Canonical Figma Variable or Style
2. Published main component and its variants
3. Newer representative pages
4. High-frequency pattern across relevant pages
5. Older or isolated instances

Do not silently pick a value when the sources remain ambiguous. Add an entry under `Design Inconsistencies` with `Observed`, `Expected Canonical`, `Evidence`, and `Recommendation`. Label the recommendation as such rather than as an existing Figma rule.

### 6. Create or update the output suite

Follow [references/design-md-schema.md](references/design-md-schema.md) for `DESIGN.md` and [references/preview-contract.md](references/preview-contract.md) for both HTML files. Make the suite operational: another agent should be able to build a consistent list, detail, form, or dashboard page using it, then visually inspect the same rules in the previews.

For an existing document:

1. Compare existing rules with current Figma evidence.
2. Preserve still-valid prose, naming, and code mappings.
3. Add newly supported rules and update changed values with evidence.
4. Move unresolved contradictions to `Design Inconsistencies` instead of flattening them.
5. Remove a prior rule only when current evidence disproves it or the user explicitly requests removal.

Avoid duplicate parallel token names. When Figma and code use different names, preserve the canonical design name and document the implementation alias in `Code Mapping`.

Update existing previews instead of replacing supported, product-specific specimens with generic galleries. Add newly established tokens, components, states, and page patterns; correct values that changed; and retain still-valid examples.

### 7. Build the previews

Both files are standalone visual acceptance artifacts, not marketing pages:

- `preview.html` presents the verified or derived light system.
- `preview-dark.html` presents the corresponding dark system.
- Lead with a realistic admin specimen that demonstrates the actual app shell and a representative page pattern. Follow it with foundations, components, states, and layout specimens.
- Use CSS custom properties whose semantic names match `DESIGN.md`.
- Keep important content and component coverage aligned between themes; vary theme values, surfaces, borders, effects, and state treatment intentionally.

When Figma defines a dark mode, use its verified Variables and components. When it does not, still create `preview-dark.html`, but label it visibly as a **Proposed Dark Mapping**, classify its tokens as derived or recommended in `DESIGN.md`, and preserve the product's hierarchy and component geometry. Never imply that a proposed mapping exists in Figma.

### 8. Verify

Before finishing, check that:

- All three output files are at the project root; `DESIGN.md` remains valid Markdown and both previews open directly without a build step.
- Exact values and semantic rules are visibly distinguished.
- Important claims cite usable Figma references.
- No estimate, recommendation, or historical exception is presented as canonical fact.
- Components cover usage and states, not just dimensions.
- Page patterns reflect observed compositions rather than a generic admin template.
- Existing supported guidance survived an incremental update.
- The document contains enough concrete values and rules to implement representative admin pages without reopening all of Figma.
- The previews contain no overlapping or clipped UI at desktop and mobile widths, expose visible keyboard focus, and differ materially between light and dark themes.

Run:

```bash
python3 <skill-directory>/scripts/validate_output.py <project-root>
```

Then inspect both previews in a browser at approximately `1440x900` and `390x844`. Check the console, responsive reflow, text containment, keyboard focus, and theme fidelity. Fix issues before reporting completion.

Report the three files created or updated, evidence sampled, whether the work was a creation or incremental update, validation performed, and any unresolved gaps. Do not paste the full document into chat.
