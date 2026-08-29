# Admin Form, Overlay, and Risk Patterns

Forms should reduce ambiguity and recovery cost. Use the smallest container that safely supports the task, then follow the existing Figma system for fields and validation.

## Choose the container

- Use an inline edit for a small, low-risk change whose context must remain visible.
- Use a modal for a short, focused decision or confirmation that should block the underlying workflow.
- Use a drawer for a moderate task that benefits from retaining list or detail context.
- Use a page for long, multi-section, high-impact, shareable, or independently navigable work.

Do not force a complex workflow into a small overlay. Define close, cancel, escape, outside-click, and unsaved-change behavior according to risk.

## Organize the form

- Group fields by business meaning, not merely by data type.
- Put the most identifying and consequential fields early.
- Use labels that match domain language and helper text only when it prevents a likely error.
- Mark required and optional fields consistently with the existing system.
- Use searchable entity selection when operators need to disambiguate similar records.
- Keep units, currency, timezone, formats, limits, and irreversible effects adjacent to the relevant input.
- Use sticky or bottom actions for long forms when operators otherwise lose access to save/cancel controls.

## Validation and save states

Define initial, focused, populated, invalid, disabled, submitting, success, and server-error behavior. Place field-specific errors by the field and preserve entered values after recoverable failures. Use a form-level summary when errors are distributed across collapsed or distant sections.

Clarify whether saving is immediate, section-based, or whole-form. Prevent duplicate submission and show a stable progress state. For long-running work, distinguish acceptance from eventual completion.

## Dangerous operations

Treat delete, ban, freeze, reject, reset, clear, force-end, and manual balance adjustments as risk-bearing operations. The flow should communicate:

1. What entity or scope will be affected
2. Whether the effect is reversible
3. The immediate and downstream impact
4. Whether a reason, evidence, or note is required
5. Who can perform the action
6. What confirmation strength is proportionate to the risk

Use danger styling on the destructive action and confirmation, not across the entire ordinary page. Require a second confirmation, typed identifier, or explicit impact acknowledgement only when the potential harm justifies the friction.

For financial adjustments, expose the current value, adjustment direction and amount, resulting value, currency, reason, and audit consequence before confirmation. Never make a balance-changing action look like a routine save.

## Overlay details

- Give modals and drawers an explicit title, affected entity, clear primary action, and safe cancel path.
- Keep the primary action label specific, such as `Freeze account` rather than `Confirm`.
- Preserve background context without allowing accidental conflicting operations.
- Provide success or failure feedback after the overlay closes when the resulting state matters on the underlying page.
