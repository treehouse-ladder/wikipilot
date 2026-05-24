---
title: Frontier LLM landscape
kind: topic
sources: ["[[introducing-claude-opus-47-b8af8104]]", "[[claude-opus-47-everything-you-need-to-know-751c1827]]", "[[introducing-gpt-55-dfe7e0c6]]", "[[openais-gpt-55-is-the-new-leading-ai-model-097f1222]]", "[[gemini-31-pro-model-card-225ab705]]", "[[gemini-3-deep-think-advancing-science-research-and-engineering-e98b788f]]", "[[deepseek-v4-pro-on-hugging-face-a0d5aaf3]]", "[[introducing-claude-sonnet-46-c4a45eed]]", "[[xai-launches-grok-43-with-improved-agentic-performance-and-lower-pricing-f1cfb522]]", "[[qwen3-max-thinking-benchmarks-and-analysis-26760cd0]]", "[[introducing-mistral-3-3772caab]]", "[[artificial-analysis-intelligence-index-07e9d51e]]", "[[gdpval-measuring-the-performance-of-our-models-on-real-world-tasks-bc53ab6b]]", "[[the-llama-4-herd-a-new-era-of-natively-multimodal-ai-7554c7f6]]", "[[gemini-35-flash-model-card-de99f770]]", "[[gemini-35-flash-the-new-leader-in-intelligence-versus-speed-d886178d]]", "[[claude-mythos-preview-d737ab91]]", "[[kimi-k26-the-new-leading-open-weights-model-0bea9ccd]]", "[[the-growing-pains-of-frontier-models-when-leaderboards-stop-separating-and-what-to-measure-next-b0488a82]]", "[[introducing-gpt-rosalind-for-life-sciences-research-078f0d54]]", "[[qwen3-6-27b-on-hugging-face-20e9d0e7]]", "[[swe-cycle-benchmarking-code-agents-across-the-complete-issue-resolution-cycle-3256d47f]]", "[[swe-chain-benchmarking-coding-agents-on-chained-release-level-package-upgrades-26980c45]]", "[[muse-spark-meta-is-back-in-the-ai-race-f945bfc7]]", "[[glm-5-everything-you-need-to-know-a53ff5c1]]", "[[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]]", "[[subquadratic-launches-with-29m-to-bring-12m-token-context-windows-to-ai-78c846ee]]", "[[zaya1-8b-frontier-intelligence-density-trained-on-amd-3012ef57]]", "[[zaya1-8b-technical-report-614bf738]]", "[[deepseek-r2-explained-92-7-aime-32b-open-weight-d990eab3]]", "[[google-accidentally-leaked-gemini-3-2-flash-and-it-already-outperforms-3-1-pro-on-coding-4c205fb8]]"]
last_updated: 2026-05-24
last_verified: 2026-05-24
freshness_window_days: 30
---

# Frontier LLM landscape

See [purpose](purpose.md) for the topic charter (in-scope / out-of-scope) and
`CLAUDE.md` "Cross-cutting relevance criteria" for the meta-bar.

## Summary (2026-05-20 update)

The frontier-LLM landscape in mid-May 2026 is a four-way contest between Anthropic, OpenAI, Google DeepMind, and DeepSeek, with xAI, Alibaba (Qwen), Meta (Llama), and Mistral providing competitive flank pressure — especially on open weights.

### Current intelligence leaders (Artificial Analysis Intelligence Index v4.0)

As of May 2026, GPT-5.5 (xhigh) leads at 60, followed by GPT-5.5 (high) at 59, then a three-way tie at 57 between Claude Opus 4.7 (Adaptive, Max), Gemini 3.1 Pro Preview, and GPT-5.4 (xhigh) [[openais-gpt-55-is-the-new-leading-ai-model-097f1222]]. Qwen3.7 Max (released May 19) also scores 57, making it the most intelligent open-ecosystem reasoning model on this index [[qwen3-max-thinking-benchmarks-and-analysis-26760cd0]]. The Intelligence Index is a 10-evaluation aggregate (GDPval-AA, Terminal-Bench Hard, SciCode, AA-LCR, AA-Omniscience, IFBench, Humanity's Last Exam, GPQA Diamond, CritPt, Tau-squared-Bench Telecom) [[artificial-analysis-intelligence-index-07e9d51e]].

> GPT-5.5 (xhigh) currently ranks #1 on the Artificial Analysis LLM Leaderboard with an Intelligence Index score of 60.

> The Artificial Analysis Intelligence Index v4.0 incorporates 10 evaluations.

### Anthropic

Claude Opus 4.7 (released April 16, 2026) is the leader on GDPval-AA at 1,753 Elo — ~79 Elo points clear of the next models [[claude-opus-47-everything-you-need-to-know-751c1827]]. It also takes #2 on AA-Omniscience behind Gemini 3.1 Pro, driven primarily by reduced hallucination. Cost per Intelligence Index run is ~$4,406, ~11% less than Opus 4.6 despite scoring 4 points higher [[claude-opus-47-everything-you-need-to-know-751c1827]].

> Opus 4.7 is the new leader on GDPval-AA, scoring 1,753 Elo, around 79 Elo points ahead of the next closest models.

> Claude Opus 4.7 is our most intelligent model, with state-of-the-art performance on coding, agentic tasks, and reasoning.

Claude Sonnet 4.6 (released Feb 17, 2026) added a 1M-token context window in beta at unchanged $3/$15 per Mtoken pricing, jumped 8 points on the AA Intelligence Index (to 51) over Sonnet 4.5, and scored 60.4% on ARC-AGI-2 with 120k thinking tokens at high effort [[introducing-claude-sonnet-46-c4a45eed]].

> Sonnet 4.6 features a 1M token context window in beta. Pricing remains the same as Sonnet 4.5, starting at $3/$15 per million tokens.

### OpenAI

GPT-5.5 (released April 23, 2026) is positioned as more token-efficient than GPT-5.4 despite higher per-token pricing, with major gains in agentic coding, computer use, and knowledge work [[introducing-gpt-55-dfe7e0c6]].

> GPT-5.5 is priced higher than GPT-5.4, but it is both more intelligent and much more token efficient, delivering better results with fewer tokens.

OpenAI's GDPval benchmark (open-sourced 220-task gold subset, 44 occupations across the top 9 US-GDP sectors covering $3T of annual labor) has become a de-facto frontier evaluation, now incorporated into the AA Intelligence Index v4.0 as GDPval-AA [[gdpval-measuring-the-performance-of-our-models-on-real-world-tasks-bc53ab6b]].

> The primary evaluation metric is head-to-head human expert comparison. OpenAI has open-sourced a gold subset of 220 tasks.

### Google DeepMind

Gemini 3.1 Pro Preview supports 1M-token input and up to 64k-token output, priced at $2/$12 per Mtoken below 200k input, jumping to $4/$18 above 200k — the first major frontier model to officially tier prices by context length [[gemini-31-pro-model-card-225ab705]].

> Input price: $2.00 for prompts <= 200k tokens, $4.00 for prompts > 200k tokens.

Gemini 3 Deep Think reached 3455 Elo on Codeforces and gold-medal level on IMO 2025 [[gemini-3-deep-think-advancing-science-research-and-engineering-e98b788f]].

> Gemini 3 Deep Think attained a staggering Elo of 3455 on Codeforces ... and reached gold-medal level performance on the International Math Olympiad 2025.

### Open weights and Chinese labs

DeepSeek V4 (released April 24, 2026) is a 1.6T MoE (49B active, V4-Pro) and 284B MoE (13B active, V4-Flash), both with 1M context, both released under the MIT license. V4-Pro-Max scores 80.6% SWE-bench Verified and 3,206 Codeforces — surpassing GPT-5.4's 3,168 [[deepseek-v4-pro-on-hugging-face-a0d5aaf3]].

> The model weights are licensed under the MIT License. V4-Pro's Codeforces rating of 3,206 surpasses GPT-5.4's 3,168.

Mistral Large 3 (released December 2025) is a sparse MoE with 41B active and 675B total parameters under Apache 2.0 [[introducing-mistral-3-3772caab]]. Llama 4 Scout (17B active, 16 experts) ships with a 10M-token context window — currently the longest in any frontier-class open model [[the-llama-4-herd-a-new-era-of-natively-multimodal-ai-7554c7f6]].

> Llama 4 Scout offers an industry-leading context window of 10M.

Qwen3.7 Max (released May 19, 2026) reaches AA Intelligence Index 57 with a 1M-token context, putting Alibaba's frontier offering at parity with closed-source leaders [[qwen3-max-thinking-benchmarks-and-analysis-26760cd0]].

### xAI

Grok 4.3 (released April 30, 2026) hit AA Intelligence Index 53, with the largest single-benchmark improvement on GDPval-AA (+321 Elo over Grok 4.20). API pricing of $1.25/$2.50 per Mtoken is well below the frontier median [[xai-launches-grok-43-with-improved-agentic-performance-and-lower-pricing-f1cfb522]].

> Grok 4.3 (high) costs $1.25 per 1M input tokens and $2.50 per 1M output tokens.

### Updates 2026-05-21

Google DeepMind released Gemini 3.5 Flash on May 19, 2026, the first model in the Gemini 3.5 series. Despite being a Flash-tier model, it outperforms Gemini 3.1 Pro on agentic and coding benchmarks: Terminal-Bench 2.1 76.2%, MCP Atlas 83.6%, GDPval-AA 1656 Elo, and CharXiv Reasoning 84.2% for multimodal understanding [[gemini-35-flash-model-card-de99f770]]. On independent evaluation it scores 55 on the AA Intelligence Index (a 9-point jump over Gemini 3 Flash, driven by agentic gains and hallucination reduction), runs at over 280 output tokens/sec, and is priced at $1.50/$9 per Mtoken — placing it on the speed-intelligence Pareto frontier [[gemini-35-flash-the-new-leader-in-intelligence-versus-speed-d886178d]].

> Gemini 3.5 Flash outperforms Gemini 3.1 Pro on challenging coding and agentic benchmarks like Terminal-Bench 2.1 with a score of 76.2%.

> Gemini 3.5 Flash (high) scores 55 on the Artificial Analysis Intelligence Index ... a 9-point improvement from Gemini 3 Flash, driven primarily by agentic performance gains and hallucination reduction.

Anthropic's most capable model is Claude Mythos Preview (announced April 7, 2026), which is state-of-the-art on SWE-bench Verified (93.9%), GPQA Diamond (94.6%), USAMO (97.6%), Terminal-Bench 2.0 (82.0%), CyberGym (83.1%), and a saturated Cybench (100% pass@1). Unusually, Anthropic deliberately withheld it from general availability because its autonomous cybersecurity capabilities are judged too dangerous to ship broadly; access is invitation-only through Project Glasswing for critical-infrastructure and open-source defenders [[claude-mythos-preview-d737ab91]]. This means the publicly-rankable frontier (GPT-5.5, Opus 4.7, Gemini 3.1 Pro) sits below an unreleased Anthropic ceiling.

> Claude Mythos Preview is state-of-the-art on SWE-bench Verified (93.9%), GPQA Diamond (94.6%), USAMO (97.6%), Terminal-Bench 2.0 (82.0%), CyberGym (83.1%), and Cybench (100% pass@1, saturated).

> Anthropic does not plan to make Claude Mythos Preview generally available; access is invitation-only as part of Project Glasswing because its autonomous cybersecurity capabilities are judged too powerful to ship without additional safeguards.

On open weights, Moonshot's Kimi K2.6 (released April 20, 2026) is the new leading open-weights model, landing #4 on the AA Intelligence Index at 54 — behind only Anthropic, Google, and OpenAI (all 57). It is a 1T-total / 32B-active MoE with a 256k context, and cut its hallucination rate to 39% from Kimi K2.5's 65%, reaching 1520 Elo on GDPval-AA [[kimi-k26-the-new-leading-open-weights-model-0bea9ccd]]. This puts the leading open-weights model within 3 AA-Index points of the closed-source frontier.

> Moonshot's Kimi K2.6 is the new leading open weights model, landing at #4 on the Artificial Analysis Intelligence Index (54) behind only Anthropic, Google, and OpenAI (all 57).

## Recent updates

### Updates 2026-05-21 (second run)

A new benchmark-methodology paper argues the frontier leaderboards have stopped separating models on independent axes, and that the more informative signal is whether capabilities reinforce or trade off across releases [[the-growing-pains-of-frontier-models-when-leaderboards-stop-separating-and-what-to-measure-next-b0488a82]]. The authors decompose paired SWE-bench and GPQA Diamond scores into a population coupling trend plus a per-release residual ("h-field") that diagnoses each release's capability emphasis. Across 34 models from 10 labs (2024–2026) capabilities mostly cooperate, but cooperation varies by lab and over time: DeepSeek reversed from reasoning-rich to coding-first, Google maintains consistent reasoning emphasis, and Anthropic oscillates between coding excursions and recovery — with five April 2026 releases confirming the diagnostic out of sample.

> We decompose paired SWE-bench and GPQA Diamond scores into a population coupling trend and per-release residual (h-field) that diagnoses capability emphasis and identifies which measurement or stress test is most informative next.

> DeepSeek reversed from reasoning-rich to coding-first; Google maintains consistent reasoning emphasis; Anthropic oscillates between coding excursions and recovery.

On the model-release side, OpenAI introduced GPT-Rosalind, a frontier reasoning model specialized for life-sciences R&D (target discovery/validation, genomics interpretation, pathway analysis, hypothesis generation), optimized for scientific tool use across chemistry, protein engineering, and genomics [[introducing-gpt-rosalind-for-life-sciences-research-078f0d54]]. Like Claude Mythos Preview, it is deliberately gated: research preview, enterprise/eligible-institution access only via a trusted-access deployment structure, with no public pricing — a continuation of the pattern where the most specialized frontier capabilities ship behind restricted access rather than open API.

> GPT-Rosalind is a frontier reasoning model built to support research across biology, drug discovery, and translational medicine, with optimization for scientific workflows that combines improved tool use with deeper understanding across chemistry, protein engineering, and genomics.

> GPT-Rosalind is currently in research preview, deployed to eligible institutions, available to eligible U.S. customers with Enterprise agreements, launching through a trusted-access deployment structure.

On open weights, Alibaba shipped Qwen3.6-27B with a 262,144-token native context extensible to ~1.01M tokens, and a notable agentic feature: a `preserve_thinking` option that retains full reasoning context across turns (interleaved thinking), which the model card claims improves decision consistency and can reduce overall token consumption by minimizing redundant reasoning — explicitly framed as beneficial for agent scenarios [[qwen3-6-27b-on-hugging-face-20e9d0e7]].

> The model supports a preserve_thinking option that can be enabled when making API calls to maintain full reasoning context across multiple turns.

> Maintaining full reasoning context can enhance decision consistency and, in many cases, reduce overall token consumption by minimizing redundant reasoning, which is particularly beneficial for agent scenarios.

### Updates 2026-05-22

Meta has re-entered the frontier race with Muse Spark, its first frontier-class model since Llama 4 Maverick (April 2025) and — notably — its first model not released as open weights [[muse-spark-meta-is-back-in-the-ai-race-f945bfc7]]. Muse Spark scores 52 on the AA Intelligence Index (top-5 overall), sitting ahead of Claude Sonnet 4.6, GLM-5.1, MiniMax-M2.7 and Grok 4.20, and behind Gemini 3.1 Pro Preview, GPT-5.4 and Claude Opus 4.6. The jump is dramatic relative to Meta's open-weight history: Llama 4 Maverick and Scout scored 18 and 13 respectively as non-reasoning models, so Muse Spark closes most of the frontier gap in a single release. It is a multimodal reasoning model (text/image/speech input, text output) with a 260k context window, currently gated to Meta's first-party products (Meta AI, Facebook, Instagram, Threads) with API access promised soon.

> Muse Spark scores 52 on the Artificial Analysis Intelligence Index, placing it within the top 5 models benchmarked.

> It is the first frontier-class model from Meta since Llama 4 Maverick was released in April 2025, and notably the first Meta model that is not being released as open weights.

On open weights, Z.AI's GLM-5 (released February 11, 2026) is the leading open-weights model on the AA Intelligence Index at 50, up 8 points from GLM-4.7's 42 [[glm-5-everything-you-need-to-know-a53ff5c1]]. It is a 744B-total / 40B-active MoE — Z.AI's first new architecture since GLM-4.5 — and is the first model on this list documented to integrate DeepSeek Sparse Attention. GLM-5 takes the highest AA Agentic Index score among open-weights models (63, third overall), driven by GDPval-AA, under an MIT license with a 200k context window (text-only I/O).

> GLM-5 is the new leading open weights model ... GLM-5 achieves the highest Artificial Analysis Agentic Index score among open weights models with a score of 63, ranking third overall.

> GLM-5 ... scaling to 744B total / 40B active parameters, and integrates DeepSeek Sparse Attention.

### Updates 2026-05-23

The most consequential entrant since the last run is architectural rather than incremental-scale. Miami startup Subquadratic launched SubQ on May 5, 2026 — billed as the first LLM on a fully subquadratic (linear-scaling) attention architecture, with a 12M-token context window, a $29M seed round, and a founding team led by CEO Justin Dangel and CTO Alex Whedon (former Head of Generative AI at Meta) [[subquadratic-launches-with-29m-to-bring-12m-token-context-windows-to-ai-78c846ee]]. The core claim is its SSA (selective sparse attention) layer, which scales linearly with context length instead of quadratically, cutting attention compute by ~1,000x at 12M tokens via content-dependent position selection that itself does not go quadratic [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]].

> SubQ is a large language model from Miami startup Subquadratic, launched May 5, 2026, claiming to be the first LLM on a fully subquadratic (linear-scaling) attention architecture with a 12-million-token context window.

> The SSA architecture scales linearly with context length instead of quadratically, cutting attention compute by roughly 1,000x at 12M tokens.

Crucially for frontier-class status, SubQ is not just a long-context novelty: it reports 81.8% on SWE-bench Verified — within the closed-frontier band — alongside 95.0% on RULER 128K and 65.9% on MRCR v2 at 1M tokens, where it beats Gemini 3.1 Pro (26.3%) but trails GPT-5.5 (74.0%) [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]]. The reported prefill speedups (7.2x at 128K up to 52.2x at 1M tokens vs FlashAttention on B200 GPUs) and the shipped agentic surface (SubQ Code coding agent, SubQ Search deep-research tool) make this directly relevant to whole-repository agentic coding loops [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]].

> SubQ scored 95.0% on RULER 128K, 65.9% on MRCR v2 at 1M tokens, and 81.8% on SWE-Bench Verified. At 1M tokens, SubQ outperforms Gemini 3.1 Pro (65.9% vs 26.3%) on MRCR v2, though it trails GPT-5.5 (74.0%).

> Subquadratic is making this model available through an API with a 12-million-token context window, as well as a coding agent (SubQ Code) and a deep research tool (SubQ Search).

The caveat is sourcing: every headline efficiency number is vendor-run, single-shot, and not yet independently reproduced [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]] — there is no artificialanalysis.ai Intelligence Index entry for SubQ yet, so it cannot be slotted into the roster comparison until independent eval lands.

### Updates 2026-05-24

The most consequential open-weight move in May was efficiency-first, not scale-first. Zyphra released ZAYA1-8B (May 6, 2026), an Apache-2.0 reasoning MoE with 8.4B total but only ~760M active parameters per forward pass, optimized for maximum intelligence density per active parameter [[zaya1-8b-frontier-intelligence-density-trained-on-amd-3012ef57]]. Despite sub-1B active params it reaches 91.9% on AIME'25 and 89.6% on HMMT'25 — competitive with models many times its size [[zaya1-8b-frontier-intelligence-density-trained-on-amd-3012ef57]]. The technical report attributes this to three architectural choices: Compressed Convolutional Attention (CCA), which mixes sequences in a compressed latent space for an 8x KV-cache reduction vs full multi-head attention; a novel MLP-based expert router that improves routing stability over standard linear routers; and learned residual scaling [[zaya1-8b-technical-report-614bf738]]. Notably, ZAYA1-8B was trained end-to-end on AMD Instinct MI300X clusters with AMD Pensando Pollara networking — a rare frontier-relevant result outside the NVIDIA training stack [[zaya1-8b-frontier-intelligence-density-trained-on-amd-3012ef57]].

> ZAYA1-8B is a Mixture-of-Experts language model optimized for maximum reasoning performance per active parameter, with 8.4B total parameters but only 760M active per forward pass.

> With 0.7B active parameters and the 40K/4K Markovian RSA configuration, ZAYA1-8B reaches 91.9% on AIME'25 and 89.6% on HMMT'25.

> Compressed Convolutional Attention (CCA) performs sequence mixing in a compressed latent space, resulting in an 8x reduction in KV-cache size compared to full multi-head attention.

The long-standing open question of whether DeepSeek's reasoning model had shipped now has an answer: DeepSeek R2 is a 32B dense transformer released April 2026 under MIT license, scoring 92.7% on AIME 2025, fitting on a single 24GB consumer GPU, and undercutting Western frontier reasoning APIs by ~70% on token cost [[deepseek-r2-explained-92-7-aime-32b-open-weight-d990eab3]]. This is a sharp departure from R1's 671B-parameter MoE — R2 trades raw scale for local-deployability, reframing the frontier question from 'which model is smartest' to 'which is smart enough at a sustainable price' [[deepseek-r2-explained-92-7-aime-32b-open-weight-d990eab3]].

> Where R1 (January 2025) was a 671-billion-parameter Mixture-of-Experts behemoth, R2 ships as a 32B dense transformer released under MIT license, small enough to fit on a single RTX 4090 or A6000.

Looking forward, Google's next Flash tier leaked ahead of I/O 2026: Gemini 3.2 Flash surfaced in the iOS Gemini app and AI Studio on May 5, with early Arena human-preference results showing it beating Gemini 3.1 Pro on creative coding (SVG generation, interactive 3D, animation), and leaked AI Studio pricing of $0.25/$2.00 per Mtoken [[google-accidentally-leaked-gemini-3-2-flash-and-it-already-outperforms-3-1-pro-on-coding-4c205fb8]]. These are preliminary human-preference signals only — Google has not published MMLU-Pro, GPQA Diamond, or SWE-bench Verified scores, expected at I/O — so the leak sits below the topic's methodology bar and is tracked as a forward indicator rather than a confirmed capability claim [[google-accidentally-leaked-gemini-3-2-flash-and-it-already-outperforms-3-1-pro-on-coding-4c205fb8]].

> Gemini 3.2 Flash outperforms Gemini 3.1 Pro on certain creative coding tasks, including the well-circulated ASCII animation benchmark where 3.1 Pro produced broken code while 3.2 Flash succeeded in under two minutes.

## Comparisons

Pre-declared comparison pages (Phase 9 Pattern A) for this topic. Listed
in prose backticks until the underlying entity pages exist; once they do,
the topic-researcher (or `wikipilot compare new`) writes them to
`wiki/comparisons/`:

- [[cost-comparison]] — input/output $/Mtoken across frontier models (created 2026-05-20).
- `benchmark-comparison` — SWE-bench / GPQA / MMLU / ARC-AGI scores.
- `context-window-comparison` — max context + long-context pricing.
- `reasoning-mode-comparison` — reasoning availability, effort/quality
  knobs, cost.

## Disputes

- [[deepseek-v4-pro-on-hugging-face-a0d5aaf3]] claims V4-Pro-Max scores 80.6% on SWE-bench Verified, but OpenAI has stopped reporting SWE-bench Verified scores after an audit found every frontier model tested could reproduce verbatim gold patches or problem-statement specifics, indicating training-data contamination; on SWE-bench Pro the leaderboard inverts. Status: unresolved — SWE-bench Pro is the more credible frontier signal in 2026 but Verified scores are still widely quoted in launch materials.
- [[openais-gpt-55-is-the-new-leading-ai-model-097f1222]] claims GPT-5.5 ranks #1 on aggregate AA Intelligence Index at 60, but [[claude-opus-47-everything-you-need-to-know-751c1827]] claims Claude Opus 4.7 leads GDPval-AA (the agentic/economic-value sub-benchmark) by 79 Elo points. Status: unresolved — aggregate-index leadership and agentic-task leadership are coming apart, so 'best model' is task-dependent in mid-2026.
- [[openais-gpt-55-is-the-new-leading-ai-model-097f1222]] claims GPT-5.5 (xhigh) as the #1 frontier model at AA Intelligence Index 60, but [[claude-mythos-preview-d737ab91]] reports an unreleased Anthropic model (Claude Mythos Preview) at state-of-the-art across SWE-bench Verified (93.9%), GPQA Diamond (94.6%), and Terminal-Bench 2.0 (82.0%), withheld from GA for safety. Status: unresolved — public-leaderboard #1 and true-frontier-capability are decoupled when the most capable model is deliberately not released.
- [[the-growing-pains-of-frontier-models-when-leaderboards-stop-separating-and-what-to-measure-next-b0488a82]] claims DeepSeek reversed from reasoning-rich to coding-first across recent releases, while the topic page narrative treats DeepSeek V4's strong coding scores (e.g. 80.6% SWE-bench Verified, 3,206 Codeforces per [[deepseek-v4-pro-on-hugging-face-a0d5aaf3]]) as straightforward frontier progress rather than a deliberate capability-emphasis shift away from reasoning. Status: unresolved — the h-field framing reads DeepSeek's coding gains as a trade-off signal, not pure cooperation.
- [[swe-cycle-benchmarking-code-agents-across-the-complete-issue-resolution-cycle-3256d47f]] claims that even on isolated tasks, traditional deterministic pass/fail script evaluation (the methodology behind SWE-bench Verified) "produces severe misjudgments and false signals" and proposes SWE-Judge (LLM-based, human-validated) as a corrective, which would invalidate the existing Verified leaderboard comparisons this page relies on; [[deepseek-v4-pro-on-hugging-face-a0d5aaf3]] and other frontier-model announcements continue to cite SWE-bench Verified scores as capability indicators. Status: unresolved — if deterministic scripts are unreliable at the granularity SWE-Cycle claims, the cross-model SWE-bench Verified comparisons on this page may not be measuring what they claim to measure.
- [[glm-5-everything-you-need-to-know-a53ff5c1]] claims GLM-5 (AA Index 50, released Feb 11 2026) is the leading open-weights model, but the topic page already names two later open-weights leaders: Moonshot's Kimi K2.6 at AA Index 54 (released Apr 20) per [[kimi-k26-the-new-leading-open-weights-model-0bea9ccd]] and Qwen3.7 Max at 57 (released May 19) per [[qwen3-max-thinking-benchmarks-and-analysis-26760cd0]]. Status: resolved-toward-B — GLM-5 was the open-weights leader at its February release but has since been overtaken; the 'new leading open weights model' framing is time-bound to early 2026.

- [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]] claims SubQ at 81.8% SWE-bench Verified and ~1,000x cheaper attention at 12M tokens, positioning a subquadratic architecture as frontier-competitive, but the same source flags that every headline number is vendor-run, single-shot, and not independently reproduced; the established roster (GPT-5.5, Opus 4.7, Gemini 3.1 Pro) all carry independent artificialanalysis.ai Intelligence Index placements. Status: unresolved — SubQ's frontier claim rests entirely on self-reported numbers pending third-party eval.
## Open questions

- [ ] Has DeepSeek R2 (reasoning model) actually been released as of 2026-05-20, or has only V4 shipped? Search results are inconsistent.
- [ ] What is the methodological difference between SWE-bench Verified and SWE-bench Pro that explains the inverted rankings?
- [ ] Does GPT-5.5's #1 AA Intelligence Index ranking hold up on long-horizon agentic benchmarks where Claude Opus 4.7 currently leads?
- [ ] Is Gemini 3 Deep Think's 3455 Codeforces Elo measured against the live competition population or against a curated/historical task pool?
- [ ] ARC-AGI-2 went from 54% to 98% in 4 months. Is this genuine capability progress or contamination?
- [ ] Does Kimi K2.6's AA Intelligence Index 54 hold on the contamination-resistant SWE-bench Pro, or does the open/closed gap re-widen there?
- [ ] Claude Mythos Preview reports a saturated Cybench (100% pass@1) — is there an independent replication of these autonomous-cybersecurity scores, given the model is invitation-only?
- [ ] Is Gemini 3.5 Flash beating Gemini 3.1 Pro on Terminal-Bench 2.1 (76.2%) a genuine Flash-over-Pro inversion on agentic coding, or an artifact of Terminal-Bench 2.1 vs 2.0 version differences?
- [ ] Does the h-field 'leaderboards stop separating' thesis from [[the-growing-pains-of-frontier-models-when-leaderboards-stop-separating-and-what-to-measure-next-b0488a82]] reconcile with the AA Intelligence Index v4.0 still producing a clear #1 (GPT-5.5 xhigh at 60), or is the separation now driven mostly by agentic sub-benchmarks rather than SWE-bench/GPQA?
- [ ] Which of the paper's seven timestamped falsifiable predictions about the next 12 months of frontier releases have come true as of mid-2026 [[the-growing-pains-of-frontier-models-when-leaderboards-stop-separating-and-what-to-measure-next-b0488a82]]?
- [ ] Is GPT-Rosalind a fine-tune/specialization of an existing GPT-5.x base or a distinct model, and how does its life-sciences reasoning compare to general frontier models [[introducing-gpt-rosalind-for-life-sciences-research-078f0d54]]?
- [ ] Does Qwen3.6-27B's preserve_thinking interleaved-reasoning mode measurably reduce total tokens vs re-deriving reasoning each turn in long agentic loops [[qwen3-6-27b-on-hugging-face-20e9d0e7]]?
- [ ] On SWE-Chain's multi-step package upgrade benchmark, Claude Opus 4.7 scores 60.8% resolving [[swe-chain-benchmarking-coding-agents-on-chained-release-level-package-upgrades-26980c45]] — how do other frontier models (GPT-5.5, Gemini 3.1 Pro, DeepSeek V4-Pro) compare on the same chained-task design?
- [ ] Does Muse Spark's AA Index 52 hold on contamination-resistant benchmarks (SWE-bench Pro), or does Meta's single-release frontier jump look weaker on harder evals [[muse-spark-meta-is-back-in-the-ai-race-f945bfc7]]?
- [ ] Is Muse Spark a clean-room new architecture or a continuation/scale-up of the Llama line, and what does Meta's pivot away from open weights imply for the open/closed competitive balance [[muse-spark-meta-is-back-in-the-ai-race-f945bfc7]]?
- [ ] How much of GLM-5's agentic-index lead (63) among open-weights models is attributable to DeepSeek Sparse Attention vs. its 28.5T-token pretraining scale-up, and does the sparse-attention integration measurably help long-horizon agentic loops [[glm-5-everything-you-need-to-know-a53ff5c1]]?

- [ ] Does SubQ's claimed 81.8% SWE-bench Verified and ~1,000x attention-compute reduction at 12M tokens hold up under independent artificialanalysis.ai / third-party evaluation, and where would it land on the AA Intelligence Index relative to the current roster [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]]?
- [ ] Does SubQ's MRCR v2 advantage at 1M tokens (65.9% vs Gemini 3.1 Pro's 26.3%) translate into measurably better whole-codebase agentic-coding loops, or does the gap to GPT-5.5 (74.0%) at the same length cap its practical edge for repo-scale context [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]]?
- [ ] Is SubQ's SSA (selective sparse attention) architecturally distinct from the DeepSeek Sparse Attention that GLM-5 integrates, or are the two converging on the same content-dependent sparse-selection idea from different directions [[the-context-window-has-been-shattered-subquadratic-debuts-a-12-million-token-window-badc2592]]?
## See also

- [purpose](purpose.md)
- [[claude-opus-4.7]]
- [[gpt-5.5]]
- [[gemini-3.1-pro]]
- [[deepseek-v4]]
