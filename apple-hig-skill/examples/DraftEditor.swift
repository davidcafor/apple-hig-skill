import SwiftUI

// Scope: iOS/iPadOS 16+, macOS 13+, visionOS 1+.
// Cancellation leaves the parent's model unchanged. Persist in the save closure.
struct DraftEditor: View {
    @Environment(\.dismiss) private var dismiss
    @State private var draft: String
    private let save: (String) -> Void

    init(title: String, save: @escaping (String) -> Void) {
        _draft = State(initialValue: title)
        self.save = save
    }

    var body: some View {
        NavigationStack {
            Form {
                TextField("Title", text: $draft)
            }
            .navigationTitle("Edit Title")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Save") {
                        save(draft)
                        dismiss()
                    }
                    .disabled(draft.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty)
                }
            }
        }
    }
}
