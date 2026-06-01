---
fetched_at: &id001 2026-06-01
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 64af1d1a2fd48283363f2a5857bf76ca426dd49457f9b6981636f637558547df
sources: []
title: How we contain Claude across products
topic: agentic-coding
url: https://www.anthropic.com/engineering/how-we-contain-claude
---

## Excerpts

> When building containment and defense systems, Anthropic applies defenses to the environment in which the agent runs, constraining where and how an agent can act with process sandboxes, VMs, filesystem boundaries, and egress controls. Telemetry showed users approved roughly 93% of permission prompts, and the more approvals a user sees, the less attention they pay to each, becoming over time much less diligent in their supervision. Between mid-2025 and January 2026, Anthropic received reports of vulnerabilities in Claude Code through their responsible disclosure program, with three exploiting code that executes before user consent. In February 2026, during a controlled internal red-team exercise, a researcher successfully phished an employee into launching Claude Code with a malicious prompt.