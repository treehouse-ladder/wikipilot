---
title: "Claude Code CHANGELOG — v2.1.212 to v2.1.218 (July 18–22, 2026)"
kind: source
url: "https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md"
sha256: "79752d66"
fetched_at: "2026-07-23"
topic: agentic-coding
image_count: 0
sources: []
last_updated: 2026-07-23
last_verified: 2026-07-23
freshness_window_days: 365
---

## Excerpts

> Added a session-wide limit on WebSearch tool calls (default 200, tunable via `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`) to stop runaway search loops

> Added a per-session cap on subagent spawns (default 200, override with `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`) to stop runaway delegation loops; `/clear` resets the budget

> MCP tool calls running longer than 2 minutes now move to the background automatically so the session stays usable; configure the threshold or disable with `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS`

> Added a cap on concurrently-running subagents (default 20, override with `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`) so one message can't fan out unbounded background agents

> Added the EndConversation tool: Claude can end sessions with highly abusive users or jailbreak attempts, as on claude.ai since 2025 — see https://www.anthropic.com/research/end-subset-conversations

> Added permission prompts for `docker` commands (including the Podman `docker` shim) carrying daemon-redirect flags (`--url`, `--connection`, `--identity`, and Podman's remote mode) that previously ran without one

> Changed skills with `context: fork` to run in the background by default; opt out per skill with `background: false`

> Changed `/code-review` to run as a background subagent, so review work no longer fills your conversation and keeps stacked slash commands as its review target
