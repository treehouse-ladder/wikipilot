"""Enumerate open ``claude/*`` PRs that need a conflict-resolver dispatch.

Invoked once per ``push`` event to ``main`` by the Conflict Resolver
routine (``prompts/conflict_resolver.md``). Lists every open PR whose:

  - Base ref equals ``--base`` (default ``main``).
  - Head ref matches a configured ``claude/*`` template (so we can route
    it).
  - ``mergeStateStatus`` indicates the PR needs an automated fix:
      * ``DIRTY`` / ``BEHIND`` → ``dispatch_kind: "rebase"`` (text-conflict
        or out-of-date; Opus ``conflict-resolver`` subagent handles it).
      * ``CLEAN`` AND ``autoMergeRequest`` is ``null`` AND every required
        check is green → ``dispatch_kind: "requeue"`` (auto-merge was
        never queued, possibly because the in-routine ``gh pr merge --auto``
        call was skipped — re-run :func:`apply_static_gate` to fix
        deterministically; no LLM dispatch).
      * ``BLOCKED`` AND the failing CI check is classifiable as
        auto-fixable lint → ``dispatch_kind: "lint_fix"`` (Opus
        ``wiki-lint-fixer`` subagent handles it).
  - Trust check passes (same-repo PR with a trusted author/association).

Emits a JSON list to stdout, one entry per dispatch-worthy PR::

    [
      {
        "number": 28,
        "head_ref": "claude/daily-2026-05-22/frontier-models",
        "base_ref": "main",
        "route": "daily_research",
        "merge_state_status": "DIRTY",
        "dispatch_kind": "rebase",
        "author_login": "rauriemo",
        "author_association": "MEMBER",
        "title": "wiki(frontier-models): daily 2026-05-22"
      },
      {
        "number": 47,
        "head_ref": "claude/daily-2026-05-24/ai-in-game-dev",
        "base_ref": "main",
        "route": "daily_research",
        "merge_state_status": "BLOCKED",
        "dispatch_kind": "lint_fix",
        "lint_categories": ["broken-wikilink"],
        "lint_excerpt": "...",
        "author_login": "rauriemo",
        "author_association": "MEMBER",
        "title": "wiki(ai-in-game-dev): daily 2026-05-24"
      }
    ]

The orchestrator then iterates this list sequentially, dispatching the
appropriate handler per ``dispatch_kind`` (rebasing or fixing lint on one
PR can affect mergeability of the next, so parallel dispatch is unsafe).

Usage::

    python scripts/conflict_resolver_scan.py --base main

Exit codes: 0 always (empty list when nothing matches); 2 on a hard
failure (``gh`` missing or returned an error). The "nothing to do" case
is the steady-state happy path on every push.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

from wikipilot.config import load_wikipilot_config
from wikipilot.git_ops import (
    check_is_green,
    classify_lint_failure,
    fetch_author_association,
    infer_route_from_branch,
    is_pr_trusted,
)

DEFAULT_CONFIG_PATH = Path("wikipilot.toml")

# Per-PR cap on the CI log we pull into memory before handing it to the
# classifier. The classifier itself caps its excerpt; this is the upstream
# safety net for the (rare) case where ``gh run view --log-failed`` returns
# many MB of repeated output.
MAX_CI_LOG_BYTES = 200 * 1024

# ``DIRTY`` and ``BEHIND`` get the existing Opus conflict-resolver. ``CLEAN``
# triggers requeue when auto-merge was never enabled. ``BLOCKED`` triggers
# lint-fix when classifier deems it tractable. Anything else (UNKNOWN,
# MERGEABLE-with-already-queued-automerge, DRAFT, etc.) is skipped.
_REBASE_STATES: frozenset[str] = frozenset({"DIRTY", "BEHIND"})

# Kept as a module-level re-export for back-compat with any caller that
# imports DISPATCH_STATES. The new triage logic in :func:`_classify_dispatch`
# is the source of truth; this constant only describes the rebase subset.
DISPATCH_STATES: frozenset[str] = _REBASE_STATES

_RUN_ID_RE = re.compile(r"/actions/runs/(\d+)")


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
    auto_fix_categories = _resolved_auto_fix_categories(config)
    prs = _list_prs(base=args.base, limit=args.limit)
    out: list[dict] = []
    for entry in prs:
        head_ref = entry.get("headRefName") or ""
        route = infer_route_from_branch(head_ref, config)
        if route is None:
            continue
        merge_state = (entry.get("mergeStateStatus") or "").upper()
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

        dispatch_kind, extras = _classify_dispatch(
            entry,
            merge_state=merge_state,
            auto_fix_categories=auto_fix_categories,
        )
        if dispatch_kind is None:
            continue

        out_entry: dict = {
            "number": pr_number,
            "head_ref": head_ref,
            "base_ref": args.base,
            "route": route,
            "merge_state_status": merge_state,
            "dispatch_kind": dispatch_kind,
            "author_login": author_login,
            "author_association": association,
            "title": entry.get("title") or "",
        }
        out_entry.update(extras)
        out.append(out_entry)
    print(json.dumps(out, indent=2))
    return 0


def _classify_dispatch(
    entry: dict,
    *,
    merge_state: str,
    auto_fix_categories: frozenset[str],
) -> tuple[str | None, dict]:
    """Decide which handler should pick up the PR and gather extra payload.

    Returns ``(dispatch_kind, extras)``:

    - ``("rebase", {})`` for DIRTY / BEHIND.
    - ``("requeue", {})`` for CLEAN with no ``autoMergeRequest`` and all
      checks green (Cause 1 in the original incident: the in-routine
      ``maybe_automerge.py`` call was skipped).
    - ``("lint_fix", {lint_categories, lint_excerpt})`` for BLOCKED with a
      classifier verdict of ``auto_fixable=True`` (Cause 2: a fixable
      broken-wikilink / frontmatter / log-format / ruff failure).
    - ``(None, {})`` when no handler is appropriate (PR is healthy, fork,
      already-queued automerge, draft, or the failure isn't tractable).
    """
    if merge_state in _REBASE_STATES:
        return "rebase", {}

    if merge_state == "CLEAN":
        if entry.get("autoMergeRequest") is not None:
            return None, {}
        rollup = entry.get("statusCheckRollup") or []
        if rollup and all(check_is_green(c) for c in rollup):
            return "requeue", {}
        # CLEAN without auto-merge but with not-yet-green checks: GitHub
        # will queue it on its own once CI completes; nothing to do.
        return None, {}

    if merge_state == "BLOCKED":
        rollup = entry.get("statusCheckRollup") or []
        failing_run_ids = _failing_run_ids(rollup)
        if not failing_run_ids:
            return None, {}
        ci_log = _fetch_failed_log(failing_run_ids[0])
        if not ci_log:
            return None, {}
        classification = classify_lint_failure(
            ci_log,
            auto_fix_categories=auto_fix_categories,
        )
        if not classification.auto_fixable:
            return None, {}
        return "lint_fix", {
            "lint_categories": classification.categories,
            "lint_excerpt": classification.excerpt,
        }

    return None, {}


def _failing_run_ids(rollup: list[dict]) -> list[int]:
    """Return distinct Actions workflow-run IDs whose check failed.

    A single PR may run multiple workflows (CI, lint, docs, ...). The
    scan grabs the first failing run and classifies it; if more than one
    workflow fails the lint-fixer can handle one and the second one shows
    up on the next push. Keeping it simple deliberately — chained
    failures are rare and the orchestrator's per-push cadence catches
    them within minutes.
    """
    ids: list[int] = []
    seen: set[int] = set()
    for check in rollup:
        conclusion = (check.get("conclusion") or "").upper()
        if conclusion != "FAILURE":
            continue
        details_url = check.get("detailsUrl") or ""
        match = _RUN_ID_RE.search(details_url)
        if not match:
            continue
        run_id = int(match.group(1))
        if run_id in seen:
            continue
        seen.add(run_id)
        ids.append(run_id)
    return ids


def _fetch_failed_log(run_id: int) -> str:
    """Run ``gh run view <id> --log-failed`` and return the (capped) output.

    A failure here (gh not installed, run already deleted, transient
    auth) is non-fatal — the caller treats an empty log as
    "couldn't classify, skip this PR for now".
    """
    cmd = ["gh", "run", "view", str(run_id), "--log-failed"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except (OSError, subprocess.SubprocessError):
        return ""
    if result.returncode != 0:
        return ""
    text = result.stdout or ""
    if len(text) > MAX_CI_LOG_BYTES:
        text = text[-MAX_CI_LOG_BYTES:]
    return text


def _resolved_auto_fix_categories(config) -> frozenset[str]:
    """Look up the per-deployment override for the auto-fix allowlist.

    Falls back to :data:`wikipilot.git_ops.DEFAULT_AUTO_FIX_LINT_CATEGORIES`
    when ``[automerge.conflict_resolver].auto_fix_lint_categories`` is
    absent from ``wikipilot.toml``.
    """
    from wikipilot.git_ops import DEFAULT_AUTO_FIX_LINT_CATEGORIES

    cfg = getattr(config, "conflict_resolver", None)
    if cfg is None:
        return DEFAULT_AUTO_FIX_LINT_CATEGORIES
    override = getattr(cfg, "auto_fix_lint_categories", None)
    if not override:
        return DEFAULT_AUTO_FIX_LINT_CATEGORIES
    return frozenset(override)


def _list_prs(*, base: str, limit: int) -> list[dict]:
    """Enumerate open PRs via ``gh pr list --json``.

    Filters head-ref-matching client-side (``gh pr list --head`` doesn't
    accept globs). Fails loud on any ``gh`` error so the orchestrator's
    log entry reflects the actual failure mode rather than silently
    moving on with an empty list.
    """
    fields = (
        "number,headRefName,baseRefName,mergeStateStatus,isCrossRepository,"
        "author,title,statusCheckRollup,autoMergeRequest"
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
