# Product flows

## FLOW-01: Settings belong at the right level

**Apple guidance:** Prefer sensible defaults and expose options people actually need. Keep task-specific choices near the task; avoid replicating system-wide preferences. On Mac, provide the conventional Settings command and shortcut through the app's scene structure. On Watch, keep necessary app settings brief and accessible within the app; do not assume a custom pane in system Settings.

**Implementation interpretation:** Separate persistent preferences from unsaved editing state. Explain the scope of a setting when it affects other windows, devices, or accounts. Do not silently overwrite a document preference with an app-wide default. Test persistence, reset behavior, and multiple windows where supported.

Source: [Settings](https://developer.apple.com/design/human-interface-guidelines/settings).

## FLOW-02: Teach in context

**Apple guidance:** Help people begin quickly and introduce unfamiliar interactions when useful. Onboarding should support the task rather than require a tour of every feature.

**Implementation interpretation:** Make optional education dismissible and discoverable later. Request setup only when needed to make the next step work; required account or safety setup can legitimately precede use. Test first launch, returning users, interrupted setup, and changed permissions. Do not treat every introductory screen as a violation.

Source: [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding).

## FLOW-03: Represent the real state of work

**Apple guidance:** Give appropriate progress feedback and avoid making an interface appear unresponsive. Use determinate progress when progress can be measured reliably. Feedback should explain results without overwhelming the task.

**Implementation interpretation:** Specify initial loading, loaded content, no content, no search results, offline, recoverable failure, and partial success where they exist. These states need different recovery actions. Preserve entered data on failure; prevent accidental duplicate submissions while allowing cancellation where feasible. Do not show invented percentages or an indefinite spinner after an operation has failed. A cached view can remain usable while refreshing if its state is clear.

**Verify:** Exercise slow responses, cancellation, failure, retry, and leaving/reentering the screen. Check VoiceOver announcements for useful updates without repeated interruption.

Sources: [Loading](https://developer.apple.com/design/human-interface-guidelines/loading), [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback).

## FLOW-04: Accounts and privacy at the point of need

**Apple guidance:** Make account interactions understandable and respect people's control over personal information. Explain why a permission benefits the current task and request it in relevant context.

**Implementation interpretation:** Handle denied, restricted, and subsequently revoked access. Provide a usable alternative when the feature permits it; do not loop permission prompts or manufacture a system dialog. Avoid putting private account data in previews, logs, notifications, or shared surfaces without an appropriate policy. Distinguish product design guidance from current App Store and legal obligations; consult those sources separately when relevant.

**Verify:** New account, signed-out state, expired session, cancellation, unavailable authentication, permission denial, and account deletion entry points if accounts are supported. Do not infer server-side deletion behavior from a button's label.

Sources: [Managing accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts), [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy).
