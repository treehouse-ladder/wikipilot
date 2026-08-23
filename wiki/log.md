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

## [2026-08-20] manual | conflict-resolver — 0 rebased, 0 requeued, 1 lint-fixed, 0 failed

pr#593 merged main into _report branch to resolve 3 broken-wikilink errors (sources from games-of-note PR #592 landed on main after _report was cut); auto-merge re-queued.

## [2026-08-20] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#590 (claude/daily-2026-08-20/frontier-models) was CLEAN with CI green and no auto-merge queued; enabled squash auto-merge via MCP tool — merged immediately.

## [2026-08-18] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

PR #581 (prior conflict-resolver session's log-only entry, claude/youthful-mayer-i4gpg5) was DIRTY after the 5 daily-research topic PRs (#575–#580) merged into main. Rebased onto main (conflict in wiki/log.md — daily entries inserted above the conflict-resolver entry), force-pushed sha=25ffdae, enabled auto-merge.

## [2026-08-18] daily | 5 topics, 8 sources, ~14 pages

Daily research run 2026-08-18: agentic-coding (1 source, 2 pages), frontier-models (2 sources, 3 pages), ai-in-game-dev (3 sources, 4 pages), games-of-note (3 sources, 4 pages), game-music (1 source, 2 pages). PRs #575–#579.

## [2026-08-18] daily | game-music — 1 source, 2 pages

Wwise 2026.1 Beta now installable from Audiokinetic Launcher; Wwise Motion adds Meta Quest/OpenXR support and Haptic Clip Player. Summary regenerated (summary_affecting). PR #579.

## [2026-08-18] daily | games-of-note — 3 sources, 4 pages

Marvel Tōkon: Fighting Souls — strong reviews, ~485K first-week sales (PS5-led), disastrous PC/Steam launch. PR #578.

## [2026-08-18] daily | ai-in-game-dev — 3 sources, 4 pages

WorldGen (Meta) and WorldClaw (Tencent) emit editable engine-importable 3D scenes (offline generators, not interactive world models). StatePlay directly addresses 'From Pixels to States' critique with MoT architecture jointly predicting visual content + game states. Summary regenerated (summary_affecting). PR #577.

## [2026-08-18] daily | frontier-models — 2 sources, 3 pages

Z.AI announced GLM-5.3 with CyberGym score 84.5% (overtaking Claude Mythos 80.3%) and AA Intelligence Index 58; weights release delayed from July 30 to August. PR #576.

## [2026-08-18] daily | agentic-coding — 1 source, 2 pages

Cursor's Origin: free cloud coding environment with 2-hour runtime, 80 GB storage, GitHub integration. PR #575.

## [2026-08-18] manual | conflict-resolver — 0 rebased, 6 requeued, 0 lint-fixed, 0 failed

Daily Research PRs #575–#580 (2026-08-18, all 5 topics + report) were CLEAN/green but lacked auto-merge (gh CLI token invalid during the daily run). Requeued all 6 via enable_pr_auto_merge: pr#575 agentic-coding, pr#576 frontier-models, pr#577 ai-in-game-dev, pr#578 games-of-note, pr#579 game-music, pr#580 _report.

## [2026-08-17] daily | 5 topics, 10 sources, ~7 pages

Daily Research 2026-08-17 complete. 5 topics processed (game-music, agentic-coding, frontier-models, ai-in-game-dev, games-of-note); 10 new source pages; ~7 pages touched. PRs #569–#573 created and merged (auto-merge). Report: wiki/reports/2026-08-17.md.

## [2026-08-17] daily | game-music — 0 sources, 1 page

Quiet day. No qualifying new sources found across the charter's sub-areas. Sentinel and Recent updates entry logged for 2026-08-17. PR #569.

## [2026-08-17] daily | agentic-coding — 3 sources, 2 pages

OpenAI Ultrafast tier (GPT-5.6 Sol Cerebras-served, up to 750 tok/s); Cursor prebuilt "builds" cut cold-start ~3x; Harness-IF benchmark (642 rules × 5 instruction surfaces; 3.6–7.4pt against-prior penalty across 12 frontier models). agent-harnesses.md updated. Summary regenerated (topic-summarizer). 3 open questions. PR #570.

## [2026-08-17] daily | frontier-models — 1 source, 1 page

Qwen3.8-27B: 27B dense VLM (Apache 2.0), 262K native context, Terminal-Bench 73.0%, SWE-bench Pro 61.7%. OSWorld benchmark-variant dispute filed. Frontier leader picture unchanged (Opus 5 max #1, 63). 4 open questions. PR #571.

## [2026-08-17] daily | ai-in-game-dev — 1 source, 1 page

Unity Neural: neural inference via URP, Neural Texture Compression (>50% runtime memory / ~70% disk reduction, rolling out in Unity 6.7). Unity Vector entering creatives + agentic phase. 1 open question. PR #572.

## [2026-08-17] daily | games-of-note — 5 sources, 1 page

Netflix closes Night School Studio (Oxenfree) and Moonloot Games — completing ~5yr gaming retreat. Double Loop Games closes (hostile mobile environment). Hello Games / Sean Murray: craft-first genAI abstention. Take-Two CEO: commercial streaming in 3 years, 10x install base. 1 dispute, 4 open questions. PR #573.

## [2026-08-13] daily | 5 topics, 9 sources, ~19 pages

Daily Research 2026-08-13 complete. 5 topics processed (frontier-models, ai-in-game-dev, games-of-note, agentic-coding, game-music); 9 new source pages; ~19 pages touched. PRs #551–#555 created and merged (auto-merge). Report: wiki/reports/2026-08-13.md.

## [2026-08-13] daily | game-music — 1 source, 2 pages

Hitoshi Sakimoto / Basiscape releases 13-track Veritas Tales: Witch of the Dark Castle OST on streaming (Spotify, Apple Music) and Steam. PR #555.

## [2026-08-13] daily | agentic-coding — 2 sources, 4 pages

SWE-Bench ProMax (170 instances, 7 languages, 41.2% best resolve rate) and HarnessCompass (3-axis harness fix: global constraints + first-person agent feedback + decoupled optimization); harness-engineering.md updated; 1 dispute, 3 open questions. PR #554.

## [2026-08-13] daily | games-of-note — 3 sources, 4 pages

Midsummer Studios (Jake Solomon, $6M raised) shuts down without shipping a game; That's No Moon lays off 14 staff; Remedy sets Control Resonant at $60 AAA for Sept 24 launch. 2 open questions. PR #553.

## [2026-08-13] daily | ai-in-game-dev — 1 source, 2 pages

Developer survey: two-thirds expect generative AI to impact team sizes in three years; publishers more bullish than developers on AI impact. PR #552.

## [2026-08-13] daily | frontier-models — 2 sources, 7 pages

Grok 4.6 launches at AA Intelligence Index 61 (tied GPT-5.6 Sol), co-trained with Cursor; grok-4.6.md entity created; cost-comparison + benchmark-leaders regenerated. PR #551.

## [2026-08-12] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#549 (wiki(reports): daily 2026-08-12, mergeable_state=clean, CI green) queued via MCP enable_pr_auto_merge (gh CLI unavailable); merged immediately.

## [2026-08-12] daily | 5 topics, 6 sources, ~15 pages

Daily Research 2026-08-12 complete. 5 topics processed (agentic-coding, frontier-models, ai-in-game-dev, games-of-note, game-music); 6 new source pages; ~15 pages touched. PRs #544–#548 created and merged (auto-merge). Report: wiki/reports/2026-08-12.md.

## [2026-08-12] daily | games-of-note — 1 source, 3 pages

Supermassive Games begins third round of layoffs in three years (up to 75 roles, post-Directive 8020 underperformance). New entity page supermassive-games.md created. PR #548.

## [2026-08-12] daily | ai-in-game-dev — 1 source, 2 pages

EA SEED's Script to Scene pipeline (text → playable mission) showcased at Advancing AI in Games Summit 2026; publisher AI bullishness vs developer-floor skepticism polarization noted. Summary updated. PR #547.

## [2026-08-12] daily | game-music — 0 sources, 1 page

Quiet day. Planet of Lana II announced but composer credits not yet established; no qualifying game-audio sources found. PR #546.

## [2026-08-12] daily | frontier-models — 1 source, 3 pages

OpenAI launches GPT-5.6-Cyber (95% cybersecurity task completion rate) and expands Daybreak initiative for authorized offensive-security workflows. Entity gpt-5.6-sol updated with cyber variant. PR #545.

## [2026-08-12] daily | agentic-coding — 3 sources, 6 pages

Three arXiv papers on agent harness self-evolution: One Recipe Many Harnesses (2608.10178), EvO-Bench (2608.09096), and Ouroboros (2608.08311). Concept pages agent-harnesses and harness-engineering updated. PR #544.

## [2026-08-11] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#542 (wiki(reports): daily 2026-08-11, mergeable_state=clean, CI green) merged via MCP merge_pull_request (gh GraphQL unavailable in this environment).

## [2026-08-11] daily | 5 topics, 3 sources, ~9 pages

Daily Research 2026-08-11 complete. 5 topics processed (agentic-coding, frontier-models, ai-in-game-dev, games-of-note, game-music); 3 new source pages; ~9 pages touched. PRs #536–#540 created and merged (auto-merge). Report: wiki/reports/2026-08-11.md.

## [2026-08-11] daily | game-music — 0 sources, 1 page

Quiet day. Big Walk (94 Metacritic, new 2026 critical leader) has no established composer credits yet; GW3/Jinnouchi reveal and Rust vinyl (2026-08-09) remain most recent events. PR #540.

## [2026-08-11] daily | games-of-note — 1 source, 2 pages

Big Walk (Tummy Games, launched Aug 5) takes 2026 critical crown with 94 Metacritic, surpassing Mina the Hollower (93); 1M copies sold in 6 days. Summary updated. PR #539.

## [2026-08-11] daily | ai-in-game-dev — 0 sources, 1 page

Quiet day. EU AI Act Article 50 enforcement regime (effective 2026-08-02) unchanged; no qualifying new sources across engine-native AI, 3D-gen, NPC/voice, or disclosure/workforce. PR #538.

## [2026-08-11] daily | frontier-models — 1 source, 3 pages

Meta releases Muse Glimmer (30B, Apache 2.0, Aug 10): AA index 35, distilled from Muse Spark 1.2, deployable on single H100 or RTX 5090. Does not displace leader (Claude Opus 5, 63). PR #537.

## [2026-08-11] daily | agentic-coding — 1 source, 1 page

Muse Glimmer launch: Meta's local 30B model targeting agentic coding workflows; AA intelligence index 35 vs frontier 63. PR #536.

## [2026-08-10] daily | agentic-coding — 2 sources, 3 pages

HarnessOpt-Bench (arXiv 2608.06301): first benchmark for automated harness optimization. LoopsBench (arXiv 2608.00267): long-horizon coding agent eval, 112 tasks, 8 languages; Opus-4.7 + Claude Code = 25% resolution. 1 dispute + 3 open questions filed. PR #530.

## [2026-08-10] daily | games-of-note — 3 sources, 2 pages

EA post-acquisition layoffs breach October no-changes pledge (fan-care + recruitment, Hyderabad). GTA 6 Netflix 6-hour trailer exclusive Aug 27; $80 price confirmed; no early access by design. Summary regenerated. PR #531.

## [2026-08-10] daily | frontier-models — 0 sources, 1 page

Quiet day. Leader picture unchanged (Opus 5 = 63, Fable 5 = 62, GPT-5.6 Sol = 61). GPT-5 Lite launch with no public benchmarks filed as open question. PR #532.

## [2026-08-10] daily | ai-in-game-dev — 0 sources, 1 page

Quiet day. EU AI Act Article 50 (effective 2026-08-02) remains most recent binding regulatory event. PR #533.

## [2026-08-10] daily | game-music — 0 sources, 1 page

Quiet day. GW3/Jinnouchi reveal and Rust vinyl (2026-08-09) remain most recent events. PR #534.

## [2026-08-10] daily | 5 topics, 5 sources, ~7 pages

Daily Research 2026-08-10 complete. 5 topics processed (agentic-coding, games-of-note, frontier-models, ai-in-game-dev, game-music); 5 new source pages created; ~7 pages touched. PRs #530–#534 created (auto-merge enabled). Report: wiki/reports/2026-08-10.md.

## [2026-08-09] health | weekly sweep — 2 disputes filed

Scanned 9 candidate sets (8 source-trigger + 1 stale sweep). Filed 2 disputes: agentic-coding dynamic-workflows default cap vs Summary framing; nemotron-3-ultra AA Intelligence Index v4.0/v4.1 version mismatch. 22 stale synthesis pages flagged. 0 lint errors.

## [2026-08-08] manual | conflict-resolver — 0 rebased, 0 requeued, 0 lint-fixed, 1 failed

pr#519 kind=rebase resolved=false — concurrent push landed during rebase (48cdc21→7f67d64); --force-with-lease correctly refused; PR merged via concurrent fix (sha 30f6029) at 09:51 UTC

## [2026-08-08] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#519 (wiki(reports): daily 2026-08-08, mergeable_state=clean, CI green) requeued auto-merge via enable_pr_auto_merge.

## [2026-08-08] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#518 (wiki(log): conflict-resolver 2026-08-08, CI green, orphan-CLEAN) requeued auto-merge via enable_pr_auto_merge.

## [2026-08-08] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#516 (wiki(games-of-note): daily 2026-08-08, CI green) requeued auto-merge via enable_pr_auto_merge.

## [2026-08-08] daily | 5 topics, 0 new sources, 5 pages

Daily Research 2026-08-08 complete. 5 topics processed (agentic-coding, frontier-models, ai-in-game-dev, games-of-note, game-music); 0 new source pages created; 5 topic index pages touched; 5 new open questions filed. PRs #513–#517 created and merged (auto-merge). Report: wiki/reports/2026-08-08.md.

## [2026-08-08] daily | agentic-coding — 2 sources (existing), 1 page

GPT-5.4/5.4-mini retirement for signed-in ChatGPT users on Aug 31 (Codex changelog); Claude Code auto-compact enforcement for unrecognized model IDs. Both sources already ingested from prior runs. PR #513.

## [2026-08-08] daily | frontier-models — 0 sources, 1 page

Quiet day. Leader picture unchanged: Opus 5=61, Fable 5=60, GPT-5.6 Sol=59, Kimi K3=57. DeepSeek-V4-Flash-0731 baseline gap filed as open question. PR #514.

## [2026-08-08] daily | ai-in-game-dev — 0 sources, 1 page

Quiet day. All sub-areas unchanged from last logged positions. PR #515.

## [2026-08-08] daily | games-of-note — 0 sources, 1 page

Quiet day. Two non-allowlist items (Marvel Tokon via gamereactor.eu; EA privatization follow-up via abcnews.com) filed as open questions. PR #516.

## [2026-08-08] daily | game-music — 0 sources, 1 page

Quiet day. Beast of Reincarnation composer-credit gap still unresolved; all primary threads (vinyl-revival, Halo/O'Donnell dispute, AI-vs-human-composer, Nintendo Music cadence) unchanged. PR #517.

## [2026-08-06] daily | 5 topics, 6 sources, ~14 pages

Daily Research 2026-08-06 complete. 5 topics processed (frontier-models, agentic-coding, games-of-note, ai-in-game-dev, game-music); 6 new sources ingested; ~14 pages touched. PRs #506–#510 created and merged (auto-merge). Report: wiki/reports/2026-08-06.md.

## [2026-08-06] daily | frontier-models — 1 source, 3 pages

Muse Spark 1.2 (AA Index v4.1 = 54): tied with Grok 4.5, one point behind GPT-5.5; no frontier leader displaced. PR #506.

## [2026-08-06] daily | agentic-coding — 3 sources, 5 pages

Meta enters agentic CLI with Muse Code + Muse Spark 1.2 (co-trained with harness); Claude Fable 5 one-shots raccoon-heist game via Playwright loop; LLM CLI 0.32 adds content-addressable log. PR #507.

## [2026-08-06] daily | games-of-note — 2 sources, 3 pages

Halo CE PS5 slow start: 452K copies, ~$28M first month (~1/6 of Xbox); Halo Studios post-launch layoffs amid troubled UE5 migration. PR #508.

## [2026-08-06] daily | ai-in-game-dev — quiet day, 0 sources, 1 page

No qualifying sources today; AI playtesting open question carried forward. PR #509.

## [2026-08-06] daily | game-music — quiet day, 0 sources, 1 page

No qualifying sources today; Beast of Reincarnation composer gap open question carried forward. PR #510.

## [2026-08-05] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#504 rebased onto main (sha 838e538); resolved wiki/log.md append-order conflict (4th-fire detail vs pr#502 detail already in main); auto-merge re-enabled.

## [2026-08-05] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#503 (wiki(log): conflict-resolver 2026-08-05) rebased onto main; resolved wiki/log.md append conflict (pr#501+pr#502 conflict-resolver entries vs pr#503 entry); auto-merge re-enabled.

## [2026-08-05] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#502 rebased onto main; resolved wiki/log.md append conflict (pr#501 conflict-resolver entry vs pr#502 conflict-resolver entry); auto-merge re-enabled (sha d7ca56f).

pr#501 (wiki(log): conflict-resolver 2026-08-05) rebased onto main; resolved wiki/log.md append conflict (daily research entries from PR #500 conflicting with prior conflict-resolver entry); SHA fc3d996; auto-merge confirmed active.

pr#500 (wiki(reports): daily 2026-08-05) rebased onto main; resolved wiki/log.md append conflict (daily research entries merged with conflict-resolver entry); SHA da7a214; auto-merge re-enabled.

## [2026-08-05] daily | 5 topics, 6 sources, ~14 pages

Daily Research 2026-08-05 complete. PRs #494–#498 created (auto-merge enabled; all CI green). Report: wiki/reports/2026-08-05.md.

## [2026-08-05] daily | games-of-note — 4 sources, 5 pages

Marathon Vault Breaker PvE triples player count; Quantic Dream strike over 115 layoffs; Paramount–WBD antitrust trial set March 2027. PR #498.

## [2026-08-05] daily | game-music — 1 source, 2 pages

Fire Emblem: Fortune's Weave 10-track Special Release on Nintendo Music; Sept 17 Switch 2 launch. PR #497.

## [2026-08-05] daily | agentic-coding — 1 source, 2 pages

Cursor Google Workspace Plugins: coding agents get Gmail, Drive, Calendar access. PR #496.

## [2026-08-05] daily | ai-in-game-dev — 0 sources, 1 pages

Null-sweep; no qualifying sources today. PR #495.

## [2026-08-05] daily | frontier-models — 0 sources, 0 pages

Null-sweep; leader picture unchanged (Opus 5 #1 AA II 61). PR #494.

## [2026-08-05] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#497 (wiki(game-music): daily 2026-08-05) requeued: CI passed (success at 09:42:52Z), auto-merge enabled via squash.

## [2026-08-04] daily | 5 topics, 7 sources, ~12 pages

Daily Research 2026-08-04 complete. PRs #488–#492 created (auto-merge enabled; all CI green). Report: wiki/reports/2026-08-04.md.

## [2026-08-04] daily | agentic-coding — 3 sources, 2 pages

Coding evaluation signal vs. noise (SWE-bench degraded); Codex AI Sites attach-app feature. PR #492.

## [2026-08-04] daily | game-music — 1 source, 1 page

Starbound 10th-anniversary 2xLP (Lost In Cult × Chucklefish × Schweitzer). PR #491.

## [2026-08-04] daily | games-of-note — 2 sources, 1 page

Beast of Reincarnation ships to mixed reception (73 Metacritic); Paramount–WBD deal frozen to June 2027. PR #490.

## [2026-08-04] daily | ai-in-game-dev — 0 sources, 1 pages

Null-sweep; no qualifying sources today. PR #489.

## [2026-08-04] daily | frontier-models — 1 source, 3 pages

Qwen3-8-Max analyzed; MiniMax H3 cross-referenced; leader picture stable. PR #488.

## [2026-08-03] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#482 (wiki(frontier-models): daily 2026-08-03) rebased onto main; resolved sources: frontmatter conflict on wiki/topics/ai-in-game-dev/index.md (took .their superset list adding [[minimaxai-minimax-h3-hugging-face-1f0e60fd]]); SHA 015272fa; CI green; auto-merged 10:28 UTC.

## [2026-07-29] daily | 5 topics, 9 sources, 11 pages

Daily Research 2026-07-29 complete. PRs #449–#453 merged. All 5 topics active. Report: wiki/reports/2026-07-29.md.

## [2026-07-29] daily | frontier-models — 2 sources, 3 pages

Poolside Laguna S 2.1 open-weight coding model beats rivals 10× its size on coding benchmarks; topic index updated.

## [2026-07-29] daily | ai-in-game-dev — 1 source, 2 pages

MAGIC: multi-agent LLM pipeline for transition-aware navigable multi-scene game world generation (Google DeepMind / KAIST).

## [2026-07-29] daily | games-of-note — 3 sources, 2 pages

Double Fine 23-person layoff post-Xbox divestiture; GoW Laufey dated Feb 16 2027; GTA 6 strongest pre-order campaign ever (Newzoo: 37–51M copies projected week-one).

## [2026-07-29] daily | game-music — 1 source, 2 pages

Gordy Haab releases first Star Wars: Zero Company track (1:17); full soundtrack due August 27.

## [2026-07-29] daily | agentic-coding — 2 sources, 2 pages

MCP 2026-07-28 FINAL published (stateless core, ttlMs/cacheScope required, Mcp-Session-Id removed); GitHub Copilot enterprise managed settings now govern cloud agent.

## [2026-07-28] daily | 5 topics, 12 sources, 18 pages

Daily Research 2026-07-28 complete. PRs #443–#447 merged. All 5 topics active. Report: wiki/reports/2026-07-28.md.

## [2026-07-28] daily | game-music — 1 source, 2 pages

GG Orchestra Herbst Theatre debut August 30, 2026 (SF); Sudo Choir; mixed game/anime programme (Genshin Impact, Dota 2, GTA, Zelda + anime). Open question: venue expansion signal.

## [2026-07-28] daily | games-of-note — 4 sources, 5 pages

Halo CE launch day: DualShockers 6.5/10 vs Push Square positive (PS5 framerate dispute, unresolved). ~20k Steam peak = 58.1% of Forza Horizon 6. SIGGRAPH 2026 Games Summit first dedicated track.

## [2026-07-28] daily | ai-in-game-dev — 3 sources, 4 pages

"From Pixels to States" (arXiv): pixel-prediction world models structurally inadequate as game engines (no explicit state). ManaMind €1.2M (86% bug catch rate). NodeMori Bug Hunter AI (LA).

## [2026-07-28] daily | frontier-models — 2 sources, 4 pages

Kimi K3 weights live: #1 LMArena Frontend Code Arena (1,679 Elo; first open-weights model beating closed flagships on blind preference axis). Qwen3.8-Max previewed (2.4T MoE, no benchmarks yet).

## [2026-07-28] daily | agentic-coding — 2 sources, 3 pages

MCP 2026-07-28 spec RC: stateless (removes initialize handshake, any request routable to any server). SDK betas: Python, TypeScript, Go, C#. GitHub MCP Server already implements new spec.

## [2026-07-27] daily | 5 topics, 7 sources, 8 pages

Daily Research 2026-07-27 complete. PRs #436–#440 merged. All 5 topics active. Report: wiki/reports/2026-07-27.md.

## [2026-07-27] daily | games-of-note — 0 sources, 1 page

No new articles in scope today. Bumped last_updated; added open question on Halo Campaign Evolved July 28 launch and whether lowest-rated-Halo tracking changes the Xbox reset narrative. PR #440.

## [2026-07-27] daily | agentic-coding — 3 sources, 3 pages

Three harness-evolution papers converge on a methodological critique: (a) 35 sequential harness releases show no statistically significant quality gain with model fixed ("Don't Blame the LLM"); (b) in-distribution evaluation overfits and doesn't consistently beat TTS ("Rethinking"); (c) gated QD framework (proposal separated from deterministic crediting) achieves +9–15.5 pp sealed-test gains across 7 domains. Cross-page sweep: harness-engineering.md, agent-harnesses.md. PR #439.

## [2026-07-27] daily | frontier-models — 1 source, 2 pages

Kimi K3 open weights confirmed landed July 27 as scheduled. MXFP4 QAT release: 2.8T parameters, ~1.4 TB, native Blackwell/MI400 support, leads SWE Marathon + Program Bench. GDPval ELO 1,668–1,687 (source discrepancy filed). kimi-k3 entity updated. PR #438.

## [2026-07-27] daily | ai-in-game-dev — 1 source, 1 page

Roblox Build (mobile AI game creation) entering New Zealand public alpha July 28, sharing back end with Roblox Studio. Open question on mobile-vs-desktop capability parity filed. PR #437.

## [2026-07-27] daily | game-music — 2 sources, 1 page

For Honor 10th-anniversary 2xLP vinyl (Kid Katana × Ubisoft, August 2026 estimate) and Akira Yamaoka confirmed at Heroes: A Video Game Symphony Toronto. PR #436.

## [2026-07-26] daily | 5 topics, 7 sources, 12 pages

Daily Research 2026-07-26 complete. PRs #430–#434 merged. All 5 topics active. Report: wiki/reports/2026-07-26.md.

## [2026-07-26] daily | game-music — 1 source, 1 page

Wall of Sound AU review of Halo: Campaign Evolved remake: O'Donnell/Salvatori score "faithfully remastered" — craft-reception data point engaging existing Halo multitrack dispute. PR #434.

## [2026-07-26] daily | games-of-note — 1 source, 2 pages

Marathon game director Joe Ziegler departs July 17 (3rd director exit in 2 years); Del Chafe III takes over. Steam concurrents: 88,337 peak → ~6,775 current, below 1,000 on multiple days — approaching matchmaking-degradation threshold. Bungie entity updated. PR #433.

## [2026-07-26] daily | ai-in-game-dev — 2 sources, 1 page

DLSS 5 announced: pixel-deterministic AI supersampling (SIGGRAPH reveal). Developers learned about DLSS 5 at the same time as the public — partner communication failure. PR #432.

## [2026-07-26] daily | frontier-models — 2 sources, 5 pages

Opus 5 AA Intelligence Index confirmed 61 (up from 58) and gdpval_aa_elo 1861 — now #1 aggregate leader, overtaking Fable 5 (60). Summary regenerated. 1 new dispute (61 vs prior 60 claim). PR #431.

## [2026-07-26] daily | agentic-coding — 1 source, 3 pages

IssueTrojanBench: 66.5% of malicious GitHub issues bypass all guardrails (LLM + harness) across Cursor, Claude Code, and Codex Desktop as shipped. First cross-product as-deployed penetration benchmark. Cross-page sweep: agent-sandboxing.md, sandboxing.md. PR #430.

## [2026-07-25] daily | 5 topics, 13 sources, 13 pages

Daily Research 2026-07-25 complete. PRs #423–#427 merged. Report: wiki/reports/2026-07-25.md.

## [2026-07-25] daily | agentic-coding — 2 sources, 4 pages

Claude Code What's New Week 30 (July 21–25): custom MCP server cert authorities, AI review in Pull Requests, per-file token budgets; Cursor Router v1.0: dynamic model routing per file/region with user-definable cost–quality profiles, supports Claude Code + Cursor SDK. PR #423.

## [2026-07-25] daily | frontier-models — 3 sources, 6 pages

Claude Opus 5 ships July 24: new Anthropic standard flagship ($5/$25 per Mtoken), tops Fable 5 on most benchmarks at half the token price; AA Intelligence Index 58, SWE-bench verified 0.939, CyberGym 0.831. Entity [[claude-opus-5]] created. Summary regenerated. PR #424.

## [2026-07-25] daily | ai-in-game-dev — 1 source, 1 page

Godot AI Assistant Hub (v1.0): open-source engine-native gateway embedding local LLMs (Ollama/llama.cpp) directly in Godot editor; supports in-scene NPC script generation, asset naming, and shader assist with zero-cloud option. PR #425.

## [2026-07-25] daily | games-of-note — 5 sources, 1 page

Halo: CE Campaign Evolved tracking at 81 Metacritic (lowest-rated Halo, PC bugs, always-online, first PlayStation appearance); EA $55B acquisition EU approved July 23 (FSR pending July 30); Rockstar RGWU voluntary recognition request 4 months before GTA 6; Ubisoft Q1 FY2026-27 €255.8M net bookings (−9.2% YoY); Palworld 1.0 launched with ~30.5M copies sold. PR #426.

## [2026-07-25] daily | game-music — 2 sources, 1 page

Splatoon Raiders (9-track) added to Nintendo Music as special release (NSO required, July 23); Forza Horizon 6 × Hospital Records DnB 3LP pink gatefold vinyl (24 tracks, £26.99, August 7). PR #427.

## [2026-07-24] daily | 5 topics, 14 sources, 16 pages

Daily Research 2026-07-24 complete. PRs #417–#421 merged. Report: wiki/reports/2026-07-24.md.

## [2026-07-24] daily | agentic-coding — 3 sources, 6 pages

AgentLens (arXiv 2607.06624): trajectory-level evaluation pairing formal verification + LLM narrative reviews for coding agents; useful for nightly regression pipelines. Benchmark-reliability audit (arXiv 2607.01211): GSO/SWE-Perf/SWE-fficiency fail cross-machine replay (39/102, 11/140, 411/498 tasks pass) and disagree on 9/28 pairwise submission rankings. Failure as a Process (arXiv 2607.09510): first large-scale anatomy of CLI coding-agent failures across 3,843 trajectories from 7 frontier models × 3 scaffolds (OpenHands, MiniSWE, Terminus2). PR #417.

## [2026-07-24] daily | frontier-models — 3 sources, 5 pages

Kimi K3: first open 3T-class MoE (896 experts, 16 active, Kimi Delta Attention + AttnRes), ~2.5× scaling efficiency vs K2, 1M context, native multimodal — new open-weights frontier leader. Open weights drop July 27; full-precision 1.4 TB (BF16 ~594 GB; Q4 quant ~310 GB). Modified MIT license. PR #418.

## [2026-07-24] daily | ai-in-game-dev — 2 sources, 3 pages

AlayaWorld (arXiv 2607.06291): first Apache 2.0 player-interactive world model (15B params, DMD 4-step distillation, 100-step horizon); enables real-time player control of generated video environments. OmniGameArena (arXiv 2606.09826): 12-game UE5 VLM benchmark with Improvement Dynamics Curve (IDC) metric; commercial models lead, reflection capability peaks mid-training. PR #419.

## [2026-07-24] daily | game-music — 3 sources, 1 page

Resonance: A Plague Tale Legacy (Olivier Derivière, Amalgamation choir + Yaylı tambur, Aug 27 2026); UNBEATABLE 3xLP vinyl (iam8bit, D-CELL Sound Team, $60, Q4 2026); Dolphin Park LP — Wave Race 64 jazz-fusion rework (Mana Wave, 500 copies ocean-blue vinyl, $30). PR #420.

## [2026-07-24] daily | games-of-note — 3 sources, 1 page

The Duskbloods Network Test (FromSoftware, Switch 2 PvPvE, 5 sessions Aug 21–23, 8 players/session); Q2 2026 M&A $2.3 bn across 54 transactions — post-pandemic high; Scopely $1 bn Loom Games. Vermila Studios (Crisol) lays off 19 staff 5 months after positive-reviewed PS5/PC/XSX launch — full closure "feasible". PR #421.

## [2026-07-21] daily | 5 topics, 5 sources, 13 pages

Daily Research 2026-07-21 complete. PRs #399–#403 queued for auto-merge. Report: wiki/reports/2026-07-21.md.

## [2026-07-21] daily | frontier-models — 0 sources, 4 pages

Quiet day: no new sources met the bar. Leader picture re-confirmed: Fable 5 (AA Index 60) > Opus 4.8 (56) > GPT-5.5 (55). Bumped last_verified on claude-fable-5, claude-opus-4.8, gpt-5.5. PR #399.

## [2026-07-21] daily | game-music — 0 sources, 1 page

Quiet day: no new sources crossed the ingestion bar. Vinyl-revival, AI-composer debate, and live-concert circuit threads remain current as of the 2026-07-19 entry. PR #400.

## [2026-07-21] daily | games-of-note — 3 sources, 4 pages

id Software: two-thirds of remaining Doom 2016 devs laid off (Hugo Martin "minimal impact" claim disputed by sources); Todd Howard confirms Bethesda-Obsidian Fallout collaboration; Netflix FIFA World Cup cloud game was a top-tier debut despite critical panning. PR #401.

## [2026-07-21] daily | ai-in-game-dev — 1 source, 2 pages

SimWorlds (CMU/Harvard/UC Merced, arXiv 2607.01766): multi-agent planner-coder-reviewer framework for dynamic 4D scene generation from text with deterministic verifier; introduces 4DBuildBench. PR #402.

## [2026-07-21] daily | agentic-coding — 1 source, 2 pages

The Harness Effect (arXiv 2607.06906): orchestration design cut cost 41%, wall-clock 44%, tokens 38% vs. model-invariant baseline across 22 enterprise tasks × 6 models × 5 vendors — harness effect dominates the full model-menu spread. PR #403.

## [2026-07-20] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#396 (claude/daily-2026-07-20/_report): CI in progress at scan time, auto-merge proactively enabled via MCP to prevent orphan-CLEAN state on CI pass.

## [2026-07-15] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#370 rebased onto main; resolved 1 conflict on wiki/log.md (chronological union); auto-merge re-queued

## [2026-07-15] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 1 failed

pr#366 (agentic-coding): rebase dispatch failed — force-push rejected (concurrent update 662b3ed→62183b6; --force-with-lease refused). Rebase resolved 4 conflicts locally (lint 0 errors) but not pushed. Requeued via MCP enable_pr_auto_merge; PR merged as 566709d.

## [2026-07-15] daily | 5 topics, 10 sources, 18 pages

Daily Research 2026-07-15 complete. PRs #364–#368 merged. Report: wiki/reports/2026-07-15.md.

## [2026-07-15] daily | frontier-models — 0 sources, 4 pages

Quiet window July 13–15: no new sources met the quality bar. Leader picture re-confirmed unchanged: Fable 5 (AA Index 60) > GPT-5.6 Sol (59) > Opus 4.8 (56) > GPT-5.5 (55) > Grok 4.5 (54); GLM-5.2 (51) open-weights #1. Bumped last_verified on claude-fable-5, claude-opus-4.8, gpt-5.5 (was stale since July 8). PR #364.

## [2026-07-15] daily | ai-in-game-dev — 2 sources, 3 pages

RigEL3D (arXiv): rig-aware latents enable animation-ready 3D asset generation preserving semantic rig structure. Unity survey: 79% of developers positive on generative AI (up from prior surveys). PR #365.

## [2026-07-15] daily | agentic-coding — 3 sources, 4 pages

PERFOPT-Bench: first benchmark evaluating coding agents on software performance optimization (algorithmic + hardware efficiency tasks). Cheap Code Costly Judgment: governable agentic software engineering — identifies governance vs. no-code-review tension as a structural risk. Datasette code-frequency chart on GitHub. PR #366.

## [2026-07-15] daily | game-music — 1 source, 2 pages

Persona 3 Reload Original Soundtrack music review (RPGFan): praised for emotional depth and faithfulness to Persona 3's themes, though rock-direction departure noted. PR #367.

## [2026-07-15] daily | games-of-note — 4 sources, 5 pages

Xbox Positron disc-to-digital teaser; AC Black Flag Remake launch-day layoffs at Ubisoft Barcelona; Save Our Devs march at Xbox HQ on July 15; Zeverland (DayZ rival) pivoting to PvE before launch. PR #368.

## [2026-07-12] health | weekly sweep — 3 disputes filed

Weekly health sweep 2026-07-12. 12 candidate sets (11 source-triggered + 1 stale sweep), 6 scanner passes. 3 new disputes filed: claude-fable-5 AA Index version discrepancy (64.9 v4.0 vs 60 v4.1); claude-fable-5 GDPval-AA version discrepancy (1932 original vs 1818 v2); deepseek-v4 AA Index version discrepancy (52 v4.0 vs 44 v4.1). Lint: 0 errors, 202 warnings. 10 stale synthesis pages. PR #345.

## [2026-07-12] daily | 5 topics, 8 sources, 18 pages

Daily Research 2026-07-12 complete. PRs #346–#350 merged. Key stories: Bun-in-Rust LLM port at ~$165k API cost + Cursor 3.11 cloud-agent lifecycle hooks + arXiv SoK on 39 execution-security failure papers (agentic-coding); IvanMurzak engine-agnostic GameDev-MCP-Server unifying Unity/Godot/Unreal via SignalR + Godot-MCP C# addon submitted to Asset Library (ai-in-game-dev); Palworld 1.0 ~500k concurrent Steam + 72 new Pals + visual reworks + Xbox accessibility team decimated in Reset (games-of-note). Report: wiki/reports/2026-07-12.md.

## [2026-07-12] daily | agentic-coding — 3 sources, 9 pages

Simon Willison: Bun-in-Rust LLM port ~$165k at API prices (5.9B uncached + 690M output + 72B cached-read tokens, 11 days, human monitors). Cursor 3.11: cloud-agent lifecycle hooks (beforeSubmitPrompt, afterAgentResponse, afterAgentThought, stop, subagentStart). arXiv 2607.05743 SoK: 39 papers, 17 execution-security failure categories (TOCTOU races, identity delegation, execution provenance). 1 new dispute, 3 new open questions. Report: wiki/reports/2026-07-12.md.

## [2026-07-12] daily | frontier-models — 0 sources, 1 page

Quiet day — no new frontier-model sources. Topic index bumped. Report: wiki/reports/2026-07-12.md.

## [2026-07-12] daily | ai-in-game-dev — 2 sources, 3 pages

IvanMurzak engine-agnostic GameDev-MCP-Server unifies Unity-MCP, Godot-MCP, Unreal-MCP via single SignalR backend; requires C#/.NET Godot 4.3+ (excludes GDScript-only projects); Unreal plugin at v0.1.x unvalidated. Godot-MCP C# editor addon submitted to Godot Asset Library. 2 new open questions. Report: wiki/reports/2026-07-12.md.

## [2026-07-12] daily | games-of-note — 3 sources, 4 pages

Palworld 1.0 launches with ~500k concurrent Steam (96% positive), 72 new Pals (287 total), Sunreach region, Mutations mechanic, player cap 65→80; Pal visual reworks hedge design-litigation risk vs Nintendo. Xbox Reset: Bethesda User Research Team decimated, Zach Clothier (accessibility test lead) departed. 2 new open questions. Report: wiki/reports/2026-07-12.md.

## [2026-07-12] daily | game-music — 0 sources, 1 page

Quiet day — Sakimoto 40th-anniversary concert + Ivors Awards already written up in June 2026 entries; no new sources. Topic index bumped. Report: wiki/reports/2026-07-12.md.

## [2026-07-10] daily | game-music — 2 sources, 1 page

Nintendo Music adds F-Zero SNES + F-Zero X Expansion Kit (64DD) for Switch Online subscribers; July vinyl picks from Black Screen Records (BPM: Bullets Per Minute), Mana Wave (Chrono Trigger EP), and Death's Gambit: Afterlife. Report: wiki/reports/2026-07-10.md.

## [2026-07-10] daily | games-of-note — 5 sources, 1 page

136 id Software layoffs confirmed via WARN Act (~50% of studio); 165/185 id Software employees form wall-to-wall CWA union with AI guardrails named as contract target; Palworld 1.0 launches today with 40M players milestone; Rockstar labor report (opt-out crunch in employment contracts, widened gender pay gap); AC Black Flag Resynced earns "high bar for legacy revival" from Game Informer. Report: wiki/reports/2026-07-10.md.

## [2026-07-10] daily | ai-in-game-dev — 1 source, 1 page

Fortnite UEFN Conversations (Experimental) enables AI-driven NPC voice dialogue via Gemini 3.1 Flash-Lite + ElevenLabs; developers define persona via prompts, not yet publishable on public islands. Report: wiki/reports/2026-07-10.md.

## [2026-07-10] daily | frontier-models — 4 sources, 10 pages

GPT-5.6 Sol (AA Intelligence Index 59, Coding Agent Index 80, $5/$30/Mtoken) and Grok 4.5 (AA Index 54, Grok Build $2.49/task) both launch; new entity pages created; comparison tables updated; Claude Fable 5 (AA Index 60) re-verified as overall leader. Report: wiki/reports/2026-07-10.md.

## [2026-07-10] daily | agentic-coding — 2 sources, 7 pages

GPT-5.6 API-native Multi-agent (parallel subagent tool calls) and Programmatic Tool Calling (V8 sandbox, structured JSON function-calling) expand the harness-vs-model boundary debate; 4 concept pages updated (parallel-subagents, agent-harnesses, harness-engineering, agent-sandboxing). Report: wiki/reports/2026-07-10.md.

## [2026-07-07] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#328 kind=rebase resolved=true sha=cdd3b0e — rebased claude/daily-2026-07-07/games-of-note onto main; resolved 4 conflicts in wiki/topics/games-of-note/index.md (frontmatter merge, Summary paragraphs, Labor/genAI section superset from HEAD, Recent Updates append-at-top with 2026-07-07 first); force-pushed and re-queued auto-merge.

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

pr#124 (games-of-note) lint_fix dispatch: lint already green at dispatch time (broken-wikilink [[round-up-the-reviews-are-in-for-final-fantasy-vii-rebirth-on-switch-2-647b3fa5]] resolved after PR #125 merged); auto-merge re-enabled via MCP. pr#126 (ai-in-game-dev): already merged when CI completed.

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

## [2026-07-04] daily | agentic-coding — 2 sources, 4 pages

DuneSlide: CVE-2026-50548 + CVE-2026-50549 (CVSS 9.8), zero-click RCE via prompt injection in Cursor IDE terminal sandbox, patched in Cursor 3.0; Copilot agent session streaming (prompts, tool calls, responses) to SIEM/Purview now in public preview. PR #309.

## [2026-07-04] daily | frontier-models — 0 sources, 1 page

Quiet day. July 3 picture holds: Fable 5 (AA v4.1 = 60) leads publicly-accessible frontier; GLM-5.2 holds open-weights #1. PR #310.

## [2026-07-04] daily | ai-in-game-dev — 0 sources, 1 page

Quiet day. No new notable sources in scope. PR #311.

## [2026-07-04] daily | game-music — 2 sources, 3 pages

Caves of Qud 3LP vinyl pre-order (Stumpy Frog Records × Saint Vulture, 2+ hours atmospheric OST); Death Stranding composer Ludvig Forssell + Chad Seiter adapting ambient/synth score for orchestra. PR #312.

## [2026-07-04] daily | games-of-note — 5 sources, 6 pages

Physical media end-of-life crystallizes: Sony halts all PlayStation disc production from January 2028 (80% digital by 2025); PS6 + Xbox Project Helix projected digital-only at 2028 launch (analyst forecast); GTA 6 confirmed disc-free — not at launch, not months after; ex-Xbox workers warn of retaliation in July 6 layoffs (>1,000 roles). PRs #313 + #314 (summary regen).

## [2026-07-04] daily | 5 topics, 9 sources, 15 pages

Physical disc death crystallizes (Sony Jan 2028 halt; GTA 6 disc-free confirmed; PS6/Project Helix digital-only forecast). DuneSlide CVEs (CVSS 9.8) in Cursor IDE patched in Cursor 3.0; Copilot enterprise session streaming GA. Caves of Qud vinyl + Death Stranding concert arrangement (game-music). Frontier-models + ai-in-game-dev quiet.

## [2026-07-05] health | weekly sweep

Weekly health sweep 2026-07-05. 19 candidate sets (18 source-triggered + 1 stale sweep), 5 scanner passes. 3 new disputes filed: Kimi K2.6 AA index version inconsistency (v4.0=54 vs v4.1=43); Qwen3.7 Max open-weights vs. closed-weights claim; GPT-5.5 score inconsistency (body claims 60 on v4.0, frontmatter records 55 on v4.1). Lint: 0 errors, 180 warnings. 10 stale synthesis pages. PR follows.

## [2026-07-06] daily | games-of-note — 5 sources, 6 pages

Xbox 3,200 layoffs officially confirmed (largest single layoff in gaming per George Broussard). Studio fates: Ninja Theory + Undead Labs sold; Compulsion + Double Fine returned as independents; Arkane Lyon in Works Council consultation. IO Interactive loses Xbox as Project Fantasy partner despite 007 First Light's 3M-copy launch. PR #318.

## [2026-07-06] daily | ai-in-game-dev — 0 sources, 1 page

Quiet day. No new in-scope sources met the quality bar. Current-state picture unchanged. PR #319.

## [2026-07-06] daily | game-music — 2 sources, 3 pages

Wuthering Waves Concert Tour: To the New World to Peacock Theater, LA, Oct 17, 2026 (first North American stop; all prior legs sold out). Rain World: The Watcher 54-track 2LP Pearl Dawn vinyl via Black Screen Records, 39 euro, July 2026. PR #320.

## [2026-07-06] daily | agentic-coding — 1 source, 3 pages

"Code Isn't Memory" (arXiv 2606.22417, SuperAGI Research): structural codebase index yields statistically-separated resolve-rate gain at no cost penalty (lower $/solve than agentic grep), creating direct tension with ContextBench's Bitter Lesson framing. 1 dispute filed; 2 open questions. PR #321.

## [2026-07-06] daily | frontier-models — 0 sources, 1 page

Quiet day. No new notable sources met the quality bar. July 3 leader picture holds: Fable 5 (AA v4.1 = 60) leads; GLM-5.2 (51) holds open-weights #1. 2 open questions filed: Sakana Fugu Ultra SWE-bench Pro claim; White House voluntary frontier-model-release standards. PR #322.

## [2026-07-06] daily | 5 topics, 8 sources, 14 pages

Xbox 3,200 layoffs confirmed — studio fates clearer (sales/independence, not closures for most). "Code Isn't Memory" — structural codebase index beats agentic grep at no cost penalty. Wuthering Waves NA concert + Rain World vinyl. Frontier-models + ai-in-game-dev quiet.

## [2026-07-07] daily | frontier-models — 0 sources, 1 page

Quiet day. No new sources met the quality bar. July 6 leader picture holds: Fable 5 (AA v4.1 = 60) leads; GLM-5.2 (51) holds open-weights #1. PR #324.

## [2026-07-07] daily | agentic-coding — 2 sources, 4 pages

"Better Models: Worse Tools" (Simon Willison / Armin Ronacher): newer Anthropic models regress on third-party edit-tool schemas, theorized as RL co-adaptation to Claude Code's native tools. sqlite-utils 4.0rc2 cost data point: ~$149.25 via Claude Fable 5, five release blockers surfaced. 1 dispute filed; 2 open questions. PR #325.

## [2026-07-07] daily | ai-in-game-dev — 1 source, 1 page

NVIDIA developer Q&A: first detailed engineering breakdown of PUBG Ally's CPC pipeline (on-device ASR + 2B-parameter SLM + TTS, behavior-tree for fast actions, structured cross-session memory). 2 open questions. PR #326.

## [2026-07-07] daily | game-music — 1 source, 1 page

Frostpunk 2 Full Original Soundtrack 2xLP announced: Black Screen Records + 11 bit studios, gold and black vinyl, gold embossed gatefold, shipping July 2026. First complete LP release of Piotr Musial's TGA 2024 Best Strategy/Sim Game score. PR #327.

## [2026-07-07] daily | games-of-note — 6 sources, 7 pages

Xbox Reset studio-level figures confirmed: id Software lost 95 jobs, Bethesda Game Studios 35, ZeniMax Online (ESO) ~50%, Obsidian ~60–70 (~¼ staff). Ninja Theory + Undead Labs sold to undisclosed buyers; Senua's Saga and State of Decay 3 committed. Arkane co-founder Colantonio publicly floats buyout interest. 2 disputes filed; 4 open questions. PR #328.

## [2026-07-07] daily | 5 topics, 10 sources, 14 pages

Xbox Reset studio-level confirmed: id Software 95, Bethesda 35, ESO ~50%, Obsidian ~60–70. Ninja Theory + Undead Labs sold (mystery buyers). RL co-adaptation regression in third-party tools. PUBG Ally engineering pipeline detail. Frostpunk 2 vinyl. Frontier-models quiet.

## [2026-07-08] daily | games-of-note — 3 sources, 5 pages

Xbox Reset studio-fate firmed: Double Fine + Compulsion independent (full IP + team runway); Ninja Theory + Undead Labs signed to new mystery owners; Arkane Lyon in Works Council consultation (possible closure). DOOM: Dark Ages — Revelations DLC launches same day id Software lost ~half its staff.

## [2026-07-08] daily | agentic-coding — 3 sources, 6 pages

Latent Programming Horizons (KTH/Monperrus): residual-stream probe predicts coding-agent correctness at AUC 0.83 before execution. Willison's "Fable's judgement": route implementation tasks to cheaper subagent as default; reserve frontier model for judgment. TestEvo-Bench: live leakage-gated Java benchmark, SOTA 77.5%.

## [2026-07-08] daily | frontier-models — 1 source, 8 pages

Sakana Fugu/Fugu-Ultra ingested (vendor-reported SWE-bench Pro SOTA, multi-agent orchestrator architecture); leader picture re-confirmed: Fable 5 (AA=60), Opus 4.8 (56), GPT-5.5 (55); cost and benchmark comparison pages regenerated. Claims not yet independently verified.

## [2026-07-08] daily | ai-in-game-dev — 1 source, 2 pages

AI Native Games survey (arXiv:2607.00527): counterfactual definition of AI-native games (runtime AI constitutive of core loop), G/N taxonomy over 53 prototypes; corpus gap in companion-play and multi-agent-simulation quadrants identified.

## [2026-07-08] daily | game-music — 1 source, 2 pages

FINAL FANTASY RESONANCE (Oct 22, 2026): Elements Garden/Noriyasu Agematsu scoring, 33 new tracks plus Brave Exvius carry-overs, 120-track CD in collector's edition; Square Enix released multiple soundtrack samples.

## [2026-07-08] daily | 5 topics, 9 sources, 23 pages

Daily Research 2026-07-08 complete. PRs #331–#335. Key stories: Xbox Reset studio fate firmed (games-of-note); latent-horizon probe AUC 0.83 + Willison's subagent-routing pattern (agentic-coding); Sakana Fugu orchestrator ingested, leaders re-confirmed (frontier-models); AI Native Games counterfactual taxonomy (ai-in-game-dev); FF Resonance Elements Garden score (game-music). Report: wiki/reports/2026-07-08.md.

## [2026-07-13] daily | agentic-coding — 2 sources, 5 pages

Claude Code Artifacts: session-native live web page (private claude.ai URL) as async oversight surface. Auto mode v2.1.205: transcript-write block + unresolved-variable rm -rf guard — closes one poisoning vector but classifier remains subject to tool-output injection.

## [2026-07-13] daily | frontier-models — 2 sources, 4 pages

Meta Muse Spark 1.1: first paid-API frontier model, 1M-token context, $1.25/$4.25 per Mtoken; AA Index v4.1 = 51 (tied with GLM-5.2, GPT-5.4, GPT-5.6 Luna, 3 pts behind Grok 4.5). Leader picture unchanged at top: Fable 5 (60) > GPT-5.6 Sol (59) > Opus 4.8 (56). Summary regenerated.

## [2026-07-13] daily | ai-in-game-dev — 1 source, 2 pages

DreamCharacter-1 (arXiv:2607.07817): post-adaptation framework (geometry + texture + acceleration) on pretrained 3D foundation models for production-ready character generation; no open-weight release confirmed, engine-ready rig validation pending.

## [2026-07-13] daily | games-of-note — 2 sources, 3 pages

Obsidian cancels Avowed sequel, pivots to Josh Sawyer-led Fallout game (Bethesda co-developing; CA WARN: 52 layoffs) — first named Xbox Reset cancellation, in tension with Microsoft's "no publicly announced games cancelled" line. AC Black Flag Resynced: 2M day-one copies, 99,451 Steam concurrent AC record, ~84 MC. Summary regenerated.

## [2026-07-13] daily | game-music — 1 source, 1 page

RPGFan first-hand recap: Sakimoto 40th-anniversary Colors of Harmony concert (13 June 2026, Fairfield Halls, Croydon) — London Mozart Players, FF XII + FFT halves, voice-cast Q&A, 45-min interview.

## [2026-07-13] daily | 5 topics, 8 sources, 14 pages

Daily Research 2026-07-13 complete. PRs #352–#356. Key stories: Meta Muse Spark 1.1 API launch at AA Index 51 (frontier-models); Obsidian cancels Avowed sequel, pivots to Sawyer-led Fallout (games-of-note); AC Black Flag Resynced 2M day-one + AC Steam record (games-of-note); auto mode transcript-write block / Artifacts observability surface (agentic-coding); DreamCharacter-1 character-refinement post-adapter (ai-in-game-dev); Sakimoto concert recap (game-music). Report: wiki/reports/2026-07-13.md.

## [2026-07-14] daily | agentic-coding — 2 sources, 4 pages

TRACEPROBE (arXiv 2607.06184): deterministic nine-type trajectory diagnostics + INSIGHT anti-patterns + CONVERGE pairwise divergence, applied to 2,500 SWE-Bench Verified trajectories — resolve-rate monoculture critique. ChainSWE (arXiv 2607.02606): first no-reset sequential-dependent bug benchmark (304 issues, 54 projects), up to 70% performance degradation as chain grows.

## [2026-07-14] daily | frontier-models — 1 source, 4 pages

SWE-1.7 (Cognition, July 8): RL on Kimi K2.7 Code open-weight base; vendor-reported Terminal-Bench 2.1 81.5% / SWE-Bench Multilingual 77.8% / FrontierCode 1.1 Main 42.3%; ~$1.97/task via Cerebras. Leaders unchanged: Fable 5 (60) > GPT-5.6 Sol (59) > Opus 4.8 (56). Fable 5 + Opus 4.8 freshness bumped.

## [2026-07-14] daily | ai-in-game-dev — 1 source, 2 pages

GameEngineBench (arXiv 2607.03525): scoped C++ implementation tasks in 9 real Unreal Engine 5 game repos (110 tasks); strongest of 12 configurations reaches 55.5% pass@1; 31 tasks unsolved by all; engine-native Play-in-Editor automation + behavior-judge harness.

## [2026-07-14] daily | game-music — 1 source, 2 pages

Nintendo Music July 13 update: additional Mario Kart World 'Free Roam' songs added (Mario Paint, NSMB, NSMB Wii, NSMB U, Super Mario Maker) — continues weekly rollout since early June 2026 when album was first added.

## [2026-07-14] daily | games-of-note — 4 sources, 5 pages

Meccha Chameleon: 15M copies in <1 month, $5.99 two-person indie, 2026 fastest- and best-selling game (supersedes ~3M earlier). Palworld 1.0: free update, 855K concurrent Steam peak, all-time top-15 spot (first title with two top-15 entries; 40M lifetime). Save Our Devs rally July 15: Bethesda/ZeniMax OneBGS union (Rockville, Austin, Dallas, Montreal; 440 positions eliminated). Summary regenerated.

## [2026-07-14] daily | 5 topics, 9 sources, 17 pages

Daily Research 2026-07-14 complete. PRs #358–#362. Key stories: Meccha Chameleon 15M copies in <1 month (games-of-note commercial leader); Palworld 1.0 855K Steam concurrent peak / all-time top-15 (games-of-note); Save Our Devs rally July 15 — Bethesda/ZeniMax union action (games-of-note); TRACEPROBE trajectory diagnostics + ChainSWE chain-degradation benchmark (agentic-coding); SWE-1.7 RL-on-Kimi-K2.7 Code at $1.97/task (frontier-models); GameEngineBench 55.5% pass@1 in UE5 (ai-in-game-dev); Nintendo Music MKW Free Roam update (game-music). Report: wiki/reports/2026-07-14.md.

## [2026-07-16] daily | frontier-models — 2 sources, 5 pages

Thinking Machines Inkling (975B total / 41B active MoE, 1M context, AA Intelligence Index v4.1 = 41) displaces Nemotron Ultra as US-hosted open-weights leader. New entity page: wiki/entities/inkling.md. PRs: #372.

## [2026-07-17] daily | 4 topics, 7 sources, 7 pages

Daily Research 2026-07-17 complete. PRs #379–#382 (game-music: no new sources). Key stories: Grok Build open-sourced under Apache 2 with upload/gcs.rs path still present (unresolved privacy dispute) + Codex $HOME-deletion case study (agentic-coding, PR #379); Kimi K3 enters closed-frontier cluster at AA v4.1 = 57 (rank 4, above Opus 4.8) — $3/$15 pricing, 130M tokens/task verbosity caveat (frontier-models, PR #381); Roblox Build public alpha scene-generation model launching New Zealand July 28 (ai-in-game-dev, PR #380); IWGB protest at Build a Rocket Boy + Kotaku labor-visibility analysis — coordinated public action pattern generalizing beyond Xbox (games-of-note, PR #382). Report: wiki/reports/2026-07-17.md.

## [2026-07-17] daily | games-of-note — 2 sources, 1 page

IWGB protesters picket Build a Rocket Boy's Leith HQ during all-expenses-paid fan playtest (400+ laid off since MindsEye launch); Kotaku: ZeniMax/Bethesda rallies signal studios can no longer quietly conduct mass layoffs — coordinated public-protest pattern generalizing beyond Xbox union footprint. PRs: #382.

## [2026-07-17] daily | frontier-models — 1 source, 4 pages

Kimi K3 (Moonshot AI, proprietary closed, 2.8T params) enters AA Intelligence Index v4.1 at 57 — ranked 4th (behind Fable 5 at 60, GPT-5.6 Sol max at 59, Sol xhigh at 58), one point above Opus 4.8; $3/$15 per Mtoken; 130M output tokens/task (2× avg), 62 tok/sec (slower than 70 avg). New entity page kimi-k3.md; Summary regenerated. PRs: #381.

## [2026-07-17] daily | ai-in-game-dev — 1 source, 1 page

Roblox Build: new scene-generation model builds entire editable and playable 3D scenes from a single prompt (gameplay mechanics, environment, characters, visual style, sound). Public alpha New Zealand July 28 for age-checked users 9+; extends Cube/CubePart thread already on page. PRs: #380.

## [2026-07-17] daily | agentic-coding — 3 sources, 1 page

Grok Build open-sourced (Apache 2) with upload/gcs.rs working-directory-upload path still present (disabled, not removed) — unresolved privacy dispute; Codex full-access run deleted $HOME contents (data point for mandatory-sandboxing debate). PRs: #379.

## [2026-07-16] daily | agentic-coding — 4 sources, 8 pages

DeepSWE contamination-free benchmark: 1.4% LLM-judge disagreement vs 32.4% for SWE-Bench Pro; MOSAIC CLI command-composition attack at 96.6% success rate across 5 agents; Microsoft enterprise study +24% PR-merge lift; Isolation SoK frames isolation as unifying safety principle. 4 concept pages updated (agent-sandboxing, harness-engineering, agent-harnesses). Summary regenerated. PRs: #373.

## [2026-07-16] daily | games-of-note — 2 sources, 3 pages

Denshattack! (MC 88 / OpenCritic Mighty 87, day-one Game Pass); July 15 'Save Our Devs' multi-city march materializes — first coordinated multi-studio labor action in gaming history (6 Xbox locations, 4 cities). PRs: #374.

## [2026-07-16] daily | game-music — 3 sources, 4 pages

Denshattack! OST: Tee Lopes + all-star VGM guest bench (Meguro, Jacques, Mitsuyoshi, Fujita, 2 Mello, Ironmouse), 80+ tracks via Kid Katana Records; Crash Bandicoot 4 Walter Mair score finally hits streaming 6 years post-launch; Outer Worlds 2 faction-structured 3LP via Laced Records (Lozowchuk/Gradanti/Bonney), $62. PRs: #375.

## [2026-07-16] daily | ai-in-game-dev — 2 sources, 3 pages

GUI Agents for Continual Game Generation: PlaytestArena (200 browser-based tasks, GUI-agent adjudicator) + Play2Code achieving 66.8% rubric pass-rate via play-driven iteration loop; PlayCoder: near-zero Play@3 across 10 SOTA LLMs despite high compile rates. PRs: #376.

## [2026-07-16] daily | 5 topics, 13 sources, 23 pages

Daily Research 2026-07-16 complete. PRs #372–#376. Key stories: Inkling displaces Nemotron Ultra as US open-weights leader (frontier-models); DeepSWE contamination-free eval + MOSAIC 96.6% CLI attack + Microsoft +24% PR-merge lift (agentic-coding); 'Save Our Devs' multi-city march + Denshattack! MC 88 (games-of-note); Denshattack! all-star VGM OST + Outer Worlds 2 3LP (game-music); Play2Code 66.8% play-driven game-gen + PlayCoder near-zero Play@3 (ai-in-game-dev). Report: wiki/reports/2026-07-16.md.

## [2026-07-19] health | weekly sweep — 1 dispute filed

Weekly health sweep 2026-07-19. 13 candidate sets (12 source-triggered + 1 stale sweep). 1 new dispute filed: Muse Spark 1.0 AA Index version ambiguity (52 on v4.0 vs 43 on v4.1). Lint: 0 errors, 212 warnings. 6 stale synthesis pages. PR #386.

## [2026-07-19] daily | frontier-models — 1 source, 2 pages

Kimi K3 GDPval-AA v2 Elo backfilled (1668, $0.94/task, native multimodal, 21% fewer tokens than K2.6). Opus 4.8 Elo discrepancy filed (1638 vs 1600). PR #388.

## [2026-07-19] daily | game-music — 1 source, 1 page

Lineage II 22nd anniversary 2LP vinyl collector's edition (40 tracks, Bill Brown/Jamie Christopherson/Inon Zur/NCSOUND, Black Screen Records, November 2026). PR #389.

## [2026-07-19] daily | games-of-note — 4 sources, 1 page

ZA/UM 32 layoffs 2 months after Zero Parades MC 83 launch (critical-vs-commercial disconnect). ZeniMax Online WARN Act: 379 workers, leadership stripped (studio head + ESO exec producer/game director), ESO at 60%+ staff loss in 12 months. CWA ULP charges against Microsoft/Xbox subsidiaries for decisional-bargaining failure. Summary regenerated. PR #390.

## [2026-07-19] daily | agentic-coding — 2 sources, 1 page

SwarmResearch: Shepherd-Agent/Search-Agent harness with git-branch-per-agent isolation + adaptive-depth parallelism beats fixed scaling on 13/15 open-ended optimization tasks. RL for orchestration traces: orchestration decisions (spawn/delegate/communicate/aggregate/stop) as RL optimization target, grounded in Kimi Agent Swarm/Codex/Claude Code. 2 new disputes, 4 new open questions. PR #391.

## [2026-07-19] daily | 4 topics, 8 sources, 5 pages

Daily Research 2026-07-19 complete. PRs #388–#391 merged. ai-in-game-dev: empty proposal. Report: wiki/reports/2026-07-19.md.

## [2026-07-20] daily | games-of-note — 1 source, 2 pages

Bethesda reaffirms Starfield long-term support: "remains an important part of our future," new Starborn content coming 2027, 17M players, nearly a billion hours played, >40% using fan Creations — counter-signal to the ZeniMax reset layoffs at id/BGS/ZeniMax Online. 1 new open question. PR #394.

## [2026-07-20] daily | frontier-models — 1 source, 3 pages

Artificial Analysis market-structure consolidation: six labs now field a model above AA Intelligence Index v4.1 = 50 (up from two in early June). Key new data: per-task cost normalization — GPT-5.6 Sol max ($1.04/task), Kimi K3 ($0.94), Luna/Muse Spark/Grok 4.5 all ≤$0.32 vs Fable 5 ($2.75). No leader moved; Fable 5 = 60 re-verified. claude-fable-5 entity `last_verified` bumped. 1 new open question. PR #395.

## [2026-07-20] daily | 2 topics, 2 sources, 5 pages

Daily Research 2026-07-20 complete. PRs #394–#395 merged. agentic-coding, ai-in-game-dev, game-music: empty proposals. Report: wiki/reports/2026-07-20.md.

## [2026-07-22] daily | agentic-coding — 1 source, 2 pages

Claude Code Week 29 changelog (July 13–17, 2026): /fork = background-session context isolation; /subtask = context-inherit child task with explicit scope handoff. Both primitives solidify the fork/subtask harness pattern for long-horizon agentic runs. 1 new open question. PR #405.

## [2026-07-22] daily | games-of-note — 1 source, 2 pages

~90% of id Software's design team cut in Xbox reset layoffs; ZeniMax branded a "slow, tortuous death" by workers. Ex-Xbox devs condemn Microsoft layoff culture — "good work will not save your job." New open question on ZeniMax Online's ESO path. PR #406.

## [2026-07-22] daily | ai-in-game-dev — 3 sources, 4 pages

Unity 7 free MCP server + AI tools announced at Unite Seoul (UGS, mesh tools, code advisor — all free tier). First multiplayer interactive world model demo: 20fps on B200, 4-player real-time at 512×288, using Representation Autoencoders. 1 new dispute (MCP vs built-in AI assistant strategy). 2 new open questions. Summary regenerated (Unity 7 MCP + world models shift best-practice). PR #407.

## [2026-07-22] daily | frontier-models — 3 sources, 4 pages

Gemini 3.6 Flash ($1.50/$7.50 per Mtoken) positioned as speed/intelligence trade-off leader; Gemini 3.5 Flash Lite halves time-per-task vs prior budget tier. Kimi K3 debuts at #2 on AA-Briefcase knowledge-work benchmark (after Fable 5). Entity updates: gemini-3.6-flash added, kimi-k3 cost + AA-Briefcase fields updated. Summary regenerated (new Flash leader, Kimi K3 benchmark position). PR #408.

## [2026-07-22] daily | game-music — 1 source, 2 pages

Donkey Kong Bananza's full OST (229 tracks, 8h36m, 159 Extended-Playback Collection) added to Nintendo Music with Switch Online requirement. DK Island & Emerald Rush DLC tracks included. 1 new open question on Extended-Playback curation criteria. PR #409.

## [2026-07-22] daily | 5 topics, 9 sources, 14 pages

Daily Research 2026-07-22 complete. PRs #405–#409 merged. All 5 topics active. Report: wiki/reports/2026-07-22.md.

## [2026-07-23] daily | agentic-coding — 1 source, 3 pages

Claude Code v2.1.212–218 (July 18–22): WebSearch cap (200), subagent spawn cap (200), concurrent cap (20, CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS), MCP auto-background after 2 min, EndConversation tool, docker daemon-redirect permission flags, context:fork background-by-default, /code-review as background subagent. Cross-page sweep: parallel-subagents.md + agent-sandboxing.md. PR #411.

## [2026-07-23] daily | frontier-models — 1 source, 1 page

BusinessCaseBench (arxiv 2607.16057): 238 real-world business cases, 615 questions, 18 disciplines. Cross-model oracle gap 4.5 points vs single-best; advisory tasks hardest at <7% all-fail. No leader/price changes; roster re-verified. PR #412.

## [2026-07-23] daily | ai-in-game-dev — 4 sources, 1 page

SIGGRAPH 2026 (July 19, LA, first-ever Games Summit): DLSS 5 revealed — 3-model neural rendering architecture (A/B/C), 4K/60fps in <16ms, per-asset model assignment, fall 2026 ship. NVIDIA MCP expanded to Adobe/Blender/Houdini (APEX Script)/Affinity/UE. Cosmos 3 Edge: 4B-param world model for Jetson/RTX. MotionBricks: 15,000 FPS real-time motion generation from 350k clips, GR00T integration. 1 new dispute (DLSS 5 "neural rendering" vs DLSS 4.x "super-resolution"). PR #413.

## [2026-07-23] daily | games-of-note — 2 sources, 1 page

Xbox Backward Compatibility on PC: 4 OG Xbox titles (BLiNX, Conker, Crimson Skies, Fuzion Frenzy), cross-buy license carry-over, ROG Xbox Ally/X support, Jason Ronald preservation framing. Roblox Grow a Garden: 21,963,800 concurrent users July 19 — new all-time gaming record, surpasses Fortnite 15.3M; 16-year-old creator, free-to-play farming sim. PR #414.

## [2026-07-23] daily | game-music — 3 sources, 1 page

Halo: Campaign Evolved remake confirms remastered O'Donnell/Salvatori score (6-hour Main Menu Theme preview); sharpens existing Halo multitrack dispute. Pokémon Legends: Z-A + Mega Dimension Super Music Complete 5CD review (RPGFan): strong DLC section, uneven overall. AV Club: Legends Z-A breaks Pokémon's linear-music convention with Lumiose city theme adaptive variations. PR #415.

## [2026-07-23] daily | 5 topics, 11 sources, 7 pages

Daily Research 2026-07-23 complete. PRs #411–#415 queued for auto-merge. All 5 topics active. Report: wiki/reports/2026-07-23.md.

## [2026-07-26] health | weekly sweep — 2 disputes filed

Weekly health sweep 2026-07-26. 12 candidate sets (11 source-triggered + 1 stale sweep). 2 new disputes filed: Kimi K3 AA index rank #3 vs #4; Fable 5 SWE-bench Pro 80.3% vs 80.0%. Lint: 0 errors, 225 warnings. 22 stale synthesis pages. PR #429.

## [2026-07-27] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#440 kind=requeue resolved=true — wiki(games-of-note): daily 2026-07-27 was orphan-CLEAN (mergeable_state=clean, CI green, auto-merge not set); enabled auto-merge via GitHub MCP (gh CLI token invalid; MCP used as fallback). Triggered by PR #439 merge.

## [2026-07-30] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#458 kind=requeue resolved=true — wiki(games-of-note): daily 2026-07-30 was orphan-CLEAN (mergeable_state=clean, CI green, auto-merge not set); enabled auto-merge via GitHub MCP (gh CLI token invalid; MCP used as fallback).

## [2026-07-31] daily | frontier-models — 2 sources, 2 pages

Inkling-Small (3B open-weights reasoning model by Thinking Machines) launches. AA Intelligence Index places it within 1 point of full Inkling at <1/3 the parameters. Context window dispute filed: launch post claims 1M tokens; AA article shows 256K. PR #462.

## [2026-07-31] daily | game-music — 1 source, 1 page

iam8bit announces ICO vinyl soundtrack + Team ICO trilogy restocks (Shadow of the Colossus, ICO, The Last Guardian). Open question: ICO track listing (straight port vs unreleased). PR #463.

## [2026-07-31] daily | games-of-note — 3 sources, 1 page

Halo: Campaign Evolved posts weakest-ever Steam peak (25k concurrent, below Halo Wars 2's 30k in 2017). ASGC layoffs tracker revised to 14,259 by end 2026 (up 78% from January forecast; 9,781 already confirmed by July 26). PR #464.

## [2026-07-31] daily | ai-in-game-dev — 2 sources, 1 page

ABot-World-0 (arXiv 2607.19191): real-time interactive world model on single RTX 5090 at 720P/16FPS. Meshy closes $400M Series B at $1.5B — largest AI 3D funding round ever; 12M users, 100M models, 12× ARR YoY. PR #465.

## [2026-07-31] daily | agentic-coding — 2 sources, 1 page

GitHub Copilot code review agent skills + MCP now generally available (Jul 29). Visual Studio July 2026 update: new Agent mode powered by Copilot SDK with built-in skills. PR #466.

## [2026-07-31] daily | 5 topics, 10 sources, 6 pages

Daily Research 2026-07-31 complete. PRs #462–#466 all merged. All 5 topics active. Report: wiki/reports/2026-07-31.md.

## [2026-08-01] daily | ai-in-game-dev — 1 source, 1 page

Tencent Hunyuan3D-PolyGen: AI model for art-grade 3D assets claiming 70% asset-time reduction and production-quality retopology. PR #468.

## [2026-08-01] daily | games-of-note — 2 sources, 1 page

EA officially goes private August 4, 2026 ($210/share, PIF/Silver Lake/Affinity Partners). August 2026 release slate: Star Wars Zero Company, Beast of Reincarnation, MARVEL Tokon, MGS Master Collection Vol. 2. PR #469.

## [2026-08-01] daily | game-music — 1 source, 1 page

Blue Reflection Official Soundtrack review (RPGFan): Hayato Asano's artcore subgenre blending game audio with classical piano composition. PR #470.

## [2026-08-01] daily | agentic-coding — 2 sources, 3 pages

Cursor ships agent-conversation hooks (beforeSubmitPrompt/afterAgentResponse/stop) and rebuilt iPad multi-agent layout. GitHub Copilot vision GA in VS Code; Agents window in public preview; BYOK in agents. PR #471.

## [2026-08-01] daily | frontier-models — 4 sources, 6 pages

DeepSeek-V4-Flash-0731 official release: Terminal-Bench 61.8→82.7, DeepSWE 7.3→54.4, AA Intelligence Index 40→50 via re-post-training; MIT-licensed, $0.14/$0.0028/$0.28/MTok. MiniMax H3: unified omni-modal 15s 2K video with stereo audio at <1/3 mainstream cost. PR #472.

## [2026-08-01] daily | 5 topics, 10 sources, 17 pages

Daily Research 2026-08-01 complete. PRs #468–#472 all merged. All 5 topics active. Report: wiki/reports/2026-08-01.md.

## [2026-08-02] health | weekly sweep — 2 disputes filed

Weekly health sweep 2026-08-02 complete. 16 candidate sets scanned (15 source-triggered + 1 stale sweep). 2 disputes filed on wiki/topics/frontier-models/index.md (DeepSeek V4 Pro AA Index v4.0/v4.1 version mismatch; Inkling-Small AA independence contradiction). 20 stale pages noted. PR #474.

## [2026-08-02] daily | games-of-note — 2 sources, 3 pages

Game Freak's Beast of Reincarnation launches Aug 3 on PS5/Xbox/PC day-one Game Pass; game was leaked three days early by pirates. PR #475.

## [2026-08-02] daily | frontier-models — 0 sources, 1 page

Quiet day: leader picture unchanged (Opus 5 #1 AA II 61, Fable 5 #2, GPT-5.6 Sol #3). MiniMax H3 open-weights release logged as open question. PR #476.

## [2026-08-02] daily | agentic-coding — 0 sources, 1 page

Quiet day: Codex Aug changelog changes (integrated terminal reading, DigitalOcean plugin, GPT-5.4 deprecation) logged as open questions pending citable primary source. PR #477.

## [2026-08-02] daily | game-music — 0 sources, 1 page

Quiet day: Beast of Reincarnation score noted as data gap (no specialist-outlet composer coverage). PR #478.

## [2026-08-02] daily | 4 topics, 2 sources, 6 pages

Daily Research 2026-08-02 complete. PRs #475–#478 created (auto-merge enabled; all CI green). ai-in-game-dev skipped (empty page_diffs). Report: wiki/reports/2026-08-02.md.

## [2026-08-03] daily | agentic-coding — 2 sources, 2 pages

OpenAI Codex Sites public beta (agent-built apps on hosted infra) and Claude Code release notes (built-in harness caps parallel subagents at <15 by default). PR #481.

## [2026-08-03] daily | frontier-models — 1 source, 2 pages

MiniMax H3 open weights (288 GB) on Hugging Face: omni-modal video, 15s 2K clips with native stereo audio. Cross-page sweep to ai-in-game-dev. PR #482.

## [2026-08-03] daily | games-of-note — 3 sources, 1 page

Beast of Reincarnation (not a soulslike), WBD/Paramount $110.9B acquisition (DOJ-approved, federally paused), Paramount freeze deal into 2027. Dispute filed on hearing cancellation. PR #483.

## [2026-08-03] daily | ai-in-game-dev — 0 sources, 1 page

Quiet day: cross-page sweeps from agentic-coding and frontier-models added Codex Sites + MiniMax H3 references. Null-sweep audit note filed. PR #484.

## [2026-08-03] daily | game-music — 1 source, 1 page

Culdcept the First Steam launch (July 30); Cepter Edition bundles 2-CD Yuzo Koshiro OST; consoles Sept 8. PR #485.

## [2026-08-03] daily | 5 topics, 7 sources, ~10 pages

Daily Research 2026-08-03 complete. PRs #481–#485 created (auto-merge enabled; all CI green). Report: wiki/reports/2026-08-03.md.

## [2026-08-09] daily | games-of-note — 1 source, 2 pages

EA $700M cost-cutting plan including $170M in "organizational efficiencies" (layoffs at Respawn + others). Dispute filed vs "gaming is the new oil" thesis. PR #524.

## [2026-08-09] daily | frontier-models — 1 source, 4 pages

AA Intelligence Index v4.1.1: Claude Opus 5 #1 at 63 (was 61), Fable 5 at 62 (was 60), Sol at 61 (was 59). Grading-robustness fixes via GPT-5.6 Luna medium grader. Entity frontmatter updated for Fable 5. Summary regenerated. PR #525.

## [2026-08-09] daily | agentic-coding — 3 sources, 4 pages

Auto mode now default for Claude Code Pro/Max/Team; Trajectory Labs 0/720 red-team eval. Codex: GPT-5.6 Terra/Luna GA, Goal mode GA, visual-feedback gap. Two disputes filed. Summary regenerated (separate commit, post-merge-queue). PR #526.

## [2026-08-09] daily | ai-in-game-dev — 2 sources, 3 pages

EU AI Act Article 50 disclosure obligations effective 2026-08-02 — market-follows scope, EUR 15M/3% fines, artistic/creative-works carve-out. EC "no obligation" counter-position. Dispute + 2 open questions filed. Summary updated. PR #527.

## [2026-08-09] daily | game-music — 2 sources, 3 pages

Guild Wars 3 composer team: Kazuma Jinnouchi (Halo/Metal Gear/Star Wars) lead, City of Prague Philharmonic. Rust OST first vinyl: Laced Records 3xLP, $62, Jan 2027. PR #528.

## [2026-08-09] daily | 5 topics, 9 sources, ~16 pages

Daily Research 2026-08-09 complete. PRs #524–#528 created (auto-merge enabled). Report: wiki/reports/2026-08-09.md.

## [2026-08-11] manual | conflict-resolver — 1 rebased, 0 requeued, 0 lint-fixed, 0 failed

pr#537 rebased onto main (frontier-models daily 2026-08-11); 1 conflict in wiki/entities/muse-spark.md (parallel Muse Glimmer additions from two sources merged additively per CLAUDE.md append-only rules); force-pushed 9244e34; auto-merge re-evaluates vs rebased tip. pr#539 (games-of-note) already merged before requeue attempted. pr#540 (game-music) BLOCKED+CI-green no failing runs not classifiable skipped.

## [2026-08-13] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#555 (game-music daily 2026-08-13) requeued: mergeable_state=clean, CI green, all gate criteria passed. gh CLI GraphQL blocked in session; squash-merged directly via MCP merge tool as equivalent to --auto (immediate effect). Merged SHA: 159a54c.

## [2026-08-14] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#559 (game-music daily 2026-08-14) requeued: mergeable_state=clean, CI green, all gate criteria passed. gh CLI token invalid in session; squash-merged directly via MCP merge tool as equivalent to --auto (immediate effect). Merged SHA: d774b30.

## [2026-08-14] manual | conflict-resolver — 0 rebased, 1 requeued, 0 lint-fixed, 0 failed

pr#561 (frontier-models daily 2026-08-14) requeued: mergeable_state=clean, CI green, all gate criteria passed. gh CLI token invalid in session; squash-merged directly via MCP merge tool as equivalent to --auto (immediate effect). Merged SHA: b15af9aa.

## [2026-08-14] daily | games-of-note — 2 sources, 4 pages

2K announces new Vancouver AAA studio Small Axe Studios (led by EA veteran Luc Shelton); Tencent launches Hunyuan 3D creator tool globally. Entity small-axe-studios.md created. 1 dispute (Tencent "empower creators" vs. hollow genAI critique), 2 open questions. PR #558.

## [2026-08-14] daily | game-music — 2 sources, 4 pages

Mick Gordon (DOOM composer) announces first live DOOM performance at RADAR Festival 2027 (Manchester); Warframe vinyl soundtrack 2XLP reissue via iam8bit. Entity mick-gordon.md created. 1 open question. PR #559.

## [2026-08-14] daily | frontier-models — 2 sources, 5 pages

DeepSeek-V4-Pro GA (v4.1.1 basis, aa_intelligence_index 52→53); Upstage Solar Pro 4 benchmarks (+27pts on agentic/long-context tasks). deepseek-v4 entity updated (field + GA build details). 3 open questions. PR #561.

## [2026-08-14] daily | agentic-coding — 3 sources, 5 pages

Claude Code cross-session messaging (SendMessage tool) + fork-as-default sub-agent model (v2.1.232); Cursor Router Auto/Intelligence/Balance mode cost logic. parallel-subagents.md updated (fork-as-default + cross-session surface). 4 open questions. PR #562.

## [2026-08-14] daily | ai-in-game-dev — 3 sources, 4 pages

Meshy 7 launches with higher-fidelity geometry + ultra_mode parameter; Saber Interactive Rideshare uses AI for infinite-passenger dialogue in free-ride mode; Saber CEO vs. ex-lead-writer factual dispute on AI writer replacement. 2 disputes, 3 open questions. PR #564.

## [2026-08-14] daily | 5 topics, 12 sources, ~22 pages

Daily Research 2026-08-14 complete. 5 topics processed (games-of-note, game-music, frontier-models, agentic-coding, ai-in-game-dev); 12 new source pages; ~22 pages touched. PRs #558, #559, #561, #562, #564 created and merged (auto-merge). Report: wiki/reports/2026-08-14.md.

## [2026-08-16] health | weekly sweep — 5 disputes filed

20 candidate sets scanned (19 source-triggered + 1 stale sweep). 5 disputes filed across 4 pages: gpt-5.6-sol (×2), frontier-models, parallel-subagents, muse-code. 24 stale pages, 0 lint errors. PR #567.

## [2026-08-19] daily | frontier-models — 2 sources, 3 pages

Gemini 3.7 Flash launched (AA Index 56, competitive with GPT-4o mini / Haiku 4.5 on cost); Google's intelligence-vs-speed Pareto positioning. Summary regenerated. PR #583.

## [2026-08-19] daily | agentic-coding — 3 sources, 6 pages

Codex CLI 0.148.0 fork-based multi-session; ClawArena-Team SMS orchestration benchmark; OrchBench deterministic simulation evaluator. Summary regenerated; parallel-subagents + harness-engineering cross-page sweep. PR #584.

## [2026-08-19] daily | ai-in-game-dev — 2 sources, 3 pages

WebGameBench: browser-native game benchmark for coding agents (76.9% usable, 20.2% excellent); ArtLLM articulated 3D asset generation from text. Summary regenerated; 2 disputes, 2 open questions. PR #585.

## [2026-08-19] daily | game-music — 1 source, 2 pages

Video Game Symphony "Choose Your Character" show in Cleveland (Borislav Slavov BG3, Castlevania suite, Chrono Cross premiere, Aug 23 2026). Divergence sentinel added. PR #586.

## [2026-08-19] daily | games-of-note — 4 sources, 5 pages

Tencent cancels Last Sentinel/Lightspeed LA (~80 of ~100 staff cut, ~6yr/$100M+ AAA cancelled); Bethesda inflatable-rat protest vs. Xbox leadership; Phil Spencer praises Elder Scrolls 6. Summary regenerated; 2 disputes, 2 open questions. PR #587.

## [2026-08-20] daily | 3 topics, 6 sources, 11 pages

Daily Research 2026-08-20 complete. 3 topics processed (agentic-coding, frontier-models, games-of-note); 6 new source pages; 11 pages touched. PRs #589, #590, #592 created. Report: wiki/reports/2026-08-20.md.

## [2026-08-20] daily | games-of-note — 3 sources, 5 pages

Warren Spector retirement (43 years in game dev), Black Pony Immersive announced (Harvey Smith + Arkane Austin vets), Raze & Rebuild Studio worker co-op launch. New entity: black-pony-immersive. PR #592.

## [2026-08-20] daily | frontier-models — 1 source, 3 pages

GLM-5.3 (max) confirmed at AA Intelligence Index 60 (+9 vs GLM-5.2); price $1.40/$4.40 per Mtoken; weights still proprietary. Updated glm-5 entity. PR #590.

## [2026-08-20] daily | agentic-coding — 2 sources, 3 pages

Cursor cloud agents with per-subagent VM isolation and event subscriptions; Willison's conceptual-integrity-erosion concern. 1 new dispute (erosion vs. orchestration-era framing), 3 new open questions. PR #589.

## [2026-08-19] daily | 5 topics, 12 sources, ~18 pages

Daily Research 2026-08-19 complete. 5 topics processed (frontier-models, agentic-coding, ai-in-game-dev, game-music, games-of-note); 12 new source pages; ~18 pages touched. PRs #583–#587 created and auto-merged. Report: wiki/reports/2026-08-19.md.

## [2026-08-21] daily | game-music — 1 source, 2 pages

ULTRAKILL Act 2: Imperfect Hatred 3×LP vinyl soundtrack released by Materia Collective. PR #595.

## [2026-08-21] daily | games-of-note — 3 sources, 1 page

Riot 2XKO shut down after less than a year; Sony Horizon Hunters Gathering rebooted as smaller story-driven co-op game; Mattel Game Studios launched. 2 new disputes, 3 new open questions. PR #596.

## [2026-08-21] daily | frontier-models — 1 source, 1 page

Artificial Analysis Optima launched as custom-benchmark platform (find best model for your task, up to 10× cost/time savings). DeepSeek V4 peak/off-peak billing filed as Open question. PR #597.

## [2026-08-21] daily | ai-in-game-dev — 1 source, 1 page

Single-image → editable-engine-scene reconstruction paper (independently editable meshes + explicit lighting). 1 new dispute, 1 new open question. PR #598.

## [2026-08-21] daily | agentic-coding — 2 sources, 1 page

Agent Lightning v1.0 (harnessed agentic RL, +14.6pp SWE-bench Verified on Qwen3.5-9B, ~3,500-LOC open framework); LongHorizon-Harness (MEA loop, externalized verified task-state). Summary updated. 2 new open questions. PR #599.

## [2026-08-21] daily | 5 topics, 8 sources, 5 pages

Daily Research 2026-08-21 complete. 5 topics processed (game-music, games-of-note, frontier-models, ai-in-game-dev, agentic-coding); 8 new source pages; 5 topic pages touched. PRs #595–#599 created and auto-merged. Report: wiki/reports/2026-08-21.md.

## [2026-08-23] health | weekly sweep — 2 disputes filed

9 candidate sets scanned (8 source-triggered + 1 stale sweep). 2 disputes filed: agent-harnesses.md (Harness-IF 4 vs 5 instruction surfaces), black-pony-immersive.md (first-generation immersive sim lineage contradiction). 27 stale synthesis pages, 0 lint errors. PR #602.
