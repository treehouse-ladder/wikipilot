---
fetched_at: &id001 2026-07-22
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 0a54e1626f1f9828a86ffb5ad7b905a03c6e7fe681b4590543ed500db1315dbb
sources: []
title: Claude Code — What's new, Week 29 (July 13–17, 2026)
topic: agentic-coding
url: https://code.claude.com/docs/en/whats-new/2026-w29
---

## Excerpts

> /fork now copies your conversation into a new background session (its own row in claude agents) while you keep working. The copy starts with everything in the conversation up to that point, plus the working directory, model, permission mode, effort level, and any directories or "don't ask again" permission grants you added during the session. The in-session forked subagent it used to launch is now /subtask.

> A forked subagent, started with /subtask, is a subagent that inherits your full conversation context instead of starting fresh. /subtask requires Claude Code v2.1.212 or later.

> Auto mode no longer needs the CLAUDE_CODE_ENABLE_AUTO_MODE opt-in on Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry; administrators can turn it off with disableAutoMode.

> MCP tool calls that run longer than two minutes now move to the background automatically so the session stays usable, with the threshold configurable via CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS.