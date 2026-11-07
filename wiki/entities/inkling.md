---
title: "Inkling"
kind: entity
aliases: ["Thinking Machines Inkling", "Inkling MoE"]
sources: ["[[thinking-machines-has-released-inkling-the-new-leading-u-s-open-weights-model-4ae0655f]]", "[[inkling-our-open-weights-model-06531d4a]]", "[[introducing-inkling-small-5c51c45f]]", "[[inkling-small-lands-within-a-point-of-inkling-on-the-artificial-analysis-intelligence-index-with-less-than-a-third-of-the-parameters-805cabb6]]", "[[thinking-machines-inkling-2-small-the-highest-scoring-open-weights-model-outside-of-china-pending-weights-release-b70ccc60]]", "[[introducing-inkling-2-small-187bb7cb]]"]
last_updated: 2026-11-07
last_verified: 2026-07-31
freshness_window_days: 30
aa_intelligence_index: 41
aa_intelligence_index_source: "[[thinking-machines-has-released-inkling-the-new-leading-u-s-open-weights-model-4ae0655f]]"
input_cost_per_mtoken: null
output_cost_per_mtoken: null
cost_source: null
swe_bench_verified: null
swe_bench_verified_source: null
cybergym: null
cybergym_source: null
arc_agi_2: null
arc_agi_2_source: null
---

# Inkling

## Summary

Inkling is Thinking Machines Lab's first open-weights model, released July 15, 2026, positioned as the new leading US/non-Chinese open-weights model at **AA Intelligence Index v4.1 = 41** — 3 points above the prior US leader NVIDIA Nemotron 3 Ultra (38) and well ahead of Gemma 4 31B (29) and gpt-oss-120b (24) [[thinking-machines-has-released-inkling-the-new-leading-u-s-open-weights-model-4ae0655f]]. It is a natively-multimodal mixture-of-experts system with **975B total parameters** drawing on about **41B active parameters** for any given task, trained on **45 trillion tokens** of text, image, audio, and video [[inkling-our-open-weights-model-06531d4a]]. Inkling supports a **1M-token context window** (256K via the Tinker API) [[inkling-our-open-weights-model-06531d4a]]. Full weights are available on Hugging Face, including an NVFP4 checkpoint for NVIDIA Blackwell systems [[inkling-our-open-weights-model-06531d4a]].

Its most agentic-workflow-relevant property is **token efficiency**: Inkling averages **~25K output tokens per Intelligence-Index task**, compared to 43K, 38K and 37K by GLM-5.2 (max), Kimi K2.6 and DeepSeek v4 Pro (max) respectively — a real per-task cost advantage on output-dominated agentic loops where verbose open-weights leaders bleed budget [[thinking-machines-has-released-inkling-the-new-leading-u-s-open-weights-model-4ae0655f]].

Thinking Machines explicitly positions Inkling as a customization base rather than a leaderboard contender, stating "Inkling is not the strongest overall model available today, open or closed" [[inkling-our-open-weights-model-06531d4a]]. The company also ships **Inkling-Small** (12B active parameters) as a preview for lower-cost fine-tuning via Tinker, its model-customization platform [[inkling-our-open-weights-model-06531d4a]].

> Thinking Machines has released Inkling, the new leading U.S. open weights model, debuting at 41 on the Artificial Analysis Intelligence Index. Inkling scores 3 points higher on the Intelligence Index (41) than the previous leading U.S. open weights model, Nemotron 3 Ultra (38), and also beats Gemma 4 31B (29) and gpt-oss-120b (24). [[thinking-machines-has-released-inkling-the-new-leading-u-s-open-weights-model-4ae0655f]]

> Inkling is token efficient compared to open weights leaders, averaging 25K output tokens per Intelligence Index task compared to 43K, 38K and 37K by GLM-5.2 (max), Kimi K2.6 and DeepSeek v4 Pro (max) respectively. [[thinking-machines-has-released-inkling-the-new-leading-u-s-open-weights-model-4ae0655f]]

> Inkling is a mixture-of-experts system with 975 billion total parameters, drawing on about 41 billion active parameters for any given task. It was trained on 45 trillion tokens of text, image, audio, and video, and reasons natively across all four. Inkling supports a context window of up to 1M tokens. [[inkling-our-open-weights-model-06531d4a]]

> Full weights for Inkling are available on Hugging Face, including an NVFP4 checkpoint for NVIDIA Blackwell systems. [[inkling-our-open-weights-model-06531d4a]]

> Inkling is not the strongest overall model available today, open or closed. [[inkling-our-open-weights-model-06531d4a]]

Thinking Machines fully released **Inkling-Small** on July 31, 2026 (previously shipped as a Tinker preview): a **276B-total / 12B-active** multimodal Mixture-of-Experts reasoning model with controllable reasoning effort, released under an **Apache 2.0** license with weights on Hugging Face [[introducing-inkling-small-5c51c45f]]. Thinking Machines positions it as "matching Inkling at a quarter of the size," with native reasoning over audio and images and a context window of up to 1M tokens [[introducing-inkling-small-5c51c45f]]. Artificial Analysis independently places Inkling-Small at **AA Intelligence Index v4.1 = 40** — one point behind the 975B Inkling (41) at less than a third of the total and active parameters — and notes **no open-weights model at its size or smaller scores higher** on the Intelligence Index; it ties Inkling on Terminal-Bench 2.1 (55%) and edges it on Humanity's Last Exam (32% vs 30%), GPQA Diamond (89% vs 87%), CritPt (8% vs 5%) and SciCode (49% vs 46%) while being more token-efficient per task [[inkling-small-lands-within-a-point-of-inkling-on-the-artificial-analysis-intelligence-index-with-less-than-a-third-of-the-parameters-805cabb6]]. This makes Inkling-Small a compact, cheaply self-hostable, permissively-licensed open-weights option for cost-sensitive agentic and game-dev tooling loops.

> Inkling Small scores 40 on the Artificial Analysis Intelligence Index, within a point of its flagship sibling Inkling with less than a third of the total and active parameters. No open weights model at its size or smaller scores higher on the Intelligence Index. [[inkling-small-lands-within-a-point-of-inkling-on-the-artificial-analysis-intelligence-index-with-less-than-a-third-of-the-parameters-805cabb6]]

> Inkling-Small is a multimodal, Mixture-of-Experts model with controllable reasoning effort that matches Inkling at a quarter of the size. [[introducing-inkling-small-5c51c45f]]

Thinking Machines previewed **Inkling 2 Small** on 2026-11-07 (closed-weights for now, Apache 2.0 release pending): it scores **31 on AA Intelligence Index v5.0.1** (+18 over Inkling Small, ~4x output tokens/task), matching Gemini 3.8 Flash (high) and surpassing MiMo-V2.6-Pro, at $1.18/task [[thinking-machines-inkling-2-small-the-highest-scoring-open-weights-model-outside-of-china-pending-weights-release-b70ccc60]]. Artificial Analysis frames it as the model that, upon weights release, would be the highest-scoring open-weights model developed **outside China** [[thinking-machines-inkling-2-small-the-highest-scoring-open-weights-model-outside-of-china-pending-weights-release-b70ccc60]]. Thinking Machines launched it as closed-weights on Tinker and intends to publish full weights under Apache 2.0 "next week" after external safety testing and red-teaming [[introducing-inkling-2-small-187bb7cb]].

> Inkling 2 Small scores 31 on the Artificial Analysis Intelligence Index v5.0.1, up 18 points from Inkling Small, with roughly 4x as many output tokens per task. It matches Gemini 3.8 Flash (high) and surpasses MiMo-V2.6-Pro. Once the weights are released, the model would be the highest-scoring open weights model developed outside China based on current rankings. [[thinking-machines-inkling-2-small-the-highest-scoring-open-weights-model-outside-of-china-pending-weights-release-b70ccc60]]

> Thinking Machines intends to make the full weights of Inkling 2 Small available under an Apache 2.0 license next week, after the completion of external safety testing and red-teaming; it is launched as a closed-weight model on the Tinker platform. [[introducing-inkling-2-small-187bb7cb]]

## Disputes

_none yet_

## Open questions

- [ ] No independent contamination-resistant coding placement (SWE-bench Pro / SWE-bench Verified) yet published for Inkling; the model card reports SWE-bench Verified via a bash-only harness with a 256K trajectory cap.
- [ ] What is Inkling-Small's contamination-resistant coding (SWE-bench Pro) and GDPval-AA placement? Only Terminal-Bench 2.1 (55%), HLE, GPQA Diamond, CritPt and SciCode were published. [[inkling-small-lands-within-a-point-of-inkling-on-the-artificial-analysis-intelligence-index-with-less-than-a-third-of-the-parameters-805cabb6]]

## See also

- [[frontier-models]]
- [[nemotron-3-ultra]]
- [[glm-5]]
