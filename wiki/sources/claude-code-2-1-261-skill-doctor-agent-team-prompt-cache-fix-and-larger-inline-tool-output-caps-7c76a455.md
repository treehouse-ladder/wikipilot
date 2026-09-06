---
fetched_at: &id001 2026-09-06
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 7c76a455bae5923b1dddb820dc6cf58e1b1a0dc651173022fe29e3066a8948a2
sources: []
title: Claude Code 2.1.261 — /skill-doctor, agent-team prompt-cache fix, and larger
  inline tool-output caps
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.261
---

## Excerpts

> Added `/skill-doctor` to show which loaded skills go unused and what they cost in context, so you can prune them

> Fixed in-process agent-team teammates re-sending their first-turn tool and skill announcements on the second turn, which changed the request prefix and missed the prompt cache

> Added `bashOutputMaxChars` and `taskOutputMaxChars` settings to raise how much command and background-task output Claude receives inline before it is saved to a file, up to 128K characters

> Added `--append-subagent-system-prompt-file` to read the subagent system prompt from a file, for prompts too large to pass on the command line

> Fixed resuming a session losing hook output and other context around parallel tool calls, which changed the resumed request