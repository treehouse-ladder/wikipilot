---
fetched_at: &id001 2026-07-25
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: cabbd7e35eddedf4c0e4273db3ec9e6b39ef732b130851f3a17e15f2533f996a
sources: []
title: Introducing Cursor Router
topic: agentic-coding
url: https://cursor.com/blog/router
---

## Excerpts

> Cursor Router is a classifier that inspects each request before a model runs, then dispatches it to the model best suited to that specific task. Simple work goes to the most price-efficient models, UI updates go to the model with the best taste, and complex, long-horizon problems go to frontier reasoning models.

> For each request, the router analyzes four inputs: query, context, task complexity, and domain, combined with learned knowledge of each model's behavior.

> Cursor Router was trained on 600k+ live requests and evaluated performance in an online A/B test across millions of live requests, optimizing for user satisfaction (AFC) as a reward.

> The cursor team reports frontier-quality performance at 60% savings in online A/B tests, and 30-50% savings for early-access enterprise accounts, versus routing everything to Opus 4.8.

> The three modes are: Intelligence mode (optimizes for frontier-quality output), Balance mode (targets strong quality at meaningfully lower cost), and Cost mode (optimizes for token efficiency on routine work).