---
fetched_at: &id001 2026-06-08
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: ab5cc8f1ea3c17772ca541b201997838623ced053b9aa27d147393abcfc1b83f
sources: []
title: 'Human oversight of agentic systems in practice: Examining the oversight work,
  challenges, and heuristics of developers using software agents'
topic: agentic-coding
url: https://arxiv.org/abs/2606.05391
---

## Excerpts

> Autonomous software agents hold promise to increase developer productivity but make mistakes and exhibit novel failure modes, making human oversight central to successful human-agent collaboration. We conducted a mixed-methods study of 23 software developers actively using agentic coding tools (Claude Code, Cursor, GitHub Copilot agent mode, Aider) for production work to understand how oversight is practiced today.

> We identify four oversight modalities — pre-flight review (specifying intent), in-flight monitoring (watching execution traces), post-flight verification (testing and reviewing diffs), and trajectory replay (reconstructing what happened after the fact) — and find that developers shift between them based on perceived risk, task novelty, and reversibility.

> Verification is the bottleneck: developers report that 60–70% of their oversight effort lands in post-flight verification because in-flight monitoring scales poorly as agents grow more capable and parallel. Participants reported that they trust trace summaries less than direct file diffs and re-read the diff even when the agent self-reports success.

> Several heuristics emerged: 'shrink the diff' (preferring smaller agent passes that are easier to review), 'trust the test, not the chat' (gating merges on tests rather than the agent's narrative), and 'reversibility first' (giving the agent broader latitude only on operations a human can undo in seconds).