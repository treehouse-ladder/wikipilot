# Routines setup

Step-by-step for creating each Wikipilot routine in `claude.ai/code/routines`. The qmd MCP connector is shared across all three; set it up once first.

## Prerequisites

- A GitHub repo containing this codebase, with the GitHub App for Claude Code installed (Settings → GitHub Apps → Claude Code).
- An Anthropic plan with routines enabled (Pro / Max / Team / Enterprise — daily run caps differ).
- Local: `gh auth login`, `uv` installed, `python 3.12+`.

## qmd MCP connector (one-time, shared by all routines)

Wikipilot uses [qmd](https://pypi.org/project/qmd/) as its hybrid BM25 + vector search layer over `wiki/`, exposed to subagents via MCP. Without it, `topic-researcher` and `query-answerer` would have to grep the wiki manually.

1. **Local install**: `pip install qmd` (or `uv pip install qmd` inside your venv).
2. **Index your vault** (run from repo root):
   ```bash
   uv run wikipilot index-wiki --full
   ```
   Subsequent runs are incremental (the cloud setup script calls this on every routine start).
3. **Register the connector in claude.ai**:
   - claude.ai → Settings → Connectors → Add MCP server
   - Server command: `qmd serve --mcp --vault wiki/`
   - Save and verify the `qmd-search` tool appears in your connector list.
4. Confirm the connector by running a routine in dry-run mode (Step 4 below).

See [`docs/qmd-setup.md`](qmd-setup.md) for local-dev qmd setup details.

## Daily Research routine

claude.ai/code/routines → New routine → Remote.

| Field | Value |
|---|---|
| Name | `Wikipilot Daily Research` |
| Repository | this repo, default branch `main` |
| Setup script | `curl -LsSf https://astral.sh/uv/install.sh \| sh && uv sync --frozen --extra dev && pip install qmd && uv run wikipilot index-wiki` |
| Connectors | qmd (only) — minimize attack surface |
| Env vars | `WIKIPILOT_AUTO_MERGE=true`, `CLAUDE_CODE_FORK_SUBAGENT=1` |
| Branch policy | Default. Cloud routines can only push to `claude/*` (which is what `git_ops.branch_for_daily` produces). |
| Network | Default policy is fine — WebSearch goes through Anthropic infra. |
| Triggers | (a) Schedule: daily 06:00 local. (b) **API trigger** (added after first save): copy URL + bearer token, paste into `~/.config/wikipilot/credentials.toml` under `[research]` for `wikipilot research --topic <id>`. |
| Model | **Sonnet** (orchestrator only — `topic-researcher` and `wiki-merger` subagents pin their own models via `.claude/agents/*.md` frontmatter). |
| Prompt | Copy `prompts/daily_runner.md` into the routine UI. We don't auto-sync because routines aren't yet API-managed. |

Daily-cap note: scheduled routines count against your plan's daily cap (Pro 5/day, Max 15/day, Team/Enterprise 25/day). Daily Research is one scheduled run/day regardless of topic count; API-triggered runs share the cap.

Beta header note: Routines API uses `experimental-cc-routine-2026-04-01`.

## Wiki Query routine

| Field | Value |
|---|---|
| Name | `Wikipilot Query` |
| Repository | same repo, default branch `main` |
| Setup script | same as Daily Research |
| Connectors | qmd (same) |
| Env vars | same |
| Triggers | (a) **GitHub trigger** (preferred for human use): see [GitHub-issue trigger](#github-issue-trigger-for-wiki-query) below. (b) **API trigger**: copy URL + token from the routine UI, paste into `~/.config/wikipilot/credentials.toml` under `[query]`. No schedule trigger (on-demand only). |
| Model | **Sonnet** (orchestrator); `query-answerer` subagent pins **Opus 4.7** via its frontmatter. |
| Prompt | Copy [`prompts/query_answerer.md`](../prompts/query_answerer.md) into the routine UI. |

### GitHub-issue trigger for Wiki Query

The Claude GitHub App turns labeled GitHub issues into routine fires. Setup:

1. **Install the Claude GitHub App** on this repo (Settings → GitHub Apps → Claude Code).
2. **Add the `query` label** to your repo (Settings → Labels → New label, name `query`, description "Triggers Wikipilot Wiki Query routine").
3. In the routine UI, **enable the GitHub trigger** with these filters:
   - Event: `issue.opened`
   - Filter: `Labels include: query`
4. Save.

Now any new issue with the `query` label kicks off a Wiki Query run. The orchestrator reads the issue body as the question (first non-empty line is the question; remaining lines are optional context), files an answer page back to `wiki/answers/`, opens a PR, and comments the answer on the issue with a link to the PR.

If the GitHub App can't be installed (private org policy, etc.), the API trigger is a drop-in substitute — `wikipilot query "<question>"` from the CLI does the same thing without going through GitHub.

## Weekly Health routine

| Field | Value |
|---|---|
| Name | `Wikipilot Weekly Health` |
| Repository | same |
| Setup script | same |
| Connectors | qmd (same) |
| Env vars | same |
| Triggers | Schedule: weekly Sunday 03:00 local. (No API trigger — weekly health is intentionally cheap and predictable.) |
| Model | **Sonnet** (orchestrator AND `wiki-disputes-scanner` subagent — both pin Sonnet via their frontmatter). |
| Prompt | Copy [`prompts/weekly_health.md`](../prompts/weekly_health.md) into the routine UI. |

The routine seeds candidate page sets with `scripts/disputes_seed.py` (overlap heuristics: shared backlinks among recent-source citers, plus a generic stale-by-`last_verified` set), fans out one `wiki-disputes-scanner` subagent per set in parallel, then applies every scanner's `## Disputes` proposals to a single `claude/health-YYYY-MM-DD` branch in series (one PR per week). The scanner **never auto-resolves** — every dispute lands as `Status: unresolved` for human review.

Tune the seed at the routine level by editing the prompt to pass `--top-k`, `--stale-k`, or `--lookback-days` (defaults: 10 / 10 / 7 days).

Daily-cap note: weekly routines count against the daily cap on the day they run.

## Triggering via API

Once the API trigger is configured for Daily Research and Wiki Query, you can fire them from the CLI:

```bash
uv run wikipilot research --topic ai-agents
uv run wikipilot query "what is the fastest way to dispatch parallel subagents?"
```

These POST to the routines' `/fire` endpoints with the bearer token from your credentials file. See [`runbook.md`](runbook.md) "Storing the API tokens".

## Verifying setup

After creating a routine, click **Run now** in the routine UI (this doesn't count against your daily cap). Watch the logs:

1. Preflight should pass.
2. Cache-warming files should be read.
3. For Daily Research: each topic should produce a `topic-researcher` subagent invocation (parallel), then a per-topic merger/linter/PR sequence (series).
4. PRs should appear on `claude/daily-YYYY-MM-DD/<topic-id>` branches with auto-merge enabled (or open with a review checklist comment if the gate blocked).

If any step fails, check `runbook.md` "Troubleshooting" (populated in Phase 8 with everything that bit us during the live smoke test).
