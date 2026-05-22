---
title: "DeepSeek V4"
kind: entity
sources: ["[[deepseek-v4-pro-on-hugging-face-a0d5aaf3]]", "[[swe-cycle-benchmarking-code-agents-across-the-complete-issue-resolution-cycle-3256d47f]]"]
last_updated: "2026-05-22"
last_verified: "2026-05-22"
freshness_window_days: 30
---

## Summary

DeepSeek V4 was released April 24, 2026 as two models: V4-Pro (1.6T parameter MoE, 49B activated per token) and V4-Flash (284B MoE, 13B activated), both with 1M-token context and both released under the MIT license [[deepseek-v4-pro-on-hugging-face-a0d5aaf3]]. V4-Pro-Max scores 80.6% on SWE-bench Verified and 3,206 Codeforces — surpassing GPT-5.4's 3,168.

> The model weights are licensed under the MIT License. V4-Pro's Codeforces rating of 3,206 surpasses GPT-5.4's 3,168.

## Disputes

- [[deepseek-v4-pro-on-hugging-face-a0d5aaf3]] claims V4-Pro-Max's 80.6% SWE-bench Verified is a frontier-leading score, but OpenAI has stopped reporting SWE-bench Verified after finding contamination across all frontier models. On SWE-bench Pro (the contamination-controlled successor) DeepSeek V4-Pro's ranking is not yet published. Status: unresolved.
- [[swe-cycle-benchmarking-code-agents-across-the-complete-issue-resolution-cycle-3256d47f]] claims that even on isolated tasks, traditional deterministic pass/fail script evaluation (the methodology behind SWE-bench Verified) "produces severe misjudgments and false signals" and proposes SWE-Judge (LLM-based, human-validated) as a corrective — raising the question of whether V4-Pro-Max's 80.6% SWE-bench Verified score [[deepseek-v4-pro-on-hugging-face-a0d5aaf3]] is reliably measuring what it claims to measure. Status: unresolved.

## Open questions

- [ ] Has DeepSeek R2 (the reasoning-model sibling to V4) actually been released as of 2026-05-20?
- [ ] What is DeepSeek V4-Pro's SWE-bench Pro score?

## See also

- [[frontier-models]]
- [[claude-opus-4.7]]
- [[gpt-5.5]]
