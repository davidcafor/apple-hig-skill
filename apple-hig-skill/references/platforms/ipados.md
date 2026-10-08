# iPadOS

## IPAD-01: Use space without losing continuity

**Apple guidance:** support different input modes and adapt to multitasking and appearance changes. Use available space to expose useful content while limiting unnecessary modal transitions. Source: [Designing for iPadOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados#Best-practices).

**Review:** inspect the narrowest supported window as well as expanded layouts. A full-screen landscape screenshot is insufficient. Ensure touch, keyboard, and pointer workflows remain usable; Pencil interaction is relevant when the task benefits from it, not a universal requirement.

**Implementation interpretation:** preserve selection and task state above any compact/expanded branching. Distinguish a tab hierarchy that can adapt into a sidebar from a source/detail hierarchy. Do not force every iPad app into three columns. Use the specific [tab/sidebar guidance](../navigation.md) for that decision.

**Failure examples:** an inspector containing the only export control disappears in compact width; changing width recreates an editor and loses an unsaved draft; the keyboard covers a form's only submit action.

**Verify:** resize during an active task; collapse and restore navigation columns; show and hide the keyboard; navigate with a pointer and keyboard; drag content only if supported by the feature. Confirm essential actions remain reachable rather than demanding identical visible controls at every width.

Window chrome belongs to the system; see [Windows](https://developer.apple.com/design/human-interface-guidelines/windows#iPadOS) and [Layout](../layout-visual.md).
