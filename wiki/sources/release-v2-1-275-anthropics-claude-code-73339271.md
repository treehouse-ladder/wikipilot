---
fetched_at: &id001 2026-09-18
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 733392711551a1c39fa410a1926200f07e98490722f4e9c61600a32969f384dd
sources: []
title: Release v2.1.275 · anthropics/claude-code
topic: agentic-coding
url: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
---

## Excerpts

> Added syncing of the skills and plugins enabled on your claude.ai account to terminal sessions signed in with it; opt out with syncClaudeAiSkills: false or syncClaudeAiPlugins: false.

> Improved responsiveness in long sessions: hook progress and sub-agent activity no longer re-process the whole conversation on every update.

> Fixed a restored memory file's age note changing between requests after a compaction or resume, which caused prompt cache misses.

> Plugin and marketplace outputs strip secrets from git/ssh/marketplace URLs to prevent credential leaks.

> Added /plugin install <plugin> --marketplace <source>, which offers to add the marketplace before installing the plugin.