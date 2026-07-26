---
fetched_at: &id001 2026-07-26
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: adf13fffe0254841d0498a6570f3fc845ba4dea0cbb201769cac3a2db98c4273
sources: []
title: 'IssueTrojanBench: Benchmarking AI Coding Agents Against Malicious Issue Requests'
topic: agentic-coding
url: https://arxiv.org/abs/2607.20759
---

## Excerpts

> IssueTrojanBench evaluate malicious issue requests against state-of-the-art coding agents (Cursor, Claude Code, and Codex Desktop), powered by OpenAI GPT-5.3 Codex/GPT-5.4 and Anthropic Sonnet 4.6.

> The novel benchmark IssueTrojanBench contains malicious issues that are constructed based on four novel attack categories (embedded as malicious instructions in issues), six delivery vectors (e.g., PDF, or issue comment), and further augmented by perturbations.

> The results reveal critical vulnerabilities in the as-deployed modern coding agents, with 66.5% of the malicious issues from IssueTrojanBench penetrating all the guardrails (agent- and LLM-level) of coding agents.

> Coding agents inherit security risks from both the LLM backbone, where adversarial prompts, poisoned training data, and backdoor triggers can cause models to emit insecure or attacker-chosen code, and their agentic architecture, where tool-using autonomy enables induced misuse of external APIs, data exfiltration, and persistent compromise of development environments.