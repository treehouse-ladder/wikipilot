# Routines setup

Step-by-step for creating each Wikipilot routine in `claude.ai/code/routines`. The qmd MCP server is wired automatically through the project's `.mcp.json` — there is **no** manual connector registration.

## Prerequisites

- A GitHub repo containing this codebase, with the GitHub App for Claude Code installed (Settings → GitHub Apps → Claude Code).
- An Anthropic plan with routines enabled (Pro / Max / Team / Enterprise — daily run caps differ).
- Local: `gh auth login`, `uv` installed, `python 3.12+`.

## qmd MCP server (auto-wired, no UI registration)

Wikipilot uses [qmd](https://pypi.org/project/qmd/) as its hybrid BM25 + vector search layer over `wiki/`, exposed to subagents via MCP. Without it, `topic-researcher` and `query-answerer` would have to grep the wiki manually.

qmd 0.1.2 doesn't ship its own MCP server — we provide a small FastMCP-based shim at [`scripts/qmd_mcp_server.py`](../scripts/qmd_mcp_server.py) that exposes `qmd_search` and `qmd_collection_info` tools over stdio. Two committed files do all the wiring:

- [`/.mcp.json`](../.mcp.json) — declares the `wikipilot-qmd` stdio server (`uv run python scripts/qmd_mcp_server.py`).
- [`/.claude/settings.json`](../.claude/settings.json) — `enabledMcpjsonServers: ["wikipilot-qmd"]` so cloud routines auto-approve it without an interactive prompt.

When a Cloud Routine container clones the repo and starts a Claude Code session, both files are picked up automatically and the agent gets `mcp__wikipilot-qmd__qmd_search` + `mcp__wikipilot-qmd__qmd_collection_info` in its tool list.

> **Do NOT try to register `wikipilot-qmd` in claude.ai → Settings → Connectors.** That dialog is for **remote URL-based** MCP servers only and will reject our stdio command. The `.mcp.json` mechanism replaces it entirely for stdio servers.

What you still need to do once, locally:

1. **Local install** (only needed for local dev / dry-runs; cloud install happens via the setup script): `uv sync --frozen --extra dev` from the repo root. This pulls in `qmd`, `rank_bm25`, and the `mcp` Python SDK as declared dependencies.
2. **Index your vault** (run from repo root):
   ```bash
   uv run wikipilot index-wiki --full
   ```
   Writes `.qmd/wiki.db` (gitignored). Subsequent runs are incremental (the cloud setup script calls this on every routine start). First-time call also downloads the `Qwen/Qwen3-Embedding-0.6B` model to `~/.cache/huggingface/` (~600 MB, one-time).
3. Confirm the connector loaded by opening any routine's first dry-run output (Step 4 below) and looking for `mcp__wikipilot-qmd__qmd_search` in the tool list.

See [`docs/qmd-setup.md`](qmd-setup.md) for the full local-dev qmd reference, troubleshooting, and the Windows stdio caveat.

## Cloud env setup script

Paste verbatim into the routine cloud env's "Setup script" field. Runs **once per session, before the repo is cloned** — so it can install OS-level binaries but cannot reach `pyproject.toml`. Repo-specific bootstrap (`uv sync`, `wikipilot index-wiki`) lives in the routine prompt's Step 0.

```bash
#!/bin/bash
set -e

# Sanity-check uv (Anthropic cloud-env images ship with uv, git, python pre-installed).
uv --version

# Install gh CLI if missing — `scripts/maybe_automerge.py` shells out to `gh pr merge`.
# We download the static binary from a GitHub release rather than apt to avoid needing
# `cli.github.com` on the network allowlist; `github.com` and `objects.githubusercontent.com`
# are both on the default Trusted set.
if ! command -v gh >/dev/null 2>&1; then
  echo "Installing gh CLI from GitHub releases..."
  GH_VERSION=2.62.0
  ARCH=$(dpkg --print-architecture)
  curl -fsSL "https://github.com/cli/cli/releases/download/v${GH_VERSION}/gh_${GH_VERSION}_linux_${ARCH}.tar.gz" -o /tmp/gh.tar.gz
  tar -xzf /tmp/gh.tar.gz -C /tmp
  install -m 0755 "/tmp/gh_${GH_VERSION}_linux_${ARCH}/bin/gh" /usr/local/bin/gh
  rm -rf /tmp/gh.tar.gz "/tmp/gh_${GH_VERSION}_linux_${ARCH}"
fi
gh --version
```

If your sandbox image already includes `gh` (recent Anthropic cloud-env releases do), the `if !` block becomes a no-op and adds <1s.

## Cloud env network allowlist

Switch the cloud env's network access from **Trusted** to **Custom** and add the following domains. The first two are needed for `wikipilot index-wiki` to download the embedding model on first run; the rest are HF CDN hosts the `huggingface_hub` library hits transparently.

| Domain | Why |
|---|---|
| `huggingface.co` | qmd's embedding model (`Qwen/Qwen3-Embedding-0.6B`) lives here. |
| `cdn-lfs.huggingface.co` | LFS-stored model weights (the actual `.safetensors` blobs). |
| `cdn-lfs-us-1.huggingface.co` | Region-routed LFS CDN. |
| `cas-bridge.xethub.hf.co` | XetHub CDN that some HF models use for chunked uploads. |
| `huggingface-hub.com` | `huggingface_hub` Python client telemetry/metadata. |

The default **Trusted** set already includes `github.com`, `objects.githubusercontent.com`, `pypi.org`, and `files.pythonhosted.org`, which is everything the rest of the bootstrap path needs. You do **not** need to add `astral.sh` (uv is pre-installed) or `cli.github.com` (we install gh from a GitHub release).

After saving, the first cloud-env spin-up downloads the embedding model (~600 MB, one-time per env). Subsequent runs reuse the cached model from `~/.cache/huggingface/`.

## A note on slow tests in routines

Routine prompts run `pytest -q -m "not slow"` (see Step 7 in `prompts/daily_runner.md`, `query_answerer.md`, and `weekly_health.md`). The `slow`-marked tests are the qmd round-trip integration tests, which depend on a real embedding-model download — fine for CI on the resulting PR (which has its own network policy), but would unnecessarily extend every routine run by ~30s and re-download the HF model on cold envs. CI on the merged PR still runs the full suite.

## Daily Research routine

claude.ai/code/routines → New routine → Remote.

| Field | Value |
|---|---|
| Name | `Wikipilot Daily Research` |
| Repository | this repo, default branch `main` |
| Cloud env Setup script | See [Setup script](#cloud-env-setup-script) below — installs `gh` from a GitHub release if missing, sanity-checks `uv`. Repo-specific bootstrap (`uv sync --frozen --extra dev` + `uv run wikipilot index-wiki`) cannot run here because the setup script executes **before** the per-session repo clone; it is therefore moved into the routine prompt's Step 0. |
| Cloud env Network access | **Custom** with the domains listed in [Network allowlist](#cloud-env-network-allowlist) below. The default **Trusted** policy blocks `huggingface.co` (which `wikipilot index-wiki` needs to download the embedding model on first run) and `astral.sh` (which we don't need because `uv` is pre-installed). |
| Connectors | **Leave empty.** The "Connectors" field is for remote URL-based MCP servers; our stdio shim is wired through `.mcp.json` automatically when the agent session starts in the cloned repo. |
| Permissions tab | "Allow unrestricted git push" → **OFF**. Routines push to `claude/*` branches by design; the auto-merge gate handles the move to `main` via `gh pr merge`, never via direct `git push`. |
| Behavior tab | "Auto-fix pull requests" → **OFF** initially. Turn it on later, after several routine runs land cleanly, if you want Claude to babysit failing CI on its own PRs. |
| Env vars (cloud env) | `WIKIPILOT_AUTO_MERGE=true`, `CLAUDE_CODE_FORK_SUBAGENT=1` |
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
| Cloud env | reuse the same env you configured for Daily Research (one env can be selected by all three routines). |
| Connectors | **Leave empty** (wired via `.mcp.json`). |
| Permissions tab | "Allow unrestricted git push" → **OFF**. |
| Behavior tab | "Auto-fix pull requests" → **OFF** initially. |
| Env vars | inherited from the cloud env. |
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
| Cloud env | reuse the same env. |
| Connectors | **Leave empty** (wired via `.mcp.json`). |
| Permissions tab | "Allow unrestricted git push" → **OFF**. |
| Behavior tab | "Auto-fix pull requests" → **OFF** initially. |
| Env vars | inherited from the cloud env. |
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
