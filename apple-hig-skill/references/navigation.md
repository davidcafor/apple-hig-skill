# Navigation, commands, search, and windows

Local rule IDs identify this project's interpretations. Read the linked Apple guidance in context before treating a recommendation as a finding.

## NAV-01: Tabs describe stable destinations

**Apple guidance:** tabs switch between major areas; they do not execute commands. Keep destinations predictable when content is empty and provide useful labels. Avoid making important sections difficult to discover through overflow. Source: [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars#Best-practices).

**Review:** a Compose tab that opens an editor is an action disguised as navigation; a Saved tab that disappears when empty makes the hierarchy unstable. Prefer an action in an appropriate toolbar and a meaningful empty destination respectively. Preserve each tab's navigation context when the product requires returning to it.

**Exceptions:** a genuinely distinct app mode can justify a different hierarchy. Do not assert a universal maximum of five tabs; assess discovery, available space, and platform guidance. A watch page-style `TabView` is not a phone tab bar.

## NAV-02: Choose tabs, sidebars, and detail columns deliberately

On iPad, consider tabs first for major sections and an adaptable sidebar for more extensive navigation. A source/detail workflow can instead justify `NavigationSplitView`. A sidebar's hierarchy should remain scannable; avoid deep nesting and undiscoverable critical actions at its bottom. Sources: [Tab bars — iPadOS](https://developer.apple.com/design/human-interface-guidelines/tab-bars#iPadOS), [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars).

**Implementation interpretation:** decide from information structure, not merely horizontal width. Keep selection outside replaced layout branches. When a sidebar disappears, preserve an alternate route to its destinations. Do not assume a split view is mandatory on every iPad screen.

**Verify NAV-01/02:** empty data, deep navigation, switching sections, compact/expanded transitions, restored selection, and accessible destination labels.

## NAV-03: Toolbars expose contextual commands

Prioritize the commands needed for the current task; group related actions and use clear standard symbols or labels. Preserve standard Back/Close behavior. In macOS, expose toolbar commands in the menu bar too. Source: [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars).

**Implementation interpretation:** use semantic toolbar placements supported by the target rather than manually positioned overlays. Attach actions to the content or scene they affect. Do not hard-code a particular OS release's visual button order when the system manages it.

**Verify:** labels in overflow, keyboard equivalents, disabled states, narrow windows, active selection, and multiple windows. Custom branding alone is not a toolbar defect; inaccessible or unreachable commands are.

## NAV-04: Search has a scope and state

Explain what is searched, offer useful suggestions where applicable, and allow refinement without obscuring the results. Placement depends on whether search filters a local list or provides an app-wide discovery destination. Sources: [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields).

**Implementation interpretation:** represent initial, searching, results, no-results, and failure states separately. Preserve the query during navigation when appropriate. Avoid stale network results replacing newer ones; treat this as implementation correctness, not an invented HIG API mandate.

**Verify:** clear and cancel, keyboard focus, a long query, zero results, failure/retry, and resizing. Do not insist every search issues a network request on every keystroke; responsiveness and request strategy are separate decisions.

## NAV-05: Windows belong to the system

Use platform window controls and let windows adapt to supported sizes. A new window should have an understandable purpose and useful context. Source: [Windows](https://developer.apple.com/design/human-interface-guidelines/windows).

**Implementation interpretation:** preserve scene-specific state, distinguish closing a window from deleting its content, and choose realistic minimum sizes from content constraints. Avoid custom traffic-light imitations or assumptions that all platforms share macOS chrome.

**Verify:** creation, closing, reopening, resize, multiple-window command targeting, unsaved work, and restoration where implemented. Report document-lifecycle concerns separately from visual preferences.
