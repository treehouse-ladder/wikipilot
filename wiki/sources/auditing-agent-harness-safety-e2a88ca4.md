---
fetched_at: &id001 2026-06-07
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: e2a88ca46e6c693f77ad4a3fcc456ffcb957c738609aa9930bee7e656d018c98
sources: []
title: Auditing Agent Harness Safety
topic: agentic-coding
url: https://arxiv.org/abs/2605.14271
---

## Excerpts

> LLM agents increasingly run inside execution harnesses that dispatch tools, allocate resources, and route messages between specialized components. A harness can return a correct, benign answer over a trajectory that accesses unauthorized resources or leaks context to the wrong agent. Output-level evaluation cannot see these failures, yet most safety benchmarks score only final outputs or terminal states, even though many violations occur mid-trajectory rather than at termination.

> We propose HarnessAudit, a framework that audits full execution trajectories across boundary compliance, execution fidelity, and system stability, with a focus on multi-agent harnesses where these risks are most pronounced.

> HarnessAudit and HarnessAudit-Bench systematically evaluate agent harnesses along boundary compliance, execution fidelity, and perturbation stability, with hidden audit channels that independently record tool use, resource access, and inter-component interactions. Results show a persistent gap between task capability and safe execution, with resource access and inter-component information flow emerging as the most critical surfaces to harden.