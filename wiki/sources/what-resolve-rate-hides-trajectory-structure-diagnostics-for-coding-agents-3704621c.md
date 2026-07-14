---
fetched_at: &id001 2026-07-14
freshness_window_days: 365
image_count: 0
kind: source
last_updated: *id001
last_verified: *id001
sha256: 3704621c105c6a41a3b028f736016af0e2bd607bd54889c22394ef0dd3e9d28a
sources: []
title: 'What Resolve Rate Hides: Trajectory Structure Diagnostics for Coding Agents'
topic: agentic-coding
url: https://arxiv.org/abs/2607.06184
---

## Excerpts

> Coding agents are ranked almost entirely by resolve rate (whether their final patch passes tests), yet two agents can reach the same outcome through very different processes, and a single pass/fail label says nothing about why a run failed or why an accepted run spent extra steps, time, or tokens.

> TRACEPROBE, a trajectory-diagnostic framework that normalizes each raw run into a canonical nine-type action taxonomy with deterministic effect labels, then applies two rule-based modules: INSIGHT names single-trajectory anti-patterns adapted from established debugging practice (e.g., search loops, verification skips), while CONVERGE aligns pairs of runs and classifies where their behavior diverges under controlled references.

> Applying TRACEPROBE to 2,500 trajectories from five production settings on SWE-Bench Verified, file choice is too coarse to separate success from failure, whereas function selection and completion behavior localize it; INSIGHT anti-patterns act mainly as corpus-level difficulty clues, with search loops the most stable; and even resolved runs differ in how quickly they reach relevant code and how much failed work they incur.