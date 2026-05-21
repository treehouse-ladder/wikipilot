"""Re-run the auto-merge gate on a PR with the real CI signal.

Invoked once per ``pull_request.opened`` / ``pull_request.synchronize``
session by ``prompts/pr_watcher.md``. Reads ``wikipilot.toml``, fetches the
PR via ``gh pr view --json`` (twice: once for branch metadata, once after
the CI wait for the rollup), waits for ``gh pr checks --watch`` to finish,
and then dispatches to :func:`wikipilot.git_ops.apply_gate` in either
``enforce`` or ``read_only`` mode depending on the head branch AND the PR
author's trust state:

  - Head matches a configured ``[branches]`` template
    (``claude/daily-…``, ``claude/query-…``, ``claude/health-…``) AND the
    PR is authored by a trusted identity (``author_association`` in
    ``[automerge.pr_watcher].trusted_associations`` *or* ``author.login`` in
    ``trusted_authors``) AND the head ref lives in this repo (not a fork)
    → ``--route`` is inferred from the prefix and the gate runs in
    ``enforce`` mode (queues auto-merge on green, undoes a premature queue
    + posts a checklist comment on red).
  - Any other case (non-claude/* head, fork PR, or untrusted author with a
    ``claude/*``-shaped head) → the gate runs in ``read_only`` mode
    (comment only, never merge). The dual head-and-author check exists so
    a hostile fork PR with a ``claude/daily-…``-shaped branch name cannot
    coerce the watcher into queueing auto-merge against ``main``.

Self-heal signalling: when CI is red on a trusted ``claude/*`` PR and the
``wikipilot:heal-attempt-{n}`` label count is below
``[automerge.pr_watcher].self_heal_max_attempts``, the script prints a
machine-readable ``HEAL_NEEDED`` line so the orchestrator prompt knows to
dispatch ``wiki-linter``. The actual heal commit/push lives in the prompt.

Usage::

    python scripts/pr_watcher_gate.py --pr 42

The script always exits 0 (matches ``maybe_automerge.py`` shim convention)
so the orchestrator session never crashes on a gate failure — the comment
on the PR is the durable artifact.
"""

from __future__ import annotations

import argparse
import contextlib
import json
import re
import subprocess
import sys
from pathlib import Path

from wikipilot.config import PRWatcherConfig, load_wikipilot_config
from wikipilot.git_ops import (
    DEFAULT_GATE_DEDUPE_KEY,
    ROUTE_WIKI_QUERY,
    apply_gate,
    comment_pr,
    infer_route_from_branch,
    wait_for_ci,
)

DEFAULT_CONFIG_PATH = Path("wikipilot.toml")
HEAL_LABEL_PREFIX = "wikipilot:heal-attempt-"
HEAL_NEEDED_TOKEN = "HEAL_NEEDED"
HEAL_CAPPED_TOKEN = "HEAL_CAPPED"
UNKNOWN_ASSOCIATION = "NONE"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pr", type=int, required=True, help="PR number to gate.")
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to wikipilot.toml (default: ./wikipilot.toml).",
    )
    parser.add_argument(
        "--skip-ci-wait",
        action="store_true",
        help="Skip the gh pr checks --watch wait (use when CI is known complete).",
    )
    args = parser.parse_args(argv)

    config = load_wikipilot_config(args.config)
    pr_meta = _fetch_pr_metadata(args.pr)
    if pr_meta is None:
        print(f"PR #{args.pr}: could not fetch metadata via gh; aborting.")
        return 0
    head_ref = pr_meta["headRefName"]
    state = pr_meta["state"].upper()
    is_draft = bool(pr_meta.get("isDraft"))
    labels = [lbl.get("name", "") for lbl in pr_meta.get("labels", [])]
    is_fork = bool(pr_meta.get("isCrossRepository"))
    author_login = ((pr_meta.get("author") or {}).get("login")) or ""

    if state in {"MERGED", "CLOSED"}:
        print(f"PR #{args.pr}: state={state}; nothing to gate.")
        return 0
    if is_draft:
        print(f"PR #{args.pr}: draft; PR Watcher skipping until ready for review.")
        return 0

    route = infer_route_from_branch(head_ref, config)
    association = UNKNOWN_ASSOCIATION
    if route is not None:
        # Defense-in-depth: branch name matched a claude/* template, but only
        # enforce when the PR is in this repo (not a fork) AND the author is
        # trusted. Without this guard a hostile fork PR with a synthetic
        # claude/daily-… head ref could coerce the watcher into queueing
        # auto-merge against main. See CLAUDE.md "Per-PR workflow" trust model.
        association = _fetch_pr_author_association(args.pr) or UNKNOWN_ASSOCIATION
        if not _is_trusted_for_enforce(
            is_fork=is_fork,
            association=association,
            author_login=author_login,
            config=config.pr_watcher,
        ):
            print(
                f"PR #{args.pr}: head={head_ref!r} matches claude/* but author "
                f"is not trusted (author={author_login!r} "
                f"assoc={association!r} fork={is_fork}); forcing read_only mode."
            )
            route = None

    if route is None:
        gate_route = ROUTE_WIKI_QUERY
        mode = "read_only"
        print(
            f"PR #{args.pr}: head={head_ref!r} author={author_login!r} "
            f"assoc={association!r} fork={is_fork}; running gate in "
            f"read_only mode (route={gate_route})."
        )
    else:
        gate_route = route
        mode = "enforce"
        print(
            f"PR #{args.pr}: head={head_ref!r} author={author_login!r} "
            f"assoc={association!r} -> route={route}, mode=enforce."
        )

    ci_green = True
    if not args.skip_ci_wait:
        timeout = config.pr_watcher.ci_wait_timeout_sec
        print(f"PR #{args.pr}: waiting up to {timeout}s for CI...")
        ci_green = wait_for_ci(args.pr, timeout_sec=timeout)
        if not ci_green:
            # The watcher prompt re-fires on the next push; a timeout/red here
            # is recoverable. Still leave a dedupe-keyed comment so humans see
            # what happened.
            print(f"PR #{args.pr}: CI did not finish green within the wait window.")
            if mode == "enforce" and route is not None:
                _maybe_signal_heal(args.pr, config.pr_watcher.self_heal_max_attempts, labels)

    decision = apply_gate(
        args.pr,
        route=gate_route,
        config=config,
        mode=mode,
        dedupe_key=DEFAULT_GATE_DEDUPE_KEY,
    )
    if decision.automerge:
        if mode == "enforce":
            print(f"PR #{args.pr}: gate passed; auto-merge enabled.")
        else:
            print(f"PR #{args.pr}: gate would pass (read-only mode); comment posted.")
        return 0
    print(f"PR #{args.pr}: gate did NOT pass. Reasons:")
    for reason in decision.reasons:
        print(f"  - {reason}")
    if decision.blocked_paths:
        print("  Human-only paths modified:")
        for path in decision.blocked_paths:
            print(f"    - {path}")
    if mode == "enforce" and route is not None and not ci_green:
        # _maybe_signal_heal already printed above, but re-issue when reached
        # without CI wait (--skip-ci-wait + red rollup) for completeness.
        _maybe_signal_heal_if_unprinted(args.pr, config.pr_watcher.self_heal_max_attempts, labels)
    return 0


def _fetch_pr_metadata(pr_number: int) -> dict | None:
    """Fetch the gh-CLI-visible subset of PR metadata.

    Returns the parsed ``gh pr view --json`` payload, extended to include the
    ``isCrossRepository`` and ``author`` fields the trust guard consumes.
    Note: GitHub's ``author_association`` is *not* exposed by
    ``gh pr view --json`` (verified empirically against ``gh 2.x``); the
    watcher reads it via :func:`_fetch_pr_author_association`.
    """
    args = [
        "gh",
        "pr",
        "view",
        str(pr_number),
        "--json",
        "headRefName,state,isDraft,labels,isCrossRepository,author,headRepositoryOwner",
    ]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=False)
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0 or not result.stdout.strip():
        return None
    try:
        return json.loads(result.stdout)
    except (ValueError, TypeError):
        return None


def _fetch_pr_author_association(pr_number: int) -> str | None:
    """Read ``author_association`` for ``pr_number`` via the GitHub REST API.

    GitHub's ``gh pr view --json`` does not expose this field even though
    the underlying REST endpoint does, so the watcher calls
    ``gh api repos/<owner>/<repo>/pulls/<num>`` directly. Returns the
    upper-case association string (e.g. ``"MEMBER"``, ``"COLLABORATOR"``,
    ``"NONE"``) on success and ``None`` on any failure mode — the caller
    treats ``None`` as untrusted so transient gh outages fail closed.
    """
    owner_repo = _resolve_owner_repo()
    if owner_repo is None:
        return None
    args = ["gh", "api", f"repos/{owner_repo}/pulls/{pr_number}"]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=False)
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0 or not result.stdout.strip():
        return None
    try:
        data = json.loads(result.stdout)
    except (ValueError, TypeError):
        return None
    assoc = data.get("author_association")
    if not isinstance(assoc, str) or not assoc.strip():
        return None
    return assoc.strip().upper()


def _resolve_owner_repo() -> str | None:
    """Return ``owner/repo`` for the current gh context, or ``None`` on failure."""
    try:
        result = subprocess.run(
            ["gh", "repo", "view", "--json", "nameWithOwner"],
            capture_output=True,
            text=True,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0 or not result.stdout.strip():
        return None
    try:
        data = json.loads(result.stdout)
    except (ValueError, TypeError):
        return None
    value = data.get("nameWithOwner")
    return value if isinstance(value, str) and value else None


def _is_trusted_for_enforce(
    *,
    is_fork: bool,
    association: str,
    author_login: str,
    config: PRWatcherConfig,
) -> bool:
    """Return True iff the PR's author may drive the watcher's enforce path.

    Trust requires *all* of:

    1. The head ref lives in this repo (``isCrossRepository`` is false).
       Fork PRs are never trusted, even when the author also belongs to the
       trusted set — GitHub's `pull_request` event still fires from forks
       and an attacker can name their fork branch anything they like.
    2. Either ``association`` (already upper-cased upstream) is in
       ``config.trusted_associations``, or ``author_login`` is in the
       explicit ``config.trusted_authors`` allowlist. The login check is
       case-sensitive (GitHub logins themselves are case-insensitive but
       the canonical form ``gh`` returns is what we compare against).
    """
    if is_fork:
        return False
    if association in config.trusted_associations:
        return True
    return bool(author_login) and author_login in config.trusted_authors


def _current_heal_attempt(labels: list[str]) -> int:
    pattern = re.compile(rf"^{re.escape(HEAL_LABEL_PREFIX)}(\d+)$")
    highest = 0
    for label in labels:
        match = pattern.match(label)
        if match:
            highest = max(highest, int(match.group(1)))
    return highest


_heal_signal_printed = False


def _maybe_signal_heal(pr_number: int, max_attempts: int, labels: list[str]) -> None:
    global _heal_signal_printed
    attempt = _current_heal_attempt(labels)
    if attempt >= max_attempts:
        print(f"{HEAL_CAPPED_TOKEN} pr={pr_number} attempt={attempt} max={max_attempts}")
        # Annotate the PR so humans see why the loop stopped — fire and forget.
        with contextlib.suppress(Exception):  # pragma: no cover — best-effort annotation
            comment_pr(
                pr_number,
                (
                    "## Self-heal cap reached\n\n"
                    f"`wiki-linter` has attempted {attempt} mechanical fix(es); "
                    "no further auto-fix attempts will be made. A human needs "
                    "to take a look."
                ),
                dedupe_key="wikipilot:heal-cap",
            )
    else:
        next_attempt = attempt + 1
        print(f"{HEAL_NEEDED_TOKEN} pr={pr_number} next_attempt={next_attempt}")
    _heal_signal_printed = True


def _maybe_signal_heal_if_unprinted(pr_number: int, max_attempts: int, labels: list[str]) -> None:
    if _heal_signal_printed:
        return
    _maybe_signal_heal(pr_number, max_attempts, labels)


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
