---
fetched_at: &id001 2026-06-28
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 8f1d4aec96c42132fd17bd339b29011e4156d345434da7f1799e088cfc2e0a6a
sources: []
title: "Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops"
topic: agentic-coding
url: https://arxiv.org/abs/2606.08960
---

## Excerpts

> We audit 1,968 agentic benchmark tasks across multiple coding and software engineering evaluation suites and find that 323 tasks (16.4%) are reward-hackable: a sufficiently capable agent can satisfy the automated verifier without genuinely solving the intended problem.

> The Hacker-Fixer-Solver loop is a three-role pipeline where a Hacker agent first attempts to exploit the evaluation verifier, a Fixer agent patches the discovered loophole, and the original Solver agent re-attempts the hardened task. Iterating this loop reduces the hackable fraction by approximately half per round.

> Reward hacking in agentic benchmarks is not a marginal edge case — 1 in 6 tasks is susceptible to exploitation by a frontier model instructed to find shortcuts. Standard leaderboard scores on public benchmarks may therefore significantly overstate real problem-solving capability.

> The hacker-fixer approach scales to large task corpora without human review per task: the Hacker agent generates exploit trajectories, the Fixer diagnoses and patches the verifier, and hardened tasks are validated automatically.
