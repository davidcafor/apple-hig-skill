# SwiftUI implementation

HIG describes user experience. SwiftUI provides implementation tools; neither determines every architecture decision. Preserve the app's existing structure unless it prevents the requested behavior.

## API and state checklist

1. Inspect deployment targets, build settings, supported destinations, and the installed SDK. An SDK can recognize an API unavailable on older supported OS releases.
2. Consult official API availability for the exact symbol. Use runtime availability branches with a usable fallback when necessary; conditional compilation alone does not guard OS versions.
3. Choose semantic system controls before recreating their interaction with gestures. Style them where appropriate. Custom controls remain valid when the task requires them and equivalent access is implemented.
4. Locate ownership of navigation, drafts, preferences, document state, and per-window state. Preserve identity and unsaved work during resize or presentation changes.
5. Keep view calculation free of unintended side effects. Investigate performance when measured or observable; do not label an architecture preference a HIG violation.
6. Validate the touched targets and interaction states. Compilation does not establish focus behavior, VoiceOver reading order, or visual fidelity.

Useful official API entry points: [SwiftUI](https://developer.apple.com/documentation/swiftui), [ViewThatFits](https://developer.apple.com/documentation/swiftui/viewthatfits), [Settings](https://developer.apple.com/documentation/swiftui/settings), [NavigationStack](https://developer.apple.com/documentation/swiftui/navigationstack), [accessibilityReduceMotion](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducemotion).

## Original examples

These small examples are original repository material. They illustrate one decision each; they are not complete apps. The stated deployment targets are the targets used by the typecheck script, not necessarily the earliest OS supporting every symbol. Adapt the surrounding model, localization, persistence, and error handling to the product.

| Example | Decision | Targets checked |
| --- | --- | --- |
| [Accessible action](../examples/AccessibleAction.swift) | Replace a tappable image with a semantic button and meaningful label | All six platform families |
| [Adaptive actions](../examples/AdaptiveActions.swift) | Rearrange content while keeping the action available | All six platform families |
| [Draft editor](../examples/DraftEditor.swift) | Commit on Save; leave the model unchanged on Cancel | iOS/iPadOS, macOS, visionOS |
| [Mac settings](../examples/MacSettings.swift) | Use the Settings scene and persistent preference | macOS |
| [Reduced motion](../examples/ReducedMotionFeedback.swift) | Retain status feedback when motion is reduced | All six platform families |
| [TV focus](../examples/TelevisionFocus.swift) | Native buttons participate in directional focus | tvOS |
| [Watch action](../examples/WatchQuickAction.swift) | Prioritize a brief task | watchOS |

### Before and after decisions

- A decorative image with `onTapGesture` as the sole Save action → a `Button` with a useful label. Adding a label alone does not provide all button semantics.
- An inflexible horizontal row → a layout with a vertical fallback. Do not solve clipping by removing the action.
- A sheet directly mutating a saved value while offering Cancel → local draft state committed only on Save. For autosaving editors, use a presentation and labels that describe autosave honestly.
- A custom settings window launched only from a gear icon → the app's native Settings scene. Additional contextual shortcuts can remain.
- Motion as the only success signal → persistent text/symbol meaning with optional motion.

### Integration limits

DraftEditor demonstrates cancellation semantics, not persistence failure recovery or a confirmation policy for dirty drafts. Supply those when the app requires them. Its initial draft belongs to one editing session: give a new session appropriate identity rather than expecting a changed initializer argument to reset existing State.

AdaptiveActions deliberately measures the horizontal candidate without text compression. The fallback still needs testing with very large content and its parent's available height. MacSettings uses an app-wide preference; document-specific preferences need different ownership. WatchQuickAction accepts a preformatted value; a production timer needs appropriate formatting and update behavior. None of these examples proves runtime accessibility.
