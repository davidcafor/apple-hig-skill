import SwiftUI

// Scope: macOS 13+. Integrate the Settings scene into your existing App.
// This is not marked @main so it can be typechecked alongside other snippets.
struct SettingsExampleApp: App {
    var body: some Scene {
        WindowGroup {
            Text("Example Workspace").padding()
        }
        Settings {
            GeneralSettings()
        }
    }
}

struct GeneralSettings: View {
    @AppStorage("showCompletedItems") private var showCompletedItems = true

    var body: some View {
        Form {
            Toggle("Show completed items", isOn: $showCompletedItems)
        }
        .padding()
        .frame(minWidth: 320, idealWidth: 380)
    }
}
