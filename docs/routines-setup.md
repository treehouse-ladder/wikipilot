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
| Triggers | (a) Schedule: daily 06:00 local. (b) **API trigger** (added after first save): copy URL + bearer token, paste into `~/.config/wikipilot/credentials.toml` (Windows: `%APPDATA%\wikipilot\credentials.toml`) under `[research]` for `wikipilot research --topic <id>`. |
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
| Triggers | (a) **GitHub trigger** (preferred for human use): see [GitHub-issue trigger](#github-issue-trigger-for-wiki-query) below. (b) **API trigger**: copy URL + token from the routine UI, paste into `~/.config/wikipilot/credentials.toml` (Windows: `%APPDATA%\wikipilot\credentials.toml`) under `[query]`. No schedule trigger (on-demand only). |
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

## Conflict Resolver routine

This fourth routine **doesn't synthesize wiki content**. It fires on every push to `main` and dispatches an Opus subagent only for the small number of `claude/*` PRs that GitHub's native auto-merge can't move on its own — those whose `mergeStateStatus` is `DIRTY` (text conflicts) or `BEHIND` (out-of-date with base). The 95% happy path runs entirely through `scripts/maybe_automerge.py` (which calls `apply_static_gate` and lets GitHub's required-status-checks rule hold the merge until CI is green), so this routine is a precision tool that fires Opus only when there is actual conflict work to do.

This replaces the previous PR Watcher routine, which fired on every PR event and was unfortunately racing the CI rollup (an empty rollup was being treated as green, which silently stranded PRs in May 2026). See [`CLAUDE.md`](../CLAUDE.md) "Conflict resolution workflow" for the design rationale.

| Field | Value |
|---|---|
| Name | `Wikipilot Conflict Resolver` |
| Repository | same repo, default branch `main` |
| Cloud env | reuse the same env you configured for Daily Research. |
| Connectors | **Leave empty** (this routine never needs qmd; it only inspects PR metadata + the diff of one PR at a time). |
| Permissions tab | "Allow unrestricted git push" → **OFF**. The `conflict-resolver` subagent only force-pushes to `claude/*` branches via `git push --force-with-lease origin "$HEAD_REF"`. |
| Behavior tab | "Auto-fix pull requests" → **OFF**. The routine already implements its narrow surface explicitly; toggling the Anthropic feature would double-fire. |
| Env vars | inherited from the cloud env. |
| Triggers | **GitHub trigger** (only): see [GitHub push trigger](#github-push-trigger-for-conflict-resolver) below. No schedule, no API trigger. |
| Model | **Sonnet** (orchestrator); `conflict-resolver` subagent pins **Opus 4.7** via its frontmatter. |
| Prompt | Copy [`prompts/conflict_resolver.md`](../prompts/conflict_resolver.md) into the routine UI. |

### GitHub push trigger for Conflict Resolver

1. The Claude GitHub App must already be installed on this repo (the [Wiki Query routine setup](#github-issue-trigger-for-wiki-query) walks through this if it isn't).
2. In the routine UI, **enable the GitHub trigger** with these filters:
   - **Event**: `Push`
   - **Filters**:
     - `Branch` `equals` `main`
3. Save.

Now every push to `main` (whether from a merge of a `claude/*` PR or a direct push from a human) spawns one Conflict Resolver session. The orchestrator runs `scripts/conflict_resolver_scan.py`, which returns the JSON list of dispatch-worthy PRs (trusted `claude/*` heads with `mergeStateStatus in {DIRTY, BEHIND}`). The vast majority of fires see an empty list and exit in seconds without any Opus dispatch.

Daily-cap note: ~5-10 pushes to `main` per day on a busy day. Each fires the Sonnet orchestrator; 90%+ of fires are no-ops. Opus tokens only burn when there is real conflict work (typically 1-3 dispatches per day). Comfortably within Pro/Max/Team caps (5/15/25 per day).

### Author trust model (centralized, applies to every gate path)

The trust check exists because GitHub fires `push` events for every commit landing on `main` and the conflict-resolver scan needs to decide which `claude/*` PRs to dispatch the Opus subagent for. The branch name alone is not a security boundary (anyone can name a fork branch `claude/daily-2026-…/anything`). The centralized check at `wikipilot.git_ops.is_pr_trusted` — called by `apply_static_gate`, `apply_gate`, AND the conflict-resolver scan — refuses to queue `--auto` or dispatch the resolver whenever any of the following is true:

- `isCrossRepository` is `true` (the head ref lives in a fork). Fork PRs are never enforce-eligible, even when the author also happens to be an org member.
- `author_association` is **not** in `[automerge.conflict_resolver].trusted_associations` (default `["OWNER", "MEMBER", "COLLABORATOR"]`) **and** `author.login` is **not** in `trusted_authors` (default empty).
- `gh repo view --json nameWithOwner` or `gh api repos/<owner>/<repo>/pulls/<num>` fails for any reason — the check fails closed, treating any missing signal as untrusted.

The defaults are sized for the canonical setup (one user with org-owner membership): every PR you open against `treehouse-ladder/wikipilot` carries `author_association: MEMBER` (GitHub only sets `OWNER` for user-owned repos, not org-owned ones), which is in the default list. Cloud Routine PRs created by the orchestrator use the same identity and pass the same check.

To extend trust to additional contributors:

- **Invite them as collaborators** via Settings → Collaborators. Their PRs to this repo will carry `author_association: COLLABORATOR`, which is in the default trusted list.
- **Whitelist a specific GitHub login** (e.g. a bot account that has no org membership) by adding it to `[automerge.conflict_resolver] trusted_authors` in [`wikipilot.toml`](../wikipilot.toml).
- **Loosen the association set** by editing `trusted_associations` directly. Adding `"CONTRIBUTOR"` would mean any GitHub user with even one prior merged PR auto-trusts — generally not what you want on a public repo.

Untrusted PRs still get a dedupe-keyed checklist comment from `scripts/maybe_automerge.py` so the contributor sees what the gate decided; the gate just never calls `gh pr merge --auto` on them, and the Conflict Resolver routine never dispatches the Opus subagent on them.

### Recovering stranded PRs by hand

If the Conflict Resolver routine misfires (or you have PRs from before it was wired up), run:

```bash
uv run wikipilot recover-prs
```

This enumerates every open `claude/*` PR to `main` and runs `apply_gate` (full gate, including CI) on each in `enforce` mode, inferring the route per PR. The centralized trust check applies here too — no out-of-band vetting needed. See [`runbook.md`](runbook.md) "Recovering stranded PRs" for the troubleshooting workflow.

### Operator handoff (rolling out the new routine)

The code changes in this branch are all additive plus one delete: the new routine is ready to run, but the **routine surface** (claude.ai/code/routines UI) still has the old PR Watcher configured. The handoff has three steps, all on the routine surface — no code edits are needed:

1. **Create the new routine.** In claude.ai/code/routines, create a new routine with the table values above. Paste the contents of `prompts/conflict_resolver.md` into the prompt field. Save. Click "Run now" once with no recent push to verify the prompt parses and the scan exits cleanly with an empty list.
2. **Verify on a real conflict.** Wait for a daily run that produces a known-conflicting pair of PRs (or manually fabricate one by pushing a conflicting commit to one `claude/*` branch). Confirm that on the next merge to `main`, the routine fires, the scan lists the dirty PR, the `conflict-resolver` subagent rebases it, and `apply_static_gate` re-queues auto-merge. The PR should land on `main` within minutes.
3. **Disable the old PR Watcher routine.** In claude.ai/code/routines, find the previous `Wikipilot PR Watcher` entry and either delete it or toggle its triggers off. Do this **only after** step 2 has succeeded — disabling the old routine before the new one is verified would leave the merge queue unguarded.

The trust check, the in-routine `apply_static_gate` call (queues `--auto` immediately, before CI even starts), and `wikipilot recover-prs` all keep working independently of the routine surface — so even during the handoff window, no PR can land without passing the gate.

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
