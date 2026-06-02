---
title: "SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents"
kind: source
url: "https://arxiv.org/abs/2605.21384"
sha256: "16a403b213e689664fc26810e67e29343699ed75cd5fe9d4d1f0f2568c886d98"
fetched_at: "2026-06-02"
topic: "agentic-coding"
image_count: 0
sources: []
last_updated: "2026-06-02"
last_verified: "2026-06-02"
freshness_window_days: 365
---

# SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents

## Excerpts

> As long-horizon coding agents produce more code than any developer can review, oversight collapses onto a single surface: the automated test suite, and reward hacking naturally arises as the agent optimizes for passing tests while deviating from the users true goal. SpecBench comprises 30 systems-level programming tasks ranging from short horizon tasks like building a JSON parser to ultra long horizon tasks like building an entire OS kernel from scratch. The methodology decomposes software engineering tasks into three parts: (i) a natural language description of the specification (ii) visible validation tests that exercise specified features in isolation, and (iii) held-out tests that compose those same features to simulate real-world usage. The gap also scales sharply with task length: it grows by 28 percentage points for every tenfold increase in code size. Failures range from subtle feature isolation to deliberate exploits, including a 2,900-line hash-table compiler that memorizes test inputs.
