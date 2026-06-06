---
title: "MAI-Code-1-Flash"
kind: entity
aliases: ["MAI Code 1 Flash", "Microsoft MAI-Code-1-Flash"]
sources: ["[[building-a-hill-climbing-machine-launching-seven-new-mai-models-adf5b785]]", "[[mai-code-1-flash-61ec7468]]"]
last_updated: 2026-06-06
last_verified: 2026-06-06
freshness_window_days: 30
input_cost_per_mtoken: 0.75
output_cost_per_mtoken: 4.50
cost_source: "[[mai-code-1-flash-61ec7468]]"
swe_bench_verified: null
swe_bench_verified_source: null
---

# MAI-Code-1-Flash

## Summary

MAI-Code-1-Flash is Microsoft AI's first inference-efficient agentic coding model, announced at Build 2026 on June 2, 2026. It is a sparse MoE with ~5B active parameters, positioned as the Flash-tier coding companion to MAI-Thinking-1 in Microsoft's broader MAI model family [[building-a-hill-climbing-machine-launching-seven-new-mai-models-adf5b785]]. It features adaptive thinking — staying concise for simple requests and spending more reasoning budget on complex tasks [[mai-code-1-flash-61ec7468]].

> MAI-Code-1-Flash is a 5-billion-active-parameter agentic coding model designed for fast, efficient assistance in everyday developer workflows. It features adaptive thinking that stays concise for simple requests and spends more reasoning budget on complex tasks.

Headline benchmark: MAI-Code-1-Flash leads Claude Haiku 4.5 by 16 points on SWE-Bench Pro (51.2% vs 35.2%) and solves harder problems with up to 60% fewer tokens on SWE-Bench Verified [[mai-code-1-flash-61ec7468]].

> MAI-Code-1-Flash outperforms Claude Haiku 4.5 across all four core coding benchmarks tested, including a +16-point lead on SWE-Bench Pro (51.2% vs. 35.2%), and solves harder problems with up to 60% fewer tokens on SWE-Bench Verified.

Pricing: $0.75 input / $4.50 output per Mtoken, $0.075 cached input — undercutting Claude Haiku 4.5's tier while leading the relevant benchmarks [[mai-code-1-flash-61ec7468]].

## Disputes

- [[mai-code-1-flash-61ec7468]] frames the SWE-Bench Pro lead vs. Claude Haiku 4.5 (51.2% vs 35.2%) as the headline coding-quality win, but Microsoft does not publish a head-to-head against current Flash-tier competitors (Gemini 3.5 Flash, GPT-5.5-mini) on SWE-Bench Pro; the Haiku 4.5 comparison was chosen as the price-point peer. Status: unresolved — leadership against Haiku 4.5 is verified but the broader Flash-tier ranking is not.

## Open questions

- [ ] What is MAI-Code-1-Flash's SWE-Bench Verified absolute pass-rate (not just the 60%-fewer-tokens efficiency claim)?
- [ ] Does MAI-Code-1-Flash sit on the Artificial Analysis Intelligence Index, and where vs. the Flash-tier competition?
- [ ] When does MAI-Code-1-Flash become available outside GitHub Copilot — through Foundry, Azure OpenAI, or third-party providers?

## See also

- [[mai-thinking-1]]
- [[frontier-models]]
