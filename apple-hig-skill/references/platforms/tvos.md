# tvOS

## TV-01: Focus is a primary navigation mechanism

**Apple guidance:** support remote interaction, clear focus, and legibility from a distance. Respect shared viewing and minimize repeated sign-in. Source: [Designing for tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos#Best-practices).

**Review:** trace directional movement through each screen, including empty lists and dynamically updated rows. Identify unreachable actions, focus traps, and unexpected focus jumps. Account for focused items growing or gaining effects without clipping or obscuring neighbors.

**Implementation interpretation:** favor native focus behavior; customize only to solve a demonstrated navigation problem. Restore a sensible item after dismissing a detail screen. Do not add a pointer to imitate desktop interaction. A playback gesture may control content rather than move focus.

**Verify:** remote navigation in every direction, selection and Back, initial/restored focus, long titles, shared-profile changes, and a realistic viewing distance. Mouse clicks in a simulator do not validate remote usability.

Source: [Focus and selection — tvOS](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection#tvOS).

## TV-02: Minimize entry effort

Use suggestions and appropriate input methods for search; consider authentication on another device where supported. Do not make a television form a pixel-scaled phone form. Read [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields#tvOS) and [Managing accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts#tvOS) before proposing a custom sign-in flow.
