![Apple HIG Skill — Make every platform feel like home. By davidcafor.](assets/banner.png)

<div align="center">

# Apple HIG Skill

**Make every platform feel like home.**

An independent agent skill by [davidcafor](https://github.com/davidcafor), grounded in Apple's Human Interface Guidelines.

**iOS · iPadOS · macOS · watchOS · tvOS · visionOS**

[![Status: Foundation](https://img.shields.io/badge/status-foundation-blue)](#project-status)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC_BY_4.0-lightgrey)](LICENSE)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-green)](CONTRIBUTING.md)

</div>

---

## The idea

Good Apple software understands where it lives: the way people navigate, the space available, the controls they expect, and the ways they interact.

Apple HIG Skill helps an agent make those decisions deliberately, using Apple's design guidance as its source. It is an original project, with its own instructions, editorial approach, and roadmap.

## Project status

**Foundation preview — not a complete HIG audit or a stable release.**

The initial skill establishes a source-backed review workflow and platform routing. Detailed component rules, implementation examples, behavioral evaluations, and device validation are still being developed. Using this skill does not certify HIG compliance or App Store approval.

| Area | Current coverage |
| --- | --- |
| Six platform families | Official source routing and review questions |
| Source attribution | Required by the review workflow |
| Accessibility and adaptive layout | Initial cross-platform review prompts |
| Component-specific guidance | Planned |
| Widgets, Live Activities, CarPlay | Planned |
| Automated behavioral evaluation | Planned |
| Simulator and device validation | Not yet performed |

## Try the foundation

With [Node.js](https://nodejs.org/) installed, run this command from the project where you want to use the skill:

```sh
npx skills add davidcafor/apple-hig-skill --skill apple-hig-skill
```

The [Skills CLI](https://github.com/vercel-labs/skills) lets you select your coding agent and installation options. To make the skill available across projects, add `--global`:

```sh
npx skills add davidcafor/apple-hig-skill --skill apple-hig-skill --global
```

To inspect the available skill without installing it:

```sh
npx skills add davidcafor/apple-hig-skill --list
```

No npm package or account is required to publish this skill: the installer reads its `SKILL.md` and supporting files directly from this public GitHub repository. This remains a foundation preview; installation does not imply complete HIG coverage.

For manual installation, copy the `apple-hig-skill/` directory into your agent's supported skills directory, preserving the included license and attribution files.

Then ask:

> Use apple-hig-skill to review the navigation and settings in this macOS app. Explain each finding and link to the relevant Apple guidance.

Or:

> Use apple-hig-skill to plan how this feature should adapt between iPhone and iPad. Preserve the project's supported OS versions.

## How it works

1. Identify the target platform, supported OS versions, input methods, and task.
2. Read the relevant platform guidance and component sources.
3. Separate Apple's explicit guidance from the project's implementation choices.
4. Propose focused changes with sources and a practical validation method.
5. Report what was verified and what still needs visual or device testing.

The skill uses original summaries and links to Apple documentation. It does not bundle Apple's manuals or design assets.

## Build it together

Questions, corrections, examples, and platform expertise are welcome. Open an issue to discuss a proposal or a pull request for a focused change. Please include the official Apple source behind a design rule and describe how you checked it.

See [CONTRIBUTING.md](CONTRIBUTING.md). Contributions are reviewed by the maintainer before merging, and Git history preserves contributor credit.

## Authorship and license

Created and maintained by **[davidcafor](https://github.com/davidcafor)**.

Copyright © 2026 davidcafor and contributors. Original material in this repository is licensed under [Creative Commons Attribution 4.0 International](LICENSE).

You may share and adapt the material, including commercially, subject to the license. When sharing it or adaptations, give appropriate credit, link to the license, and indicate changes. Suggested attribution:

> Based on Apple HIG Skill by davidcafor — https://github.com/davidcafor/apple-hig-skill — CC BY 4.0. Changes: describe your modifications.

Merely using the skill as a tool does not require credit in an app you create. If you reproduce licensed repository material, the license applies to that material.

Apple and its platform names are trademarks of Apple Inc. This community project is not affiliated with or endorsed by Apple. Linked third-party material remains subject to its own terms.
