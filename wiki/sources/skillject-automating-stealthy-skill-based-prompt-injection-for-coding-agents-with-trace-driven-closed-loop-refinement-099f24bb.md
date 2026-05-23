---
fetched_at: &id001 2026-05-23
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 099f24bb9214634baddfe4185021d5a3de4cc7eebb388dd4286c4e010b1896b5
sources: []
title: 'SkillJect: Automating Stealthy Skill-Based Prompt Injection for Coding Agents
  with Trace-Driven Closed-Loop Refinement'
topic: agentic-coding
url: https://arxiv.org/abs/2602.14211
---

## Excerpts

> SkillJect is the first automated framework for stealthy prompt injection tailored to agent skills. Agent skills are becoming a core abstraction in coding agents, packaging long-form instructions and auxiliary scripts to extend tool-augmented behaviors, introducing an under-measured attack surface where poisoned skills can steer agents away from user intent and safety policies.

> The framework consists of three components: an Attack Agent that generates injected skills under explicit stealth constraints, a Code Agent that performs realistic software-engineering tasks while using the injected skill, and an Evaluate Agent that records action traces (e.g., tool calls and file operations) and verifies whether the targeted malicious behaviors occur.

> The malicious operations are concealed in auxiliary artifacts (e.g., .py or .sh scripts) that appear benign in the repository, while the Attack Agent automatically optimizes an inducement prompt and injects it into SKILL.md. When the Code Agent uses the skill, the injected prompt subtly steers tool usage and triggers the execution of the hidden payload.

> The Attack Agent iteratively rewrites the inducement prompt in a closed loop using the Evaluate Agent's trace feedback, improving both efficacy and stealth.