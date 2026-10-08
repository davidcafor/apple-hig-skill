# Review and validation

## Evidence and priority

A finding needs an observable issue, a relevant source, and a concrete consequence. Use local rule IDs to organize reviews, never as invented Apple policy numbers.

| Priority | Meaning | Example |
| --- | --- | --- |
| High | Core task blocked, destructive surprise, or essential access unavailable | Cancel saves a destructive edit; an essential icon has no accessible name |
| Medium | Material usability problem with a workaround | Narrow window hides an action that remains reachable from a menu |
| Low | Specific, supported refinement | A recoverable error omits a useful next step |

Priority follows impact and context, not the number of guidelines cited. A theoretical concern is a question or test request, not a confirmed defect.

## Resolve uncertainty

1. Locate the platform-specific recommendation and its exceptions.
2. Check the live official source for disputed measurements, changed visual treatments, or availability-sensitive advice.
3. Separate design guidance from API availability, App Store rules, and your preferred implementation.
4. If two recommendations appear inconsistent, explain their scope and retain uncertainty rather than inventing a universal rule.
5. If sources cannot be accessed, state that the stored reference is dated. Do not fabricate quotations or verification dates.

## Useful finding format

- **Location and platform:** file/line or identifiable screen; supported OS context.
- **Observed behavior:** what the evidence establishes.
- **Impact and priority:** who cannot do what, and under which condition.
- **Basis:** Apple guidance, implementation interpretation, or needs verification; local ID and exact official URL.
- **Correction:** the smallest change that addresses the issue.
- **Validation:** checks performed and remaining runtime/device checks.

Example: “On iPhone, the sheet's text field edits the stored title directly; Cancel dismisses without reverting. This can save changes the person explicitly canceled. PRESENT-02 is an implementation interpretation supporting a clear scoped task. Use local draft state and commit on Save. Verified in the state flow; still test interactive dismissal and relaunch.” Link the relevant [Sheets guidance](https://developer.apple.com/design/human-interface-guidelines/sheets); do not claim Apple mandates one Swift property wrapper.

Weak finding: “This uses a custom font, so it violates HIG.” A custom font alone establishes no violation. Look for actual readability, scaling, or meaning problems.

## Validation matrix

| Evidence | Can establish | Cannot establish alone |
| --- | --- | --- |
| Source inspection | State flow, labels, selected APIs | Final contrast, focus order, comfort |
| Typechecking/build | Syntax and selected SDK availability | Interaction correctness or all deployment configurations |
| Screenshot | Visible arrangement in one state | VoiceOver, keyboard, scrolling, dynamic transitions |
| Simulator interaction | Reproducible behavior under tested conditions | Real hardware inputs, viewing distance, physical comfort |
| Device/assistive technology session | Behavior in that tested configuration | Universal accessibility or complete HIG compliance |

Choose relevant checks: narrow/wide resizing, larger text, long translations, RTL, light/dark appearance, Increase Contrast, Reduce Transparency, Reduce Motion, VoiceOver, keyboard, pointer, Switch Control or Voice Control, focus on TV, Crown on Watch, and indirect input in visionOS. Do not claim every check is possible on every platform.

Include empty/loading/error/offline states, cancellation and recovery, window restoration and multiple windows where supported. Re-run checks affected by the change; avoid unrelated rewrites just to increase coverage.

## Evaluation discipline

The repository's evaluation cases define expected behavior and false-positive controls. An evaluation requires an actual agent response scored against the rubric. Valid JSON, Markdown links, and successful sample compilation are useful structural checks, not a behavioral evaluation. Track agent/version, prompt, repository fixture, enabled skills, date, raw response, and reviewer scores. Compare the same tasks with and without the skill; do not publish invented pass rates.
