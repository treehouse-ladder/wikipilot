# Proposed topics — rationale + adjacent considerations

This file captures the reasoning behind the five topics seeded in Phase 9 and the design choices that shaped how the `topic-researcher` ingests sources. It's a future-self note, not a charter — the actual charters live in `wiki/topics/<id>/purpose.md` and the operational config in `topics.yaml`. When a topic gets added, removed, or significantly retargeted, append a short note here so the rationale doesn't get lost in git history.

## The five Phase 9 topics

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
