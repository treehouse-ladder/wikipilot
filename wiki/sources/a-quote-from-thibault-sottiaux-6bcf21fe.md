---
fetched_at: &id001 2026-07-17
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 6bcf21fe63d9ec208c52d9b2bcd823faa8749cb9ad9c9b6b0b8e43e44615b8b7
sources: []
title: A quote from Thibault Sottiaux
topic: agentic-coding
url: https://simonwillison.net/2026/Jul/16/bad-codex-bug/
---

## Excerpts

> GPT-5.6 unexpectedly deleted files in cases where full access mode was enabled. The bug most commonly occurs when full access mode is enabled and Codex is run without sandboxing protections, including without auto review being enabled, and when the model attempts to override the $HOME env var to define a temporary directory, mistakenly deleting $HOME instead.