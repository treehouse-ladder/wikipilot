---
fetched_at: &id001 2026-05-20
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: c78d84ac1a7e3d92b1c154937089c02222f1748af3b0c6ea9a587012b52948e3
sources: []
title: Quantifying infrastructure noise in agentic coding evals (Anthropic Engineering)
topic: agentic-coding
url: https://www.anthropic.com/engineering/infrastructure-noise
---

## Excerpts

> Infrastructure configuration can swing agentic coding benchmarks by several percentage points — sometimes more than the leaderboard gap between top models.

> In experiments running Terminal-Bench 2.0 across six resource configurations with different levels of resource headroom, success rates increased with resource headroom, primarily driven by infrastructure error rates dropping monotonically from 5.8% at strict enforcement to 0.5% when uncapped.

> Unnecessary shared state between runs (leftover files, cached data, resource exhaustion) can cause correlated failures due to infrastructure flakiness rather than agent performance.