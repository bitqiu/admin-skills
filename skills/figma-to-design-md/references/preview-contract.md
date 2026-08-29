# Preview Contract

Create `preview.html` and `preview-dark.html` beside `DESIGN.md` in the project root. They are visual acceptance artifacts for the extracted admin design system. The collection pattern is informed by [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md), while the content must remain specific to the inspected Figma product.

## File roles

| File | Role |
| --- | --- |
| `preview.html` | Light-theme product specimen and visual catalog |
| `preview-dark.html` | Corresponding dark-theme specimen and catalog |

Both files must open directly in a browser without a build step. Inline the CSS and small scripts needed for the preview. External fonts or assets must have usable local/system fallbacks so loss of network access does not make the preview blank or illegible.

## Shared information architecture

Keep both previews aligned in structure and demonstrated content:

1. Compact catalog navigation
2. First-viewport representative admin specimen
3. Semantic color roles and contrast pairings
4. Typography hierarchy
5. Spacing, shape, border, and elevation tokens
6. Controls and form states
7. Table and data-display behavior
8. Overlays, feedback, and empty/loading/error states
9. Observed page-pattern specimens
10. Evidence and theme-status note

Omit a catalog area only when it is unsupported by the sampled evidence and explain the omission in `DESIGN.md`. Do not invent a large component family merely to fill the preview.

## First viewport

Show a realistic product screen, not a marketing hero or a decorative cover. Use the actual observed app shell and one high-value page pattern, typically a list/work-queue view with sidebar, header, filters, table, status treatment, pagination, and an action or detail region. Choose a different pattern when the Figma evidence makes it more representative.

Use credible domain labels and data inferred from the product context. Keep the specimen dense, quiet, and work-focused. Avoid giant headings, generic card grids, nested decorative cards, gradients without a source role, and explanatory feature copy inside the UI.

## Design fidelity

- Define CSS custom properties using the same semantic token names as `DESIGN.md` where CSS naming permits.
- Match documented typography, dimensions, spacing, radius, borders, shadows, icon treatment, and component states.
- Demonstrate normal plus important hover, focus, selected, disabled, loading, empty, error, and destructive states when supported.
- Use the repository's icon library only when it can run in a standalone preview; otherwise use accessible text or a stable icon source and document the substitution.
- Keep the previews visually inspectable as design-system catalogs, but make every specimen native to the source product rather than a generic UI kit.

## Light and dark themes

The two files should share product identity, structure, component geometry, content hierarchy, and catalog coverage. They must differ materially in theme tokens and tuned surface behavior; changing only `color-scheme` is insufficient.

When Figma provides dark Variables, Styles, or representative dark frames, use those verified values. When Figma has no dark system:

- Still create `preview-dark.html` as a **Proposed Dark Mapping**.
- Add a visible status note near the top of the preview.
- Classify dark values as Derived Rule or Recommendation in `DESIGN.md`.
- Preserve semantic contrast, hierarchy, density, and geometry from the verified light system.
- Do not edit Figma or call the proposed theme canonical.

## Responsive and interaction quality

- Support at least `390px`, `768px`, `1024px`, and `1440px` widths.
- Use explicit constraints such as stable sidebar/control dimensions, `minmax()`, and overflow behavior so dynamic labels or states do not shift the layout unexpectedly.
- Reflow or scroll wide tables deliberately at narrow widths; never squeeze columns until content overlaps.
- Provide semantic HTML, labels, visible `:focus-visible` treatment, adequate contrast, keyboard-operable controls, and reduced-motion handling.
- Use lightweight interactions only when they clarify the system, such as tabs, selected rows, filters, sidebar collapse, dialog/drawer toggles, or pagination. Static state galleries are acceptable when they communicate the rule more clearly.

## Incremental maintenance

Read existing previews before editing. Preserve correct, product-specific examples and interaction behavior. Keep both themes synchronized when adding or removing catalog areas. If the source Figma changes only one mode, update that mode and verify that shared geometry and component structure remain aligned.

## Browser verification

After running `scripts/validate_output.py`, inspect screenshots of both previews near `1440x900` and `390x844`. Confirm:

- The first viewport unmistakably resembles the source admin product.
- No text, control, table, navigation, dialog, or drawer overlaps or clips incoherently.
- Referenced fonts, icons, and assets render; fallback behavior remains legible.
- Keyboard focus and important interaction states are visible.
- Light and dark themes are clearly distinct and each has intentional surface, border, shadow, and muted-text treatment.
- Browser console errors are resolved.
