---
fetched_at: &id001 2026-11-13
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 8427d4fee9a7d1b919f4589a4ce314f8fc01d9717ecee020b3eed38f0bbd7bd4
sources: []
title: Release v2.1.323 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.323
---

## Excerpts

> Added Code Mode, an experimental opt-in in which Claude writes JavaScript to call its tools; see https://code.claude.com/docs/en/code-mode to turn it on, or to turn it off for an organization

> Added `engines["claude-code"]` to `plugin.json`: plugins outside their stated Claude Code version range are not installed, updated or loaded, and install and update pick the newest version that fits

> Added support for `CLAUDE_CODE_AUTO_MODE_MODEL` in managed settings for Claude Desktop sessions on third-party providers (takes effect once Claude Desktop includes this version)

> Fixed `--permission-mode auto` or a settings `defaultMode: auto` starting in a mode that could allow more when auto mode was unavailable. It now starts in Manual mode, which asks first

> Fixed a case where the Write and Edit tools could write to a path covered by a `Read` deny rule

> Fixed `sandbox.excludedCommands` letting a command that it does not name run outside the sandbox in some cases

> Fixed `claude -p` and the Agent SDK running Bash unsandboxed when `--settings` or SDK settings that turn the sandbox on fail validation; Claude Code now stops at start-up and names the invalid setting

> Fixed a case where the Bash sandbox could switch off during a session

> Fixed sandboxed commands being able to read Claude Code's file checkpoint copies under the config directory

> Fixed a case where Bash permission checks judged an `rm` from the wrong folder and skipped the dangerous-removal prompt under bypass permissions or a Bash allow rule

> Fixed a case where some `lsof` commands ran without a permission prompt

> Fixed plan files sometimes being written outside the project when `plansDirectory` is set; a write that can't be shown to stay inside the project is now refused

> Fixed auto mode running behind a gateway at `ANTHROPIC_BASE_URL` on a model whose gateway name contains "haiku"; such a model, other than `claude-haiku-5-5`, is now refused, as Haiku 4.5 is

> Fixed Bash deny and ask rules missing some commands run through `sudo`, `env` and similar wrappers

> Fixed the Bash sandbox not fully protecting Claude Code's own config on installs still using the legacy config file