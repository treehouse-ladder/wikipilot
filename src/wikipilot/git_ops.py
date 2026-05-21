"""Per-route git operations: branches, commits, PRs.

The Daily Research, Wiki Query, and Weekly Health routines each produce a
different shape of PR (one per topic, one per question, one per week). The
helpers in this module produce the branch name, stage the commit, push, and
open the PR via ``gh``. ``scripts/maybe_automerge.py`` then applies the
per-route auto-merge gate.

Every subprocess call accepts an injectable ``runner`` (defaults to
``subprocess.run``) so tests can swap in a recording fake without touching
the real git or gh binaries. The expected signature is
``runner(args, capture_output=True, text=True, check=False)``.
"""

from __future__ import annotations

import re
import subprocess
from collections.abc import Callable
from dataclasses import dataclass
from datetime import date
from typing import Any

from wikipilot.config import (
    AutomergeRoute,
    BranchesConfig,
    WikipilotConfig,
)
from wikipilot.lint import HUMAN_ONLY_PATHS
from wikipilot.wiki import slugify

ROUTE_DAILY_RESEARCH = "daily_research"
ROUTE_WIKI_QUERY = "wiki_query"
ROUTE_WEEKLY_HEALTH = "weekly_health"
VALID_ROUTES: tuple[str, ...] = (ROUTE_DAILY_RESEARCH, ROUTE_WIKI_QUERY, ROUTE_WEEKLY_HEALTH)


@dataclass(frozen=True)
class GateDecision:
    """Outcome of applying the per-route auto-merge gate to a PR."""

    automerge: bool
    reasons: list[str]  # human-readable reasons each gate criterion did/didn't pass
    blocked_paths: list[str]  # human-only paths the PR modified (if any)

    def render_review_checklist(self) -> str:
        lines = [
            "## Auto-merge gate did not pass",
            "",
            "This PR is left open for human review. Failed criteria:",
            "",
        ]
        lines.extend(f"- {reason}" for reason in self.reasons)
        if self.blocked_paths:
            lines.extend(["", "### Human-only paths modified", ""])
            lines.extend(f"- `{p}`" for p in self.blocked_paths)
        return "\n".join(lines)


def evaluate_gate(
    pr_view: PRView,
    *,
    route: str,
    config: WikipilotConfig,
) -> GateDecision:
    """Return a :class:`GateDecision` for ``pr_view`` against the ``route`` gate.

    Routes:
      - ``daily_research`` uses ``max_files_changed_per_topic`` and
        ``max_total_diff_lines_per_topic``.
      - ``wiki_query`` uses ``max_files_changed`` and ``max_total_diff_lines``.
      - ``weekly_health`` uses ``max_files_changed`` and ``max_total_diff_lines``.

    Common gate (``[automerge.common]``):
      - ``require_lint_green`` and ``require_tests_green`` map to
        ``pr_view.checks_passing`` (CI runs both — see ``ci.yml``).
      - ``block_human_only_file_changes`` blocks any PR that touches a path
        in :data:`wikipilot.lint.HUMAN_ONLY_PATHS` or any
        ``wiki/topics/<id>/purpose.md``.
    """
    if route not in VALID_ROUTES:
        raise ValueError(f"Unknown route {route!r}; expected one of {VALID_ROUTES}")
    common = config.automerge_common
    route_cfg = _route_config(config, route)
    reasons: list[str] = []
    blocked: list[str] = []

    if pr_view.is_draft:
        reasons.append("PR is a draft")
    if pr_view.state.upper() != "OPEN":
        reasons.append(f"PR state is {pr_view.state} (must be OPEN)")
    if (common.require_lint_green or common.require_tests_green) and not pr_view.checks_passing:
        reasons.append("CI checks are not green")

    max_files = _resolve_files_limit(route_cfg)
    max_lines = _resolve_lines_limit(route_cfg)
    diff_lines = pr_view.additions + pr_view.deletions
    if max_files is not None and len(pr_view.files) > max_files:
        reasons.append(f"PR touches {len(pr_view.files)} files (gate: max {max_files})")
    if max_lines is not None and diff_lines > max_lines:
        reasons.append(f"PR diff is {diff_lines} lines (gate: max {max_lines})")

    if common.block_human_only_file_changes:
        for path in pr_view.files:
            if _is_human_only_path(path):
                blocked.append(path)
        if blocked:
            reasons.append(f"PR modifies {len(blocked)} human-only path(s) — see review checklist")

    automerge = not reasons
    return GateDecision(automerge=automerge, reasons=reasons, blocked_paths=blocked)


def apply_gate(
    pr_number: int,
    *,
    route: str,
    config: WikipilotConfig,
    runner: PRRunner | None = None,
) -> GateDecision:
    """View ``pr_number``, evaluate the gate, and either enable auto-merge or comment.

    Returns the :class:`GateDecision` so callers (e.g. ``maybe_automerge.py``)
    can log the outcome.
    """
    pr_view = view_pr(pr_number, runner=runner)
    decision = evaluate_gate(pr_view, route=route, config=config)
    if decision.automerge:
        enable_automerge(pr_number, runner=runner)
    else:
        comment_pr(pr_number, decision.render_review_checklist(), runner=runner)
    return decision


def _route_config(config: WikipilotConfig, route: str) -> AutomergeRoute:
    if route == ROUTE_DAILY_RESEARCH:
        return config.daily_research
    if route == ROUTE_WIKI_QUERY:
        return config.wiki_query
    if route == ROUTE_WEEKLY_HEALTH:
        return config.weekly_health
    raise ValueError(f"unknown route {route!r}")


def _resolve_files_limit(route_cfg: AutomergeRoute) -> int | None:
    return route_cfg.max_files_changed_per_topic or route_cfg.max_files_changed


def _resolve_lines_limit(route_cfg: AutomergeRoute) -> int | None:
    return route_cfg.max_total_diff_lines_per_topic or route_cfg.max_total_diff_lines


def _is_human_only_path(path: str) -> bool:
    """Mirror of ``wikipilot.lint._is_human_only`` (kept duplicated to avoid
    importing the private helper; see ``HUMAN_ONLY_PATHS`` for the canonical set)."""
    normalized = path.replace("\\", "/")
    if normalized in HUMAN_ONLY_PATHS:
        return True
    for prefix in HUMAN_ONLY_PATHS:
        if prefix.endswith("/") and normalized.startswith(prefix):
            return True
    if normalized.startswith("wiki/topics/") and normalized.endswith("/purpose.md"):
        return True
    last_segment = normalized.rsplit("/", 1)[-1]
    return (
        normalized.startswith("wiki/")
        and normalized.endswith(".md")
        and last_segment.startswith("_")
    )


PRRunner = Callable[..., subprocess.CompletedProcess[str]]


class GitOpsError(RuntimeError):
    """Raised when a git/gh subprocess returns non-zero."""


@dataclass(frozen=True)
class PRRef:
    """A pull request created by ``create_pr``."""

    number: int
    url: str


@dataclass(frozen=True)
class PRView:
    """Subset of ``gh pr view --json`` we consume."""

    number: int
    state: str
    files: list[str]
    additions: int
    deletions: int
    checks_passing: bool
    is_draft: bool


def branch_for_daily(
    topic_id: str, *, today: date | None = None, config: BranchesConfig | None = None
) -> str:
    today = today or date.today()
    template = (config or BranchesConfig()).daily_template
    return template.format(date=today.isoformat(), topic_id=topic_id)


def branch_for_query(
    question: str, *, today: date | None = None, config: BranchesConfig | None = None
) -> str:
    today = today or date.today()
    template = (config or BranchesConfig()).query_template
    slug = slugify(question)[:48].rstrip("-") or "untitled"
    return template.format(date=today.isoformat(), slug=slug)


def branch_for_health(*, today: date | None = None, config: BranchesConfig | None = None) -> str:
    today = today or date.today()
    template = (config or BranchesConfig()).health_template
    return template.format(date=today.isoformat())


def checkout_new_branch(
    name: str,
    *,
    base: str = "main",
    runner: PRRunner | None = None,
) -> None:
    """Create ``name`` from ``base`` and switch to it."""
    runner = runner or subprocess.run
    _run(runner, ["git", "fetch", "origin", base], allow_fail=True)
    _run(
        runner,
        ["git", "checkout", "-B", name, f"origin/{base}"],
        allow_fail=True,
        fallback=["git", "checkout", "-B", name],
    )


def stage_and_commit(
    message: str,
    *,
    paths: list[str] | None = None,
    runner: PRRunner | None = None,
) -> str:
    """Stage ``paths`` (or all changes), commit with ``message``, return the SHA."""
    runner = runner or subprocess.run
    if paths:
        _run(runner, ["git", "add", *paths])
    else:
        _run(runner, ["git", "add", "-A"])
    _run(runner, ["git", "commit", "-m", message])
    sha_result = _run(runner, ["git", "rev-parse", "HEAD"])
    return sha_result.stdout.strip()


def push_branch(name: str, *, runner: PRRunner | None = None) -> None:
    runner = runner or subprocess.run
    _run(runner, ["git", "push", "-u", "origin", name])


def create_pr(
    *,
    title: str,
    body: str,
    base: str = "main",
    head: str | None = None,
    runner: PRRunner | None = None,
) -> PRRef:
    """Open a PR via ``gh pr create``; return ``PRRef``."""
    runner = runner or subprocess.run
    args = ["gh", "pr", "create", "--title", title, "--body", body, "--base", base]
    if head:
        args.extend(["--head", head])
    result = _run(runner, args)
    url = result.stdout.strip().splitlines()[-1] if result.stdout.strip() else ""
    number = _extract_pr_number(url)
    return PRRef(number=number, url=url)


def view_pr(pr_number: int, *, runner: PRRunner | None = None) -> PRView:
    """Fetch PR metadata via ``gh pr view --json``."""
    runner = runner or subprocess.run
    fields = "number,state,files,additions,deletions,statusCheckRollup,isDraft"
    result = _run(runner, ["gh", "pr", "view", str(pr_number), "--json", fields])
    import json as _json

    data = _json.loads(result.stdout)
    files = [f["path"] for f in data.get("files", [])]
    rollup = data.get("statusCheckRollup", []) or []
    checks_passing = all(_check_is_green(c) for c in rollup) if rollup else True
    return PRView(
        number=int(data.get("number", pr_number)),
        state=str(data.get("state", "OPEN")),
        files=files,
        additions=int(data.get("additions", 0)),
        deletions=int(data.get("deletions", 0)),
        checks_passing=checks_passing,
        is_draft=bool(data.get("isDraft", False)),
    )


def comment_pr(pr_number: int, body: str, *, runner: PRRunner | None = None) -> None:
    runner = runner or subprocess.run
    _run(runner, ["gh", "pr", "comment", str(pr_number), "--body", body])


def enable_automerge(pr_number: int, *, runner: PRRunner | None = None) -> None:
    """``gh pr merge --squash --auto``."""
    runner = runner or subprocess.run
    _run(runner, ["gh", "pr", "merge", str(pr_number), "--squash", "--auto"])


def render_pr_body_daily(
    *,
    topic_id: str,
    today: date,
    sources_added: list[str],
    pages_touched: list[str],
    new_disputes: list[str],
    new_open_questions: list[str],
    report_path: str | None,
) -> str:
    parts = [
        f"# Daily research — {topic_id} — {today.isoformat()}\n",
        "_Generated by the Wikipilot Daily Research routine; review and merge or comment._\n",
        "## Sources added",
        _bullets(sources_added),
        "## Pages touched",
        _bullets(pages_touched),
        "## New disputes",
        _bullets(new_disputes),
        "## New open questions",
        _bullets(new_open_questions),
    ]
    if report_path:
        parts.extend(["## Run report", f"[{report_path}]({report_path})"])
    return "\n\n".join(parts)


def render_pr_body_query(
    *,
    question: str,
    answer_slug: str,
    sources_added: list[str],
    backfilled_pages: list[str],
    issue_url: str | None,
) -> str:
    parts = [
        f"# Wiki query answer — {question}\n",
        f"Answer page: `wiki/answers/{answer_slug}.md`",
        "## Sources added",
        _bullets(sources_added),
        "## Back-filled pages",
        _bullets(backfilled_pages),
    ]
    if issue_url:
        parts.append(f"## Source issue\n\n{issue_url}")
    return "\n\n".join(parts)


def render_pr_body_health(
    *,
    today: date,
    disputes_filed: list[str],
    stale_pages: list[str],
    lint_summary: str,
    report_path: str | None,
) -> str:
    parts = [
        f"# Weekly health sweep — {today.isoformat()}\n",
        "## Disputes newly filed",
        _bullets(disputes_filed),
        "## Stale pages",
        _bullets(stale_pages),
        "## Lint summary",
        f"```\n{lint_summary.strip()}\n```",
    ]
    if report_path:
        parts.append(f"## Health report\n\n[{report_path}]({report_path})")
    return "\n\n".join(parts)


def _check_is_green(check: dict[str, Any]) -> bool:
    """Return True if a single statusCheckRollup entry indicates a passing check."""
    conclusion = (check.get("conclusion") or "").upper()
    state = (check.get("state") or "").upper()
    if conclusion in {"SUCCESS", "NEUTRAL", "SKIPPED"}:
        return True
    return state in {"SUCCESS", "PASSED"}


def _extract_pr_number(url: str) -> int:
    match = re.search(r"/pull/(\d+)", url)
    return int(match.group(1)) if match else 0


def _bullets(items: list[str]) -> str:
    if not items:
        return "_None._"
    return "\n".join(f"- {item}" for item in items)


def _run(
    runner: PRRunner,
    args: list[str],
    *,
    allow_fail: bool = False,
    fallback: list[str] | None = None,
) -> subprocess.CompletedProcess[str]:
    """Invoke ``runner(args)`` and convert non-zero into ``GitOpsError``.

    ``allow_fail=True`` allows a non-zero return; if ``fallback`` is provided,
    it is run on failure (used by ``checkout_new_branch`` to handle the case
    where ``origin/main`` doesn't exist locally).
    """
    result = runner(args, capture_output=True, text=True, check=False)
    if result.returncode == 0:
        return result
    if allow_fail and fallback is not None:
        result2 = runner(fallback, capture_output=True, text=True, check=False)
        if result2.returncode == 0:
            return result2
        raise GitOpsError(
            f"git/gh subprocess failed: {' '.join(args)} (and fallback {' '.join(fallback)}): "
            f"{result2.stderr.strip() or result2.stdout.strip()}"
        )
    if allow_fail:
        return result
    raise GitOpsError(
        f"git/gh subprocess failed: {' '.join(args)}: "
        f"{result.stderr.strip() or result.stdout.strip()}"
    )
