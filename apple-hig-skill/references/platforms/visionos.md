# visionOS

## VISION-01: Choose the right spatial container

**Apple guidance:** use familiar windows for ordinary interface tasks; select immersion according to the experience rather than maximizing it. Prioritize visual and physical comfort. Source: [Designing for visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos#Best-practices).

**Decision:** a window suits text and controls; a volume suits bounded spatial content; an immersive space suits content that needs the surrounding environment. Check actual APIs and capabilities for the target. Do not prescribe an immersive space for a settings form.

**Verify:** entry/exit, interruptions, recentering, different window sizes, readable content, and accessibility. A simulator can establish some layout behavior but not headset comfort or reliable eye targeting.

## VISION-02: Stable placement and comfortable targeting

**Apple guidance:** keep important content conveniently visible, favor indirect interaction, and avoid attaching substantial content rigidly to the wearer's head. Provide space for targeting and hover feedback. Source: [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout).

**Implementation interpretation:** anchor scene content in space where appropriate; do not implement constant head-following as a shortcut for visibility. Avoid overlapping targets, dense icon rows, or sustained reach requirements. Source-specific point spacing is not an arbitrary world-space distance.

## VISION-03: Preserve control over immersion

Let people choose entry and exit; use predictable transitions and maintain meaningful access at supported immersion levels. Avoid encouraging movement through obscured surroundings. Source: [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences).

Prefer system window materials and controls. Ornaments serve related controls; they are not a universal replacement for supplemental windows. Read [Windows](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS) and [Layout](../layout-visual.md). Test the actual headset before claiming ergonomic validation.
