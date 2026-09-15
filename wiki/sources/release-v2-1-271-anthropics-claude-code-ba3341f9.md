---
fetched_at: &id001 2026-09-15
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: ba3341f9799b1e8e27294e996daf4b97a09cdf3b6d8c7bc967a7ee1764115a34
sources: []
title: Release v2.1.271 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
---

## Excerpts

> Bash, PowerShell and Monitor commands running in auto mode with sandboxing can now declare the hosts they need, and those hosts are reviewed together with the command and opened for that command alone. The domain list sits on the command rather than on the session, so approving one curl does not widen the network for the next one.

> Added omitClaudeMd to agent frontmatter and --agents JSON, letting custom and plugin subagents run without user, project and local CLAUDE.md files; managed policy files still load.

> Added fast mode in Claude Code Remote sessions (cloud and self-hosted runners): the host's fast-mode setting or /fast typed in the session applies where your organization allows it.

> Added claude self-hosted-runner --drain-marker-file <path>: when that file exists at a SIGTERM drain, the runner reports its exit to the server as a host drain.