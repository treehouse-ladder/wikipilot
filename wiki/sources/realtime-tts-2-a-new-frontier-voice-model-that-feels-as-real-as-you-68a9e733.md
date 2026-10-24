---
fetched_at: &id001 2026-10-24
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 68a9e733e8a1d92dc6b45aa74cb92c533d5e9465770cf27f61c236a0fd8e78ca
sources: []
title: 'Realtime TTS-2: A new frontier voice model that feels as real as you'
topic: ai-in-game-dev
url: https://inworld.ai/blog/realtime-tts-2
---

## Excerpts

> Realtime TTS-2 from Inworld AI is a new generation of voice model built for realtime conversation. It hears the full audio of the exchange, picks up the user's tone, pacing and emotional state, then takes voice direction in plain English the way developers prompt an LLM. It holds one voice identity across over 100 languages. Available today via the Inworld API and the Inworld Realtime API in general availability.

> Realtime TTS 1.5 already ranked #1 on the Artificial Analysis Speech Arena, ahead of Google and ElevenLabs. Quality is solved. So we asked the next question: what does voice AI sound like when it is built for the way humans actually talk to each other?

> Realtime TTS-2 is built from the ground up for realtime conversation. It listens to the prior turns of the exchange, so your tone and pacing carry forward. It takes voice direction in plain English, so you steer the read the way a director would. It holds one voice identity across over 100 languages, so the speaker stays the same person mid-switch. And Advanced Voice Design lets you build a saved voice from prose. Four capabilities that work together, in one model, on the same realtime connection.

> Voice Direction. What it is. A natural-language description of how a line should be delivered, passed inline at the start of your text. Not a fixed list of preset emotions. Not a slider. Write the prompt the way you'd write a stage direction. Best practice: long, descriptive prompts beat short labels — [speak sadly, as if something bad just happened] directs the model far better than [sad]. Inline non-verbals like [sigh], [breathe], [laugh] go anywhere in the text.

> What is the latency? Sub-200ms median time-to-first-audio for the TTS layer alone. End-to-end through the Realtime API depends on what reasoning has to do, but the pipeline is designed to stay alive while reasoning runs: backchannel fillers stream in parallel, anticipatory generation begins before reasoning finishes, and partial responses reach the user before the full sentence is composed.

> What is the pricing model? Pricing is metered per character (about 1,000 characters per minute of audio) and lives at inworld.ai/pricing. Pay-as-you-go with volume tiers. Realtime TTS-2 ships under the same metering as Realtime TTS 1.5, so customers upgrading do not see a model-side pricing change.