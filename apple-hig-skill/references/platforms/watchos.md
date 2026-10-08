# watchOS

## WATCH-01: Design the wrist task separately

**Apple guidance:** prioritize brief, glanceable interactions, shallow navigation, and Digital Crown support. Complications and notifications may be more important entry points than the main app. Source: [Designing for watchOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos#Best-practices).

**Review:** identify the information needed now and the action possible in a short interaction. Flag a copied phone workflow that requires long text entry or several configuration screens before a simple action.

**Implementation interpretation:** choose a focused task with sensible defaults and visible success/failure. Use system scrolling and pickers before custom Crown handling. Preserve task state when the wrist lowers; inspect any Always On behavior for privacy and legibility using its dedicated guidance before changing it.

**Verify:** small and large supported watch sizes, readable labels, Crown scrolling, reduced motion, accessibility, interruption and resumption. Do not claim physical comfort based on the simulator.

## WATCH-02: Controls and settings fit the context

Favor a small set of large actions rather than a dense control strip. Corner actions belong in the system toolbar. For occasional essential settings, evaluate a small in-app area rather than assuming a custom pane in the system Settings app is available. Read [Buttons — watchOS](https://developer.apple.com/design/human-interface-guidelines/buttons#watchOS), [Layout — watchOS](https://developer.apple.com/design/human-interface-guidelines/layout#watchOS), and [Settings — watchOS](https://developer.apple.com/design/human-interface-guidelines/settings#watchOS).

A SwiftUI `TabView` can support watch-specific page navigation; the HIG's phone-style tab-bar advice is not a requirement for watchOS. See [System experiences](../system-experiences.md) for complications and Smart Stack widgets.
