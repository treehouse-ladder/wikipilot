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

## [2026-05-24] health | weekly sweep — 0 disputes filed

Scanned 22 candidate sets across 5 parallel agents; no new disputes found. 0 errors, 16 lint warnings (5 orphans, 7 citation-density, 4 disputes-format). Full details in wiki/reports/health-2026-05-24.md.

## [2026-05-24] daily | frontier-models — 4 sources, 3 pages

ZAYA1-8B (first AMD-trained frontier model, CCA subquadratic attention); DeepSeek R2 confirmed (32B dense, MIT, 92.7% AIME'25); Gemini 3.2 Flash leaked (outperforms 3.1 Pro on coding). Updated: topic index, deepseek-v4 entity, subquadratic-attention concept.

## [2026-05-24] daily | agentic-coding — 5 sources, 1 page

Google I/O 2026: Antigravity 2.0 (desktop + CLI). Three new behavioral-lens evals: SWE-Atlas (resolution-rate inadequacy), scaffold taxonomy (4 architecture classes across 20+ agents), behavioral drivers (process over outcome).

## [2026-05-24] daily | ai-in-game-dev — 5 sources, 1 page

Sprite (static mockup → engine-ready UI pipeline); GameUIAgent (LLM + SIR for UI generation); SLM vs LLM for real-time DOOM control (1.3M params wins on latency); emotional-arc procgen (All Stories Are One Story).

## [2026-05-24] daily | games-of-note — 4 sources, 1 page

Bungie layoffs (no Destiny 3 greenlit); Build a Rocket Boy/MindsEye further cuts; Eurogamer editorial layoffs (IGN parent); EA stock below $55B PIF buyout price as CFIUS review continues despite record FY26.

## [2026-05-24] daily | game-music — 3 sources, 1 page

MOUSE P.I. For Hire OST (Patryk Scelina, big-band noir, Mondo vinyl); Ghost of Yotei vinyl (Toma Otowa, Milan Records gold-shimmer 2LP); Clair Obscur Grammy snub (Wintory won for Sword of the Sea; Testard 10-week Billboard Classical leader not nominated).

## [2026-05-24] daily | 5 topics, 21 sources, 7 pages

Daily research run complete: 5 topics, 21 new sources, 7 synthesis pages updated (5 topic pages + deepseek-v4 entity + subquadratic-attention concept), 5 PRs opened (#46–#50), all queued for auto-merge. 7 new disputes filed, 20 new open questions added.

## [2026-05-24] manual | conflict-resolver — 0 PRs rebased, 1 failed

pr#46 (claude/daily-2026-05-24/frontier-models) was DIRTY; rebased cleanly onto main and resolved 5 add/add source conflicts (frontier-models richer versions kept), but --force-with-lease refused due to concurrent push to origin (591dc9b → a48dee0). Will retry on next push to main.

## [2026-05-24] manual | conflict-resolver — 1 lint-fix dispatched, 1 resolved

pr#47 (claude/daily-2026-05-24/agentic-coding) was BLOCKED by broken-wikilink CI failure (io→i-o slug mismatch in Antigravity/Google-IO source refs, 7 occurrences). wiki-lint-fixer rebased onto main, repaired all 7 wikilinks, lint exits 0, pushed 92662b1; auto-merge re-queued via MCP. pr#53 had already auto-merged before dispatch.

## [2026-05-24] manual | conflict-resolver — 1 re-queued, 0 failed

pr#47 (claude/daily-2026-05-24/agentic-coding) BEHIND main with broken wikilink (at-io-2026 → at-i-o-2026 in topic index); fix + rebase already present from prior run (SHA 92662b1); auto-merge re-queued via MCP (gh unauthenticated in this env).

## [2026-05-26] daily | ai-in-game-dev — 3 sources, 4 pages

Genie + Street View (Google I/O 2026): prompt-to-playable grounded in real geometry; two empirical NPC studies (Dialogs VR; Beyond Scripts ICEC) filed as dispute against vendor engagement-positive framing. PR #66 merged.

## [2026-05-26] daily | agentic-coding — 7 sources, 9 pages

Code w/ Claude 2026: multi-agent orchestration, Outcomes, Dreaming (self-improvement loop) launched in public beta; FeatureBench: ~7x SWE-bench → feature-dev collapse (74.4% → 11.0%), largest gap on record; RoadmapBench: 39.1% Opus-4.7 long-horizon; OPENDEV cacheable/non-cacheable prompt segmentation; 70-project harness taxonomy; vibe architecting. PR #67 merged.

## [2026-05-26] daily | frontier-models — 2 sources, 7 pages

MiMo-V2.5-Pro (Xiaomi): open-weights co-leader tied with Kimi K2.6 at AA Index 54, MIT, $1/$3 Mtoken; Qwen3.7 Max: closed-weights correction (not open-weights), GPQA 92.4 / SWE-Pro 60.6. PR #68 merged.

## [2026-05-26] daily | games-of-note — 3 sources, 4 pages

Paramount/WBD acquisition: WB Games mentioned once in 30-min investor event; Mina the Hollower (Yacht Club, May 29, GBC-style); 007 First Light late review-code distribution (May 22 for May 26 launch). PR #69 merged.

## [2026-05-26] daily | game-music — 4 sources, 5 pages

Silent Hill Townfall composer reveal (Pilotpriest/Anthony Scott Burns, 'Home' April 7); Nintendo Music subscription-gated Star Fox pre-release drop; Namco×Capcom streaming after 20 years (Koshiro); Grim Fandango 25th-anniversary vinyl repress (iam8bit, McConnell). PR #70 queued for auto-merge.

## [2026-05-26] daily | 5 topics, 19 sources, 29 pages

Daily research run complete: 5 topics, 19 new sources, 29 pages touched (5 topic indices + mimo-v2.5-pro entity + cross-page sweeps on claude-opus-4.7/kimi-k2.6/glm-5/qwen3.7-max), 5 PRs opened (#66–#70). PRs #66–#69 merged; #70 (game-music) queued pending CI. 10 new disputes filed, 19 new open questions added.

## [2026-05-27] daily | frontier-models — 2 sources, 5 pages

Gemini 3.5 Flash (AA Index 55, default Gemini/Search model) confirmed; Gemini 3.5 Pro internal-only ~June ship; MiniMax M2.7 (open-weights 230B/10B-active MoE, AA Index 50, lowest hallucination rate 34%). Cross-page: gemini-3.1-pro entity updated, agentic-coding agentic-benchmark context. PR #72 merged.

## [2026-05-27] daily | agentic-coding — 3 sources, 5 pages

Apple Xcode 26.3 ships native Claude Agent SDK (subagents, background tasks, bidirectional MCP for visual Previews); SWE-Bench Mobile (12% ceiling, 6x cross-agent gap, multimodal PRD+Figma inputs); RGAO topology-aware orchestration (30.1%→8.2% misrouting reduction). Cross-page: ai-in-game-dev sweep (SWE-Bench Mobile Figma). PR #73 merged.

## [2026-05-27] daily | ai-in-game-dev — 3 sources, 4 pages

DancingBox lightweight single-webcam mocap via physical proxies; meta-ethnography of genAI in game dev (persistent 2D→3D production gap, authorship-erosion concern); VidAnimator mixed-initiative 4-stage video→stylized-animation pipeline. PR #74 merged.

## [2026-05-27] daily | games-of-note — 3 sources, 5 pages

007 First Light ships at ~88 Metacritic (IO Interactive's highest-rated game ever); Mina the Hollower pre-launch design profile; WotC MTG Arena union (supermajority cards, NLRB election June 2, genAI governance as core demand — first studio-union effort with explicit genAI demands). Cross-page: ai-in-game-dev WotC question. PR #75 merged.

## [2026-05-27] daily | game-music — 3 sources, 5 pages

Jake Kaufman (Shovel Knight) scores Mina the Hollower in MSX chiptune style (launches May 29); Lorien Testard + Alice Duport-Percier created 8+ hours of music for Clair Obscur: Expedition 33 (Laced vinyl in development); FFVIII OST 2026 RPGFan retrospective (Uematsu orchestral/electronic/chanting experiment, "partial failure that still coheres"). Cross-page: games-of-note Mina Kaufman detail. PR #76 merged.

## [2026-05-27] daily | 5 topics, 14 sources, 24 pages

Daily research run complete: 5 topics, 14 new sources, 24 pages touched (5 topic indices + gemini-3.1-pro entity + cross-page sweeps on agentic-coding/ai-in-game-dev/games-of-note), 5 PRs opened (#72–#76), all merged. 6 disputes filed, 12 open questions added.

## [2026-05-28] daily | game-music — 3 sources, 4 pages

Jake Kaufman Mina the Hollower craft detail (Furnace Tracker/Game Boy+MSX-SCC, 100+ tracks, 2 Yuzo Koshiro guest tracks, "Cajunvania" Zydeco/folk areas); Doom OST inducted into US National Recording Registry (only 3rd game-music entry after SMB theme and Minecraft: Volume Alpha); Elder Scrolls: Arena full-score remake (Ryan Zachariah Martin, fidelity-to-intent). 1 dispute resolved (Mina track count/Koshiro), 4 open questions. PR #78 queued.

## [2026-05-29] daily | frontier-models — 2 sources, 4 pages

Claude Opus 4.8 released (May 28): retakes AA Intelligence Index #1 at 61.4 (was GPT-5.5 at 60), retakes GDPval-AA at 1,890 Elo. SWE-bench Pro 69.2% (up from 4.7's 64.3%). Dynamic workflows research preview in Claude Code. New entity [[claude-opus-4.8]]; claude-opus-4.7 updated. 2 disputes, 4 open questions. PR #84 merged.

## [2026-05-29] daily | agentic-coding — 4 sources, 2 pages

Claude Code dynamic workflows (hundreds of parallel subagents, test-suite-as-oracle for codebase-scale migrations); fast mode 2.5x speed / 3x cheaper. Willison: "modest but tangible", unchanged Jan 2026 cutoff + model-level prompt-cache lever. AgentFlow synthesized harness tops TerminalBench-2 (84.3%) + finds 10 Chrome CVEs (2 Critical sandbox-escape). Terminal Wrench: 331 reward-hackable benchmark environments (output spoofing → rootkit hijacking). 3 disputes, 6 open questions. PR #85 queued.

## [2026-05-29] daily | ai-in-game-dev — 3 sources, 2 pages

Cutscene Agent: MCP-based director/specialist subagent system for Unreal cutscenes (CutsceneBench benchmark); diagnoses LLM spatial-reasoning weakness (degenerate 3D layouts). AutoUE: multi-agent full-game generation in UE with RAG-grounded tool use + automated play-testing. Take-Two's Slatoff: Genie "not a game engine" (first AAA-publisher on-record world-model skepticism). 2 disputes, 3 open questions. PR #86 merged.

## [2026-05-29] daily | games-of-note — 5 sources, 2 pages

GameMaker adds Claude Code to GM-CLI (opt-in agentic workflow surface, mainstream 2D engine). Studio Reset launched by ex-BioWare veterans (Parallax Deduction mechanic, "no moon logic" design). Ubisoft Halifax union settlement (confidential, 61 members). Ustwo CEO: employee job security "too romantic", pivoting to contractor-heavy PC-first model. Iron Galaxy: "adopting a new posture to accept these current market conditions as permanent" (2nd round in 13 months). 3 disputes, 5 open questions. PR #87 merged.

## [2026-05-29] daily | game-music — 4 sources, 2 pages

Mina the Hollower 96-track OST drops day-one as Name Your Price Bandcamp + Steam DLC (Game Boy + SCC+; Koshiro guest tracks 57 & 63 — resolves open questions). Scott Pilgrim EX: Anamanaguchi's biggest game-soundtrack (71 tracks, Polyvinyl 2xLP Aug 7). Phandelver: adaptive stinger vocabulary applied to TTRPG (Josh Barron). AudioNewsRoom: hybrid AI-procedural/human-core is the studio consensus; 50%+ cost savings only in narrow cases; AI-generated content not copyrightable in US; anti-training contract clauses now standard. 1 dispute, 4 open questions. PR #88 queued.

## [2026-05-29] daily | 5 topics, 17 sources, 12 pages

Daily research run complete: 5 topics, 17 new sources, 12 pages touched (5 topic indices + claude-opus-4.8 entity + claude-opus-4.7 update + wiki/index.md). 5 per-topic PRs opened (#84–#88); #84/#86/#87 merged, #85/#88 queued for auto-merge. 11 disputes filed, 22 open questions added. Report: wiki/reports/2026-05-29.md. Note: gh CLI unauthenticated in cloud env; GitHub ops via MCP tools; index-wiki model download blocked (existing .qmd index used).

## [2026-05-28] daily | agentic-coding — 6 sources, 7 pages

OpenAI harness trilogy: Symphony (Linear-as-state-machine orchestration spec, devbox-resident), Harness Engineering (3.5 PRs/eng/day, ~1M LOC, ~10x), Unrolling the Codex Agent Loop (first-party internals). GitHub-scale AIDev field-data wave: adoption study (22–29% in 128k projects), failure study (33k PRs; bug-fix tasks worst merge success; larger PRs fail CI), security study (4% of OSS PRs = hardening/testing). 3 new disputes, 7 open questions. PR #79 queued.

## [2026-05-28] daily | frontier-models — 5 sources, 9 pages

Open-weights late-May wave: Gemma 4 31B (AA Index 39, MacBook-runnable), NVIDIA Nemotron 3 Super (120B/12B-active hybrid Mamba-Transformer MoE, AA Index 36, open data+recipes), MiniCPM5-1B (AA Index 17.9, leading ≤1B, 131K context, Apache-2.0 full stack). GLM-5.1 independent AA placement (51) narrows vendor SWE-Bench Pro SOTA claim to coding-axis-only. Cross-page sweep: glm-5 entity, deepseek-v4, kimi-k2.6. 2 disputes, 4 open questions. PR #80 queued.

## [2026-05-28] daily | ai-in-game-dev — 4 sources, 5 pages

Capcom 30,000+ hrs/month autonomous playtesting (4-agent Google Cloud toolset, Monster Hunter Stories 3); PUBG Ally on-device SLM CPC (NVIDIA ACE, H1 2026 Arcade playtest, EN/KO/ZH voice); NVIDIA NVIGI 1.5 code-agent (program-once NPC, no per-frame SLM calls); Aura proprietary UE AI agent (Editor-Use + Coding Agent, invite-only). 2 disputes, 4 open questions. PR #81 queued.

## [2026-05-28] daily | games-of-note — 6 sources, 7 pages

Mina the Hollower ships at ~93 Metacritic (2026's highest-rated game, $20); Witcher 3: Songs of the Past (2027) announced (12-years-later CDPR expansion, Fool's Theory co-dev); Destruction AllStars shutdown after 5 years; Piranha Games 30% layoffs (2nd round in 16 months); Hasbro/WotC Atomic Arcade closure (Snake Eyes game); Behaviour Interactive ~40 layoffs (denied union/AI link). 3 disputes, 5 open questions. PR #82 queued.

## [2026-05-28] daily | 5 topics, 24 sources, 32 pages

Daily research run complete: 5 topics, 24 new sources, 32 pages touched (5 topic indices + glm-5/deepseek-v4/kimi-k2.6 entity cross-page sweeps + 24 source pages). 5 per-topic PRs opened (#78–#82), all queued for auto-merge. 11 disputes filed (1 resolved), 26 open questions added. Report: wiki/reports/2026-05-28.md. Note: gh CLI unauthenticated in cloud env; GitHub ops via MCP tools; index-wiki model download blocked (existing .qmd index used).

## [2026-05-29] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#85 (claude/daily-2026-05-29/agentic-coding) was BEHIND main by 3 commits (PRs #86, #88, #89 landed after PR was opened); no text conflicts. Branch updated via GitHub API to current main tip (c74a6ef); auto-merge confirmed active (enabled at PR creation 09:28Z). CI will re-run on updated tip.

## [2026-05-30] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#93 (ai-in-game-dev) self-merged before dispatch; pr#94 (games-of-note) CI green, auto-merge enabled (requeue).
