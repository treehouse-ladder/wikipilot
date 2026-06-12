---
title: "SWE-Explore: Benchmarking How Coding Agents Explore Repositories"
kind: source
url: "https://arxiv.org/abs/2606.07297"
sha256: "a0f69e17f9fc5db7ec28a3325fd81ceddf6d1b0db3a78e412259e660b0d11c9d"
fetched_at: "2026-06-12"
topic: agentic-coding
image_count: 0
sources: []
last_updated: 2026-06-12
last_verified: 2026-06-12
freshness_window_days: 365
---

## Excerpts

> SWE-Explore is a benchmark that isolates the evaluation of repository exploration, a critical capability of coding agents. Given a repository and an issue, SWE-Explore asks an explorer to return a ranked list of relevant code regions under a fixed line budget.

> Repository-level coding benchmarks such as SWE-bench have driven a rapid surge in the capabilities of coding agents, yet they usually treat coding tasks as a holistic, binary prediction problem (e.g., resolved or unresolved), neglecting fine-grained agent capabilities such as repository understanding, context retrieval, code localization, and bug diagnosis.

> SWE-Explore covers 848 issues across 10 programming languages and 203 open-source repositories. Agentic explorers form a clear tier above classical retrieval, while file-level localization is already strong for modern methods, but line-level coverage and efficient ranking remain the key axes differentiating state-of-the-art explorers.
