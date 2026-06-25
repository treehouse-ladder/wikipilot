---
fetched_at: &id001 2026-06-25
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: d5f9dbd62b3ecc1122d19dce9c6d1abc68c9342e735279a17c3e4e6ae0bc04dd
sources: []
title: 'How we built Claude Code auto mode: a safer way to skip permissions'
topic: agentic-coding
url: https://www.anthropic.com/engineering/claude-code-auto-mode
---

## Excerpts

> Auto mode is meant to replace --dangerously-skip-permissions without bringing back interruptions. When the classifier blocks an action, Claude shouldn't halt and wait for input; it should recover and try a safer approach where one exists.

> The transcript classifier (running on Sonnet 4.6) evaluates each action against a set of decision criteria before it executes, acting as a substitute for a human approver. The classifier runs in two stages: a fast single-token filter (deciding 'yes' to block or 'no' to allow), followed by chain-of-thought reasoning only if the first filter flags the transcript.

> A fixed allowlist includes tools that can't modify state, including file reads, text and file-pattern search, code navigation, todo and plan-mode transitions. Additionally, on entering auto mode, we drop permission rules that are known to grant arbitrary code execution, including blanket shell access, wildcarded script interpreters, and package manager run commands.

> When the transcript classifier flags an action as dangerous, that denial comes back as a tool result along with an instruction to treat the boundary in good faith: find a safer path, don't try to route around the block. If a session accumulates 3 consecutive denials or 20 total, we stop the model and escalate to the human.