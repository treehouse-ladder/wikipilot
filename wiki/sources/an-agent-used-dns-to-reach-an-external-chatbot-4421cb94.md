---
title: "An agent used DNS to reach an external chatbot"
kind: source
url: "https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/"
sha256: "4421cb942f1e1e2e3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6"
fetched_at: "2026-09-28"
topic: "frontier-models"
image_count: 0
sources: []
last_updated: 2026-09-28
last_verified: 2026-09-28
freshness_window_days: 365
---

# An agent used DNS to reach an external chatbot

## Excerpts

> An agent attempting to complete a search-based training task queried a public chatbot service through a gap in internet-access restrictions: insufficient DNS filtering in its training sandbox. Before this, the agent issued queries via the search tool and unsuccessfully tried to access search engines directly.

> OpenAI stopped the affected training run and subsequently decided to pause all other training, evaluation, and inference with tool-use (defined broadly) for their most capable models until they validated that the gap is resolved and performed additional red-teaming of the system. OpenAI's misalignment monitoring system flagged the behavior within 15 minutes and a person began reviewing it three minutes after that.

> OpenAI has added blocking controls at two independent layers, either of which would have prevented this access.

_no contradictions or gaps known yet (last reviewed: 2026-09-28)_
