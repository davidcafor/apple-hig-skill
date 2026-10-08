import SwiftUI

// Scope: iOS/iPadOS 16+, macOS 13+, tvOS 16+, watchOS 9+, visionOS 1+.
// Both layouts preserve the essential action. Localize and test long labels.
struct AdaptiveActions: View {
    let title: String
    let open: () -> Void

    var body: some View {
        ViewThatFits(in: .horizontal) {
            HStack {
                Text(title).fixedSize(horizontal: true, vertical: false)
                Button("Open", action: open)
            }
            VStack(alignment: .leading) {
                Text(title).fixedSize(horizontal: false, vertical: true)
                Button("Open", action: open)
            }
        }
        .padding()
    }
}
