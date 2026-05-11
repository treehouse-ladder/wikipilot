# qmd setup

[qmd](https://pypi.org/project/qmd/) is the local hybrid BM25 + vector search tool Wikipilot exposes to subagents via MCP. The cloud routines install it during their setup script (see [`routines-setup.md`](routines-setup.md)); this page covers local-dev install for offline `wikipilot lint` / `wikipilot dry-run` workflows.

## Local install

```bash
# Inside the wikipilot venv:
uv pip install qmd
qmd --version
```

Or system-wide:

```bash
pip install --user qmd
```

## Initial index

```bash
uv run wikipilot index-wiki --full
```

This builds the index under `.qmd/` (gitignored). On a small wiki (< 100 pages) it takes seconds. The `--full` flag is only needed for first index or after major schema changes; subsequent calls without `--full` are incremental.

## Refresh after writes

The cloud setup script runs `wikipilot index-wiki` (incremental, no `--full`) on every routine start, so cloud runs are always fresh. Locally, you can:

- Run `uv run wikipilot index-wiki` after every batch of edits.
- Or set up a pre-commit hook that runs it before every commit:
  ```bash
  # .git/hooks/pre-commit
  #!/usr/bin/env bash
  set -e
  uv run wikipilot index-wiki
  git add .qmd/  # NOT recommended — keep .qmd/ gitignored
  ```
  (We don't actually want `.qmd/` checked in; the hook just keeps your local index current. The line above is illustrative — most users skip the `git add`.)

## Verifying the MCP connector

Once registered in claude.ai → Settings → Connectors:

1. Open Claude Code locally.
2. Confirm the `qmd-search` tool appears in the available tools list.
3. Run a smoke search: ask Claude "search the wiki for 'attention'" — it should call `qmd-search` and return ranked results from `wiki/concepts/transformer-attention.md` (or wherever your real content lives).

## Why qmd specifically

- Hybrid BM25 + vector means typo-tolerance + synonym-tolerance without an external API call.
- Local-only — no data leaves the machine.
- MCP-native — drops into the routine's connector list with one command.
- Sized for personal-wiki scale (hundreds to low thousands of pages); we'd revisit if your wiki grew past ~10k pages.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `qmd not found` from `wikipilot index-wiki` | `pip install qmd`; ensure your shell PATH includes the user-scripts dir. |
| `qmd serve --mcp` fails to register in claude.ai | Check the qmd version is recent enough to support `--mcp` (≥ 0.5). |
| Search returns stale results | Run `uv run wikipilot index-wiki --full`. |
| Index builds slowly | `qmd index --jobs 4 wiki/` to parallelize. |
