---
fetched_at: &id001 2026-09-16
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 6726c9df5fadbf36c281744662bdb98ca54c0d8577cf1fa26dc28f5f6cad9bfe
sources: []
title: Release v2.1.273 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
---

## Excerpts

> Added a notification when an MCP server disconnects mid-session and automatic reconnection gives up, pointing at /mcp

> Added forking a session started with claude --remote-control or /remote-control from the Claude app; the fork runs as a background session on your computer

> Added x-claude-code-request-class, x-claude-code-agent-type, x-claude-code-prev-tool-durations, x-claude-code-compaction and x-claude-code-context-compacted request headers for LLM gateways; opt in with CLAUDE_CODE_GATEWAY_HINT_HEADERS=1

> Fixed Bash commands the permission checker cannot fully analyze skipping the prompt under permissions.blockReadsOutsideWorkingDirectories, and a subshell hiding a dangerous rm in bypass mode

> Reverted a 2.1.268 change that checked Read and Edit deny rules on Bash lines the permission checker can't analyze (eval, env -C); commands like time -p make build prompt again instead of being denied

> Changed auto mode on Bedrock, Vertex and Foundry to use the local classifier by default for now; set CLAUDE_CODE_AUTO_MODE_SERVER=1 to use the platform's server-side classifier

> Fixed /login, /upgrade, and /extra-usage discarding earlier thinking from the conversation, which forced a full prompt-cache rewrite on the next request

> Fixed sub-agents and background agents being reported as failed, with their result never delivered, when the final streamed reply omitted token usage or carried no model id

> Fixed the context meter and auto-compact counting advisor-tool turns at roughly twice their real context size, which made auto-compact fire at about half the real window