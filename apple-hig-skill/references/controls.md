# Controls and forms

## CONTROL-01: Actions have native semantics

Use recognizable buttons with understandable purposes and feedback states. A custom button needs a visible press response. Emphasize the most likely action without making every choice equally prominent. Source: [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons).

**Implementation interpretation:** prefer `Button` over a styled text/image with a tap gesture for an ordinary action. An icon-only visual presentation can be correct if its accessible name conveys the action. A custom drawing gesture is not a button and should not be mechanically replaced.

**Verify:** hit area, VoiceOver label/trait, keyboard activation where supported, disabled/busy states, and repeated activation. Use platform-specific sizing; see [ACCESS-04](accessibility-input.md#access-04-measure-targets-in-context).

## CONTROL-02: Menus and context menus are different

Ordinary menus can keep unavailable commands visible to teach the command structure. Context menus contain relevant actions and generally omit unavailable items; macOS Cut/Copy/Paste are a documented exception. Context-menu commands need a discoverable route in the main interface as well. Sources: [Menus](https://developer.apple.com/design/human-interface-guidelines/menus), [Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus).

**Implementation interpretation:** do not apply one hide/disable policy to both. Give ellipses their platform meaning: more information is needed before completing the action, rather than decorating every label. Long nested menus may signal an information architecture problem.

**Verify:** no selection, multiple selection, unsupported content, keyboard access, and the alternate route to each essential command.

## CONTROL-03: Match the control to the value

| Value or operation | Candidate | Review |
| --- | --- | --- |
| Immediate command | Button | Does it communicate action and state? |
| Boolean preference | Toggle | Is the label unambiguous in both states? |
| Small set of related choices | Segmented control / radio group | Are options readable and mutually understood? |
| Longer set of choices | Picker / menu | Is ordering predictable and selection visible? |
| Approximate continuous value | Slider | Are direction and current value understandable? |
| Precise value | Field with formatter, optionally stepper | Can the user enter and correct an exact value? |

This mapping is an implementation interpretation. Platform styling is part of the choice: a Mac checkbox is not an inferior switch; outside iOS list rows a switch may be inappropriate. Sources: [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles), [Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers), [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls), [Sliders](https://developer.apple.com/design/human-interface-guidelines/sliders).

Do not mechanically use segmented controls for every kind of view navigation. On macOS, consult the tab-view guidance for switching views in the main content area. Let the system choose a sensible picker style unless the use case supports a specific one.

## CONTROL-04: Forms retain meaning during entry

Text fields suit short input; provide a useful hint, secure entry for private data, sensible tab order, appropriate formatting, and relevant keyboard behavior. Minimize typing on Watch and TV. Source: [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields).

**Implementation interpretation:** keep field identity understandable after a placeholder disappears. Use persistent visible context or accessible labeling; do not require both redundantly when a native labeled form already supplies them. Preserve valid input on errors, explain the correction near the field, and move focus deliberately. Do not disable paste in credential fields as a generic security measure.

**Verify:** empty/invalid/valid values, submission, hardware keyboard traversal, long names, locale-specific numbers, password-manager behavior if applicable, and focus after an error. Keyboard type is a convenience, not input validation.

## CONTROL-05: Customization carries interaction obligations

A custom control must preserve its role, value, disabled state, focus, labels, and supported activation paths. Use native control styling where possible before reconstructing behavior. This is an implementation interpretation of [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons), [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/voiceover), and [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection).

A visual resemblance to a system control is not evidence that these behaviors exist. Conversely, a custom color, font, or shape alone is not evidence of a HIG violation.
