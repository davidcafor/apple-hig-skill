# Adaptive layout and visual design

## LAYOUT-01: Adapt to the container, preserve the task

**Apple guidance:** respond to available space, text changes, localization, and window changes. Where meaningful, use size classes rather than device identity or orientation; preserve access to functionality as space changes. Source: [Layout](https://developer.apple.com/design/human-interface-guidelines/layout#Adaptability).

**Implementation interpretation:** let native containers lay out ordinary content. Use fitting layouts, wrapping, scrolling, or contextual disclosure before fixed screen dimensions. Optional size classes are not universal measurements: use actual container constraints when needed, especially outside iOS/iPadOS. A fixed icon or illustration size can be valid; a fixed height that clips an essential label is not.

**Verify:** narrow and short windows, large text, keyboard shown, safe areas, and long localized content. Check transitions while editing, not only fresh launches. Preserve state outside mutually exclusive layout branches.

## LAYOUT-02: Treat safe areas as environment data

Use system layout guides to keep readable and interactive content clear of system UI. Sources: [Layout](https://developer.apple.com/design/human-interface-guidelines/layout#Guides-and-safe-areas), [Windows](https://developer.apple.com/design/human-interface-guidelines/windows).

**Implementation interpretation:** edge-to-edge backgrounds can ignore safe areas while foreground controls remain inset. Do not replace a system inset with a guessed home-indicator height. A custom pinned bar must reserve layout space and remain accessible with the keyboard. Do not flag `ignoresSafeArea` solely by matching its name; inspect what it affects.

## VISUAL-01: Typography supports hierarchy and scale

Prefer system text styles for familiar hierarchy. Custom typography is valid when legible and adaptable. Larger text may require rearrangement and more vertical space; preserve important content rather than shrinking it back down. Source: [Typography](https://developer.apple.com/design/human-interface-guidelines/typography).

**Implementation interpretation:** inspect fixed frames, forced line limits, and aggressive minimum scale factors around essential text. Use truncation deliberately for summaries with an accessible route to the full value. Platform font tables differ; do not apply an iPhone body size to every platform. Font weight choices are not universal HIG violations.

**Verify:** meaningful labels and values remain comprehensible at supported large sizes; icons do not become misleadingly tiny relative to text. Inspect both actual rendering and accessibility output.

## VISUAL-02: Color conveys meaning accessibly

Use semantic system colors where they match the role, preserve their meaning, and test light/dark and increased-contrast appearances where supported. Communicate important state through more than color. Source: [Color](https://developer.apple.com/design/human-interface-guidelines/color).

**Implementation interpretation:** pair validation colors with explanatory text or symbols. A brand color is allowed, but measure its actual foreground/background contrast. A hex value alone cannot establish contrast over translucent or varying content. Do not claim visual contrast passes from source inspection.

## VISUAL-03: Materials distinguish controls from content

Current HIG guidance reserves Liquid Glass for appropriate control/navigation layers and recommends restraint. Standard materials and Liquid Glass are not interchangeable labels for any blur. Source: [Materials](https://developer.apple.com/design/human-interface-guidelines/materials).

**Implementation interpretation:** use supported system components first. Do not apply glass to every content card or manually recreate system chrome. Inspect legibility over real content and accessibility appearance settings. Account for API availability and platform material differences; newer appearance alone is not permission to raise a deployment target.

## VISUAL-04: Symbols preserve meaning

Choose symbols by meaning and validate their rendering mode, scale, weight, and availability in context. Use animation to communicate, not decorate continuously. Custom symbols need appropriate alternative labels. Source: [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols).

**Verify:** selected/unselected states, monochrome or tinted contexts, labels with the symbol hidden, and the oldest supported OS. Decorative symbols should not create duplicate accessibility stops. Do not infer that every SF Symbol name exists on every target.
