---
title: Generative media models — purpose
kind: purpose
sources: []
last_updated: 2026-10-24
last_verified: 2026-10-24
freshness_window_days: 365
---

# Generative media models — topic charter

This file is **HUMAN-OWNED** (per the file ownership matrix in `CLAUDE.md`).
The synthesis page for this topic is [[generative-media-models]].

## Cross-cutting bar (applies first)

See `CLAUDE.md` "Cross-cutting relevance criteria" for the meta-bar:
**highly relevant**, **highly innovative**, or **directly impacts/improves
agentic workflow OR video game development**. Any one suffices. Bias
toward inclusion when on the fence — every model in this topic is a
candidate step in a game-asset pipeline, so criterion 3 (game-dev impact)
is satisfied almost by construction. The sections below narrow the bar
with topic-specific in-scope / out-of-scope rules.

## What this topic is

The current **lineup** of models that generate images, video, music, sound
effects and speech — which ones exist, how you reach them (vendor API,
fal.ai, Replicate, open weights), what they cost, under what license you
may ship their output in a commercial game, which leaderboards rank them
and where, and which have been deprecated or shut down.

This topic is a *vendor-and-lineup tracker*, not a pipeline-integration
topic. "Does this ship inside a game-dev workflow" is `ai-in-game-dev`'s
lens; "what is the current frontier for generating this kind of asset,
and what does it cost to use it" is this topic's lens.

The wiki should accumulate working answers to:

- What is the current best model (per leaderboard with methodology) for
  text-to-image, image editing, image-to-video, text-to-music, SFX, TTS?
- Which of those are reachable by API today, through which host, at what
  per-unit price?
- Which licenses allow shipping generated assets in a commercial game, and
  which require an enterprise tier or forbid it?
- Which open-weight releases are runnable on a workstation (hardware
  floor), and which need a cluster?
- What got deprecated or shut down this month, and what replaces it?

## In scope

- Releases and capability changes of models that generate **images**
  (GPT Image, Nano Banana / Gemini image, Seedream, Flux, Ideogram,
  Recraft, Reve, Stable Diffusion, Midjourney, Imagen).
- Releases and capability changes of **video** models used for 2D
  animation and cutscenes (Veo, Sora, Kling, MiniMax Hailuo / H-series,
  Runway, Luma Ray, Wan).
- **Music** and **sound-effect** generators (Suno, Udio, Lyria,
  Stable Audio, ElevenLabs SFX, AudioCraft, MMAudio).
- **Speech** models: TTS, voice cloning, speech-to-speech (ElevenLabs,
  Inworld TTS, Cartesia, MiniMax Speech, OpenAI TTS, Kokoro).
- **Game-oriented sprite, pixel-art, tileset and spritesheet
  generators** — PixelLab, Retro Diffusion, Scenario, Layer, Ludo,
  SpriteCook. Explicitly in scope even when the vendor is small.
- **API availability**, model ids, pricing per unit (image / second /
  minute / character), rate limits.
- **License and commercial-use terms** — including changes to them.
- **Arena and leaderboard movements that come with methodology**:
  arena.ai text-to-image / image-edit / image-to-video / text-to-video
  boards, Artificial Analysis image / video / speech arenas, published
  human-preference studies.
- **Deprecations and shutdowns** (e.g. the Sora API, Udio exports) and the
  migration path the vendor recommends.
- **Aggregator hosting changes** (fal.ai, Replicate) that make a model
  reachable by API or change its price there.
- **Open-weight releases** with their stated hardware floor (VRAM,
  quantization) and license.

## Out of scope

- LLM text models, including multimodal *input* capabilities of LLMs —
  `frontier-models`.
- 3D generation, retexture / PBR materials, auto-rigging, text-to-motion,
  video mocap, facial animation — `ai-in-game-dev`. (A video model used
  for 2D animation belongs *here*; a video-to-3D-motion model belongs
  *there*.)
- Engine-embedded generators with no public API (Unity AI Material
  Generator, Roblox Cube inside Studio). Note them once as
  `access: [none]` documented-only entries and move on; the engine news
  itself is `ai-in-game-dev`.
- Marketing without methodology — "best image model ever" with no
  leaderboard, no eval, no pricing page.
- Composers, soundtracks, adaptive-music middleware — `game-music`.

## Key entities to track

Every model or product in this topic is an **entity page with
`profile: tool`** (see `CLAUDE.md` "Tool entity profile"). The structured
frontmatter is what the comparison pages and the benchmark scout read;
the prose is what humans read.

`wiki/entities/` (create as they enter the news cycle):

- Image: `gpt-image`, `nano-banana`, `seedream`, `flux`, `ideogram`,
  `recraft`, `reve`, `stable-diffusion`, `midjourney`, `imagen`
- Video: `veo`, `sora`, `kling`, `minimax-h3`, `runway-gen`, `luma-ray`,
  `wan`
- Music / SFX: `suno`, `udio`, `lyria`, `stable-audio`, `elevenlabs-sfx`,
  `mmaudio`
- Speech: `elevenlabs`, `inworld-realtime-tts-2`, `cartesia`,
  `minimax-speech`, `openai-tts`, `kokoro`
- Sprites: `pixellab`, `retro-diffusion`, `scenario`, `layer-ai`, `ludo-ai`,
  `spritecook`
- Hosts / arenas (plain entities, no tool profile): `fal-ai`, `replicate`,
  `arena-ai`, `artificial-analysis`

## Key concepts to track

`wiki/concepts/`:

- `text-to-image-pipelines`, `sprite-generation`, `pixel-art-generation`
- `image-to-video-for-2d-animation`, `video-model-consistency`
- `text-to-music-licensing`, `sfx-generation`
- `tts-latency-and-emotion-control`, `voice-cloning-consent`
- `generative-media-arenas` (how the boards are built, what they miss)
- `commercial-use-terms-for-generated-assets`

## Comparison pages this topic produces

`wiki/comparisons/` — see `CLAUDE.md` "Comparison pages". All compare
tool entities on `access, pricing, commercial_use, status, arena_rank`:

- `image-tools` — created by the first run that yields ≥ 2 image tool
  entities (`wikipilot compare new image-tools --of ... --fields
  access,pricing,commercial_use,status,arena_rank --title "Image
  generation tools"`).
- `video-tools` — same rule; `minimax-h3` is the first entry.
- `audio-tools` — music, SFX and speech tools together (exists; seeded
  with `inworld-realtime-tts-2`, `elevenlabs`).

Cross-reference (owned by `ai-in-game-dev`, same field set): `3d-tools`,
`rig-and-motion-tools`.

## Roster sweep (every run)

This topic owns the `image`, `video`, `music`, `sfx`, `voice` and
`sprite` modalities in `wikipilot.toml [tool_profiles].modality_topics`.
On every run the researcher:

1. Runs `uv run wikipilot tools --topic generative-media-models --format json`
   to get the **derived roster** — every `profile: tool` entity whose
   `modality` maps to this topic. There is no static list to edit; a new
   tool entity proposed via `page_diffs` joins the roster on the next run.
2. Re-confirms every `[tool_profiles].tracked_fields` value (`status`,
   `pricing`, `commercial_use`, `arena_rank`) against the vendor's pricing
   / terms page, the aggregator listing, or the arena board, and emits
   `entity_field_updates` for anything that moved (or was re-confirmed
   unchanged, with `verified_today: true`).
3. **Sweep fetches are exempt from `allowlist_domains`** for an existing
   entity's `vendor` domain and for `fal.ai` / `replicate.com`.
   Discovery of *new* sources still honors the allowlist.

Never guess a field. If the source doesn't state it, the value is the
literal string `unknown` and the gap goes under `## Open questions`.

## Counter-arguments to actively look for

The researcher MUST attempt to find at least one counter-argument or data
gap per non-trivial claim, OR add the divergence sentinel. Examples:

- "Model X leads the text-to-image arena" → look for a second board that
  disagrees, or a methodology critique (prompt-set bias, vote volume).
- "License permits commercial use" → look for the exception clause
  (games / interactive media often need an enterprise tier; some forbid
  training on outputs; some require attribution).
- "Open weights run on 24 GB" → look for the quantization caveat and
  reported generation times.
- "Model deprecated" → look for whether an aggregator still serves it.

## Source quality bar

Prefer vendor pricing / terms / changelog pages, model cards, arena
methodology pages, Artificial Analysis, arxiv. Aggregator (fal.ai,
Replicate) model pages count as primary for *availability and hosted
price*, not for capability claims. Reject listicles and re-aggregated
"X beats Y" posts that don't link the board or the pricing page.

## Voice

Expert. Dense. Price-and-license literate. Always state the unit
(per image / per second / per 1k characters) and the date next to a
price or a license claim — both change monthly.

## Citation discipline reminder

Every claim MUST be backed by a wikilink to a source page (slug in double
square brackets) and a `>` quote from that source. Every tool-profile
tracked field MUST carry its `_source` sibling.
