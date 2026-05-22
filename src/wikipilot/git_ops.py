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

import json as _json
import re
import subprocess
from collections.abc import Callable
from dataclasses import dataclass
from datetime import date
from typing import Any, Literal

from wikipilot.config import (
    AutomergeRoute,
    BranchesConfig,
    ConflictResolverConfig,
    WikipilotConfig,
)
from wikipilot.lint import HUMAN_ONLY_PATHS
from wikipilot.wiki import slugify

ROUTE_DAILY_RESEARCH = "daily_research"
ROUTE_WIKI_QUERY = "wiki_query"
ROUTE_WEEKLY_HEALTH = "weekly_health"
VALID_ROUTES: tuple[str, ...] = (ROUTE_DAILY_RESEARCH, ROUTE_WIKI_QUERY, ROUTE_WEEKLY_HEALTH)

GateMode = Literal["enforce", "read_only"]
DEFAULT_GATE_DEDUPE_KEY = "wikipilot:gate"
UNKNOWN_ASSOCIATION = "NONE"


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


def evaluate_static_gate(
    pr_view: PRView,
    *,
    route: str,
    config: WikipilotConfig,
) -> GateDecision:
    """Return a :class:`GateDecision` for the *deterministic* gate criteria.

    Identical to :func:`evaluate_gate` except it does NOT check
    ``pr_view.checks_passing``. This is the gate the in-routine
    ``maybe_automerge.py`` call uses to decide whether to queue
    ``gh pr merge --squash --auto``: CI is enforced separately by GitHub's
    own required-status-checks ruleset, so the local prediction added
    nothing but a race condition (the empty-rollup-as-green bug that
    stranded PRs in May 2026 — see PR Watcher v2 design notes).

    All other criteria still fire: draft, state, file count, diff lines,
    human-only paths, and the centralized trust check.
    """
    return _evaluate_gate_impl(pr_view, route=route, config=config, check_ci=False)


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

    Plus the centralized trust check (``[automerge.conflict_resolver]``):
    a PR from a fork or from an untrusted author is blocked regardless of
    other criteria. See :func:`is_pr_trusted` for the semantics.
    """
    return _evaluate_gate_impl(pr_view, route=route, config=config, check_ci=True)


def _evaluate_gate_impl(
    pr_view: PRView,
    *,
    route: str,
    config: WikipilotConfig,
    check_ci: bool,
) -> GateDecision:
    """Shared body of :func:`evaluate_gate` and :func:`evaluate_static_gate`."""
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
    if (
        check_ci
        and (common.require_lint_green or common.require_tests_green)
        and not pr_view.checks_passing
    ):
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

    if not is_pr_trusted(
        is_cross_repository=pr_view.is_cross_repository,
        association=pr_view.author_association or UNKNOWN_ASSOCIATION,
        author_login=pr_view.author_login,
        config=config.conflict_resolver,
    ):
        reasons.append(
            f"PR author is not trusted "
            f"(assoc={(pr_view.author_association or UNKNOWN_ASSOCIATION)!r}, "
            f"login={pr_view.author_login!r}, fork={pr_view.is_cross_repository})"
        )

    automerge = not reasons
    return GateDecision(automerge=automerge, reasons=reasons, blocked_paths=blocked)


def apply_gate(
    pr_number: int,
    *,
    route: str,
    config: WikipilotConfig,
    runner: PRRunner | None = None,
    mode: GateMode = "enforce",
    dedupe_key: str = DEFAULT_GATE_DEDUPE_KEY,
) -> GateDecision:
    """View ``pr_number``, evaluate the full gate (including CI), and act.

    Used by :func:`wikipilot.cli.recover_prs_cmd` and any caller that wants
    to re-validate a PR against the current CI signal. The in-routine
    ``maybe_automerge.py`` shim uses :func:`apply_static_gate` instead,
    since the static gate is what GitHub's required-status-checks can't
    enforce on its own.

    Modes:
      - ``"enforce"`` (default): on pass, calls ``gh pr merge --squash --auto``;
        on fail with red CI, calls ``gh pr merge --disable-auto`` to undo any
        premature queue and then posts/edits a dedupe-keyed review-checklist
        comment.
      - ``"read_only"``: never invokes ``gh pr merge`` in either direction.
        Only posts/edits the dedupe-keyed checklist comment so the caller
        sees the gate's decision without the gate trying to merge.

    ``dedupe_key`` is embedded as an HTML comment (``<!-- ... -->``) inside
    the posted body so subsequent calls *edit* the existing comment instead
    of spamming a new one. Returns the :class:`GateDecision`.
    """
    pr_view = view_pr(pr_number, runner=runner)
    decision = evaluate_gate(pr_view, route=route, config=config)
    if decision.automerge:
        if mode == "enforce":
            enable_automerge(pr_number, runner=runner)
        else:
            comment_pr(
                pr_number,
                _RENDER_READONLY_PASS,
                runner=runner,
                dedupe_key=dedupe_key,
            )
        return decision
    if mode == "enforce" and not pr_view.checks_passing:
        disable_automerge(pr_number, runner=runner)
    comment_pr(
        pr_number,
        decision.render_review_checklist(),
        runner=runner,
        dedupe_key=dedupe_key,
    )
    return decision


def apply_static_gate(
    pr_number: int,
    *,
    route: str,
    config: WikipilotConfig,
    runner: PRRunner | None = None,
    dedupe_key: str = DEFAULT_GATE_DEDUPE_KEY,
) -> GateDecision:
    """View ``pr_number``, evaluate the *static* gate, and act on the decision.

    Same shape as :func:`apply_gate` but skips the CI check: it queues
    ``gh pr merge --squash --auto`` if every deterministic criterion passes
    (draft, state, file count, diff lines, human-only paths, trust) and
    lets GitHub's own required-status-checks ruleset hold the merge until
    CI is green. This is the in-routine shim's contract — see
    ``scripts/maybe_automerge.py``.

    Always runs in enforce mode. The trust check is baked into the static
    gate itself (see :func:`is_pr_trusted`), so this call site is safe to
    invoke from any orchestrator that creates a PR.
    """
    pr_view = view_pr(pr_number, runner=runner)
    decision = evaluate_static_gate(pr_view, route=route, config=config)
    if decision.automerge:
        enable_automerge(pr_number, runner=runner)
        return decision
    comment_pr(
        pr_number,
        decision.render_review_checklist(),
        runner=runner,
        dedupe_key=dedupe_key,
    )
    return decision


_RENDER_READONLY_PASS = (
    "## Auto-merge gate would pass\n\n"
    "The gate is running in read-only mode for this branch (no auto-merge "
    "is queued). All gate criteria are currently satisfied; merge manually "
    "when ready."
)


def _route_config(config: WikipilotConfig, route: str) -> AutomergeRoute:
    if route == ROUTE_DAILY_RESEARCH:
        return config.daily_research
    if route == ROUTE_WIKI_QUERY:
        return config.wiki_query
    if route == ROUTE_WEEKLY_HEALTH:
        return config.weekly_health
    raise ValueError(f"unknown route {route!r}")


def infer_route_from_branch(branch: str, config: WikipilotConfig | None = None) -> str | None:
    """Infer which routine produced ``branch`` by matching the templates in ``[branches]``.

    Returns one of :data:`VALID_ROUTES` for branches that match a known
    routine template, or ``None`` for human / unknown / non-claude branches.
    ``None`` is the explicit signal callers (``recover-prs``, the conflict
    resolver scan) use to switch to read-only mode for that PR.

    Matching is anchored to the template prefix up to the first ``{`` (e.g.
    ``claude/daily-{date}/{topic_id}`` becomes prefix ``claude/daily-``). This
    keeps the rule simple and template-driven so a ``wikipilot.toml [branches]``
    override is honoured automatically.
    """
    if not branch:
        return None
    branches_cfg = (config or WikipilotConfig()).branches
    candidates: tuple[tuple[str, str], ...] = (
        (branches_cfg.daily_template, ROUTE_DAILY_RESEARCH),
        (branches_cfg.query_template, ROUTE_WIKI_QUERY),
        (branches_cfg.health_template, ROUTE_WEEKLY_HEALTH),
    )
    for template, route in candidates:
        prefix = _template_prefix(template)
        if not prefix:
            continue
        if branch.startswith(prefix):
            return route
    return None


def _template_prefix(template: str) -> str:
    """Return the literal prefix of a branch template (everything before the first ``{``)."""
    idx = template.find("{")
    return template if idx < 0 else template[:idx]


def wait_for_ci(
    pr_number: int,
    *,
    timeout_sec: int = 1200,
    interval_sec: int = 30,
    runner: PRRunner | None = None,
) -> bool:
    """Block until ``gh pr checks --watch`` exits, then return CI pass/fail.

    Returns ``True`` when the wrapped ``gh pr checks`` invocation exits zero
    (every required check green); ``False`` on a non-zero exit (any check
    failed) **or** when the subprocess raised :class:`subprocess.TimeoutExpired`
    after ``timeout_sec``.

    ``interval_sec`` is forwarded to ``gh`` as ``--interval``; ``timeout_sec``
    drives the hard timeout passed to the runner. The watcher prompt always
    polls again on the next ``pull_request.synchronize`` event so a False here
    is recoverable.
    """
    runner = runner or subprocess.run
    args = [
        "gh",
        "pr",
        "checks",
        str(pr_number),
        "--watch",
        "--interval",
        str(interval_sec),
    ]
    try:
        result = runner(
            args,
            capture_output=True,
            text=True,
            check=False,
            timeout=timeout_sec,
        )
    except subprocess.TimeoutExpired:
        return False
    return result.returncode == 0


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
    """Subset of ``gh pr view --json`` (+ trust info) the gate consumes.

    Trust fields (``is_cross_repository``, ``author_login``,
    ``author_association``) are populated by :func:`view_pr` via two
    additional ``gh`` calls: ``gh pr view --json author,isCrossRepository``
    (already part of the main view) and ``gh api repos/<o>/<r>/pulls/<n>``
    (since ``author_association`` is exposed by the REST API but not by
    ``gh pr view --json``).

    Defaults intentionally trip the gate's centralized trust check
    (``author_association=None`` is treated as untrusted) — fail-closed
    when the trust info couldn't be fetched. Test fixtures that want to
    exercise the trusted path must set the trust fields explicitly.
    """

    number: int
    state: str
    files: list[str]
    additions: int
    deletions: int
    checks_passing: bool
    is_draft: bool
    is_cross_repository: bool = False
    author_login: str = ""
    author_association: str | None = None


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
    """Fetch PR metadata via ``gh pr view --json`` + trust info via ``gh api``.

    Issues up to three ``gh`` calls per invocation:

    1. ``gh pr view --json`` — the main payload (always).
    2. ``gh repo view --json nameWithOwner`` — only when the trust check
       needs to resolve ``owner/repo`` for the REST endpoint (memoized at
       the call-site is a future optimization).
    3. ``gh api repos/<o>/<r>/pulls/<n>`` — fetches ``author_association``,
       which is not exposed by ``gh pr view --json``.

    Failures of (2) or (3) are tolerated and leave the corresponding
    ``PRView`` fields at their fail-closed defaults — the gate's trust
    check then refuses to enable auto-merge, which is the desired
    fail-closed semantics for the missing-signal case.
    """
    runner = runner or subprocess.run
    fields = (
        "number,state,files,additions,deletions,statusCheckRollup,isDraft,isCrossRepository,author"
    )
    result = _run(runner, ["gh", "pr", "view", str(pr_number), "--json", fields])
    data = _json.loads(result.stdout)
    files = [f["path"] for f in data.get("files", [])]
    rollup = data.get("statusCheckRollup", []) or []
    checks_passing = all(_check_is_green(c) for c in rollup) if rollup else True
    author = data.get("author") or {}
    author_login = str(author.get("login") or "") if isinstance(author, dict) else ""
    is_cross_repository = bool(data.get("isCrossRepository", False))
    author_association = fetch_author_association(pr_number, runner=runner)
    return PRView(
        number=int(data.get("number", pr_number)),
        state=str(data.get("state", "OPEN")),
        files=files,
        additions=int(data.get("additions", 0)),
        deletions=int(data.get("deletions", 0)),
        checks_passing=checks_passing,
        is_draft=bool(data.get("isDraft", False)),
        is_cross_repository=is_cross_repository,
        author_login=author_login,
        author_association=author_association,
    )


def fetch_author_association(pr_number: int, *, runner: PRRunner | None = None) -> str | None:
    """Read ``author_association`` for ``pr_number`` via the GitHub REST API.

    ``gh pr view --json`` does not expose this field even though the
    underlying REST endpoint does, so callers reach for ``gh api
    repos/<owner>/<repo>/pulls/<num>`` directly. Returns the upper-case
    association string (e.g. ``"MEMBER"``, ``"COLLABORATOR"``, ``"NONE"``)
    on success and ``None`` on any failure mode. Callers treat ``None``
    as untrusted so transient ``gh`` outages fail closed.
    """
    runner = runner or subprocess.run
    owner_repo = _resolve_owner_repo(runner=runner)
    if owner_repo is None:
        return None
    try:
        result = _run(
            runner,
            ["gh", "api", f"repos/{owner_repo}/pulls/{pr_number}"],
            allow_fail=True,
        )
    except GitOpsError:
        return None
    if result is None or result.returncode != 0 or not result.stdout.strip():
        return None
    try:
        data = _json.loads(result.stdout)
    except (ValueError, TypeError):
        return None
    assoc = data.get("author_association")
    if not isinstance(assoc, str) or not assoc.strip():
        return None
    return assoc.strip().upper()


def is_pr_trusted(
    *,
    is_cross_repository: bool,
    association: str | None,
    author_login: str,
    config: ConflictResolverConfig,
) -> bool:
    """Return True iff the PR's author may drive the enforce-mode path.

    Trust requires *all* of:

    1. The head ref lives in this repo (``is_cross_repository`` is False).
       Fork PRs are never trusted, even when the author also belongs to
       the trusted set — GitHub's ``pull_request`` event fires from forks
       and an attacker can name their fork branch anything they like
       (including a synthetic ``claude/daily-…`` shape).
    2. Either ``association`` (upper-cased upstream) is in
       ``config.trusted_associations``, or ``author_login`` is in the
       explicit ``config.trusted_authors`` allowlist. The login check is
       case-sensitive against the canonical form ``gh`` returns.

    Defense in depth: any caller that calls ``gh pr merge --squash --auto``
    is expected to pass through the gate, which calls this helper. The
    structural guarantee that orchestrators only invoke
    ``maybe_automerge.py`` on PRs they themselves created remains as
    belt-and-suspenders, but the trust check is no longer the only thing
    protecting auto-merge — this function is.
    """
    if is_cross_repository:
        return False
    if association is None:
        return False
    if association in config.trusted_associations:
        return True
    return bool(author_login) and author_login in config.trusted_authors


def comment_pr(
    pr_number: int,
    body: str,
    *,
    runner: PRRunner | None = None,
    dedupe_key: str | None = None,
) -> None:
    """Post a comment on the PR, or edit an existing one when ``dedupe_key`` matches.

    When ``dedupe_key`` is provided, the body is prefixed with
    ``<!-- {dedupe_key} -->`` and the function scans existing comments via
    ``gh pr view --json comments`` for that exact marker. If found, the
    matching comment is edited in place via ``gh api -X PATCH``; otherwise a
    new comment is posted with ``gh pr comment``. This keeps the watcher from
    spamming a fresh comment every time CI flips.
    """
    runner = runner or subprocess.run
    if dedupe_key:
        marker = f"<!-- {dedupe_key} -->"
        body = f"{marker}\n{body}" if not body.startswith(marker) else body
        existing_id = _find_existing_comment_id(pr_number, marker, runner=runner)
        if existing_id is not None:
            owner_repo = _resolve_owner_repo(runner=runner)
            if owner_repo is not None:
                _run(
                    runner,
                    [
                        "gh",
                        "api",
                        "-X",
                        "PATCH",
                        f"repos/{owner_repo}/issues/comments/{existing_id}",
                        "-f",
                        f"body={body}",
                    ],
                )
                return
    _run(runner, ["gh", "pr", "comment", str(pr_number), "--body", body])


def _find_existing_comment_id(pr_number: int, marker: str, *, runner: PRRunner) -> int | None:
    """Return the id of the first comment whose body contains ``marker``, or ``None``."""
    try:
        result = _run(
            runner,
            ["gh", "pr", "view", str(pr_number), "--json", "comments"],
            allow_fail=True,
        )
    except GitOpsError:
        return None
    if not result or result.returncode != 0 or not result.stdout.strip():
        return None
    try:
        data = _json.loads(result.stdout)
    except (ValueError, TypeError):
        return None
    for comment in data.get("comments") or []:
        body = comment.get("body") or ""
        if marker in body:
            comment_id = comment.get("id") or comment.get("databaseId")
            if isinstance(comment_id, int):
                return comment_id
            if isinstance(comment_id, str) and comment_id.isdigit():
                return int(comment_id)
    return None


def _resolve_owner_repo(*, runner: PRRunner) -> str | None:
    """Return ``owner/repo`` for the current GitHub remote via ``gh repo view``."""
    try:
        result = _run(
            runner,
            ["gh", "repo", "view", "--json", "nameWithOwner"],
            allow_fail=True,
        )
    except GitOpsError:
        return None
    if not result or result.returncode != 0 or not result.stdout.strip():
        return None
    try:
        data = _json.loads(result.stdout)
    except (ValueError, TypeError):
        return None
    value = data.get("nameWithOwner")
    return value if isinstance(value, str) and value else None


def enable_automerge(pr_number: int, *, runner: PRRunner | None = None) -> None:
    """``gh pr merge --squash --auto``."""
    runner = runner or subprocess.run
    _run(runner, ["gh", "pr", "merge", str(pr_number), "--squash", "--auto"])


def disable_automerge(pr_number: int, *, runner: PRRunner | None = None) -> None:
    """``gh pr merge --disable-auto`` — undo a previously-queued auto-merge.

    Used by :func:`apply_gate` in ``enforce`` mode when re-evaluation finds CI
    has gone red, so a queued ``--auto`` from the in-routine call doesn't
    merge the PR once branch protection later allows it. Idempotent: if no
    auto-merge is queued, ``gh`` returns non-zero and we swallow it via
    ``allow_fail``.
    """
    runner = runner or subprocess.run
    _run(
        runner,
        ["gh", "pr", "merge", str(pr_number), "--disable-auto"],
        allow_fail=True,
    )


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
