# iOS

## IOS-01: A task-first touch experience

**Apple guidance:** prioritize the primary task, make secondary functionality discoverable, and accommodate handheld interaction. Support changes in appearance and text size. Source: [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios#Best-practices).

**Review:** identify the shortest meaningful task, its entry and exit, and whether a person can recover after switching apps. Check controls near screen edges, system gestures, keyboard presentation, and whether essential actions require an undiscoverable gesture.

**Implementation interpretation:** keep the system Back behavior where using hierarchical navigation; provide an accessible action for custom gesture-only operations. Choose persistent top-level navigation independently from the controls that act on the current content. System containers usually handle these distinctions better than a custom bottom bar.

**Exceptions:** a game, camera, drawing canvas, or immersive media viewer can justify a specialized layout. Evaluate its alternative controls and exit behavior rather than insisting that every screen be a form or list.

**Verify:** the relevant phone window sizes and orientations, largest supported text settings, keyboard shown, interactive Back, task interruption, and VoiceOver. Check both initial and populated states. A screenshot cannot establish usable hit regions.

Related: [Navigation](../navigation.md), [Layout](../layout-visual.md), [Input](../accessibility-input.md).
