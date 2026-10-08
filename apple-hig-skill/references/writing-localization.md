# Writing and localization

## WRITE-01: Explain the action and recovery

**Apple guidance:** Use clear, concise language consistent with the interface and task. Labels should help people predict what happens. Messages should communicate actionable information respectfully.

**Implementation interpretation:** Prefer a specific action such as “Delete Recording” when “OK” leaves the consequence unclear. This is contextual, not a ban on conventional short labels. Associate errors with the relevant field and describe how to recover when recovery is possible. Do not expose implementation jargon, blame people, or promise an outcome the system cannot guarantee. Preserve necessary domain terminology for expert audiences.

**Verify:** Read the interface without supporting marketing copy. Can someone identify the object, consequence, and next step? Check accessible names as well as visible strings.

Source: [Writing](https://developer.apple.com/design/human-interface-guidelines/writing).

## LOCAL-01: Layout follows language and content

**Apple guidance:** Support right-to-left interfaces appropriately. Mirroring is contextual: reading order and directional navigation differ from content with an intrinsic direction.

**Implementation interpretation:** Use leading/trailing layout and system localization facilities. Do not blindly flip every image, symbol, chart, media control, or number. Keep phone numbers, mixed-direction text, and domain-specific diagrams legible. Review system-provided symbol behavior before applying manual transforms.

**Verify:** Test a right-to-left locale with actual text, including mixed scripts and the navigation back action. Check reading order with assistive technology; a visually mirrored view may still expose the wrong order.

Source: [Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left).

## LOCAL-02: Avoid English-sized assumptions

**Implementation interpretation:** Localize complete phrases rather than concatenating fragments, use plural-aware resources, and format dates, numbers, measurements, and currency for their intended locale. These are implementation techniques supporting adaptable content, not a claim that HIG mandates one localization architecture. Avoid fixed widths that clip translations or accessibility text. Do not translate user-generated names as if they were interface labels.

**Verify:** Long translations, plural boundaries, non-Latin scripts, larger text, locale-specific calendars and number formats relevant to the app, and fallback strings. Use real translations for release validation; pseudolocalization is an early stress test.

Sources: [Writing](https://developer.apple.com/design/human-interface-guidelines/writing), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout), [Typography](https://developer.apple.com/design/human-interface-guidelines/typography).
