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

## [2026-06-30] manual | conflict-resolver — 0 rebased, 3 requeued, 0 lint-fixed, 0 failed

pr#287 (ai-in-game-dev) requeued; pr#288 (game-music) requeued; pr#289 (agentic-coding) requeued (ci pending at dispatch time)

## [2026-06-28] daily | 5 topics, 11 sources, 17 pages

Daily Research 2026-06-28 complete. PRs #266–#270 merged. Key stories: Hy3-preview (Tencent, AA=34, 295B/21B MoE, $0.12/$0.43/Mtoken) + Step 3.7 Flash (StepFun, AA=30, 387.6 tok/s) confirmed (frontier-models); SWE-Marathon <30% solve rate on ultra-long-horizon tasks + 16.4% reward-hacking audit + Verification Horizon paper (agentic-coding); Epic CEO Sweeney "Scarlet Letter" framing on Steam AI disclosure + ~8,000 disclosed Steam games (700% YoY) + Hy-Motion 1.0 text-to-3D motion (ai-in-game-dev); Quantic Dream ~115-role layoffs put Star Wars Eclipse at cancellation risk + STJV sector-wide strike Jun 25 (games-of-note); iam8bit vinyl bonanza — Dead By Daylight 10th anniversary 4LP (€150) + Amnesia AMFP LP (£28) + Viridi jade vinyl (game-music). Report: wiki/reports/2026-06-28.md.

## [2026-06-28] daily | game-music — 1 source, 2 pages

## [2026-06-28] daily | games-of-note — 2 sources, 3 pages

## [2026-06-28] daily | ai-in-game-dev — 3 sources, 4 pages

## [2026-06-28] daily | agentic-coding — 3 sources, 4 pages

## [2026-06-28] daily | frontier-models — 2 sources, 4 pages

## [2026-06-28] health | weekly sweep — 2 disputes filed

Weekly health sweep 2026-06-28. 13 candidate sets scanned (12 source-triggered + 1 stale_sweep), 12 parallel scanner agents. 2 disputes filed on Kimi model pages: K2.7-Code summary claims 42 is "above" K2.6 (43) but 42 < 43 (high confidence); K2.6 frontmatter shows aa_intelligence_index=54 (v4.0) conflicting with body citing 43 on AA Index v4.1 (medium confidence). 9 stale synthesis pages. Lint: 0 errors, 164 warnings. PR #265 opened and queued for auto-merge.

## [2026-06-27] daily | 5 topics, 11 sources, 8 pages

Daily Research 2026-06-27 complete. PRs #259–#263 merged. Key stories: Self-Harness (arXiv 2606.09498) — fully self-supervised harness-improvement loop, no external agent required (agentic-coding); Nex-N2-Pro AA=41 open-weights MoE + Qwen3.7 Plus AA=39 multimodal confirmed (frontier-models); UE6 AI/Blueprints phaseout backlash + Valve Steam AI disclosure clarification + Krafton CAIO appointment (ai-in-game-dev); Bungie WARN 292 jobs Jul 9 + Compulsion layoffs begun Jun 25 + GTA 6 stock −3% on pre-order open (games-of-note); AC Black Flag 5LP + Hitman: WoA 4LP vinyl announced (game-music). Report: wiki/reports/2026-06-27.md.

## [2026-06-27] daily | game-music — 2 sources, 1 page

## [2026-06-27] daily | games-of-note — 3 sources, 2 pages

## [2026-06-27] daily | ai-in-game-dev — 3 sources, 1 page

## [2026-06-27] daily | frontier-models — 2 sources, 2 pages

## [2026-06-27] daily | agentic-coding — 1 source, 2 pages

## [2026-06-25] daily | 5 topics, 10 sources, 8 pages

Daily Research 2026-06-25 complete. PRs #252–#256 merged. Key stories: Claude Code auto-mode transcript-classifier replacing --dangerously-skip-permissions + Cursor 3.9 unified Customize page (agentic-coding); AA-Briefcase multi-week agentic KW benchmark (Fable 5 suspended leads) + Cohere North Mini Code open-weights 30B coding MoE (frontier-models); LLM+RL hierarchical control reaches parity with hand-crafted BTs in 2v2 game AI (ai-in-game-dev); GTA 6 confirms $80/$100 pricing, code-in-box no-disc launch, two retailers boycotting (games-of-note); Deltarune Ch5 OST most guest-heavy chapter + Stellar Blade OST PLUS review (game-music). Report: wiki/reports/2026-06-25.md.

## [2026-06-25] daily | game-music — 2 sources, 1 page

## [2026-06-25] daily | games-of-note — 3 sources, 1 page

## [2026-06-25] daily | ai-in-game-dev — 1 source, 1 page

## [2026-06-25] daily | frontier-models — 2 sources, 2 pages

## [2026-06-25] daily | agentic-coding — 2 sources, 3 pages

## [2026-06-23] daily | 5 topics, 13 sources, 8 pages

Daily Research 2026-06-23 complete. PRs #245–#249 merged. Key stories: agent CLAUDE.md config anti-patterns + dynamic workflow orchestration (agentic-coding); Kimi K2.7 Code (AA=42, SWE-bench 63.1%) + GLM-5.2 leads open-weights AA Index at 51 (frontier-models); JAMER benchmark for pro game-engine code + UE6 announced as UE5/UEFN merger (ai-in-game-dev); OtherSide/Deus Ex cancelled + Xbox leadership crisis deepens (games-of-note); Castlevania 46LP boxset + Adventures of Elliot OST review (game-music). Report: wiki/reports/2026-06-23.md.

## [2026-06-23] daily | game-music — 2 sources, 1 page

## [2026-06-23] daily | games-of-note — 4 sources, 1 page

## [2026-06-23] daily | ai-in-game-dev — 2 sources, 1 page

## [2026-06-23] daily | frontier-models — 3 sources, 4 pages

## [2026-06-23] daily | agentic-coding — 2 sources, 1 page

## [2026-06-22] daily | 4 topics, 6 sources, 9 pages

Daily Research 2026-06-22 complete. PRs #239-242 created. Key stories: NSA Director Gen. Rudd Senate testimony reveals Fable 5 ban is architectural autonomous-offense concern, not a fixable jailbreak; prediction markets 57–75% probability of restoration before July 1–17 (frontier-models); benchmark evaluation methodology challenge from arXiv (agentic-coding); GMF 2026 June 27 double-bill confirmed — Hades at 1:30pm, Persona at 8pm (game-music); EA Stockholm RL vision paper for game AI (ai-in-game-dev). games-of-note: 0 new sources. Report: wiki/reports/2026-06-22.md.

## [2026-06-22] daily | game-music — 1 source, 2 pages

## [2026-06-22] daily | ai-in-game-dev — 1 source, 2 pages

## [2026-06-22] daily | frontier-models — 2 sources, 3 pages

## [2026-06-22] daily | agentic-coding — 2 sources, 3 pages

## [2026-06-21] daily | 5 topics, 12 sources, 12 pages

## [2026-06-21] daily | game-music — 2 sources, 2 pages

## [2026-06-21] daily | games-of-note — 1 source, 1 page

## [2026-06-21] daily | ai-in-game-dev — 5 sources, 1 page

## [2026-06-21] daily | frontier-models — 1 source, 4 pages

## [2026-06-21] daily | agentic-coding — 3 sources, 4 pages

## [2026-06-18] daily | 5 topics, 9 sources, 19 pages

Daily Research 2026-06-18 complete. PRs #211-215 merged. Key stories: Ultracode GA + HarnessX composable harness foundry + CoDA-Bench data-intensive evaluation (agentic-coding); AA Intelligence Index v4.1 re-placements for Opus 4.8/GPT-5.5/Fable 5 (frontier-models); UE 5.8 first-party MCP plugin + UE6 open MCP foundation (ai-in-game-dev); Xbox Reset first confirmed closures (Ninja Theory), Luna Abyss 26-day postmortem, Meccha Chameleon 3M solo-dev breakout (games-of-note). Report: wiki/reports/2026-06-18.md.

## [2026-06-18] daily | games-of-note — 4 sources, 5 pages

Xbox Reset's first confirmed studio closure: Ninja Theory closing, Double Fine in spin-off talks; Hellblade Senua reveal was strategic buyer-bait; Luna Abyss (Kwalee Labs) closes 26 days post-launch due to flat Game Pass licensing fee; Meccha Chameleon solo dev 3M units in one week, #1 Steam. 2 new disputes, 3 new open questions. PR #215.

## [2026-06-18] daily | agentic-coding — 3 sources, 4 pages

Claude Code Week 25 changelog (Ultracode GA, /config syntax, subagent panel polish); HarnessX arXiv 2606.14249 — composable adaptive harness foundry with AEGIS trace-driven evolution (+14.5% avg across 5 benchmarks); CoDA-Bench arXiv 2606.15300 — 1,009 data-intensive coding tasks from Kaggle ecosystem. 2 new open questions. PR #214.

## [2026-06-18] daily | frontier-models — 1 source, 7 pages

AA Intelligence Index v4.1 re-placements for closed-frontier tier: Opus 4.8 (56, -5), GPT-5.5 (55, -5), Fable 5 (60, -4.9) — v4.0→v4.1 migration complete; GDPval-AA v2 Elo scale applied. Opus 4.8 retains AA #1 but lead over GPT-5.5 compresses 1.2→1 pt. Benchmark-leaders and cost-comparison regenerated. PR #213.

## [2026-06-18] daily | ai-in-game-dev — 1 source, 2 pages

UE 5.8 ships experimental first-party MCP plugin connecting Claude/Gemini/any model to Unreal Editor; UE6 (Early Access end-2027) built on open MCP foundation. Both major engines (Unity AI Gateway + Unreal MCP plugin) now have first-party agent paths. PCG graduated to Production-Ready. Summary regenerated. PR #212.

## [2026-06-18] daily | game-music — 0 sources, 1 page

No new game-music sources today; minimal log entry with pending GMF 2026 London June 27 closer. PR #211.

## [2026-06-17] daily | 5 topics, 12 sources, 22 pages

Daily Research 2026-06-17 complete. PRs #205-209 merged. Key stories: Bayesian-Agent posterior skill evolution + BugBot speed/cost upgrade (agentic-coding); AA Intelligence Index v4.1 agentic shift + GLM-5.2 open-weights leader (frontier-models); NVIDIA ACE Game Agent SDK Beta + Ubisoft AI NPC experiment (ai-in-game-dev); Xbox spin-off negotiations for Double Fine/Ninja Theory/Compulsion + Ninja Theory cancels Project Mara (games-of-note). Report: wiki/reports/2026-06-17.md.

## [2026-06-17] daily | game-music — 0 sources, 1 page

No new game-music sources today; GMF 2026 London cycle continues. Minimal log entry. PR #209.

## [2026-06-17] daily | games-of-note — 4 sources, 6 pages

Xbox spin-offs: Double Fine, Ninja Theory, and Compulsion reportedly in equity spin-off negotiations (studios retain IP licence); Ninja Theory cancels Project Mara to focus on Hellblade 3; Psychonauts 2 studio responds to Xbox layoff discussion. Summary regenerated with structured spin-off mechanic framing. PR #208.

## [2026-06-17] daily | ai-in-game-dev — 2 sources, 3 pages

NVIDIA ACE Game Agent SDK Beta for Unreal Engine 5: first SDK targeting on-device AI companions with context memory; Ubisoft debuts generative AI NPC experiment (Project NEO Alive). Summary regenerated. PR #207.

## [2026-06-17] daily | frontier-models — 3 sources, 6 pages

Artificial Analysis Intelligence Index v4.1 shifts to agentic workloads (v4.0 scores non-comparable); GLM-5.2 is open-weights leader at AA rank 51 on v4.1; Grok V9-Medium mid-cycle drop. Summary regenerated. Dispute filed on v4.0/v4.1 score comparability. PR #206.

## [2026-06-17] daily | agentic-coding — 3 sources, 6 pages

Bayesian-Agent posterior-guided skill evolution framework (arxiv 2606.08348); BugBot 3×+ speed / 22%-cheaper upgrade; harness-flaw diagnosis from failed trajectories (arxiv 2606.09876). Concept pages updated: agent-harnesses, harness-engineering. PR #205.

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

## [2026-05-30] daily | agentic-coding — 4 sources, 2 pages

Cursor 3.6 Auto-review Run Mode (auto-lint/format before agent submits); Willison PMF thesis (Claude Code + Codex = agentic-coding PMF achieved); BenchJack (331 gameable SWE-bench-style environments — most pointed eval-rigour critique yet); Dataset of 44 agentic coding-tool configs (1.3K configs, zero standardization). 3 sources dropped as already-ingested (AHE, SWE-Cycle, SWE-WebDevBench). 1 new dispute (BenchJack gameable-eval vs. PMF evidence), 3 open questions. PR #91 merged.

## [2026-05-30] daily | frontier-models — 1 source, 2 pages

Cursor Composer 2.5 reaches 62 on AA Coding Agent Index (3rd place, behind Claude Code 66 + Codex 65) at $0.07–0.44/task vs $4.10–4.82 for leaders — 10-60× cost advantage at modest capability discount. 0 disputes, 1 open question (cache-miss qualification). PR #92 merged.

## [2026-05-30] daily | ai-in-game-dev — 3 sources, 2 pages

PCSP: shared RL policy for infinite persona-consistent NPCs (ArXiv 2605.23652). ReactiveGWM: conditional world-model steered by NPC personality text at inference time (ArXiv 2605.15256). Momentum: autonomous agent validates PCG at runtime in endless-runner (ArXiv 2605.01783). 2 new disputes (PCSP vs per-NPC SLMs; ReactiveGWM vs Take-Two world-model pushback), 3 open questions. PR #93 merged.

## [2026-05-30] daily | games-of-note — 4 sources, 2 pages

007 First Light: 1.5M+ units in opening weeks (IO Interactive's biggest launch). MW4 on Switch 2: native build, CoD returns to Nintendo hardware after ~10 years. Slay the Spire 2 Chinese review-bomb: top players explain save-scumming removal + doormaker mechanic as grievances. 1 source dropped (vgchartz.com not in allowlist). 0 new disputes, 3 open questions. PR #94 merged.

## [2026-05-30] daily | game-music — 1 source, 2 pages

Square Enix Jazz –Chrono Trigger– closes the 2017–2022 SE Jazz series (5 albums + 1 live); 11 traditional jazz combo tracks arranged by Eijiro Nakagawa and Ryu Kawamura; reviewer frames jazz quality by emotional latitude over precision. 0 disputes, 2 open questions (series continuation; 'Secret of the Forest' omission). PR #95 open / auto-merge queued.

## [2026-05-30] daily | 5 topics, 13 sources, 10 pages

Daily research run complete: 5 topics, 13 new sources, 10 pages touched (5 topic indices + 1 source file deduped into _report + wiki/index.md + wiki/log.md + report). 5 per-topic PRs opened (#91–#95); #91–#94 merged, #95 queued for auto-merge. 4 disputes filed, 11 open questions added. Report: wiki/reports/2026-05-30.md. Note: gh CLI unauthenticated in cloud env; GitHub ops via MCP tools; index-wiki model download blocked (HuggingFace 403); qmd index has 0 docs/chunks.

## [2026-05-31] health | weekly sweep — 2 disputes filed

Scanned 17 candidate sets across 6 parallel wiki-disputes-scanner agents. 2 disputes filed in stale entity pages whose #1-leaderboard claims were superseded by Claude Opus 4.8 (May 28): Sonnet 4.6 GDPval-AA claim, GPT-5.5 AA Index / GDPval-AA claim. 0 errors, 62 lint warnings (all pre-existing). Full details in wiki/reports/health-2026-05-31.md.

## [2026-05-31] daily | agentic-coding — 6 sources, 7 pages

Harness-as-first-class-object cluster (4 arXiv preprints): system-scaling position paper, 11-component software-agent harness taxonomy, categorical architecture formalization, inference-time alignment showing more-elaborate harnesses not uniformly better. SQLite hardened anti-agentic-code stance (removed "(currently)"). Cursor Bugbot switches to usage-based pricing ($1.00–$1.50/run, 0.7–0.95 bugs/run). 1 new dispute, 3 open questions. PR #98 queued.

## [2026-05-31] daily | frontier-models — 4 sources, 7 pages

ITBench-AA: new K8s-incident-RCA agentic benchmark; all frontier models <50%; Opus 4.7 leads at 47% ($5.38/task). AA-LCR (100k-token multi-doc reasoning) added to Intelligence Index v4.0; GPT-5.2 Codex leads at 75.7%. Mistral Medium 3.5 (128B, 256k ctx, 77.6% SWE-Bench Verified, parallel cloud agents). DeepSeek V4 Pro confirmed at AA Index 52 (#2 open-weights). Cross-page sweep: deepseek-v4 entity, claude-opus-4.7 entity (re-verified). 0 disputes, 4 open questions. PR #99 queued.

## [2026-05-31] daily | ai-in-game-dev — 5 sources, 6 pages

AssetGen (Meta): image-to-mesh in 30s (Flash: 14s), mobile-ready polygon budget. World-Gen-to-Quest-Line dependency pipeline: coherent RPG PCG without degradation. NVIDIA DLSS 4.5 UE plugin + ACE Chatterbox Multilingual 500M (24 languages). Audio2Face open-sourced under MIT. Unity AI open beta (Editor 6.3+, MCP Server included). 1 dispute (AssetGen vs HunyuanStudio deployment-vs-fidelity tradeoff), 3 open questions. PR #100 queued.

## [2026-05-31] daily | games-of-note — 8 sources, 9 pages

Subnautica 2: 4M units in 17 days, ~$250M Krafton earnout on the line. CCP Games → Fenris Creations: $120M management buyout from Pearl Abyss, Google DeepMind minority stake + research partnership. Bungie: significant layoffs imminent post-final Destiny 2 update, no Destiny 3. Build a Rocket Boy (MindsEye): 170/250 staff cut, IWGB surveillance-software lawsuit. MercurySteam, Hinterland (Blackfrost delayed), Visual Concepts layoffs. EA: $8B record sales + $55B Saudi-led LBO (largest LBO in history). 1 dispute (MindsEye failure attribution), 3 open questions. PR #101 queued.

## [2026-05-31] daily | game-music — 0 sources, 1 page

No new qualifying sources from allowlist domains in the 2026-05-24–2026-05-31 window (low-flow topic, expected). last_updated bumped; divergence sentinel already satisfied from 2026-05-30. PR #102 queued.

## [2026-05-31] daily | 5 topics, 23 sources, 30 pages

Daily research run complete: 5 topics, 23 new sources, 30 pages touched (5 topic indices + 2 entity pages [deepseek-v4, claude-opus-4.7] + 23 source pages). 5 per-topic PRs opened (#98–#102), all queued for auto-merge. 3 disputes filed, 13 open questions added. Report: wiki/reports/2026-05-31.md. Note: gh CLI unauthenticated in cloud env; GitHub ops via MCP tools; index-wiki model download blocked (HuggingFace 403); existing .qmd index used.

## [2026-06-01] daily | agentic-coding — 7 sources, 11 pages

Harness engineering crystallizes as the binding-constraint thesis: harness governs more performance variance than model. 7 new sources (arxiv: BCT, Priority-Ranking, Eval-Engineering, Life-Harness, Continual-Harness; Anthropic containment; Thrive Holdings Codex loop). New concepts: harness-engineering, sandboxing. 1 dispute (BCT vs. Beyond Resolution Rates). 3 open questions. PR #104 merged.

## [2026-06-01] daily | frontier-models — 4 sources, 8 pages

Cohere Command A+ (218B/25B MoE, Apache 2.0, AA Index 37) joins roster as first fully-open-weights 200B-class model. Claude Opus 4.8 CyberGym backfilled (0.788). New entity: cohere-command-a-plus. 2 disputes, 3 open questions. PR #105 merged.

## [2026-06-01] daily | ai-in-game-dev — 6 sources, 8 pages

PBRFusion (NVIDIA/Painkiller RTX): 80% repetitive texture elimination. Roblox Cube 4D generation: mesh + interactivity from text prompt. PhysForge: VLM+diffusion, 150k-asset PhysDB. CA2: call-stack-fed RL game tester. GamED.AI: LangGraph game-dev agent ($0.46/game). Unreal Engine as multi-agent training substrate at CES 2026. 1 dispute, 4 open questions. PR #106 merged.

## [2026-06-01] daily | games-of-note — 4 sources, 6 pages

Stop Killing Games EU petition success. Embracer Fellowship of the Ring IP sale. Playstack (Balatro publisher) acquisition by IMC. CI Games / Epic Games Lords of the Fallen II deal termination. 3 disputes, 4 open questions. PR #107 merged.

## [2026-06-01] daily | game-music — 6 sources, 2 pages

Akira Yamaoka returns (Remothered: Red Nun's Legacy). NME AI/vinyl/indie feature (Wintory + Raine). BAFTA Games in Concert (BBC Concert Orchestra, Jan 31 Royal Festival Hall + UK tour). Sakimoto 40th anniversary at Game Music Festival 2026 (June 13 Fairfield Halls). Persona Live 2026: Awakenings (Hollywood, 30th anniversary). Deltarune Piano Collections Vol. 1 (Materia Collective, Trevor Alan Gomes). 1 dispute, 3 open questions. PR #108 queued.

## [2026-06-01] daily | 5 topics, 27 sources, 35 pages

Daily research run complete: 5 topics, 27 new sources, 35 pages touched (5 topic indices + 2 new concepts [harness-engineering, sandboxing] + 1 new entity [cohere-command-a-plus] + 1 updated entity [claude-opus-4.8] + 27 source pages). PRs #104–#108 opened; #104–#107 merged; #108 in merge queue. 8 disputes filed, 17 open questions added. Report: wiki/reports/2026-06-01.md. Note: gh CLI unauthenticated; GitHub ops via MCP tools; index-wiki model download blocked (HuggingFace 403); existing .qmd index used.

## [2026-06-02] daily | agentic-coding — 3 sources, 4 pages

Claude Opus 4.8 dynamic workflows (hundreds of parallel subagents via Outcomes API), SpaceX compute deal + doubled rate limits, Anthropic 2026 Dev Conference (Outcomes, Multi-agent orchestration, Dreaming), SpecBench reward-hacking benchmark (28pp gap growth per 10× code size). 1 dispute, 2 open questions. PR #110 merged.

## [2026-06-02] daily | frontier-models — 1 source, 4 pages

NVIDIA Nemotron 3 Ultra (550B/55B MoE): AA Index 48, US open-weights leader, 300+ tok/s. New entity: nemotron-3-ultra. claude-opus-4.8 AA Index re-verified at 61. 1 dispute, 2 open questions. PR #111 merged.

## [2026-06-02] daily | ai-in-game-dev — 7 sources, 8 pages

HY-World 2.0 (Tencent open-source 3D world model). Tripo P1.0 (native-3D-diffusion, ~2s, GDC 2026). UE5.7 PCG Biome Core (2× perf, production-ready). Total War:Pharaoh NVIDIA ACE on-device SLM advisor. GameDevBench (132 tasks, best agent 54.5%). MIMIC-Py personality-driven game tester. GDC 2026 AI workforce backlash (52% say AI harms industry). 2 disputes, 4 open questions. PR #112 merged.

## [2026-06-02] daily | games-of-note — 6 sources, 7 pages

Hazelight (Split Fiction) 50M lifetime sales. Studio Ricochet launched (ex-Gearbox Quebec). Marvel's Wolverine PS5 Sept 15 2026. UK social-media ban risk for game platforms. Lucy James → Player.gg. Xbox showcase June 7 safe (no Project Helix). 0 disputes, 3 open questions. PR #113 merged.

## [2026-06-02] daily | game-music — 2 sources, 1 page

Ivors Composers Awards 2026 Video Games category (entries open June 1, ceremony Nov 17 London). Game Music Festival + Infernal Symphony (Diablo 30th anniversary, June 6 Royal Festival Hall). SXSW London panel June 5 (Derek Duke + Ted Reedy). 0 disputes, 2 open questions. PR #114 merged.

## [2026-06-02] daily | 5 topics, 19 sources, 24 pages

Daily research run complete: 5 topics, 19 new sources, 24 pages touched (5 topic indices + 1 new entity [nemotron-3-ultra] + 1 updated entity [claude-opus-4.8] + 19 source pages). PRs #110–#114 opened and merged. 4 disputes filed, 13 open questions added. Report: wiki/reports/2026-06-02.md. Note: gh CLI unauthenticated; GitHub ops via MCP tools; index-wiki model download blocked (HuggingFace 403); existing .qmd index used.

## [2026-06-03] daily | agentic-coding — 5 sources, 6 pages

Cursor research preview: hundreds of concurrent agents, planner/worker/judge architecture, browser built in ~1 week. OpenHands May 2026: sub-agent delegation, Critic Result Display UI, Tavily MCP proxy. arXiv: proactivity vs. autonomy framing (Cursor Automations / Claude Code Routines / Jules Scheduled Tasks). Sandboxed coding agents outperform native omnimodal models on audio-video benchmarks (arXiv May 30). The New Stack: Claude Code / Cursor / Codex / Antigravity category convergence on distinct human-in-the-loop operating points. 0 disputes, 3 open questions. PR #116 merged.

## [2026-06-03] daily | frontier-models — 3 sources, 5 pages

Microsoft Build 2026: MAI-Code-1-Flash (51.2% SWE-Bench Pro, ships to all GitHub Copilot plans). MAI-Thinking-1: 35B-active sparse MoE, 256k context, commercially licensed, claims Opus 4.6 SWE Bench Pro parity (vendor-only). Mythos expanded from ~50 to 150 orgs across 15+ countries, $25/$125 per Mtoken, GA "coming weeks". New entity: claude-mythos. 1 dispute (MAI-Thinking-1 benchmark), 2 open questions. PR #117 merged.

## [2026-06-03] daily | ai-in-game-dev — 5 sources, 6 pages

NVIDIA ACE production launch across PUBG, inZOI, MIR5, NARAKA (Mistral-Nemo-Minitron-8B for PUBG Ally). Dual-agent Actor+Critic PCG for zero-shot 3D map generation. RuleSmith: multi-agent LLM game balancing + Bayesian optimization. RPGAgent: story-to-play via Elemental Tetrad. Meshy-6: Low Poly Mode for game developers. 1 dispute, 3 open questions. PR #118 merged.

## [2026-06-03] daily | games-of-note — 5 sources, 6 pages

PlayStation State of Play June 2026: God of War: Laufey (Faye protagonist, sentient cube voiced by Jack Quaid), Marvel's Wolverine, Until Dawn 2. Atari acquires Hipster Whale ($29.3M–$39.3M, Crossy Road 340M downloads). Ivy Road (Stanley Parable/Wanderstop devs) closes after Engine Angel funding failure (Metacritic 80). 0 disputes, 2 open questions. PR #119 merged.

## [2026-06-03] daily | game-music — 3 sources, 4 pages

Cyberpunk 2077: Future Sound of Night City (WRWTFWW Records, June 5, 22 tracks, 3 LP yellow vinyl, Polish beats curated by Grobel & Sokil). Merregnon: Heart of Ice — Uematsu's first original concert work (Decca Classics, Abbey Road + LSO, Alicia Vikander narration, June 19 + Paris Philharmonie June 25). Breath of the Wild 8-LP vinyl (Nintendo × Laced Records, 130 remastered tracks, June 19). 1 dispute, 3 open questions. PR #120 merged (flaky qmd integration test fixed en route).

## [2026-06-03] daily | 5 topics, 21 sources, 28 pages

Daily research run complete: 5 topics, 21 new sources, 28 pages touched (5 topic indices + 1 new entity [claude-mythos] + 21 source pages + 1 test fix). PRs #116–#120 opened and merged. 3 disputes filed, 13 open questions added. Report: wiki/reports/2026-06-03.md. Note: gh CLI unauthenticated; GitHub ops via MCP tools; index-wiki model download blocked (HuggingFace 403); existing .qmd index used; qmd integration test fixed to skip on HuggingFace rate-limit.

## [2026-06-04] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#124 (games-of-note) lint_fix dispatch: lint already green at dispatch time (broken-wikilink [[round-up-...-647b3fa5]] resolved after PR #125 merged); auto-merge re-enabled via MCP. pr#126 (ai-in-game-dev): already merged when CI completed.

## [2026-06-04] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#127 kind=requeue resolved=true — orphan-CLEAN (CI green, auto-merge not queued); enabled auto-merge via MCP `enable_pr_auto_merge`; PR entered merge queue and self-merged. Triggered by merge of PR #124 (games-of-note → main).

## [2026-06-04] daily | frontier-models — 8 sources, 10 pages

Nemotron 3 Ultra GA confirmed June 4 (HuggingFace/ModelScope/OpenRouter, 300+ tok/s on DeepInfra). Project Polaris replaces GPT-4 in GitHub Copilot from August 2026 (runs on Maia 200). Trump AI EO: voluntary 30-day pre-release cybersecurity review for frontier models. OpenAI GPT-5.5 + Codex on Amazon Bedrock. Anthropic Series H: $65B raised, $965B post-money, $47B ARR. Qwen3.7-Plus: multimodal MoE, ScreenSpot Pro 79.0, Terminal Bench 70.3, $0.40/$1.60/Mtoken. 3 disputes, 6 open questions. PR #122 merged.

## [2026-06-04] daily | agentic-coding — 7 sources, 8 pages

Claude Code dynamic workflows: Bun Zig→Rust 750k LOC in 11 days via Outcomes API. MCP 2026-07-28 RC: stateless core, Tasks extension, MCP Apps. GitHub Copilot app: Canvases, worktree isolation, cloud sessions. Build 2026: MXC declarative agent sandbox, agent-as-OS-principal identity via Entra ID. Cursor 3.4: full-screen tabs, floating prompt bar. Salt Code: first MCP-policy layer, day-one support for 8 coding assistants. 4 disputes, 8 open questions. PR #123 merged.

## [2026-06-04] daily | games-of-note — 9 sources, 14 pages

GoW Laufey: platforming returns (first since Ascension 2013), Faye double-jumps, DMC-style combat. FF7R Switch 2: Metacritic 86 vs PS5 92. Star Fox Switch 2: June 25 exclusive, GameChat. PlayStation permanently ends single-player PC ports (Hulst town hall May 18). Bungie third layoff wave: Destiny 2 ends June 9, no Destiny 3. Until Dawn 2: Firesprite replaces Supermassive. Onimusha Sep 25; Silent Hill Townfall Sep 24; Fable Feb 2027. New entities: bungie, santa-monica-studio. New concept: playstation-pc-port-strategy. 2 disputes, 4 open questions. PR #124 merged.

## [2026-06-04] daily | game-music — 4 sources, 5 pages

Rayman Legends Remake: Grant Kirkhope joins Christophe Héral, 55 min new music. FF7R Switch 2 reviews: music called "genuinely in the running for my favorite video game soundtrack of all-time." Atelier Ryza Official Soundtrack Trilogy vinyl box set: 3 LPs, 45 songs, 69 EUR, June 2026. Sledding Game vinyl: 180g blue marble, $35, late June/early July. 0 disputes, 2 open questions. PR #125 merged.

## [2026-06-04] daily | ai-in-game-dev — 5 sources, 6 pages

Meshy 3D Agent Beta: agentic iterative 3D creation, launched exactly June 4. Rodin Gen-2.5: production-level control, Smart Low-Poly topology for animation. Godot AI MCP server: production-grade, ~39 tools / 120 ops, one-click install. RTX Spark: 120B parameter LLMs + AAA gaming cohabitation on one chip. 0 disputes, 4 open questions. PR #126 merged.

## [2026-06-04] daily | 5 topics, 33 sources, 43 pages

Daily research run complete: 5 topics, 33 new sources, 43 pages touched (11 synthesis pages + 33 source pages; includes 2 new entity pages [bungie, santa-monica-studio] and 1 new concept page [playstation-pc-port-strategy]). PRs #122–#126 opened and merged. CI failure on #124 (broken-wikilink to game-music source) fixed via rebase onto main after #125 merged. 9 disputes, 24 open questions. Report: wiki/reports/2026-06-04.md. Note: gh CLI unauthenticated; GitHub ops via MCP tools; index-wiki blocked (HuggingFace network policy); existing .qmd index used.

## [2026-06-04] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#128 (claude/daily-2026-06-04/_report) BEHIND main by 1 commit (pr#129 conflict-resolver log entry landed after report branch was cut); wiki/log.md append-only conflict resolved (kept both the resolver entry from main and 6 daily report entries from PR); force-pushed sha=23d5d1e; auto-merge already enabled, will land when CI passes.

## [2026-06-04] manual | conflict-resolver — 1 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#128 (daily-2026-06-04/_report): DIRTY — wiki/log.md append-only conflict (both main and _report appended 2026-06-04 entries); rebased onto main, force-pushed SHA 2dd738a, auto-merge enabled. pr#129 (youthful-mayer-twoqH): orphan-CLEAN — CI passed after requeue scan; auto-merge enabled.

## [2026-06-04] manual | conflict-resolver — 2 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#131 (youthful-mayer-CRjOK): DIRTY — wiki/log.md append-only conflict; rebased onto main (6fc21ee), force-pushed sha=55a775f, auto-merge enabled. pr#130 (youthful-mayer-Ox0kT): stacked rebase onto rebased pr#131 tip to prevent re-conflict on merge, force-pushed sha=af40a32, auto-merge enabled. Triggered by merge of PR #128 (daily-2026-06-04/_report → main).

## [2026-06-04] manual | conflict-resolver — 2 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#130 (youthful-mayer-Ox0kT): DIRTY — wiki/log.md append-only conflict; rebased onto main (288ccc8), dropped already-squash-merged first commit, force-pushed sha=2293f51, auto-merge enabled. pr#132 (youthful-mayer-ZHcLr): DIRTY — stacked rebase onto rebased pr#130 tip (2293f51), append-only conflict resolved, force-pushed sha=a5855a9, auto-merge enabled. Triggered by merge of PR #131 (youthful-mayer-CRjOK → main).

## [2026-06-04] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#130 (youthful-mayer-Ox0kT): CLOSED as superseded — single commit (2293f51, "1 rebased, 1 requeued") already squash-merged into main via PR #132; rebase produced 0 commits ahead of main. pr#133 (youthful-mayer-Qibm2): DIRTY — first two commits already incorporated via PR #132 squash; skipped 2293f51, auto-dropped a5855a977c (already upstream); force-pushed sha=14b28eb onto main (f47605d); auto-merge enabled. Triggered by merge of PR #132 (youthful-mayer-ZHcLr → main).

## [2026-06-04] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#134 (youthful-mayer-RhH3E): DIRTY — wiki/log.md append-only conflict; rebased onto main (e03099c), kept both entries, force-pushed sha=3582d19, auto-merge enabled. Triggered by merge of PR #133 (youthful-mayer-Qibm2 → main).

## [2026-06-04] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#135 (youthful-mayer-8QMaM): DIRTY — wiki/log.md append-only conflict; rebased onto main (0649c1d), kept both entries (PR #134's entry + PR #135's entry), force-pushed, auto-merge enabled. Triggered by merge of PR #134 (youthful-mayer-RhH3E → main).

## [2026-06-05] daily | agentic-coding — 7 sources, 9 pages

GPT-5.3-Codex (SWE-bench Pro 56.8%, Terminal-Bench 77.3%, OSWorld 64.7%), Codex-Spark (1000+ tok/s, 15x), Uber $1,500/tool/month cap, Gartner MQ Leader, RHB reward-hacking benchmark, Agent Psychometrics, Cursor 3.7 context explorer. PR #136.

## [2026-06-05] daily | frontier-models — 3 sources, 5 pages

MAI-Thinking-1 new entity (35B-active MoE, AIME 2025 97%, SWE-bench Pro 52.8%, private preview), Build 2026 MAIA 200 chip (30% perf/dollar vs GB200), Claude Partner Network Services Track ($100M, 40K+ firms). PR #137.

## [2026-06-05] daily | ai-in-game-dev — 5 sources, 6 pages

TRELLIS.2 (MIT 4B-param, 3s 512³, full PBR), panoramic NPC grounding (structured JSON from segmentation), deflanderization failure mode, Sympatheia continuous-affect voice synthesis. PR #138.

## [2026-06-05] daily | games-of-note — 9 sources, 11 pages

Summer Game Fest week (SGF June 5, Xbox Showcase June 7, Gears E-Day), Star Wars Zero Company Aug 27, Marvel's Wolverine Sept 15, Control Resonant Sept 24, Gothic 1 Remake launched, Solarpunk Game Pass June 8, Destiny 2 end-of-active-dev, Rec Room shutdown, Stop Killing Games EU deadline July 27. PR #139.

## [2026-06-05] daily | game-music — 5 sources, 6 pages

Mewgenics 3LP vinyl (Ridiculon, 7 colorways), LBP+Sackboy iam8bit vinyl Q4 2026, Infernal Symphony Diablo 30th concert June 6 Royal Festival Hall, Ballads of the Underworld (Hades/Hades II, Korb/Barrett/Wintory) June 27, DK Bananza composer team (Naoto Kubo, live-orchestra-first, not David Wise). PR #140.

## [2026-06-05] daily | 5 topics, 29 sources, ~42 pages

agentic-coding, frontier-models, ai-in-game-dev, games-of-note, game-music. PRs #136–140 all squash-merged to main. 1 new entity (mai-thinking-1). Report: wiki/reports/2026-06-05.md.

## [2026-06-06] daily | game-music — 1 sources, 2 pages

Hitoshi Sakimoto confirms FFT is rock at London Game Music Festival 2026 debut — tuba/trombone as bass drum, other instruments as snare/hi-hat. PR #142.

## [2026-06-06] daily | agentic-coding — 4 sources, 9 pages

Agent sabotage detection study (human devs detect only 7% of subtle inserts), ADK Arena multi-framework eval (LangGraph leads), Cursor SDK programmatic agent access, Sandlock unprivileged sandbox (user-ns + seccomp + overlay + cgroups). 3 new concept pages: agent-sandboxing, parallel-subagents, agent-harnesses. PR #143.

## [2026-06-06] daily | frontier-models — 3 sources, 7 pages

ChatGPT Dreaming memory architecture (factual recall 41.5% → 82.8%), MAI-Code-1-Flash launch ($0.75/$4.50 per Mtoken, SWE-bench Verified 73.1%), MAI family context. 1 new entity: mai-code-1-flash. PR #144.

## [2026-06-06] daily | ai-in-game-dev — 4 sources, 5 pages

Bounded autonomy for LLM NPCs in live multiplayer (control loop, rollback, filter layers), Skin Tokens compact rigging representation (unified autoregressive), Reallusion AI Studio 3D-to-AI workflow, hybrid AI 2026 vision (Neri Neto). PR #145.

## [2026-06-06] daily | games-of-note — 11 sources, 12 pages

Summer Game Fest 2026 full slate: FF7 Revelation (Spring 2027, open-world Highwind), RE Code Veronica remake (likely first-person), Gen Atlas (Fumito Ueda, sci-fi kaiju mech), Cuphead sequel + Mighty Cuphead Adventure (8-bit physical), TMNT Last Ronin → PlatinumGames, Guild Wars 3 (NCSoft, fall 2027 beta), Alien Isolation 2, Palworld 1.0 July 10, Stellar Blade: Blood Rain (Sony publishing dropped). PR #146.

## [2026-06-06] daily | 5 topics, 23 sources, ~35 pages

game-music, agentic-coding, frontier-models, ai-in-game-dev, games-of-note. PRs #142–146 all squash-merged to main. 1 new entity (mai-code-1-flash), 3 new concept pages (agent-sandboxing, parallel-subagents, agent-harnesses). Report: wiki/reports/2026-06-06.md.

## [2026-06-07] health | weekly sweep — 1 dispute filed

Weekly health sweep 2026-06-07. 32 candidate sets scanned (31 source-triggered + 1 stale_sweep), 9 parallel scanner runs, 1 genuine dispute filed (Mythos availability supersession on frontier-models/index.md). No stale synthesis pages. PR #148 opened and queued for auto-merge.

## [2026-06-07] daily | agentic-coding — 5 sources, 8 pages

Harness-engineering wave: RHO (retrospective trajectory self-preference), HarnessForge (joint policy + harness co-evolution), Harness-Bench (multi-model harness-effect measurement), harness-updating vs AHE disentanglement, HarnessAudit (mid-trajectory safety audit channels). 2 concept pages updated (harness-engineering, sandboxing). PR #149.

## [2026-06-07] daily | frontier-models — 5 sources, 8 pages

MiniMax M3 launch: open-weight frontier model (1M context, native multimodality, SWE-Bench Pro 59.0% vendor-reported, $0.60/$2.40 per Mtoken). Gemini 3.5 Pro imminent (2M context, Deep Think). 1 new entity: minimax-m3. PR #150.

## [2026-06-07] daily | ai-in-game-dev — 6 sources, 7 pages

World-model wave: Matrix-Game 3.0 (real-time streaming + long-horizon memory), Hunyuan-GameCraft-2 (NL-steerable world model), WorldPlay (long-term geometric consistency), WorldCam (camera-pose-unified world generation). NVIDIA-Korea gaming partnership. Panic Playdate generative-AI ban. PR #151.

## [2026-06-07] daily | games-of-note — 11 sources, 12 pages

PlayerUnknown Productions halts Go Wayback, Paramount Game Studios launches, Wolf Among Us 2 confirmed 2027 + remaster, Tifa joins Street Fighter 6, Day of the Devs/SGF showcase, 33 Immortals full release soon, Gothic 1 Remake ships requiring day-1 patch. PR #152.

## [2026-06-07] daily | game-music — 2 sources, 3 pages

Mr. Records (Glee-Cheese / Wired Productions): 45 original songs by Bardin & Ducloux (funk/prog rock/hip-hop/electro), music-as-level-geometry mechanic, Q1 2027. Announced Day of the Devs. PR #153.

## [2026-06-07] manual | conflict-resolver — 3 rebased

pr#151 ai-in-game-dev rebased sha=815b7551, merged; pr#152 games-of-note rebased sha=823e364, merged; pr#153 game-music rebased sha=4186508, auto-merge queued

## [2026-06-07] daily | 5 topics, 29 sources, 38 pages

agentic-coding, frontier-models, ai-in-game-dev, games-of-note, game-music. PRs #149–153 all squash-merged to main. 1 new entity (minimax-m3). Conflict resolver handled 3 PRs with merge conflicts (PRs #151, #152, #153) — all resolved via synthesis union. Report: wiki/reports/2026-06-07.md.

## [2026-06-07] manual | conflict-resolver — 1 rebased

pr#155 rebased onto main (wiki/log.md chronological conflict resolved); auto-merge re-queued via MCP.

## [2026-06-08] daily | agentic-coding — 4 sources, 6 pages

Human oversight study (4 modalities: pre-flight/in-flight/post-flight/trajectory-replay; verification = 60-70% of effort), dynamic workflows (Bun Zig→Rust 750k lines, 11 days), skills taxonomy (9 categories), agentic replication eval. PR #157.

## [2026-06-08] daily | frontier-models — 3 sources, 5 pages

MiniMax-M3 AA Intelligence Index confirmed 55 (well above avg 23); Apple WWDC Gemini-powered Siri (custom 1.2T-param model, Private Cloud Compute); Codex expansion to non-code workflows. PR #158.

## [2026-06-08] daily | ai-in-game-dev — 5 sources, 6 pages

NVIDIA Cosmos 3 open omnimodel for physical AI (vision+text+action); SGF 2026 AI disclosure wave — Tomb Raider: Legacy of Atlantis declared AI use, community backlash; Unity AI Gateway early access beta. PR #159.

## [2026-06-08] daily | games-of-note — 11 sources, 12 pages

Xbox Showcase 2026 wave: Gears of War E-Day, Halo Campaign Evolved (July 28), Persona 4 Revival, Spyro A Realm Beyond (Tom Kenny), Stronghold (Beart+Starr), Valheim 1.0, Fields of Mistria 1.0; Future Games Show, PC Gaming Show, Wholesome Direct (53 games) recaps. PR #160.

## [2026-06-08] daily | game-music — 1 source, 2 pages

Square Enix Jazz series provenance confirmed: Nakagawa (trombone) + Kawamura (bass) arranged every track across entire series. PR #161.

## [2026-06-08] daily | 5 topics, 24 sources, 31 pages

agentic-coding, frontier-models, ai-in-game-dev, games-of-note, game-music. PRs #157–#161 all squash-merged to main. MiniMax-M3 AA Index updated (null→55). Report: wiki/reports/2026-06-08.md.

## [2026-06-09] daily | agentic-coding — 5 sources, 10 pages

Copilot SDK GA (cross-vendor agent standard); GitHub Shape AI code-review customization; SciVisAgent skills benchmark (scientific data analysis + visualization); MicroPython WASM sandboxing pattern for agentic code execution; Claude credit overhaul June 15. PR #163.

## [2026-06-09] daily | frontier-models — 5 sources, 8 pages

Project Glasswing expands Claude Mythos from ~50 to 150 orgs across 15 countries. Grok 4.3 new entity: Build 0.1 (API agentic), V9-Medium inference, Imagine 1.5 Preview (image gen). Grok coding lead mid-June release expected. PR #164.

## [2026-06-09] daily | ai-in-game-dev — 5 sources, 6 pages

AI disclosure debate intensifies: Crazy Taxi World Tour producer clarifies limited AI use; Fumito Ueda confirms zero AI in Gen Atlas; Shadow of the Colossus team same pledge. UE5.7 built-in AI assistant vs MCP practical comparison. PR #165.

## [2026-06-09] daily | games-of-note — 5 sources, 7 pages

Nintendo Direct June 9 — confirmed major reveals. Mina the Hollower hits 500K copies (Yacht Club's first original IP commercial milestone). Where Winds Meet Xbox expansion July. Summer Game Fest 2026 record 3.8M peak viewers. PR #166.

## [2026-06-09] daily | game-music — 2 sources, 3 pages

Mario Kart World's 323-song catalog lands on Nintendo Music (CarPlay/web expansion; open question on Spotify competition intent). Infinity Arranged soundtrack review added. PR #167.

## [2026-06-09] daily | 5 topics, 22 sources, 34 pages

agentic-coding, frontier-models, ai-in-game-dev, games-of-note, game-music. PRs #163–#167 all squash-merged to main. 1 new entity (grok-4.3). Report: wiki/reports/2026-06-09.md.

## [2026-06-11] daily | agentic-coding — 5 sources, 8 pages

Claude Fable 5 lands as agentic-coding workhorse (pause-resume tool calls, cross-repo scope expansion); silent capability dampening disclosed (0.03% traffic, PEFT/steering); Live-SWE-agent runtime self-evolution SOTA 45.8% SWE-Bench Pro; HAL eval infra (higher reasoning effort reduces accuracy in majority of runs); datasette-agent-edit reusable tool primitive. PR #171.

## [2026-06-11] daily | ai-in-game-dev — 3 sources, 4 pages

Post-SGF disclosure fallout: 1666 Amsterdam caught with AI art in prologue demo, apologized and reversed; vague-disclosure critique argues Steam policy fails its stated purpose; Inworld Realtime TTS-2 (sub-130ms, #1 Speech Arena, bracket-tag voice direction, 100+ languages). PR #173.

## [2026-06-11] daily | games-of-note — 10 sources, 11 pages

Nintendo Direct June 9: OoT remake confirmed for 2026 (gameplay-free cinematic reveal), Switch 2 AAA port wave (DMC5 June 23, Dragon's Dogma 2 Oct 9, Metaphor Nov 12, Stellar Blade TBA, KH4 day-and-date). Ubisoft closes Winnipeg+Belgrade studios, 380 layoffs. Xbox "this cannot continue" email: $20B content spend, half-billion revenue decline, 3% margin, major layoffs post-June 30. PR #174.

## [2026-06-11] daily | 5 topics, 27 sources, 38 pages

agentic-coding (#171 ✓), ai-in-game-dev (#173 ✓), games-of-note (#174 ✓) merged. frontier-models (#172) and game-music (#175) pending CI with auto-merge enabled. 1 new entity (claude-fable-5). Key story: Claude Fable 5 launched — #1 AA Index (64.9), SWE-bench Pro 80.3%, $10/$50 per Mtoken. OoT Remake confirmed for Switch 2 2026. Xbox "this cannot continue." Report: wiki/reports/2026-06-11.md.

## [2026-06-11] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#172 (wiki/frontier-models daily 2026-06-11) rebased onto main; resolved 1 conflict on wiki/entities/claude-mythos.md (Fable 5 + Mythos 5 content merged); pushed sha 0ada8b2; auto-merge re-queued.

## [2026-06-12] daily | agentic-coding — 4 sources, 5 pages

Nested subagents ship simultaneously in Claude Code 2.1.172 (5 levels deep) and Cursor SDK (JSONL stores, auto-review). SWE-Explore benchmark isolates repository exploration as first-class axis; datasette-agent 0.2a0 ships propose-then-persist human-approval primitive. PR #178.

## [2026-06-12] daily | frontier-models — 4 sources, 8 pages

Apple AFM 3 family: Cloud Pro positioned as Gemini-frontier-quality; Core Advanced is 20B sparse model with NAND-flash weight routing (1-4B active params/request, first to route around DRAM limit). Grok V9-Medium (1.5T) rolling out to Tesla/X ahead of public API. PR #179.

## [2026-06-12] daily | game-music — 3 sources, 4 pages

Stellar Blade vinyl via Brave Wave Productions. Elliot Millennium Tales 105-song OST (Iwadare, June 24). Wwise 2025.1 Haptic Clip Player: native haptic-audio authoring inside Wwise. PR #180.

## [2026-06-12] daily | games-of-note — 11 sources, 12 pages

Ubisoft restructuring wave continues (further closures, Rainbow Six staff ramp-down to Barcelona). Xbox post-June-30 layoffs may include studio closure. Destiny 2 final update live (8-year era over). Gothic 1 Remake PCGamer 72/100. Halo: Campaign Evolved July 28 confirmed. PR #181.

## [2026-06-13] daily | 5 topics, 14 sources, 28 pages

agentic-coding (#184 ✓), frontier-models (#185 ✓), game-music (#187 ✓), games-of-note (#186 ✓) merged. ai-in-game-dev (#188) auto-merge enabled post-CI. Key stories: Xbox business reset + exclusivity pivot; US government Fable 5/Mythos 5 suspension order; GitHub agentic coding at ~36% of new repos; Unity 2026 report: 95% AI adoption, 77% project-time drop; Hunyuan3D 2.1 open PBR pipeline. Report: wiki/reports/2026-06-13.md.

## [2026-06-13] daily | ai-in-game-dev — 4 sources, 6 pages

Unity 2026 report: 95% AI adoption, median project time down 77%. Owlcat prototyping-only policy for genAI. Take-Two's former AI head warns genAI hype is damaging behavioral/procedural AI research; his team disbanded April 2026. Hunyuan3D 2.1 open-weight PBR pipeline released (Unity/Unreal-ready). PR #188.

## [2026-06-13] daily | game-music — 1 source, 2 pages

Cyberpunk 2077 Future Sound of Night City physical soundtrack announced for July 2026 order. PR #187.

## [2026-06-13] daily | games-of-note — 4 sources, 5 pages

Xbox business reset: major layoffs announced, console exclusivity returning case-by-case. Game Awards 2026 date set (December 4); GTA 6 looms large. ESA opposes California offline-mode bill AB 1921 (passed Assembly, now Senate). PR #186.

## [2026-06-13] daily | frontier-models — 1 source, 7 pages

US government directive to suspend Fable 5 and Mythos 5 access in 15 countries; first documented federal intervention in frontier-model deployment. PR #185.

## [2026-06-13] daily | agentic-coding — 4 sources, 8 pages

Claw-SWE-Bench harness eval framework; frontier agents use metaprogramming for language adaptation; GitHub agentic adoption ~36% of new repos; GitHub Copilot moves to usage-based billing across all plans. PR #184.

## [2026-06-12] daily | ai-in-game-dev — 6 sources, 7 pages

Roblox CubePart: part-labeled engine-ready 3D generator (460K assets, no rigging). KH Collection AI-art community detection. PUBG Ally beta (NVIDIA ACE SLM on RTX Spark). Tripo AI $200M + Project Eden world model. Autodesk Wonder 3D USD-native. HDSL hierarchical scene DSL arxiv. PR #182 (pending CI).

## [2026-06-12] daily | 5 topics, 25 sources, 30 pages

agentic-coding (#178 ✓), frontier-models (#179 ✓), game-music (#180 ✓), games-of-note (#181 ✓) merged. ai-in-game-dev (#182) pending CI with auto-merge enabled. Key stories: Apple AFM 3 NAND-flash sparse architecture; Grok V9-Medium rolling out; Destiny 2 era closes; Ubisoft restructuring deepens; Roblox CubePart engine-ready 3D generator. Report: wiki/reports/2026-06-12.md.

## [2026-06-14] health | weekly sweep — 3 disputes filed

Weekly health sweep 2026-06-14. 31 candidate sets scanned (30 source-triggered + 1 stale_sweep), 6 parallel scanner agents. 3 disputes filed: Grok V9-Medium training date conflict (May 25 vs June 5), Binding Constraint Thesis vs LLM-primacy on harness-engineering.md, Muse Spark top-5 staleness superseded by Opus 4.7/4.8/Fable 5. No stale synthesis pages with zero divergence signals. Lint: 0 errors. PR #190 opened and queued for auto-merge.

## [2026-06-14] daily | agentic-coding — 1 source, 2 pages

PR #191. "The End of Code Review" (Monperrus, arxiv 2606.13175): agents have crossed the capability threshold making human code review structurally unnecessary. New disputes filed on agent-review-vs-sabotage and merge-success evidence. Summary updated with two-sided pressure framing.

## [2026-06-14] daily | frontier-models — 2 sources, 3 pages

PR #192. Gemini 3.5 Live Translate announced (speech-to-speech, preserves voice character/emotion); model card confirms it is based on Gemini 3 Pro and explicitly less capable than Gemini 3.1 Pro. No leader changes on cost/benchmark tables.

## [2026-06-14] daily | ai-in-game-dev — 1 source, 2 pages

PR #193. 3DCodeBench (arxiv 2606.01057): first benchmark for code-based procedural 3D modeling, covering 12 VLMs across 1,600 tasks. Open question filed on editability vs neural mesh generation.

## [2026-06-14] daily | games-of-note — 3 sources, 4 pages

PR #194. GTA 6 analyst split: van Dreunen (NYU Stern) says GTA 6 won't rescue industry; Circana forecasts $62.8B record year. Behaviour Interactive second layoff wave (95 jobs, strategic pivot to horror/service/LBE). New dispute and open question filed.

## [2026-06-14] daily | game-music — 1 source, 2 pages

PR #195. Stellar Blade vinyl pre-orders confirmed live June 11 (4LP $98 / 2LP $42); standard black editions available at retail partners.

## [2026-06-14] daily | 5 topics, 8 sources, 13 pages

Daily Research 2026-06-14 complete. PRs #191-195 queued for auto-merge. Key stories: agents supersede code review (agentic-coding); Gemini 3.5 Live Translate (frontier-models); 3DCodeBench procedural 3D (ai-in-game-dev); GTA 6 analyst split + Behaviour Interactive layoffs (games-of-note); Stellar Blade vinyl live (game-music). Report: wiki/reports/2026-06-14.md.

## [2026-06-16] daily | agentic-coding — 4 sources, 7 pages

Harness constitutive definition (arxiv 2606.10106); Windsurf retired, relaunched as Devin Desktop with ACP; MCP donated to Linux Foundation Agentic AI Foundation (co-founded with Block and OpenAI); Parallel-Synthesis KV-cache-space merge for parallel subagents. Summary regenerated. PR #199.

## [2026-06-16] daily | frontier-models — 2 sources, 3 pages

FrontierMath v2 audit: 42% of problems had errors; GPT-5.5 Tier 4 score jumped 35->73% from fixes; Fable 5 leads at 87-88% on audited axis. No leader changes. PR #200.

## [2026-06-16] daily | ai-in-game-dev — 1 source, 2 pages

Pearl Abyss/Crimson Desert undisclosed GenAI placeholder art: largest-scale caught-apologized-pledged-audit case to date. PR #201.

## [2026-06-16] daily | games-of-note — 3 sources, 4 pages

Xbox June 15: Compulsion Games (South of Midnight/We Happy Few, 100+ staff) reportedly to be shut down; Craig Duncan and Louise O'Connor exit Xbox Game Studios. Summary regenerated. PR #202.

## [2026-06-16] daily | game-music — 1 source, 2 pages

Shoji Meguro confirmed as special guest at GMF 2026 London Persona Grooves concert (Bartosz Pernal jazz orchestra + London Mozart Players, June 27 Royal Festival Hall). PR #203.

## [2026-06-16] daily | 5 topics, 11 sources, 18 pages

Daily Research 2026-06-16 complete. PRs #199-203 queued for auto-merge. Key stories: MCP to Linux Foundation AAIF + Windsurf to Devin Desktop/ACP (agentic-coding); FrontierMath v2 42%-error-rate audit (frontier-models); Crimson Desert undisclosed AI art (ai-in-game-dev); Compulsion Games closure + Craig Duncan resignation (games-of-note); Shoji Meguro at GMF London (game-music). Report: wiki/reports/2026-06-16.md.

## [2026-06-19] daily | agentic-coding — 6 sources, 4 pages

Cursor /in-cloud VM-per-subagent isolation + Automations v2 GitHub/Slack triggers; APEX three-layer co-evolution (arXiv 2606.15363); Codex Record & Replay demonstration-to-Skill; FastContext +5.5% SWE/RepoQA at -60% tokens (arXiv 2606.14066); agent trajectory fingerprinting 85.7% (arXiv 2606.16988). PR #217.

## [2026-06-19] daily | frontier-models — 3 sources, 2 pages

Grok 4.3 AA Intelligence Index 53→38 (re-benchmarked vs v4.1); Fable 5 Kalshi/Polymarket 68-71% odds of return before July 1; Anthropic MD "very confident" Fable 5 returns in coming days (Seoul, June 18). Summary regenerated. PRs #218, #219.

## [2026-06-19] daily | ai-in-game-dev — 3 sources, 1 page

PUBG Ally Duo Mode two-week beta (NVIDIA ACE, RTX ≥8GB); GameCraft-Bench 41.46% agent game-dev pass rate in Unity (arXiv 2606.17861); TechRadar counter-review: CPCs as "glorified bots." PR #220.

## [2026-06-19] daily | games-of-note — 4 sources, 1 page

Global games revenue $201.6B in 2025 (Newzoo, first time over $200B, +9.1% YoY); ZeniMax/id Software layoffs begin; July 1 wave threatens Sony/EA/BioWare; GTA 6 pre-orders June 25, Nov 19 release confirmed. Summary regenerated. PR #221.

## [2026-06-19] daily | game-music — 4 sources, 1 page

Bobby Prince (Doom/Wolfenstein/Duke Nukem 3D) dies June 16 at 81; Doom OST in Library of Congress National Recording Registry. Stellar Blade Arranged Tracks and CS2 OST reviews. Umineko vinyl pre-orders open (Materia Collective, $39.99, Q3 2026). Summary regenerated. PR #222.

## [2026-06-19] daily | 5 topics, 20 sources, 9 pages

Daily Research 2026-06-19 complete. PRs #217-#222 merged. Key stories: Cursor cloud VM subagents + APEX co-evolution (agentic-coding); Grok 4.3 re-benchmarked at AA=38 + Fable 5 imminent return (frontier-models); PUBG Ally beta + GameCraft-Bench 41.46% (ai-in-game-dev); $201.6B games revenue record + July 1 layoff wave + GTA 6 (games-of-note); Bobby Prince death + Doom OST in Library of Congress (game-music). Report: wiki/reports/2026-06-19.md.

## [2026-06-20] daily | frontier-models — 1 source, 1 page

Trump described G7 Fable 5 discussions as "going fine" with no deal terms; refund deadline June 20; no new model releases confirmed. PR #224.

## [2026-06-20] daily | ai-in-game-dev — 1 source, 1 page

Epic live-demo'd Claude driving UE6 editor directly (furnishing apartment, adjusting lighting); UE6 Early Access targeting end of 2027 with open MCP foundation. PR #225.

## [2026-06-20] daily | games-of-note — 1 source, 1 page

11 Bit Studios cancels Project 8 (narrative console game, 2018–2026, 37-person team, PLN 48.4M/$11.8M loss); staff cuts with half offered internal transfers. PR #226.

## [2026-06-20] daily | game-music — 4 sources, 1 page

Halo Original Trilogy 8LP vinyl: O'Donnell objects ("none of the composers or performers will see a dime," no original multitracks). Bobby Prince tributes (Romero, Broussard). Stewart Copeland not returning for Spyro: A Realm Beyond. Summary regenerated. PRs #227, #228.

## [2026-06-20] daily | 4 topics, 7 sources, 4 pages

Daily Research 2026-06-20 complete. PRs #224–#228 merged. Key stories: Fable 5 suspension ongoing with June 20 refund deadline (frontier-models); Epic UE6 Claude-driven editor live demo (ai-in-game-dev); 11 Bit Studios Project 8 cancelled after 7 years ($11.8M loss) (games-of-note); Halo vinyl O'Donnell compensation controversy + Bobby Prince tributes (game-music). Report: wiki/reports/2026-06-20.md.

## [2026-06-21] health | weekly sweep — 1 dispute filed

Weekly health sweep 2026-06-21. 12 candidate sets (11 source-triggered + 1 stale sweep), 6 scanner passes. 1 new dispute on frontier-models/index.md: Grok 4.3 v4.1 AA score (38) documented in 2026-06-19 log entry but Summary still carries stale "pending re-placement" framing. Lint: 0 errors, 147 warnings. 1 stale page (kimi-k2.6). PR #231.

## [2026-06-28] manual | conflict-resolver — 4 rebased, 0 requeued, 0 lint-fixed, 0 failed

4 daily research PRs (#267–#270) for 2026-06-28 cherry-picked onto force-pushed main (no shared merge base); conflicts resolved in 4 topic index files (agentic-coding, ai-in-game-dev, games-of-note, game-music); auto-merge re-queued via MCP.

## [2026-06-29] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#278 requeued — CI green (success 09:51Z), auto-merge re-enabled for game-music daily 2026-06-29

## [2026-06-29] daily | agentic-coding — 3 sources, 6 pages

ContextBench "Bitter Lesson" (scaffolding marginal on retrieval); multimodal repo-understanding study (vision-only hurts, supplementary visual context graph helps); Codex Remote GA (phone-as-control-plane). PR #274.

## [2026-06-29] daily | frontier-models — 2 sources, 6 pages

GPT-5.6 (Sol/Terra/Luna) limited preview, Sol SOTA on Terminal-Bench 2.1, tiered pricing; Mythos 5 cleared for US critical-infra orgs without export license, Fable 5 globally suspended. PR #275.

## [2026-06-29] daily | ai-in-game-dev — 2 sources, 3 pages

Nwiro Integration Kit: third-party Fab plugin connecting Claude Code/Codex CLI/Meshy/Tripo to UE; GBQA benchmark: 30 games, 124 bugs, best model finds only 48.39%. PR #276.

## [2026-06-29] daily | games-of-note — 3 sources, 4 pages

EU Commission rejects binding Stop Killing Games rule (voluntary code of conduct instead); Ubisoft Barcelona 51 layoffs (~28%), rolling strike June 30–July 16; GTA 6 record pre-orders ($1B/hr analyst estimate unverified, Piper Sandler 45M launch projection). PR #277.

## [2026-06-29] daily | game-music — 3 sources, 4 pages

NieR:Orchestra Concert 12026 [YoRHa] 10-stop US tour Aug 2026–Mar 2027 (Okabe + Yoko Taro at Seattle opener); Blue Prince 2LP via iam8bit ($43, Q2 2026); ARC Raiders 2LP via iam8bit ($43, Q4 2026). PR #278.

## [2026-06-29] daily | 5 topics, 13 sources, 23 pages

Daily Research 2026-06-29 complete. PRs #274–#278 merged. Key stories: ContextBench Bitter Lesson + Codex Remote GA (agentic-coding); GPT-5.6 Sol preview + Mythos 5 US critical-infra carve-out + Fable 5 suspended (frontier-models); Nwiro UE plugin + GBQA sub-50% QA ceiling (ai-in-game-dev); EU SKG rejection + Ubisoft Barcelona strike + GTA 6 pre-order demand (games-of-note); NieR:Orchestra Concert 12026 US tour + Blue Prince/ARC Raiders vinyl (game-music). Report: wiki/reports/2026-06-29.md.

## [2026-06-29] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#280 (_report daily 2026-06-29) rebased onto main; conflict in wiki/log.md resolved (append-only merge: conflict-resolver entry #279 + 6 daily research entries in chronological order); auto-merge re-queued via MCP.

## [2026-06-29] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#281 (claude/youthful-mayer-0nj7cs, prior conflict-resolver log entry) rebased onto main; wiki/log.md conflict resolved (append-only merge: 6 daily entries from #280 + prior resolver entry); force-pushed sha=9d86adf; auto-merge re-queued via MCP.

## [2026-06-30] daily | 5 topics, 13 sources, 10 pages

Daily Research 2026-06-30 complete. PRs #284–#288 merged; PR #289 (agentic-coding supplemental — Foundry GA entry on agentic-coding topic) auto-merge queued pending CI. Key stories: Cursor iOS + Claude Code Week 26 MCP OAuth (agentic-coding); GPT-5.5 Instant ChatGPT default + Azure Foundry GA for Opus 4.8 (frontier-models); MW4 skips Game Pass + ~$300M lost-sales figure for Black Ops 6 + Xbox ZeniMax union actions (games-of-note); Undertale orchestral UK tour expansion + WoW 20th anniversary world tour (game-music). Report: wiki/reports/2026-06-30.md.

## [2026-06-30] daily | game-music — 2 sources, 1 page

Undertale: The Determination Symphony 2026 — 7 UK shows (25-piece orchestra, September–November); WoW: 20 Years of Music World Tour 2026 — 6 North American cities (Helvepic, September–October). PR #288.

## [2026-06-30] daily | ai-in-game-dev — 0 sources, 1 page

Quiet day (fiscal year-end); GBQA 48.39% bug-detection ceiling carried forward; open question on AI tooling offsetting Xbox headcount reductions filed. PR #287.

## [2026-06-30] daily | games-of-note — 7 sources, 1 page

MW4 confirmed October 23 launch without Game Pass day-one inclusion; Black Ops 6 Game Pass cost ~$300M in lost sales (Bloomberg); analysts warn other marquee releases may follow; CWA/ZeniMax workers demand advance notice, hiring freezes, 2-year recall rights ahead of fiscal-year-end layoffs. PR #286.

## [2026-06-30] daily | frontier-models — 2 sources, 3 pages

GPT-5.5 Instant becomes ChatGPT consumer default (52.5% hallucination reduction in law/medicine/finance, 30% fewer words per response); Claude Opus 4.8 + Haiku 4.5 GA in Microsoft Azure Foundry (Azure-native identity/networking/governance). PR #285.

## [2026-06-30] daily | agentic-coding — 2 sources, 4 pages

Cursor for iOS launched (mobile agent supervision, Remote Control, Live Activities on lock screen, approve diffs from app); Claude Code Week 26 (`claude mcp login/logout` OAuth, background subagent permission prompts surface in main session, 37% streaming CPU reduction). PR #284.

## [2026-06-30] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#292 (claude/daily-2026-06-30/_report) rebased onto main (c8779f3); deduplicated wiki/log.md (6 unique 2026-06-30 entries) and wiki/index.md (1 report entry + 13 source slugs); force-pushed sha=8754805; auto-merge re-queued via MCP enable_pr_auto_merge.

## [2026-07-02] daily | agentic-coding — 2 sources, 6 pages

Claude Sonnet 5 becomes default model in Claude Code (v2.1.197, 1M context, $2/$10 intro); v2.1.198 adds auto-commit/push/PR for background agents and Explore-on-Opus upgrade. PR #297.

## [2026-07-02] daily | frontier-models — 3 sources, 7 pages

Claude Sonnet 5 (AA Index 53, SWE-bench 85.2%, GDPval-AA 1603) + new claude-sonnet-5 entity page; Fable 5 GA on AWS Bedrock + Claude Platform; Opus 4.8 re-verified. PR #298.

## [2026-07-02] daily | ai-in-game-dev — 0 sources, 1 pages

Quiet day — no new in-scope sources; sub-50% agentic game-dev ceiling unchanged. PR #299.

## [2026-07-02] daily | games-of-note — 3 sources, 4 pages

Xbox Reset July 6 wave: 5 studios at risk (Arkane Lyon, Compulsion, Double Fine, Ninja Theory, Undead Labs); Marvel's Blade cancellation candidate; Kojima's OD reportedly safe. PR #300.

## [2026-07-02] daily | game-music — 2 sources, 3 pages

Rhythm Heaven Groove Nintendo Music special release (Tsunku); Saint Slayer 300-copy 8-bit vinyl indie pressing. PR #301.

## [2026-07-02] daily | 5 topics, 9 sources, 21 pages

Claude Sonnet 5 default in Code v2.1.197; autonomous background agents in v2.1.198; Fable 5 on AWS; Xbox/MS cutting Marvel Blade, exploring Arkane sale; OD safe; game-music quiet day.

## [2026-07-03] daily | agentic-coding — 5 sources, 8 pages

Cursor iOS mobile oversight for cloud agents; CapCode/CapReward reward-hacking detection in SWE-bench evals; SWE-INTERACT + SWE-Together reframe coding-agent evaluation as multi-turn interactive sessions; Codex subagent error-propagation fix. PR #303.

## [2026-07-03] daily | frontier-models — 4 sources, 6 pages

Fable 5 redeployed (export controls lifted June 30); Claude Sonnet 5 released (AA Index 53, $2/$10 intro pricing, GDPval-AA 1603); new claude-sonnet-5 entity; Fable 5 jailbreak "not unique" per Anthropic (dispute filed vs. NSA testimony). PR #304.

## [2026-07-03] daily | ai-in-game-dev — 1 source, 4 pages

Aura 15.0 (Ramen): Sandbox Mode (isolated editor changes), Aura Skills, unlimited Auto Mode for Unreal + Unity. Game-engine counterpart to agentic-coding worktree-isolation pattern. PR #305.

## [2026-07-03] daily | games-of-note — 4 sources, 6 pages

Xbox July 6 mass layoffs (>1,000 roles), Arkane Lyon named as sell-or-close target, Marvel's Blade cancellation disputed by Jeff Grubb, Xbox vendor contracts being cut ahead of full-time layoffs, Ubisoft Barcelona strike active July 1–17. PR #306.

## [2026-07-03] daily | game-music — 3 sources, 5 pages

The Witcher in Concert 2026: 25+-city European tour (Dublin Oct 21, Percival Schuttenbach + Marcin Przybyłowicz); FFX 25th-anniversary 'Eternal Calm' 2xLP (July 1); Saint Slayer 300-copy splatter vinyl. PR #307.

## [2026-07-03] daily | 5 topics, 17 sources, 29 pages

Fable 5 redeployed + Claude Sonnet 5 launched (frontier-models leader picture updates); Xbox July 6 purge: Arkane Lyon, Compulsion, Double Fine, Ninja Theory, Undead Labs + >1,000 roles; Ubisoft Barcelona on strike; CapCode/SWE-INTERACT reframe agentic-coding evals; Aura 15.0 Sandbox Mode for Unreal/Unity; Witcher Concert European tour + FFX vinyl.

## [2026-07-04] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#312 (claude/daily-2026-07-04/game-music) requeued: mergeable_state=clean, CI green, auto-merge re-enabled via MCP
