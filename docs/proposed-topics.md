# Proposed topics — rationale + adjacent considerations

This file captures the reasoning behind the five topics seeded in Phase 9 and the design choices that shaped how the `topic-researcher` ingests sources. It's a future-self note, not a charter — the actual charters live in `wiki/topics/<id>/purpose.md` and the operational config in `topics.yaml`. When a topic gets added, removed, or significantly retargeted, append a short note here so the rationale doesn't get lost in git history.

## The five Phase 9 topics (plus `generative-media-models`, added 2026-10-24)

The set was chosen to span the user's two anchor domains (agentic AI workflow and video-game development) at three levels of abstraction: the toolchain, the underlying capabilities, and the surrounding industry. Each topic earns its keep by producing synthesis that another topic can't.

### `agentic-coding`

Agentic systems for software engineering — IDEs, CLIs, harnesses, skills, MCP, parallel subagents, prompt caching, sandboxing, eval harnesses. This is the "what tools should I be using and how" topic, scoped tightly to the coding-agent layer (not general LLM research, not non-coding agents).

Adjacent terms considered and folded in: `ai-coding-tools`, `agentic-ides`, `claude-code-ecosystem`, `cursor-and-friends`. All collapse to this one — the entity seeds (`claude-code`, `cursor`, `codex`, `aider`, `devin`, `openhands`, `swe-agent`, `windsurf`, `cline`) cover the field cleanly.

### `frontier-models`

Frontier LLM landscape — model releases, capability changes, costs, context windows, reasoning models, multi-modal, open-weight. The "what's available and at what price" topic; deliberately separated from `agentic-coding` so the comparison-page surface area for cost / benchmarks / context is its own first-class artifact rather than a section buried in an IDE comparison.

Adjacent terms considered: `llm-research`, `model-releases`, `ai-capabilities`. The first is too broad (training-methodology research belongs elsewhere if we ever do it); the latter two were merged into this charter.

### `ai-in-game-dev`

AI in game-development tools and pipelines — engine integrations, content gen (text-to-image, text-to-3D, 2D character rigs, sprite gen, mocap, voice), AI NPC behavior, dialog, playtesting. The bridge topic between the user's two anchor domains; explicitly scoped to game-dev workflows so generic image/3D-gen research doesn't flood the topic.

Adjacent terms considered: `procedural-generation` (folded in as a concept, `procgen-with-llms`), `ai-mocap` (folded in as a concept), `unity-ai`/`unreal-ai` (folded in as entities). The boundary against `agentic-coding` is "is the agent operating inside a game engine?" — Unity MCP and Blender MCP land here; Claude Code and Cursor land in `agentic-coding`.

### `games-of-note`

Notable games and the games industry — AAA + indie releases, studio news, awards, genre revivals, significant DLC, commercial-vs-critical disconnects. The "what's worth paying attention to as a game" topic; the keyword is *notable*, which is what keeps the noise floor manageable.

Adjacent terms considered: `gamedev-industry`, `game-releases-2026`. The first is partly covered (studio news) and partly out (engine releases live in `ai-in-game-dev` if AI-related, otherwise out of scope for now); the second is too narrow and time-bound. Music explicitly split out into `game-music` because the entity universe is different (composers, audio middleware, labels).

### `game-music`

Game composers, soundtracks, audio tech, live concerts, music criticism. Low natural source flow; the safety cap of 20 will rarely if ever trip here.

Adjacent terms considered: `vgm` (folded in — same domain), `game-audio` (broader; would include sound design, foley — out of scope for now since the user's interest is composer-and-soundtrack-centric).

### `generative-media-models` (added 2026-10-24)

Image, video, music, SFX, speech and sprite generation models — releases, API availability, pricing, commercial-use terms, arena / leaderboard movements with methodology, deprecations, aggregator (fal.ai / Replicate) hosting changes, open-weight releases with hardware floor. Added because the user is building a monthly benchmark of generative tools for game creators and uses the wiki as its scout feed: a script diffs the wiki's tool entities and comparison pages against the benchmark's model registry before each round.

**Why a new topic rather than widening `ai-in-game-dev`.** The diagnosis the benchmark agent brought was "the charter excludes general-purpose image generation". That was only half right: `ai-in-game-dev` already listed SD / Flux / Midjourney, sprite generation and ElevenLabs voice as in-scope and promised a `text-to-image-pipeline-comparison`. Nothing landed because (a) its `allowlist_domains` and `search_hints` point at engine vendors and arxiv, and (b) its lens — "does this ship inside a pipeline" — is not the lineup / price / license lens the benchmark needs. A vendor-and-lineup tracker is a different topic with different sources, so it got its own charter, and the overlapping items were moved out of `ai-in-game-dev` explicitly (entities `stable-diffusion`, `flux`, `midjourney`, `comfyui`, `elevenlabs`; concepts `text-to-image-pipelines`, `sprite-generation`; the text-to-image comparison, now `image-tools`).

**Boundary resolutions.**

- `ai-in-game-dev` keeps 3D generation, retexture / PBR, auto-rigging, text-to-motion, video mocap and facial animation, and now states explicitly that for those tools the vendor changelog, API availability, model ids, pricing and commercial-use terms are in-scope (not just capabilities). Its `allowlist_domains` gained `meshy.ai`, `docs.meshy.ai`, `tripo3d.ai`, `docs.tripo3d.ai`, `hyper3d.ai`, `hunyuan.tencent.com`, `fal.ai`, `replicate.com`, `github.com` so the roster sweep can cite vendor pricing pages.
- `frontier-models` had "multi-modal capabilities (vision, audio, video input/output)" in scope and shares `openai.com`, `deepmind.google`, `huggingface.co` with the new allowlist — a gpt-image or Veo launch would have been claimed by two researchers. Its charter now sends generation-model releases to `generative-media-models` and keeps multimodal *input*; a launch post covering both gets `also_relevant_to`.
- `game-music` is composer-centric and said nothing about generative music; it now points generative music / SFX / speech models at the new topic and keeps the craft debate.

**Tool entity profile.** Alongside the topic, entity pages gained a machine-readable `profile: tool` frontmatter block (see `CLAUDE.md` "Tool entity profile") with a lint rule, derived per-topic rosters (`wikipilot.toml [tool_profiles].modality_topics`), per-modality comparison pages (`3d-tools`, `rig-and-motion-tools`, `audio-tools`; `image-tools` / `video-tools` once ≥ 2 entities exist), a roster sweep in the `topic-researcher`, and two zero-LLM CLIs for the scout: `wikipilot tools --format json` (full registry dump) and `wikipilot tool-changes --since DATE | --since-rev SHA` (versioned delta, also rendered as `## Creator tooling changes` in the daily and weekly reports). The `kind: tool` the benchmark agent first proposed was rejected in favor of `kind: entity` + `profile: tool` to keep `VALID_KINDS`, `Vault.page_path`, index sections and every agent prompt unchanged; the proposed `wiki/entities/_tool-template.md` was rejected because `_*.md` is the personal-scratch convention (lint-exempt, agents never read it) — the template lives in `CLAUDE.md` and `docs/architecture.md` instead.

Adjacent terms considered: `ai-art-tools` (too narrow — misses audio), `creator-tooling` (too broad — would pull in editors and DCC apps), `media-foundation-models` (research-flavored; the lens here is lineup and price, not architecture).

## Topics explicitly considered and rejected

- **`general-ml-research`** — too broad to charter usefully without a dedicated curator. The interesting subset (model capability changes) is already covered by `frontier-models`; the rest is noise the auto-merge gate would trip on daily.
- **`ai-safety` / `alignment`** — the user is interested but doesn't want a daily firehose; a future Wiki Query can pull the salient claims into an answer page on demand.
- **`game-design-theory`** — slow-moving, high-quality field; doesn't fit the daily cadence. Would belong in a hypothetical `weekly-deep-reads` topic if we ever add a weekly-frequency tier.
- **`hardware` / `gpu-stack`** — adjacent and interesting but the user isn't building an inference stack; the relevant slice (cost trends) is captured in `frontier-models` `cost-comparison`.

## Why permissive inclusion?

Phase 9 explicitly rejected three encoded-quota approaches in favor of a qualitative judgment passed to the Opus 4.7 researcher:

1. **Tiered numeric caps** (`max_sources_per_run: 8/8/5/5/3` per topic, scaled to expected flow) — would cap the wrong thing on busy days, and the agent already has the context to make a better call than a static number.
2. **Per-source scoring rubric** (relevance × novelty × impact, threshold 7.0) — overhead-heavy, brittle to prompt-engineering, and the rubric would itself need to drift over time as topics mature. The judgment lives better in natural language.
3. **Strict allowlist-only filtering** — too brittle; an interesting source from an unlisted domain is a regular occurrence (a researcher's personal blog, a one-off conference talk).

Instead, `CLAUDE.md` "Cross-cutting relevance criteria" gives the agent three OR'd inclusion criteria and an explicit "when on the fence, include" bias. The reasoning:

- **Coverage > precision at this stage.** With ~0 wiki content today, missing an interesting source is more costly than ingesting a slightly-too-broad one. We can prune later from the run reports.
- **The agent is the right judge.** Opus 4.7 with the topic charter, the cross-cutting criteria, and the source content has more context than any pre-encoded rule. Asking it to pre-filter at ingest is cheaper and higher-quality than post-filtering with a numeric threshold.
- **Tightening lives in plain text.** When a topic over-ingests, the fix is one or two `## Out of scope` bullets in the topic's `purpose.md`, observed from the daily run report. Lower friction than schema migrations.
- **`max_sources_per_run: 20` as a safety cap.** Uniform across all topics; the auto-merge gate is calibrated to trip on a 20-source day, surfacing it for human review. The cap is not a quality lever — if it routinely engages, the rubric needs tightening, not the cap raising.

This also means the cost shape is harder to predict precisely: realistic busy day is 5–12 sources per topic at ~$0.50–$1 per topic, so ~$3–6/day total; quiet day ~$1/day; safety-cap day ~$15/day (bounded by the cap). These numbers will be revisited after a month of real runs.

## When to add or remove a topic

Add a topic when:
- A clear domain has emerged that doesn't fit cleanly under any existing charter, AND
- You're willing to write a real `purpose.md` (in-scope, out-of-scope, key entities, key concepts, comparisons, counter-arguments to look for, source quality bar, voice).

Remove or consolidate when:
- Two topics are routinely producing the same sources (the boundary isn't carrying its weight).
- A topic stays cold across multiple weeks and the wiki has no synthesis pages benefiting from it.
- The user's interests have shifted and the topic isn't being read.

When swapping topics, update this file with a one-paragraph note (date, what changed, why) so the next pass through the rationale isn't a reconstruction from git log.

## Future surface (not in Phase 9)

- **Routing layer** — when a `topic-researcher` flags `also_relevant_to: [other-topic]` on a `ProposalSource`, a future routine could route the source's synthesis edits to the other topic's PR instead of the current one's. Phase 9 just records the flag; the routing logic is deferred until cross-topic spillover is observed in real run reports.
- **Auto-generation of comparison pages** — Phase 9 ships the helper (`compare new` / `compare regen`) and CLI; a future phase can wire the daily routine to call `compare regen` on every comparison page that includes an entity touched in the current run.
- **Weekly-frequency tier** — for slow-moving, high-quality topics like `game-design-theory` that don't fit a daily cadence. Would require schema and orchestrator changes; deferred until clearly needed.
