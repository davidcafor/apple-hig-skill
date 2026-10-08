# System experiences

Treat each surface as a distinct interaction contract. Confirm current platform, entitlement, family, and API support before implementation. These references establish review questions; they do not implement an extension or guarantee eligibility.

## SYS-01: Widgets

**Apple guidance:** Present useful, timely, glanceable information appropriate to the widget's size and context. Use system conventions and make navigation into the app meaningful.

**Implementation interpretation:** Choose a small useful task rather than shrinking an entire screen. Validate supported families, system rendering modes, content margins, privacy/redaction, placeholder states, and stale data. Check current WidgetKit rules before adding interactions; a widget is not an arbitrary live SwiftUI screen. Deep links should reach the corresponding content and recover gracefully when it no longer exists.

Source: [Widgets](https://developer.apple.com/design/human-interface-guidelines/widgets).

## SYS-02: Live Activities

**Apple guidance:** Support an ongoing activity with concise, current information in the system-provided presentations.

**Implementation interpretation:** Model start, update, stale, ended, and dismissed states. Adapt information density to supported presentations instead of repeating identical content everywhere. Do not assume all platforms, devices, or OS releases support the same surfaces and interaction. Confirm current ActivityKit constraints separately. Avoid using an ongoing-activity surface as an unrelated promotion.

Source: [Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities).

## SYS-03: Watch complications

**Apple guidance:** Make useful information recognizable at a glance in the available complication space.

**Implementation interpretation:** Select the right information for each supported family, provide a meaningful app destination, and account for stale data, privacy, and limited update opportunities. Test on actual watch faces and with accessibility settings. Do not assume a round screenshot proves every family works.

Source: [Complications](https://developer.apple.com/design/human-interface-guidelines/complications).

## SYS-04: Notifications

**Apple guidance:** Deliver relevant, understandable information and actions with respect for attention and privacy.

**Implementation interpretation:** Explain the benefit before requesting authorization at an appropriate point. Support denied permission without blocking unrelated tasks. Make notification destinations valid after sign-out, deletion, or state changes. Avoid exposing sensitive content in previews. Urgency and interruption levels must reflect the event; review current API and entitlement rules before choosing privileged delivery modes.

**Verify:** Foreground/background handling, grouped messages, long localized content, disabled permissions, and expired destinations.

Source: [Notifications](https://developer.apple.com/design/human-interface-guidelines/notifications).

## SYS-05: CarPlay

**Apple guidance:** Use the system templates appropriate to the supported app category and prioritize the driving context. Keep interactions brief and legible. Present relevant errors on the car display rather than depending on unlocking the phone while driving.

**Implementation interpretation:** Establish category and entitlement eligibility before designing screens. Do not port an iPhone settings hierarchy into arbitrary car UI. Prefer the template's supported controls, navigation, and content limits. Review current CarPlay framework documentation for category-specific capabilities; this skill does not certify automotive suitability.

**Verify:** Available templates, error recovery, voice and hardware inputs, interrupted connectivity, and the actual supported display configurations. Simulator inspection alone does not establish safe in-car behavior.

Source: [CarPlay](https://developer.apple.com/design/human-interface-guidelines/carplay).
