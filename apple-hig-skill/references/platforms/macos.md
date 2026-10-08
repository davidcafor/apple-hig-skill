# macOS

## MAC-01: Commands and windows are part of the interface

**Apple guidance:** support window management, menu-bar commands, keyboard shortcuts, precise input, and appropriate information density. Source: [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos#Best-practices).

**Review:** determine which document, window, or selection a command acts on. Check that a keyboard command and its toolbar counterpart act on the same current target, especially when multiple windows are open. Verify disabled states instead of silently ignoring an action.

**Implementation interpretation:** use native scenes and window controls. For document apps, inspect document lifecycle and undo integration before inventing parallel save or close behavior. Restore useful context without making every preference or selection global across unrelated windows.

**Exceptions:** a dedicated utility or menu-bar app may not need a document browser or multiple windows. Judge missing features against the app's workflow, not a generic desktop checklist.

**Verify:** keyboard-only task completion, window resizing, key/main/inactive windows, menu availability, Return and Escape behavior, and command routing. Test with two windows when supported.

## MAC-02: Settings have an expected entry point

Use the app menu and standard settings shortcut; separate app-wide preferences from document or task options. Prefer a native `Settings` scene in SwiftUI. Do not build a replica of the System Settings app merely to look native. A gear-only toolbar entry is insufficient when it replaces expected menu access.

Source and pane details: [Settings — macOS](https://developer.apple.com/design/human-interface-guidelines/settings#macOS). See [Product flows](../product-flows.md#flow-01-settings-belong-at-the-right-level) for scope and validation.
