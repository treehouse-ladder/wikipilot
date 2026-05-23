# Log

Chronological, append-only record of every routine run. Parseable with `grep "^## \[" wiki/log.md`.

Format (every entry uses this exact prefix):

```
## [YYYY-MM-DD] kind | subject

One-line summary.
```

Where `kind` is one of: `daily`, `query`, `health`, `manual`.

This file is **LLM-write, human-read**. Do not hand-edit; routines maintain it.

---

## [2026-05-11] manual | bootstrap

Empty wiki initialized. No topics enabled yet.

## [2026-05-20] daily | game-music — 6 sources, 1 page

First daily research pass for game-music topic covering vinyl releases, notable 2026 scores, and adaptive-audio middleware comparison.

## [2026-05-20] daily | games-of-note — 11 sources, 1 page

Daily research run for games-of-note topic.

## [2026-05-20] daily | ai-in-game-dev — 15 sources, 1 page

Applied proposal to topic index with engine-native AI assistants, generative content pipelines, AI-driven NPCs, and world-model research.

## [2026-05-20] daily | frontier-models — 14 sources, 6 pages

Applied proposal from topic-researcher: 14 sources ingested, topic index updated with 2026-05-20 summary, 4 entity pages created (claude-opus-4.7, gpt-5.5, gemini-3.1-pro, deepseek-v4), 1 comparison page created (cost-comparison).

## [2026-05-20] daily | agentic-coding — 12 sources, 1 page

Added Agent Skills pattern, long-running-agent harnesses, Claude Agent SDK rename, code execution with MCP, context engineering, infrastructure noise in evals, Opus 4.7, and OpenAI Codex subagents documentation.

## [2026-05-21] health | weekly sweep — 1 dispute filed

Scanned 6 candidate sets (5 source-triggered, 1 stale sweep); 1 dispute filed on gpt-5.5 entity (release date discrepancy between two sources: April 24 vs April 23, 2026).

## [2026-05-21] daily | game-music — 3 sources, 5 pages

Haptics convergence in FMOD/Wwise middleware; David Wise interview (Gamescom LATAM 2026); Distant Worlds Carnegie Hall June 2026 concert.

## [2026-05-21] daily | games-of-note — 4 sources, 6 pages

Nacon publisher collapse and Spiders liquidation; STJV boycott and Kylotonn strike; Zero Parades: For Dead Spies launch (May 21) and ZA/UM founder controversy.

## [2026-05-21] daily | ai-in-game-dev — 6 sources, 8 pages

Unity AI open beta; Autodesk acquires Radical AI mocap; production-ready 3D gen survey + Hunyuan3D Studio; NVIGI SDK; NVIDIA reliable AI coding for UE.

## [2026-05-21] daily | frontier-models — 4 sources, 6 pages

Gemini 3.5 Flash beats Gemini 3.1 Pro on agentic benchmarks; Claude Mythos Preview (93.9% SWE-bench, withheld via Project Glasswing); Kimi K2.6 new open-weights leader.

## [2026-05-21] daily | agentic-coding — 6 sources, 8 pages

Agentic Harness Engineering (automated harness evolution beats human-designed); prompt injection SoK (>85% attack success); Saving SWE-Bench (20-50% overestimation); Willison subagents guide; Anthropic 2026 Trends Report; SWE Context Bench.

## [2026-05-21] daily | 5 topics, 23 sources, 33 pages

Daily research run complete: 5 topics, 23 new sources, 33 pages touched, 5 PRs opened (#7–#11).

## [2026-05-21] query | Wwise vs FMOD vs MetaSounds for UE5 audio middleware — answers/2026-05-21-wwise-fmod-metasounds-ue5-comparison.md

Answer page created with 5 sources (1 existing, 4 new); back-filled into game-music topic page.

## [2026-05-21] daily | game-music — 3 sources, 1 page

Aether & Iron score (Christopher Tin / Alex Williamson, RPGFan review); Octopath Traveler 0 OST (Yasunori Nishiki, 2-CD Square Enix); Prescription for Sleep: Ocarina of Time (GENTLE LOVE arrangement album).

## [2026-05-21] daily | frontier-models — 3 sources, 1 page (run 2)

Growing Pains of Frontier Models (h-field benchmark methodology paper; DeepSeek capability-emphasis reversal); GPT-Rosalind (OpenAI life-sciences reasoning model, gated research preview); Qwen3.6-27B (256k/1M context, preserve_thinking agentic feature).

## [2026-05-21] daily | games-of-note — 4 sources, 1 page (run 2)

EA Battlefield layoffs post-record-launch; MercurySteam layoffs post-harassment allegations; Arc Raiders live-service counter-narrative (14M+ sales, ~6M WAU); Mixtape review (Annapurna, Beethoven & Dinosaur, GameSpot 9/10).

## [2026-05-21] daily | ai-in-game-dev — 2 sources, 1 page (run 2)

UE 5.7 in-editor AI assistant (C++/Verse code gen, F1 context help, scriptable MetaHuman); NVIDIA RTX Kit 2026.2 GDC roundup (ReSTIR PT, RTX Mega Geometry foliage, on-device ACE SLM/TTS).

## [2026-05-21] daily | agentic-coding — 6 sources, 1 page (run 2)

Sandboxing-as-autonomy: Claude Code OS-level sandbox (84% permission-prompt reduction), checkpoints/rewind autonomy feature; Cursor harness layer (Split PRs, CursorBench, per-model Codex alignment); SWE-WebDevBench production-readiness cliff (no platform >60% engineering quality).

## [2026-05-21] daily | 5 topics, 18 sources, 5 pages (run 2)

Second daily research pass for 2026-05-21: 5 topics, 18 new sources, 5 topic pages updated, 5 PRs created.

## [2026-05-22] daily | agentic-coding — 5 sources, 5 pages

Parallel-Claudes C compiler (2K sessions/$20K/100K-line), Managed Agents brain/hands decoupling, SkillsBench (+4.5pp SE), SWE-Chain (Opus-4.7 60.8%), SWE-Cycle+SWE-Judge (deterministic scoring "severe misjudgments").

## [2026-05-22] daily | frontier-models — 2 sources, 4 pages

Muse Spark (Meta AA Index 52, first closed-weight Meta model, 260k ctx multimodal); GLM-5 (Z.AI open-weights leader AA 50, 744B/40B MoE + DeepSeek Sparse Attention, MIT). New entities: muse-spark, glm-5.

## [2026-05-22] daily | ai-in-game-dev — 4 sources, 1 page

MoCapAnything V2 (end-to-end arbitrary-skeleton, ~20x faster); symbolically-scaffolded NPC dialogue (role-dependent scaffolding effects); fixed-persona SLM on-device; SMART LLM-guided RL playtesting (94% branch coverage).

## [2026-05-22] daily | games-of-note — 5 sources, 1 page

Contraction wave: Metacore/Supercell (160 roles), Survios near-shuttered, 31st Union roguelike pivot, Hinterland/Blackfrost delay. GDC 2026 genAI survey: 36% using, 52% negative, 7% positive (down from 13%).

## [2026-05-22] daily | game-music — 1 source, 1 page

Blue Prince OST (Trigg & Gusset debut): percussion-free ambient-jazz, rubato, ostinato 3/4.

## [2026-05-22] daily | 5 topics, 17 sources, 12 pages

Daily research run complete: 5 topics, 17 new sources, 12 synthesis pages updated (9 topic/entity + 3 cross-page), 5 PRs opened (#27-#31). 7 new disputes filed, 16 new open questions added.

## [2026-05-23] daily | agentic-coding — 6 sources, 1 page

Cursor 3 Agents Window; SWE-EVO (~25% vs ~73% long-horizon capability cliff); SlopCodeBench (77% erosion rate); SWE-CI (CI-loop maintainability); SkillJect (automated SKILL.md injection); MCP tool-description quality study.

## [2026-05-23] daily | frontier-models — 2 sources, 2 pages

SubQ from Subquadratic ($29M seed): first subquadratic-attention (SSA) LLM, 12M-token context, claimed 81.8% SWE-bench Verified (vendor-run, not independently reproduced). New concept page: subquadratic-attention.

## [2026-05-23] daily | ai-in-game-dev — 4 sources, 1 page

UE 5.8 Preview MetaHuman Crowds (tens→thousands); TITAN MMORPG LLM playtesting (8 commercial QA pipelines); overhearing-agent DM-assist paradigm (D&D case study); database-driven 3D level procgen (AAAI AIIDE).

## [2026-05-23] daily | games-of-note — 3 sources, 1 page

Bungie ends Destiny 2 active dev (June 9 final update, Sony layoffs, no D3); EA $55B PIF buyout analysis (sovereign-wealth vs LBO framing); Directive 8020 formula shift (over-the-shoulder + Turning Points, mixed reception).

## [2026-05-23] daily | game-music — 3 sources, 1 page

WoW Midnight composer Leo Kaliski on human-first stance + AI music perceptibility; Lies of P OST (70 tracks, RPGFan); Citizen Sleeper OST (Amos Roddy, 23-track ambient sci-fi, RPGFan).

## [2026-05-23] daily | 5 topics, 18 sources, 7 pages

Daily research run complete: 5 topics, 18 new sources, 7 synthesis pages updated (6 topic pages + 1 new concept page), 5 PRs opened (#38–#42), all queued for auto-merge. 7 new disputes filed, 16 new open questions added.

## [2026-05-23] manual | conflict-resolver — 1 PR rebased, 0 failed

pr#38 (claude/daily-2026-05-23/agentic-coding) was BEHIND main after PRs #39-#42 merged; rebased cleanly onto b738b33, force-pushed to 89b30b7, auto-merge re-queued.
