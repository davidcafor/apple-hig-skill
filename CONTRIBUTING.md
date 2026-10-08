# Contributing

Thank you for helping make Apple HIG Skill more useful.

## Propose a change

Open an issue for a missing topic, ambiguous rule, outdated source, or unexpected agent behavior. Describe the platform, supported OS version, task, current result, and intended improvement. Never include private code or credentials.

For larger changes, discuss the scope in an issue before investing in implementation. Small corrections can go directly to a pull request.

## Submit a pull request

- Keep the change focused and write your own explanations and examples.
- Link the exact official Apple source that supports a design claim.
- Distinguish explicit Apple guidance, recommendations, and your implementation interpretation.
- State applicable platforms, version limits, exceptions, and the date you checked the source.
- Explain what you tested. Do not claim device validation from code inspection alone.
- Include a realistic positive and negative example when introducing a new review rule.
- Keep the skill concise; load detailed references only when relevant.

Do not copy another skill's instructions or redistribute Apple design assets or documentation. Quote sparingly with attribution where appropriate.

## Validate the change

Run `python3 scripts/validate.py`. When changing Swift examples, also run `scripts/typecheck_examples.py` with full Xcode selected through `DEVELOPER_DIR`. Record unavailable SDKs rather than silently skipping them.

Update `apple-hig-skill/references/sources.json` when substantively checking a source. Keep review scope honest. Add a focused case to `evals/cases.json` for a new behavior or observed regression, including a valid design that should not be flagged where relevant. Follow `evals/README.md` before reporting behavioral results.

Keep README text, instructions, examples, and repository documentation in English. Reports and discussions may use the contributor's preferred language.

## Review and credit

The maintainer reviews pull requests before merging. A proposal is welcome even if its implementation is not accepted. Be specific, constructive, and respectful; discuss the work rather than the person.

Contributors retain rights in their contributions. By submitting material for inclusion, you agree to license your contribution under this repository's CC BY 4.0 license and confirm that you have the right to do so. You do not transfer ownership to the maintainer.

Git history and GitHub's contributor listing credit accepted contributions. Preserve existing authorship and attribution notices when adapting material.
