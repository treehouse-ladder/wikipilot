# Architecture

Wikipilot is a single-repo, Obsidian-friendly wiki maintained by three [Claude Code Cloud Routines](https://docs.anthropic.com/en/docs/claude-code/web-scheduled-tasks). All compute happens on Anthropic's infrastructure; Obsidian runs locally over the same git-versioned `wiki/` directory.

## Multi-routine system overview

Three routines share the same repo, the same agents, and the same MCP connectors. Each produces a different shape of PR.

```mermaid
flowchart TD
    subgraph triggers [Triggers]
        CronD["cron: daily 06:00"]
        CronW["cron: weekly Sun 03:00"]
        Issue["GitHub: issue with /query label"]
        APIr["API: POST /fire (research)"]
        APIq["API: POST /fire (query)"]
    end
    subgraph routines [Claude Code Cloud Routines]
        Daily["Daily Research routine"]
        Query["Wiki Query routine"]
        Weekly["Weekly Health routine"]
    end
    subgraph mcp [Shared MCP connectors]
        Qmd["qmd MCP: hybrid BM25+vector search over wiki/"]
        Gh["GitHub MCP: issue/PR ops"]
    end
    Repo[("Single repo: wikipilot/ (code + wiki/)")]
    CronD --> Daily
    APIr --> Daily
    Issue --> Query
    APIq --> Query
    CronW --> Weekly
    Daily --> Qmd
    Query --> Qmd
    Weekly --> Qmd
    Daily --> Gh
    Query --> Gh
    Weekly --> Gh
    Daily -->|"per-topic PR"| Repo
    Query -->|"per-question PR"| Repo
    Weekly -->|"per-week health PR"| Repo
    Repo -.read.-> Daily
    Repo -.read.-> Query
    Repo -.read.-> Weekly
```

## Daily Research routine: per-topic loop

The most complex of the three. Topic researchers fan out in parallel (sharing the orchestrator's prompt cache via `CLAUDE_CODE_FORK_SUBAGENT=1`), then mergers run in series to produce one PR per topic.

```mermaid
flowchart TD
    Cron["Daily 06:00 schedule"] --> Routine["Daily Research routine"]
    Routine --> Clone["Clone wikipilot repo on Anthropic cloud"]
    Clone --> Setup["Cached setup: uv sync; wikipilot index-wiki (qmd refresh)"]
    Setup --> Orchestrator["Orchestrator: read CLAUDE.md, topics.yaml, wiki/index.md, recent log.md, every wiki/topics/<id>/purpose.md → warm cache"]
    Orchestrator --> Fanout["Parallel Task dispatch with CLAUDE_CODE_FORK_SUBAGENT=1"]
    Fanout --> R1["topic-researcher: topic A (uses qmd MCP + WebSearch)"]
    Fanout --> R2["topic-researcher: topic B"]
    Fanout --> Rn["topic-researcher: topic N"]
    R1 --> P1["Proposal A (cited, cross-page sweep, image refs)"]
    R2 --> P2["Proposal B"]
    Rn --> Pn["Proposal N"]
    P1 --> SerialLoop["For each topic in series:"]
    P2 --> SerialLoop
    Pn --> SerialLoop
    SerialLoop --> Branch["Checkout claude/daily-YYYY-MM-DD/<topic-id>"]
    Branch --> Merger["wiki-merger applies proposal (cross-page sweep, freshness bumps)"]
    Merger --> Images["download-source-images skill writes wiki/assets/<source-slug>/"]
    Images --> Lint["wiki-linter + ruff + pytest + wikipilot lint wiki/"]
    Lint --> Commit["Commit, push, gh pr create"]
    Commit --> Gate{"Per-topic gate: lint+tests green AND diff under threshold AND no human-only file changes?"}
    Gate -- yes --> Auto["gh pr merge --squash --auto"]
    Gate -- no --> Open["gh pr comment with structured review checklist"]
    Auto --> Next["Next topic"]
    Open --> Next
    Next --> Report["After all topics: write wiki/reports/YYYY-MM-DD.md"]
```

## Repo layout

```text
wikipilot/
├── README.md
├── CLAUDE.md                       # the wiki schema (single source of truth)
├── AGENTS.md                       # pointer to CLAUDE.md for non-Claude tools
├── pyproject.toml                  # uv-managed deps, ruff, pytest config
├── topics.yaml                     # human-owned: list of topics
├── wikipilot.toml                  # human-owned: per-route auto-merge thresholds, image policy
├── .claude/
│   ├── agents/                     # 5 subagent definitions (added in Phase 2)
│   └── skills/                     # 8 skill manifests (added in Phase 2)
├── prompts/                        # 3 routine prompts (added in Phases 4, 6, 7)
├── wiki/                           # the Obsidian vault — content source of truth
│   ├── index.md                    # catalog (LLM-write, human-read)
│   ├── log.md                      # chronological append-only
│   ├── topics/<id>/                # topic landing page + human-owned purpose.md
│   ├── concepts/                   # cross-topic concept pages
│   ├── entities/                   # people/projects/orgs
│   ├── sources/                    # one .md per ingested URL
│   ├── answers/                    # Wiki Query answer pages
│   ├── reports/                    # daily and weekly run reports
│   ├── decks/                      # `wikipilot deck` Marp output
│   └── assets/<source-slug>/       # downloaded images
├── src/wikipilot/                  # Python core
├── scripts/                        # operational scripts
├── tests/                          # pytest suite
└── docs/                           # design docs and runbooks
```

## File ownership matrix

The wiki only stays maintainable if it's clear who owns each file. The Python lint enforces this; the auto-merge gate blocks any `claude/*` branch that touches a human-only file.

- **Human-only**: `topics.yaml`, `CLAUDE.md`, `AGENTS.md`, `wikipilot.toml`, `prompts/`, `wiki/topics/<id>/purpose.md`, `README.md`, `LICENSE`, `.claude/`, `docs/`
- **LLM-only**: `wiki/index.md`, `wiki/log.md`, `wiki/sources/`, `wiki/reports/`, `wiki/answers/`, `wiki/decks/`, `wiki/assets/`
- **Mixed**: `wiki/topics/<id>/index.md`, `wiki/concepts/`, `wiki/entities/`

See [`CLAUDE.md`](../CLAUDE.md) for the full conventions, frontmatter contract, citation discipline, and per-agent model assignments.

## Cost shape

- **Daily Research**: O(topics × Opus_cached_prefix × cache_read_multiplier + topics × Opus_proposal_size + topics × Sonnet_merger + topics × Haiku_lint). Opus pricing on `topic-researcher` dominates. Mitigated by `CLAUDE_CODE_FORK_SUBAGENT=1` (shared cached prefix) and `max_sources_per_run` per topic.
- **Wiki Query**: O(1) per question on Opus.
- **Weekly Health**: O(candidate_sets × pages_per_set) on Sonnet — tunable via `K` in `scripts/disputes_seed.py`.

The per-run report (`wiki/reports/YYYY-MM-DD.md` and `health-YYYY-MM-DD.md`) records token usage by model tier, so we can validate the Opus investment with real numbers after Phase 8.
