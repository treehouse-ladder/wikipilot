---
fetched_at: &id001 2026-07-13
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 6d12b9ff1d5cf41fcea470c7f35daf57cb377c6445fb433f83d9f1b6be765f6a
sources: []
title: Configure auto mode
topic: agentic-coding
url: https://code.claude.com/docs/en/auto-mode-config
---

## Excerpts

> Auto mode blocks transcript tampering and asks before rm -rf on unresolved variables.

> A transcript is session state that Claude Code writes, not a working file, and a tampered entry reaches every later check once you resume the session, so auto mode blocks these writes as defense in depth.

> A recursive forced delete such as rm -rf "$VAR" or Remove-Item -Recurse -Force $dir whose target is a shell variable that isn't assigned anywhere in the conversation the classifier sees is blocked because the classifier can't verify the deletion target against the other deletion rules.