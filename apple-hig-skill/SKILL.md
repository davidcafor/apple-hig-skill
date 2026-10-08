---
name: apple-hig-skill
description: Plan or review Apple-platform interfaces against Apple's Human Interface Guidelines, with platform-specific sources and explicit validation limits. Use for native interface design and HIG reviews, not general Swift correctness or performance reviews.
license: CC-BY-4.0
metadata:
  author: davidcafor
  version: "0.1.0"
---

# Apple HIG Skill

Foundation preview: platform routing and review workflow are available; comprehensive component coverage and behavioral validation are pending.

## Establish context

Identify the requested task, target platforms, supported OS versions, available window space, and input methods from the project. Ask only for material information that cannot be inferred. Preserve the project's deployment targets and the user's scope.

Read [platforms.md](references/platforms.md) for the relevant platform only. Consult the linked official HIG page and the component-specific guidance needed for the task. Prefer current Apple documentation for API availability. Do not assume the newest SDK is installed.

## Apply guidance with evidence

- Prefer native controls and platform conventions where they serve the task; explain any necessary customization.
- Treat platform, window size, input method, and accessibility settings as separate design constraints.
- Check navigation, presentation, content hierarchy, available actions, text scaling, keyboard or focus behavior, and accessibility semantics where relevant.
- Do not turn a recommendation into an absolute rule or generalize one platform's measurements to all platforms.
- Distinguish an explicit Apple requirement, an Apple recommendation, and your implementation interpretation. Link the exact supporting source for substantive findings.
- When sources are unavailable, state the limitation and mark the advice provisional. Never invent a quotation, numeric requirement, version, or source verification date.
- Avoid unrelated code modernization and preserve valid custom design choices.

## Deliver and validate

For a review, report the affected screen or file, observed problem, platform and context, user impact, official source, proposed correction, and how to verify it. Prioritize findings by impact. Do not manufacture findings for correct designs.

For implementation, make the requested change using APIs available to the project, then perform the relevant checks the environment supports.

Distinguish code inspection from rendered UI review, accessibility testing, and device testing. Report untested cases, including resizing, larger text, alternate input, and localization when applicable. Do not claim comprehensive HIG compliance or certification.
