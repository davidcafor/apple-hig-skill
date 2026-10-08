import SwiftUI

// A real Button retains standard activation and accessibility semantics.
// The visible text remains available when a symbol is unfamiliar.
struct AccessibleAction: View {
    let isSaved: Bool
    let save: () -> Void

    var body: some View {
        Button(action: save) {
            Label(isSaved ? "Saved" : "Save", systemImage: isSaved ? "checkmark" : "square.and.arrow.down")
        }
        .disabled(isSaved)
    }
}
