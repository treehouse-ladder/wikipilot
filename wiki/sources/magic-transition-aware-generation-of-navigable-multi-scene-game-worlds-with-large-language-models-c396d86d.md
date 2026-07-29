---
fetched_at: &id001 2026-07-29
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: c396d86d47d15f93f6dd13fcc7cf0f39a6ad3f7b4d274d348fb5fc09d27e6a24
sources: []
title: 'MAGIC: Transition-Aware Generation of Navigable Multi-Scene Game Worlds with
  Large Language Models'
topic: ai-in-game-dev
url: https://arxiv.org/abs/2607.11594
---

## Excerpts

> MAGIC is a four-stage pipeline that turns a single natural-language prompt into a runnable multi-scene game project: it plans a shared transition-aware intermediate representation, specifies each scene while enforcing portal reachability with a flood-fill validator, generates the scenes together with their transition scripts, and combines them into one project.

> MAGIC identifies three obstacles that single-scene methods leave unsolved: cross-scene consistency, in-scene navigability, and the evaluation of whether a transition actually works.

> The scene specification stage expands each scene and places objects, rejecting layouts whose portals fail a flood-fill reachability check on a 2D occupancy grid, enforcing navigability.

> On a new benchmark of 100 multi-scene cases, MAGIC produces an executable project for every case and reaches 0.99 precision, 0.95 recall, and 0.96 F1 on end-to-end transition identification.

> The system includes a transition-focused evaluation agent that operates directly on the packaged Unity project, executes each transition in play, and reports Precision, Recall, F1, Approach Rate, and Portal Match Rate against a ground-truth scene plan.