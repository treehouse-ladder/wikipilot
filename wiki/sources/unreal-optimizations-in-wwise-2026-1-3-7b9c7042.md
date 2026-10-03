---
fetched_at: &id001 2026-10-03
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 7b9c7042e8b889404cfd6978b3b6b755aacfbbd39e48ff4850b7772f775a2e62
sources: []
title: Unreal Optimizations in Wwise 2026.1.3
topic: game-music
url: https://www.audiokinetic.com/en/community/blog/unreal-optimizations-in-wwise-2026.1.3/
---

## Excerpts

> The 26.1.3 version of the Wwise Unreal Integration includes extensive optimizations that reduce CPU usage. The architecture has been reworked with the goal of moving as much audio processing as possible from the Unreal game thread to a dedicated audio thread.

> The WwiseProcessing module now manages all calls to the sound engine and Wwise Acoustics through asynchronous jobs and tasks, greatly reducing resource usage on the game thread and allowing for batched, asynchronous audio processing.