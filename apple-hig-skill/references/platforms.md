# Platform selection

Read the platform that the app actually targets, then the component references needed for the task. Reuse product intent across platforms; reassess navigation, density, input, and presentation independently.

| Platform | Read | Distinct concerns |
| --- | --- | --- |
| iOS | [iOS](platforms/ios.md) | Touch, task continuity, compact layouts, system integration |
| iPadOS | [iPadOS](platforms/ipados.md) | Resizable space, adaptable navigation, multiple input modes |
| macOS | [macOS](platforms/macos.md) | Windows, menu commands, keyboard, settings conventions |
| watchOS | [watchOS](platforms/watchos.md) | Brief interactions, Crown, glanceable content |
| tvOS | [tvOS](platforms/tvos.md) | Directional focus, remote input, viewing distance |
| visionOS | [visionOS](platforms/visionos.md) | Space, indirect interaction, comfort, immersion |

CarPlay is a distinct system experience: use [system-experiences.md](system-experiences.md#sys-05-carplay). Do not assume every Apple device runs an arbitrary SwiftUI app. Widgets, complications, and Live Activities have their own lifecycle, layout, and API constraints.

A device model, orientation, or marketing screen size does not establish the usable window area. For compatible apps running on another platform, inspect the actual execution mode and supported features before prescribing native-only behavior. Do not change the app's identity or target to make a recommendation compile.
