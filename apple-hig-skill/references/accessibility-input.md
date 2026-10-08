# Accessibility and input

## ACCESS-01: Inspect the semantic interface

**Apple guidance:** meaningful elements and images need useful descriptions; purely decorative images should not add noise. Organize groups, headings, and traversal in a meaningful way. Source: [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/voiceover).

**Implementation interpretation:** preserve native labels before adding overrides. A row containing several independent actions must not become one inaccessible combined element. A chart needs an equivalent way to understand its data, not a label saying only "Chart". Avoid labels that repeat a role already announced by the control.

**Verify:** perform the task with VoiceOver, including updates, modal entry/exit, errors, selection, and focus restoration. An `accessibilityLabel` modifier alone is not a passing audit. Do not flag a correctly labeled icon-only button simply because its visible text is hidden.

## ACCESS-02: Cover more than vision

Support alternatives to essential audio cues, captions where appropriate, simple interactions, and ways to complete tasks without a precise or time-limited gesture. Source: [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).

**Implementation interpretation:** identify essential information available only through color, sound, motion, or a gesture. Prefer redundant channels and accessible actions. Treat Switch Control and Voice Control as distinct checks; passing VoiceOver is not proof they work.

**Verify:** muted audio, speech input where available, alternative controls for dragging, and sufficient time to perceive/act on transient feedback.

## ACCESS-03: Honor motion preferences without losing feedback

Motion should explain a transition or state, remain controllable, and avoid discomfort. Sources: [Motion](https://developer.apple.com/design/human-interface-guidelines/motion), [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).

**Implementation interpretation:** use the environment's Reduce Motion setting to replace large spatial movement with a gentler transition or immediate update. Keep success and failure understandable. Do not erase all feedback or add an arbitrary delay when reducing animation. Spatial experiences need additional comfort validation.

## ACCESS-04: Measure targets in context

Apple's [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Mobility) page distinguishes default and minimum control sizes, while [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons#Best-practices) gives a general hit-region recommendation. These are different statements. Do not collapse them into "every Apple control must be 44 × 44" or apply a bare minimum as a universal design goal.

**Review procedure:** identify platform, input, control type, actual hit region and spacing; consult both relevant sections for numeric claims; favor native controls and comfortable targets. Explain the cited recommendation and context when flagging a size issue. A 20-point glyph inside a larger button is not automatically a 20-point target. Do not enlarge Mac controls mechanically to phone dimensions.

## ACCESS-05: Keyboard and focus follow the task

Preserve platform shortcuts, support logical traversal and visible focus, and avoid unsolicited focus movement. Sources: [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards), [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection).

**Implementation interpretation:** assign focus when it helps a deliberate transition, such as submitting an invalid field or opening a search task. Distinguish keyboard input focus, tvOS directional focus, selection state, and accessibility focus. Avoid trying to solve all of them with one binding.

**Verify:** Tab/Shift-Tab where supported, arrows, Return/Space, Escape/Back, standard shortcuts, modal containment, and restoration after dismissal. Never assume a mouse can reach every remote-focus target.

## ACCESS-06: Dragging and undo have alternatives

Offer another route for drag-and-drop operations and predictable outcomes; preserve recoverability where appropriate. Use standard undo/redo conventions for reversible editing. Sources: [Drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop), [Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo).

**Verify:** invalid drops, move versus copy, multiple items where supported, cancellation, undo/redo, keyboard commands, and a non-dragging route. Do not add drag support to an unrelated feature merely because it is possible.

## ACCESS-07: Contrast is a rendered property

Measure actual text/control states against their displayed backgrounds, including transparency and supported appearance settings. Use the current source's criteria and a suitable measurement tool. Sources: [Color](https://developer.apple.com/design/human-interface-guidelines/color), [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility#Vision).

Report the measured pair, state, method, and criterion. A screenshot can support a visual measurement but cannot prove all states or assistive-technology behavior. For text resizing, use [VISUAL-01](layout-visual.md#visual-01-typography-supports-hierarchy-and-scale).
