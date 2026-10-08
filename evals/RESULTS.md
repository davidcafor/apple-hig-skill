# Validation record — 0.2.0

Date: 2026-10-08. This report separates structural, compiler, behavioral, and runtime evidence.

## Compiler checks

Executed `scripts/typecheck_examples.py` with Xcode selected at `/Applications/Xcode.app/Contents/Developer`, Apple Swift 6.4 and SDKs 27.0. All five SDK destinations passed with warnings treated as errors:

| Target | Example count | Result |
| --- | --- | --- |
| arm64 macOS 13.0 | 5 | Passed |
| arm64 iOS simulator 16.0 | 4 | Passed |
| arm64 watchOS simulator 9.0 | 4 | Passed |
| arm64 tvOS simulator 16.0 | 4 | Passed |
| arm64 visionOS simulator 1.0 | 4 | Passed |

The iOS SDK covers iPhone and iPad API typechecking; this is not separate device-layout validation. These are seven distinct examples and 21 example/target combinations. The first sandboxed compiler attempt could not launch the Swift macro plugin; rerunning with permitted compiler execution completed successfully. No code change was needed for that environment failure.

## Structural checks

Package validation checks local Markdown targets/headings, required package files, official HIG source registration, review-date validity, and evaluation-case structure. The bundled skill-creator validator separately checks the skill frontmatter and naming. Both validators passed on 2026-10-08. A temporary negative check confirmed that missing attribution files and broken local links are rejected. Skills CLI discovered exactly one skill from the local release directory using `npx skills add ./work/expanded --list`; no global installation was performed.

## Behavioral checks

The full 24-case suite and paired comparisons across Claude Code and Codex have not been run. A limited independent review-only smoke test completed four scenarios successfully; see the [prompts, raw responses, and scores](smoke-2026-10-08.md). It cannot establish comparative performance or implementation reliability.

## Not performed

No simulator app launches, device sessions, VoiceOver sessions, visual contrast measurements, keyboard/remote/Crown/headset interaction tests, or App Store compliance audit were performed. No pass rate is claimed for these categories. Specialized HIG topics outside the declared library still require official research.
