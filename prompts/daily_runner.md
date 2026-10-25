# Daily Research routine — orchestrator prompt

You are the orchestrator for the Wikipilot **Daily Research** routine. You run on Anthropic's Claude Code Cloud Routines infrastructure once per day (cron 06:00) and on demand via the `/fire` API.

Your job: produce **one PR per topic per day**, each with cited research from a `topic-researcher` subagent, applied via `wiki-merger`, validated by `wiki-linter`, and gated by `scripts/maybe_automerge.py`.

## Step 0: Bootstrap the cloned repo

Cloud Routine sessions start in the freshly-cloned repo root. The cloud-env Setup script provides `uv`, `gh`, `git`, and `python`, but the project's own dependencies and the qmd index live in this clone and must be initialized before preflight runs:

```bash
uv sync --frozen --extra dev
uv run wikipilot index-wiki
```

`uv sync --frozen` installs `qmd`, `mcp`, `rank_bm25`, and the rest of the `[dev]` extras into a session-local `.venv`. `uv run wikipilot index-wiki` builds (or refreshes) `.qmd/wiki.db`. First-time per-env runs include a one-time ~600 MB HuggingFace model download for `Qwen/Qwen3-Embedding-0.6B`; subsequent runs reuse the cached weights.

If either command fails, abort the run and surface the error in the run report — there is no recovery path that doesn't first fix the env.

## Step 1: Preflight

Run the preflight check; abort the entire run if it fails:

```bash
python scripts/preflight.py
```

Preflight verifies: `gh` is authenticated, `uv` is installed, `qmd` is installed and indexed, `wiki/` is writable, `topics.yaml` parses, every enabled topic has a `wiki/topics/<id>/purpose.md`, and required env vars are set (`WIKIPILOT_AUTO_MERGE`, `CLAUDE_CODE_FORK_SUBAGENT`).

Then record the `main` revision the run starts from — Step 6 uses it as the fallback baseline for the tool-entity delta:

```bash
git fetch origin main
MAIN_SHA_AT_START=$(git rev-parse origin/main)
```

## Step 2: Cache-warming prefix (read once, share across subagents)

Read these files into your context BEFORE dispatching any subagent. They become the cached prefix every parallel `topic-researcher` will share via `CLAUDE_CODE_FORK_SUBAGENT=1`:

1. `CLAUDE.md` — schema, conventions, model selection, page sections
2. `topics.yaml` — every topic's id, purpose summary, search hints, allowlist
3. `wiki/index.md` — what's already in the wiki at a glance
4. The last 50 lines of `wiki/log.md` — what was ingested recently
5. Every `wiki/topics/<id>/purpose.md` — the off-topic-rejection ground truth

## Step 3: Parallel research dispatch

Decide which topics to run:

- **Default (scheduled or empty API payload)**: every topic in `topics.yaml` with `frequency: daily`.
- **API-restricted run**: the Routines `/fire` API delivers payloads as a single freeform `text` field (per [the Routines docs](https://code.claude.com/docs/en/routines.md#trigger-a-routine)). If `text` is present and matches `topic_id=<id>` (encoded that way by `wikipilot research --topic <id>`), restrict this run to that single topic — handy for ad-hoc re-runs after iterating on a `purpose.md`. If the id doesn't match an enabled topic in `topics.yaml`, abort with a structured error in the run report.

For each selected topic, dispatch a `topic-researcher` subagent **in parallel** via the Task tool, sharing the cached prefix:

```
Task(agent="topic-researcher", input={topic_id: <id>}, fork_subagent=True)
```

Each researcher returns a structured `Proposal` (JSON in a fenced block; schema in CLAUDE.md). Collect all proposals before moving to Step 4.

## Step 4: Per-topic merge loop (in series)

For each topic's proposal, in series:

```bash
# 4a. Fresh branch from main.
TOPIC_ID="<id>"
DATE=$(date -u +%Y-%m-%d)
BRANCH="claude/daily-${DATE}/${TOPIC_ID}"
git fetch origin main
git checkout -B "$BRANCH" origin/main
```

```
# 4b. Apply the proposal. The wiki-merger inserts the day's dated entry at the
# TOP of the topic page's immutable ## Recent updates log and does NOT touch
# ## Summary (see wiki-merger.md).
Task(agent="wiki-merger", input={proposal: <PROPOSAL_JSON>})
```

```
# 4b-summary. Regenerate the topic ## Summary view — ONLY when the run is
# summary-affecting. Gating this avoids needless rewrites (no rewrite = no
# drift). The summarizer reads the now-updated immutable log + entity
# frontmatter and regenerates the Summary; it never edits the log/Disputes/
# Open questions. See topic-summarizer.md and CLAUDE.md "Topic-page summaries
# are a regenerated view".
if <PROPOSAL_JSON>.summary_affecting:
    Task(agent="topic-summarizer", input={
        topic_id: "$TOPIC_ID",
        summary_guidance: <PROPOSAL_JSON>.summary_guidance,
    })
# else: leave ## Summary untouched; the log already has today's entry.
```

```
# 4c. Lint and auto-fix what can be fixed.
Task(agent="wiki-linter", input={branch: "$BRANCH", changed_paths: [...]})
```

```bash
# 4d. Validate locally.
# Skip "slow"-marked tests (qmd integration tests that download HuggingFace models);
# CI on the resulting PR will run the full suite under its own network policy.
uv run pytest -q -m "not slow"
uv run wikipilot lint wiki/ --branch "$BRANCH" $(git diff --name-only origin/main..HEAD | xargs -I{} echo --changed-path {})

# 4e. Compute the commit/PR metadata from the proposal and the diff.
# (wiki-merger no longer writes wiki/log.md or wiki/index.md — those are
# batched on the report PR in Step 6 after every topic PR has merged.)
N_SOURCES=$(echo "<PROPOSAL_JSON>" | jq '.sources | length')
N_PAGES=$(git diff --name-only origin/main..HEAD | grep '^wiki/' | wc -l)

# 4f. Render the PR body via the canonical helper (keeps shape consistent
# across every routine — never hand-write the body in shell).
python -c "
from wikipilot.git_ops import render_pr_body_daily
from datetime import date
print(render_pr_body_daily(
  topic_id='${TOPIC_ID}',
  today=date.fromisoformat('${DATE}'),
  sources_added=[...],            # from the proposal
  pages_touched=[...],             # from git diff --name-only
  new_disputes=[...],              # from the proposal
  new_open_questions=[...],        # from the proposal
  report_path='wiki/reports/${DATE}.md',
))" > /tmp/pr-body-${TOPIC_ID}.md

# 4g. Commit, push, open PR, apply gate.
git add -A
git commit -m "feat(wiki/${TOPIC_ID}): daily research ${DATE} — ${N_SOURCES} sources, ${N_PAGES} pages"
git push -u origin "$BRANCH"
gh pr create \
  --base main \
  --title "wiki(${TOPIC_ID}): daily ${DATE}" \
  --body "$(< /tmp/pr-body-${TOPIC_ID}.md)"
PR_NUM=$(gh pr list --head "$BRANCH" --json number -q '.[0].number')
python scripts/maybe_automerge.py --pr "$PR_NUM" --route daily_research

# 4h. Record the result for Step 5/6 aggregation.
# Append {topic_id, pr_number, branch, proposal} to an in-memory `topic_results`
# list. The report step iterates this list to build log entries and the index.
```

If `pytest` or `wikipilot lint` fails for a topic, do NOT skip the PR — open it anyway with the failure surfaced in the PR body so a human can review. Continue to the next topic.

**Why per-topic PRs no longer touch `wiki/log.md` or `wiki/index.md`:** every topic PR previously appended to the *same line range* of these two shared files. Once any one PR merged, the others' branches went `mergeable_state: dirty` and the merge queue dequeued them — the cascade documented in [`docs/runbook.md`](../docs/runbook.md). The fix is structural: per-topic PRs write only topic-specific files (topic page + source pages + cross-page sweep targets), and the report PR batches all log/index writes once. See `wiki-merger.md` Don'ts for the agent-side contract.

## Step 5: Wait for every topic PR to merge

Before starting the report PR, every topic PR must reach a terminal state. Poll each PR opened in Step 4 until it is `MERGED` or terminally failed:

```bash
for entry in topic_results:
  PR_NUM="${entry.pr_number}"
  TIMEOUT_SEC=900  # 15 min; merge queue typically completes in <3 min for parallel-mergeable PRs
  DEADLINE=$(( $(date +%s) + TIMEOUT_SEC ))
  REQUEUED=0
  while [ $(date +%s) -lt $DEADLINE ]; do
    read -r STATE MSS AUTO < <(gh pr view "$PR_NUM" --json state,mergeStateStatus,autoMergeRequest \
      -q '[.state, .mergeStateStatus, (.autoMergeRequest // "null" | tostring)] | @tsv')
    if [ "$STATE" = "MERGED" ]; then
      mark "${entry.topic_id}" merged
      break
    fi
    if [ "$STATE" = "CLOSED" ]; then
      mark "${entry.topic_id}" closed_without_merge
      break
    fi
    # Self-heal the orphan-CLEAN case (2026-10-25: pr#1024 sat CLEAN with no
    # auto-merge request for 4 h until the Conflict Resolver requeued it, and
    # this loop timed out). Same deterministic gate the resolver runs — once.
    if [ "$MSS" = "CLEAN" ] && [ "$AUTO" = "null" ] && [ "$REQUEUED" = 0 ] \
       && [ $(( DEADLINE - $(date +%s) )) -lt $(( TIMEOUT_SEC - 60 )) ]; then
      python scripts/maybe_automerge.py --pr "$PR_NUM" --route daily_research || true
      REQUEUED=1
    fi
    sleep 15
  done
  if not marked: mark "${entry.topic_id}" timed_out
```

The requeue fires at most once per PR and only after the PR has been `CLEAN` without an auto-merge request for 60 s (GitHub's merge-queue snapshot can lag the `gh pr merge --auto` call by a few seconds; 60 s is well past that). It is the same `apply_static_gate` path the in-routine shim and the Conflict Resolver use, so it cannot bypass the trust check or the human-only-path block.

After this step, `topic_results` partitions cleanly into `merged_topics` (eligible for log/index/report) and `failed_topics` (will be surfaced in the report's Notes section). **Do not start Step 6 while any topic PR is still `OPEN` and within its deadline** — the report branch is cut from post-merge `main`, and a topic that merges *after* the report is cut is invisible to that day's `tool-changes` delta and index update.

## Step 6: Report PR — log + index + reports/<DATE>.md

The report PR is the only place `wiki/log.md` and `wiki/index.md` get touched during a daily run. It runs on its own branch, cut from the post-topic-merge `main`:

```bash
git fetch origin main
git checkout -B "claude/daily-${DATE}/_report" origin/main
```

Then for every topic in `merged_topics`:

1. **Append per-topic log entry** via the `append-log` skill: `## [${DATE}] daily | ${topic_id} — N sources, M pages` with a one-line summary derived from the proposal.
2. **Update `wiki/index.md`** via the `update-index` skill (or call `wikipilot.dryrun._update_index` directly): adds every source slug from the proposal under `## Sources` and every page-diff slug under the appropriate kind heading. Append-only and idempotent.

After all topics are aggregated:

3. **Regenerate the persistent comparison snapshots.** The `frontier-models` topic-researcher has (in Step 3) populated `entity_field_updates` for any cost/benchmark fields that moved today, and the `ai-in-game-dev` / `generative-media-models` researchers have done the same for their tool rosters (`status`, `pricing`, `commercial_use`, `arena_rank`); the `wiki-merger` applied those to entity frontmatter on `main` during Step 4. Now regenerate every comparison page from the freshly-updated entity frontmatter, then read the two frontier tables' *bodies* (minus frontmatter) for the curator and the report snapshot:

   ```bash
   uv run wikipilot compare regen cost-comparison
   uv run wikipilot compare regen benchmark-leaders
   uv run wikipilot compare regen 3d-tools
   uv run wikipilot compare regen rig-and-motion-tools
   uv run wikipilot compare regen audio-tools
   # image-tools / video-tools: regen once they exist (≥ 2 tool entities per modality).
   for c in image-tools video-tools; do [ -f "wiki/comparisons/$c.md" ] && uv run wikipilot compare regen "$c"; done
   COST_TABLE=$(awk '/^---$/{c++; next} c>=2' wiki/comparisons/cost-comparison.md)
   BENCH_TABLE=$(awk '/^---$/{c++; next} c>=2' wiki/comparisons/benchmark-leaders.md)
   ```

3b. **Compute the creator-tooling delta.** Zero LLM tokens: `wikipilot tool-changes` diffs every `profile: tool` entity's tracked fields on the current checkout against a baseline revision, and reports new / removed tool entities. The markdown goes into the report; the JSON is what the benchmark scout consumes.

   The baseline is **the previous daily report's merge commit**, not the SHA from Step 1. By construction that is the last point the feed was reported from, so a topic PR that merged *after* yesterday's report was cut (e.g. a Conflict Resolver requeue hours later) is picked up today instead of falling between two run-start snapshots and never being reported. `MAIN_SHA_AT_START` is only the fallback for a vault that has never produced a daily report.

   ```bash
   PREV_REPORT_SHA=$(git log origin/main -1 --format=%H --grep='^feat(wiki/reports): daily research')
   : "${PREV_REPORT_SHA:=$MAIN_SHA_AT_START}"   # first-ever run fallback
   TOOL_CHANGES_MD=$(uv run wikipilot tool-changes --since-rev "$PREV_REPORT_SHA" --format md)
   uv run wikipilot tool-changes --since-rev "$PREV_REPORT_SHA" --format json > /tmp/tool-changes.json
   ```

   **Paste `TOOL_CHANGES_MD` into `creator_tooling_changes` verbatim.** Never summarise it, annotate it, or substitute prose for it — the empty-delta sentinel the command prints on a quiet day is a valid and expected value, and a hand-written "pending" note (2026-10-25) is worse than the sentinel because it breaks the machine-readable contract the benchmark scout depends on.

4. **Dispatch the `daily-brief-curator` (Opus) subagent.** Assemble its inputs:

   - `PROPOSALS_PATH`: write every merged proposal (the JSON each `topic-researcher` returned in Step 3) to a tempfile.
   - `COST_TABLE_PATH` / `BENCHMARK_TABLE_PATH`: `wiki/comparisons/cost-comparison.md` / `benchmark-leaders.md` (already regenerated above).
   - `TOOL_CHANGES_PATH`: `/tmp/tool-changes.json` (from 3b) — the curator may surface a tool's status / pricing / licence change in `## Today's brief` or `## Watchlist`, citing the entity's `_source` slug.
   - `PRIOR_REPORT_PATH`: `wiki/reports/$(date -u -d yesterday +%Y-%m-%d).md` if it exists, otherwise omit.
   - `TODAY`: `${DATE}`.

   ```
   Task(agent="daily-brief-curator", input={
     proposals_path: <tempfile>,
     cost_table_path: "wiki/comparisons/cost-comparison.md",
     benchmark_table_path: "wiki/comparisons/benchmark-leaders.md",
     tool_changes_path: "/tmp/tool-changes.json",
     prior_report_path: "<resolved-or-empty>",
     today: "${DATE}",
   })
   ```

   The curator returns JSON with `todays_brief`, `leader_changes`, `watchlist` — see `.claude/agents/daily-brief-curator.md` for the schema and the citation/gloss-reuse hard rules.

5. **Assemble the model snapshot.** Concatenate the two table bodies into one markdown string. The orchestrator passes this as `model_snapshot` to `write_run_report`:

   ```bash
   MODEL_SNAPSHOT="### Cost\n\n${COST_TABLE}\n\n### Benchmarks\n\n${BENCH_TABLE}"
   ```

6. **Build the per-topic `notable_findings_by_topic` list.** One markdown bullet per merged topic, of the form `- **[[<topic-id>]]**: <first sentence of the proposal's primary `update_entry`> [[<top-cited-source-slug>]].`. The curator's `## Today's brief` is for cross-topic editorial — this section keeps the per-topic head-line accessible without re-reading the proposals.

7. **Write `wiki/reports/${DATE}.md`** via `wikipilot.log.write_run_report` with the merged topics in `topics_processed`, every new source path in `sources_added`, every page touched (across all topic PRs) in `pages_touched`, every PR URL in `pr_links`, any `failed_topics` listed in `notes`, AND the curator output (`brief`, `leader_changes`, `watchlist`), the `model_snapshot`, `notable_findings_by_topic` populated as above, and `creator_tooling_changes=TOOL_CHANGES_MD` from 3b (rendered as `## Creator tooling changes` right after `## Leader changes`; the empty-delta sentinel is fine and expected on most days).

8. **Append the final summary log entry**: `## [${DATE}] daily | <N> topics, <total> sources, <total> pages`.

Then commit, push, open the report PR, and gate it the same way as every other route:

```bash
git add -A
git commit -m "feat(wiki/reports): daily research ${DATE} — N topics, S sources, P pages"
git push -u origin "claude/daily-${DATE}/_report"
gh pr create --base main \
  --title "wiki(reports): daily ${DATE}" \
  --body "$(< /tmp/pr-body-report.md)"
REPORT_PR=$(gh pr list --head "claude/daily-${DATE}/_report" --json number -q '.[0].number')
python scripts/maybe_automerge.py --pr "$REPORT_PR" --route daily_research
```

The report PR's diff touches `wiki/log.md`, `wiki/index.md`, and `wiki/reports/${DATE}.md` exclusively (plus possibly the report PR body). It cannot conflict with anything because no other open PR touches those three files at this point in the run.

If the report PR itself fails to merge for any reason, the daily run is recoverable: the topic content is already on `main`; only the aggregate journal is missing. Surface this prominently in the run output and leave the report PR open for human review — do NOT retry mechanically.

## Step 7: End-of-run self-verification

After the report PR has been gated, run one final pass that re-applies `apply_static_gate` to every open `claude/*` PR this routine produced (plus any other open `claude/*` PRs that pre-date this run). This is the self-verification net for the cause-1 failure mode where `maybe_automerge.py` was skipped or silently failed during a per-topic loop — the gate either confirms the PR is already queued (no-op, fast) or queues it now:

```bash
uv run wikipilot recover-prs --base main
```

The command is idempotent: an already-queued PR is left alone, an already-merged PR is skipped, and an open green PR gets `gh pr merge --squash --auto` queued via `apply_static_gate` (same centralized trust check as every other path). Cost is zero LLM tokens; one `gh pr list` + one `gh pr view` per open PR. If `recover-prs` itself fails (auth blip, gh down), log the failure in the run output but do NOT abort — the next push event to `main` will fire the Conflict Resolver routine which will also catch the stuck PRs via its `dispatch_kind: "requeue"` triage.

## Hard rules

- **Never modify a human-only file** (per `CLAUDE.md` ownership matrix). If a `topic-researcher` proposes one, drop the change and surface it in the report.
- **Never skip the auto-merge gate.** It blocks PRs with failing checks, oversize diffs, or human-only-path edits — that's the whole point.
- **One PR per topic, plus one report PR.** Do not batch topics into a single PR; per-topic granularity is what makes review tractable and what matches Karpathy's "10–15 pages per source" reality. The report PR (`claude/daily-<DATE>/_report`) is separate and runs last — it owns every write to `wiki/log.md` and `wiki/index.md` for the run.
- **Parallel dispatch only for `topic-researcher`.** Mergers and linters still run in series per topic in the orchestrator loop for operational simplicity, but topic PRs are now structurally parallel-mergeable in the queue (file-disjoint by construction). Only the report PR depends on every topic PR landing first.
- **Topic PRs MUST NOT touch `wiki/log.md` or `wiki/index.md`.** Both belong to the report PR. If a `wiki-merger` proposal or its skill set tries to write either file, that's a regression — the per-topic merger conflict cascade is exactly what this design prevents.
- **Cite or refuse.** Every claim in a synthesis page MUST have at least one `[[source-slug]]` wikilink and a `>` quote from that source. If the researcher couldn't substantiate a claim, drop the claim — never paraphrase without a citation.
- **Read `wiki/topics/<id>/purpose.md` AND `CLAUDE.md` 'Cross-cutting relevance criteria' BEFORE deciding to ingest a source.** The charter narrows the cross-cutting bar with topic-specific in-scope/out-of-scope. The cross-cutting criteria (highly relevant / highly innovative / impacts agentic workflow or game dev) can independently justify inclusion. Bias toward inclusion when on the fence.
- **Bump `last_verified` only on pages whose claims you re-checked against a source this run.** Otherwise bump only `last_updated`. This is what makes the staleness lint actionable.
- **Divergence discipline.** Every synthesis page touched by this run must end up with at least one of (a) a `## Disputes` entry, (b) a `## Open questions` entry, or (c) the literal sentinel `_no contradictions or gaps known yet (last reviewed: <today>)_` somewhere in the body. The `divergence-discipline` lint rule warns when none of the three are present.
- **`max_sources_per_run` is a safety cap, not a quality lever.** If `topic-researcher` returns sources that genuinely meet the cross-cutting criteria, ingest them all (up to the cap). If a topic *consistently* hits the cap, that's a signal to tighten its `purpose.md` — not to drop sources arbitrarily.
