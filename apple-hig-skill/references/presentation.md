# Presentation and task boundaries

## PRESENT-01: Pick the surface by the interaction

| Need | Candidate | Important qualification |
| --- | --- | --- |
| Navigate deeper into persistent content | Navigation destination | Preserve a clear return path |
| Complete a focused task related to the current view | Sheet | Decide cancellation and save semantics |
| Inspect or adjust content while continuing the task | Inspector, panel, or supported nonmodal sheet | Presentation behavior differs by platform |
| Show brief anchored information or controls | Popover | Compact environments may adapt it |
| Resolve an important interruption or unexpected risk | Alert | Do not use for routine status updates |
| Choose among responses to an intentional action | Confirmation dialog/action sheet | Use platform-appropriate behavior |
| Work on an independent document or long task | Window or suitable full-screen flow | Preserve ownership and exit behavior |

This table is an **implementation interpretation**, not a universal API mapping. Sources: [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets), [Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers), [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts), [Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets).

## PRESENT-02: Sheets have an intelligible exit

Apple recommends scoped tasks, avoiding sheet-on-sheet navigation from the main interface, and providing a clear alternative to committing changes. iOS/iPadOS can support nonmodal sheets; other listed platforms have different modality expectations. Source: [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets).

**Implementation interpretation:** decide whether edits are live or staged. For staged edits, Cancel discards the draft and Save commits it; merely dismissing a view does not undo mutations made through a binding. A multi-step flow can navigate within one sheet rather than accumulating sheets.

**Verify:** button dismissal, supported gesture dismissal, Escape/Back, unfinished input, keyboard, and parent-window interaction. If dismissal must be blocked to protect unsaved work, explain the reason and provide an exit; do not disable it indiscriminately. Detents must leave content and actions reachable.

## PRESENT-03: Popovers remain lightweight and anchored

Keep content limited and related to the trigger; avoid presenting warnings or stacking popovers. Account for automatic dismissal and compact adaptation. Source: [Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers).

**Implementation interpretation:** do not discard a user's work merely because they click outside. For substantial editing or decisions that must be explicit, reconsider the surface. Avoid insisting that an iPhone popover look identical to a Mac popover.

**Verify:** trigger visibility, anchor movement, outside click/tap, keyboard exit, resize, and whether edited values survive or cancel according to the promised semantics.

## PRESENT-04: Alerts and confirmations are proportional

Use alerts for important actionable interruptions, not ordinary empty states or every successful save. Routine undoable actions often do not warrant a warning. Use clear action labels and an appropriate destructive role with a safe cancellation path. Source: [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts).

A set of choices following an intentional action may fit a confirmation dialog instead. Source: [Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets).

**Implementation interpretation:** distinguish irreversible deletion from reversible removal. Avoid a Return-key default that unexpectedly destroys data. Confirm a delayed action still targets the intended item, not a newly selected one.

**Verify:** destructive and cancel paths, rapid repeated invocation, disappearing targets, long translations, and assistive-technology announcement. Existing absence of an alert is not automatically a defect: inspect undo and recoverability first.
