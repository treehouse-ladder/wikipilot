---
title: "Release v2.1.283 · anthropics/claude-code"
kind: source
url: "https://github.com/anthropics/claude-code/releases/tag/v2.1.283"
sha256: "35ab415a"
fetched_at: "2026-09-26"
topic: "agentic-coding"
image_count: 0
sources: []
last_updated: 2026-09-26
last_verified: 2026-09-26
freshness_window_days: 365
---

# Release v2.1.283 · anthropics/claude-code

## Excerpts

> Added `availableModelsMatch` managed setting: with "exact", an `availableModels` entry allows only the model version it names, so new releases stay blocked until listed

> Added `deniedModels` managed setting to block specific models, even when `availableModels` allows them

> Added `/doctor prompt-audit` (also `/checkup prompt-audit`) to audit your CLAUDE.md files, skills, agents and commands for prompting patterns written for older models

> Added MCP tool, WebFetch and WebSearch outputs to the `tool.output` OpenTelemetry span event when `OTEL_LOG_TOOL_CONTENT=1`

> Fixed dynamic workflows started during a model fallback running every agent on the fallback model instead of retrying the configured model

> Windows: Fixed the PowerShell tool letting `cmd /c rd`, `rmdir`, `del` or `erase` delete drive roots, the home folder and other folders that `Remove-Item` refuses

> Fixed managed `sandbox` settings being ignored entirely when one nested value was invalid; the invalid value now fails closed and the rest of the block still applies

> Fixed `DISABLE_PROMPT_CACHING_HAIKU` having no effect when Haiku is the session's main model

> Fixed `/context` not counting MCP server instructions: they now appear as their own row and count toward the total

> Fixed a brief HTTP 404 from a stateless remote MCP server (for example a proxy mid-redeploy) leaving that server unusable for the rest of the session while still shown as connected

_no contradictions or gaps known yet (last reviewed: 2026-09-26)_
