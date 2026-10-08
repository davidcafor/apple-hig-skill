import SwiftUI

// Scope: iOS/iPadOS 16+, macOS 13+, tvOS 16+, watchOS 9+, visionOS 1+.
// The status remains understandable when animation is disabled.
struct ReducedMotionFeedback: View {
    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    let isComplete: Bool

    var body: some View {
        Label(isComplete ? "Complete" : "In progress",
              systemImage: isComplete ? "checkmark.circle.fill" : "clock")
            .scaleEffect(isComplete && !reduceMotion ? 1.04 : 1)
            .animation(reduceMotion ? nil : .easeInOut(duration: 0.2), value: isComplete)
    }
}
