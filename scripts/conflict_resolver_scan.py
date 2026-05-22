"""Enumerate open ``claude/*`` PRs that need a conflict-resolver dispatch.

Invoked once per ``push`` event to ``main`` by the Conflict Resolver
routine (``prompts/conflict_resolver.md``). Lists every open PR whose:

  - Base ref equals ``--base`` (default ``main``).
  - Head ref matches a configured ``claude/*`` template (so we can route
    it).
  - ``mergeStateStatus`` is ``DIRTY`` (text conflicts vs the base) OR
    ``BEHIND`` (out-of-date with the base but no conflicts — a simple
    rebase will unblock GitHub's auto-merge queue).
  - Trust check passes (same-repo PR with a trusted author/association).

Emits a JSON list to stdout, one entry per dispatch-worthy PR::

    [
      {
        "number": 28,
        "head_ref": "claude/daily-2026-05-22/frontier-models",
        "base_ref": "main",
        "route": "daily_research",
        "merge_state_status": "DIRTY",
        "author_login": "rauriemo",
        "author_association": "MEMBER",
        "title": "wiki(frontier-models): daily 2026-05-22"
      }
    ]

The orchestrator then iterates this list sequentially, dispatching the
``conflict-resolver`` Opus subagent per entry (rebasing one PR can
affect mergeability of the next, so parallel dispatch is unsafe).

Usage::

    python scripts/conflict_resolver_scan.py --base main

Exit codes: 0 always (empty list when nothing matches); 2 on a hard
failure (``gh`` missing or returned an error). The "nothing to do" case
is the steady-state happy path on every push.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from wikipilot.config import load_wikipilot_config
from wikipilot.git_ops import (
    fetch_author_association,
    infer_route_from_branch,
    is_pr_trusted,
)

DEFAULT_CONFIG_PATH = Path("wikipilot.toml")

# Merge states we consider dispatch-worthy. ``DIRTY`` = textual conflicts,
# ``BEHIND`` = out-of-date with base (rebase resolves both). GitHub's
# ``UNKNOWN`` state means GitHub hasn't computed mergeability yet — we
# skip rather than racing it; the next push will re-evaluate.
DISPATCH_STATES: frozenset[str] = frozenset({"DIRTY", "BEHIND"})


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--base",
        type=str,
        default="main",
        help="Base branch to scan PRs against (default: main).",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to wikipilot.toml (default: ./wikipilot.toml).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=200,
        help="Max PRs to enumerate (default: 200; below GitHub's max page size).",
    )
    args = parser.parse_args(argv)

    config = load_wikipilot_config(args.config)
    prs = _list_prs(base=args.base, limit=args.limit)
    out: list[dict] = []
    for entry in prs:
        head_ref = entry.get("headRefName") or ""
        route = infer_route_from_branch(head_ref, config)
        if route is None:
            continue
        merge_state = (entry.get("mergeStateStatus") or "").upper()
        if merge_state not in DISPATCH_STATES:
            continue
        author = entry.get("author") or {}
        author_login = str(author.get("login") or "") if isinstance(author, dict) else ""
        is_cross_repository = bool(entry.get("isCrossRepository", False))
        pr_number = int(entry.get("number", 0))
        association = fetch_author_association(pr_number)
        if not is_pr_trusted(
            is_cross_repository=is_cross_repository,
            association=association,
            author_login=author_login,
            config=config.conflict_resolver,
        ):
            continue
        out.append(
            {
                "number": pr_number,
                "head_ref": head_ref,
                "base_ref": args.base,
                "route": route,
                "merge_state_status": merge_state,
                "author_login": author_login,
                "author_association": association,
                "title": entry.get("title") or "",
            }
        )
    print(json.dumps(out, indent=2))
    return 0


def _list_prs(*, base: str, limit: int) -> list[dict]:
    """Enumerate open PRs via ``gh pr list --json``.

    Filters head-ref-matching client-side (``gh pr list --head`` doesn't
    accept globs). Fails loud on any ``gh`` error so the orchestrator's
    log entry reflects the actual failure mode rather than silently
    moving on with an empty list.
    """
    fields = (
        "number,headRefName,baseRefName,mergeStateStatus,isCrossRepository,author,title"
    )
    cmd = [
        "gh",
        "pr",
        "list",
        "--state",
        "open",
        "--base",
        base,
        "--json",
        fields,
        "--limit",
        str(limit),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except (OSError, subprocess.SubprocessError) as exc:
        print(f"ERROR: gh pr list failed: {exc}", file=sys.stderr)
        sys.exit(2)
    if result.returncode != 0:
        print(
            f"ERROR: gh pr list returned {result.returncode}: "
            f"{result.stderr.strip() or result.stdout.strip()}",
            file=sys.stderr,
        )
        sys.exit(2)
    body = result.stdout.strip() or "[]"
    try:
        data = json.loads(body)
    except (ValueError, TypeError) as exc:
        print(f"ERROR: could not parse gh pr list output: {exc}", file=sys.stderr)
        sys.exit(2)
    if not isinstance(data, list):
        print("ERROR: gh pr list returned non-list payload", file=sys.stderr)
        sys.exit(2)
    return data


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
