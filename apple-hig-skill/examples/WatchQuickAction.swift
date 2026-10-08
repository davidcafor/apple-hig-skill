import SwiftUI

// Scope: watchOS 9+. The primary task stays brief and visible.
struct WatchQuickAction: View {
    let remaining: String
    let pause: () -> Void

    var body: some View {
        VStack {
            Text("Time remaining").font(.headline)
            Text(remaining).font(.title2).monospacedDigit()
            Button("Pause", action: pause)
        }
        .padding()
    }
}
