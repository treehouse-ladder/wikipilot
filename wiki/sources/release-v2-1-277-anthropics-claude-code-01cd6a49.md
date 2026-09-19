---
fetched_at: &id001 2026-09-19
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 01cd6a498d377caff37af8c0f2707493e6c5d125586b96b61db75872400d7aba
sources: []
title: Release v2.1.277 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
---

## Excerpts

> Added AGENTS.md support: in a project with no CLAUDE.md, Claude Code reads AGENTS.md instead; change it under "Project instructions" in /config (not yet on Bedrock, Vertex or Foundry)

> Fixed sessions continued after /clear (restart, --continue, --resume) missing part of their first message when a SessionStart hook printed output, causing a full prompt-cache miss

> Fixed resumed subagents and teammates re-rendering the MCP tool definitions they had loaded, which broke prompt caching for that agent

> Fixed attachments recorded earlier in a conversation being re-rendered after a resume or relaunch, which dropped extended thinking and missed the prompt cache

> Fixed a sandbox.excludedCommands glob exempting an entire compound Bash command from the sandbox when only one part matched; every part must now match

> Fixed project skills from the main repository not loading in --worktree sessions when .claude/skills is untracked

> Added CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1 for Claude apps gateways whose only egress is a forward proxy: every outbound request hands the proxy the hostname instead of resolving it locally