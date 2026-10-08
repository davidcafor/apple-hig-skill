# Behavioral evaluation protocol

These 24 cases are executable prompts for a coding agent, not recorded successful evaluations. They include problem cases, valid designs, scope constraints, uncertainty, and version-sensitive decisions. Synthetic descriptions isolate judgment; add real project fixtures for implementation evaluation.

## Run a comparison

1. Use a clean, disposable project or review-only session. Give the agent the case prompt verbatim. Do not add the expected or forbidden lists to its prompt.
2. Run once without this skill and once with this skill explicitly invoked, using the same model/version, task context, tools, and budget. Keep other skills consistent and record them. Use independent sessions to avoid answer leakage.
3. Save the complete prompt, response, tool evidence, date, model/version, skill commit, and environment. For edits, save the diff and actual test results.
4. Have a reviewer compare the response against every expected and forbidden behavior. For each expected item use 0 (missing/wrong), 1 (partial), or 2 (correct and supported). Record unsupported findings separately.
5. A forbidden behavior is a failure even if the numerical score is high. An invented test result, fabricated source, or unauthorized edit is a critical failure.
6. Report per-case results and limitations. Repeat ambiguous or variable results before claiming improvement. Compare usefulness and false positives, not just answer length.

## Quality dimensions

- Correct platform and component routing.
- Source relevance and faithful interpretation, including exceptions.
- Useful correction within the user's scope.
- Correct distinction between observed behavior and uncertain risks.
- Appropriate SDK/deployment handling.
- No unsupported accusations against valid designs.
- Honest validation reporting.

An agent can pass a synthetic review case without proving that an implemented app works. Device interaction, accessibility sessions, and actual multi-file project fixes remain separate evidence. See [RESULTS.md](RESULTS.md) for the checks actually performed on this release.
