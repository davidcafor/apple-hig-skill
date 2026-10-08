import SwiftUI

// Scope: tvOS 16+. Native buttons participate in directional focus.
// Test real spacing, focus movement, and scrolling in the containing screen.
struct TelevisionFocus: View {
    let play: () -> Void
    let showDetails: () -> Void

    var body: some View {
        HStack(spacing: 40) {
            Button("Play", action: play)
            Button("Details", action: showDetails)
        }
        .padding(40)
    }
}
