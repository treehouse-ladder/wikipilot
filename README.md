# Wikipilot

An autonomous-research, Obsidian-friendly wiki maintained by [Claude Code Cloud Routines](https://docs.anthropic.com/en/docs/claude-code/web-scheduled-tasks).

Inspired by [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). The core idea: instead of having LLMs re-derive knowledge from raw documents at every query (RAG), we let them **incrementally build and maintain a persistent wiki** — a structured, interlinked collection of markdown files that compounds with every source. The wiki is a persistent, compounding artifact: cross-references are already there, contradictions have already been flagged, the synthesis already reflects everything we've ingested.

## What this is

Three Claude Code Cloud Routines run on Anthropic's infrastructure (no laptop required) and maintain the wiki in `wiki/`:

- **Daily Research** (cron daily 06:00 + API trigger) — for each topic in [`topics.yaml`](topics.yaml), a topic-researcher subagent searches the web, drafts cited synthesis with cross-page sweeps, downloads source images locally, and opens **one PR per topic per day**.
- **Wiki Query** (GitHub-issue trigger with `/query` label + API trigger) — answers an ad-hoc question against the existing wiki using a qmd MCP search, files the answer back as a new page in `wiki/answers/`, comments on the originating issue.
- **Weekly Health** (cron weekly Sunday 03:00) — runs an LLM-judge semantic stale-claim sweep, files contradictions/staleness as `## Disputes` proposals for human review, writes a health report.

Every PR auto-merges if lint and tests pass and the diff is under threshold; otherwise it stays open with a structured review checklist.

## Local view

The wiki at `wiki/` is a plain git-versioned Obsidian vault. Open it in Obsidian to read, navigate the graph view, and (rarely) edit pages by hand.

## Architecture

See [`docs/architecture.md`](docs/architecture.md) for the full diagram and prose.

## Schema

The conventions Claude follows when maintaining the wiki — frontmatter contract, page sections, file ownership matrix, citation discipline, model selection per agent — live in [`CLAUDE.md`](CLAUDE.md). This is the highest-leverage file in the repo; co-evolve it as you learn what works for your domain.

## Project status

In active development. Phase plan checked into `.cursor/plans/`. Currently bootstrapping (Phase 0).

## License

MIT — see [LICENSE](LICENSE).
