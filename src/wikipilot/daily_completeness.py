"""Daily completeness sentinel — detect when a Daily Research run is incomplete.

Fires once per evening (typically via the GitHub Actions workflow at
``.github/workflows/daily-completeness.yml`` on a cron schedule) and answers
one question: **did every daily topic produce a merged PR today, and did the
report PR merge?** If the answer is no, file a single GitHub issue tagged
``daily-incomplete`` listing exactly what's missing.

Why this exists: the Daily Research orchestrator has three layers of recovery
for the "PR sits unmerged" failure mode (in-routine ``maybe_automerge.py``,
end-of-run ``recover-prs``, push-event Conflict Resolver). On 2026-05-25 all
three failed simultaneously because the orchestrator died mid-loop, leaving
3 of 5 expected topics with no PR at all (the existing safety nets only
catch already-existing-but-stuck PRs). The sentinel closes the structural
gap: it inspects the *expected* set (from ``topics.yaml``) against the
*observed* set (merged PRs to ``main`` today) and surfaces the delta.

This module is pure Python. The GitHub-calling code accepts an injectable
``runner`` (matching the rest of ``wikipilot.git_ops``) so unit tests can
exercise every branch without hitting the real ``gh`` binary. ``gh`` is
only invoked through the runner — never via ``gh`` directly in this module.

The output schema is :class:`CompletenessReport`. The CLI wrapper
(:func:`wikipilot.cli.daily_completeness_check_cmd`) turns it into a
GitHub issue when there's anything missing and prints a one-line status
otherwise.
"""

from __future__ import annotations

import json as _json
import subprocess
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Literal

from wikipilot.config import BranchesConfig, TopicConfig
from wikipilot.git_ops import PRRunner

DEFAULT_LABEL = "daily-incomplete"
DEFAULT_ISSUE_TITLE_PREFIX = "Daily Research incomplete"
DEFAULT_LABEL_COLOR = "FBCA04"  # GitHub's built-in `yellow`/`warning`.
DEFAULT_LABEL_DESCRIPTION = (
    "Daily Research completeness sentinel found gaps for the indicated date."
)

ReportStatus = Literal["merged", "open", "missing"]


@dataclass(frozen=True)
class TopicStatus:
    """One topic's resolution for a given date."""

    topic_id: str
    expected_branch: str
    state: ReportStatus
    pr_number: int | None = None
    pr_url: str = ""


@dataclass(frozen=True)
class CompletenessReport:
    """Aggregate verdict for one daily run, suitable for issue rendering.

    ``report_pr_state`` distinguishes the three meaningful outcomes for the
    daily aggregate PR (``claude/daily-<DATE>/_report``):

    - ``"merged"``: the aggregate landed; the day's log + index + report
      page are present in ``main``.
    - ``"open"``: the report PR exists but hasn't merged yet (still in
      review, in the merge queue, or blocked on CI). The routine ran
      far enough to produce the aggregate.
    - ``"missing"``: the orchestrator never got to Step 6 — most likely
      it died during the per-topic loop or during Step 5's wait.

    The sentinel files an issue when ANY of ``missing_topics``,
    ``open_topics`` (only when ``flag_open_topics`` is True),
    OR ``report_pr_state in {"open", "missing"}`` is non-trivial.
    """

    today: date
    expected_topic_ids: list[str]
    topic_results: list[TopicStatus]
    report_pr_state: ReportStatus
    report_pr_number: int | None = None
    report_pr_url: str = ""

    @property
    def missing_topics(self) -> list[TopicStatus]:
        return [t for t in self.topic_results if t.state == "missing"]

    @property
    def open_topics(self) -> list[TopicStatus]:
        return [t for t in self.topic_results if t.state == "open"]

    @property
    def merged_topics(self) -> list[TopicStatus]:
        return [t for t in self.topic_results if t.state == "merged"]

    def has_gap(self, *, flag_open_topics: bool = False) -> bool:
        """True iff the run looks incomplete and an issue should be filed.

        ``flag_open_topics=False`` (the default) deliberately ignores
        topics whose PR is open-but-not-merged. The sentinel is meant
        to catch the "orchestrator died, PR never created" case; a PR
        sitting open with green CI is the Conflict Resolver routine's
        problem, not the sentinel's. Set ``flag_open_topics=True``
        when you want the strictest signal.
        """
        if self.missing_topics:
            return True
        if self.report_pr_state in ("open", "missing"):
            return True
        return bool(flag_open_topics and self.open_topics)


def daily_topics(topics: Iterable[TopicConfig]) -> list[TopicConfig]:
    """Filter to topics the Daily Research routine processes (``frequency: daily``)."""
    return [t for t in topics if t.frequency == "daily"]


def expected_topic_branches(
    topics: Iterable[TopicConfig],
    *,
    today: date,
    branches: BranchesConfig | None = None,
) -> dict[str, str]:
    """Return ``{topic_id: expected_branch_name}`` for the daily-frequency topics."""
    template = (branches or BranchesConfig()).daily_template
    iso = today.isoformat()
    return {t.id: template.format(date=iso, topic_id=t.id) for t in daily_topics(topics)}


def expected_report_branch(
    *,
    today: date,
    branches: BranchesConfig | None = None,
) -> str:
    """Return the expected report-PR branch name (``claude/daily-<DATE>/_report``).

    The orchestrator's Step 6 cuts this branch from post-topic-merge ``main``
    (see ``prompts/daily_runner.md``). The slug ``_report`` is reserved by
    the daily run; it can't be a topic id (topic ids are kebab-case, and the
    leading underscore conflicts with the personal-scratch convention).
    """
    template = (branches or BranchesConfig()).daily_template
    return template.format(date=today.isoformat(), topic_id="_report")


def build_completeness_report(
    *,
    topics: Iterable[TopicConfig],
    today: date,
    branches: BranchesConfig | None = None,
    runner: PRRunner | None = None,
) -> CompletenessReport:
    """Inspect GitHub and produce a :class:`CompletenessReport` for ``today``.

    The inspection issues two ``gh pr list`` calls:

    1. Merged PRs to ``main`` whose ``mergedAt`` falls inside the ``today``
       UTC day window. This is the source of truth for "what landed".
    2. Open PRs on ``main`` whose head ref starts with the daily template
       prefix. This catches in-flight PRs (still in the merge queue, still
       open) so the sentinel doesn't falsely flag a slow-merging run.

    Per-topic resolution is then:

    - ``merged``: a merged PR exists for the expected branch.
    - ``open``: no merged PR, but an open PR exists for the expected branch.
    - ``missing``: no PR exists at all (neither merged nor open).

    Report PR resolution follows the same three states, applied to
    ``claude/daily-<DATE>/_report``.
    """
    branches = branches or BranchesConfig()
    expected = expected_topic_branches(topics, today=today, branches=branches)
    expected_report = expected_report_branch(today=today, branches=branches)

    merged = _list_merged_prs_on(today, runner=runner)
    open_prs = _list_open_claude_prs(runner=runner)
    merged_by_branch = {pr["headRefName"]: pr for pr in merged}
    open_by_branch = {pr["headRefName"]: pr for pr in open_prs}

    topic_results: list[TopicStatus] = []
    for topic_id, branch in expected.items():
        if branch in merged_by_branch:
            pr = merged_by_branch[branch]
            topic_results.append(
                TopicStatus(
                    topic_id=topic_id,
                    expected_branch=branch,
                    state="merged",
                    pr_number=_int_or_none(pr.get("number")),
                    pr_url=str(pr.get("url") or ""),
                )
            )
        elif branch in open_by_branch:
            pr = open_by_branch[branch]
            topic_results.append(
                TopicStatus(
                    topic_id=topic_id,
                    expected_branch=branch,
                    state="open",
                    pr_number=_int_or_none(pr.get("number")),
                    pr_url=str(pr.get("url") or ""),
                )
            )
        else:
            topic_results.append(
                TopicStatus(
                    topic_id=topic_id,
                    expected_branch=branch,
                    state="missing",
                )
            )

    if expected_report in merged_by_branch:
        pr = merged_by_branch[expected_report]
        report_pr_state: ReportStatus = "merged"
        report_pr_number = _int_or_none(pr.get("number"))
        report_pr_url = str(pr.get("url") or "")
    elif expected_report in open_by_branch:
        pr = open_by_branch[expected_report]
        report_pr_state = "open"
        report_pr_number = _int_or_none(pr.get("number"))
        report_pr_url = str(pr.get("url") or "")
    else:
        report_pr_state = "missing"
        report_pr_number = None
        report_pr_url = ""

    return CompletenessReport(
        today=today,
        expected_topic_ids=list(expected.keys()),
        topic_results=topic_results,
        report_pr_state=report_pr_state,
        report_pr_number=report_pr_number,
        report_pr_url=report_pr_url,
    )


def render_issue_title(report: CompletenessReport) -> str:
    return f"{DEFAULT_ISSUE_TITLE_PREFIX} — {report.today.isoformat()}"


def render_issue_body(report: CompletenessReport) -> str:
    """Render the markdown body for the GitHub issue.

    Structure (stable across runs so existing issues can be edited in place):

    - One-line summary: how many topics merged / open / missing, and the
      report PR's state.
    - ``## Missing topics`` — one bullet per missing topic with the
      expected branch name. If empty, the section is omitted.
    - ``## Open topics`` — one bullet per still-open PR with link.
    - ``## Merged topics`` — one bullet per merged PR with link.
    - ``## Report PR`` — state + link if applicable.
    - ``## Suggested remediation`` — point at the right CLI commands.
    """
    today_iso = report.today.isoformat()
    merged = report.merged_topics
    open_ = report.open_topics
    missing = report.missing_topics
    lines: list[str] = []
    lines.append(
        f"Daily Research run for **{today_iso}** looks incomplete: "
        f"{len(merged)} merged, {len(open_)} open, {len(missing)} missing — "
        f"report PR: **{report.report_pr_state}**."
    )
    lines.append("")
    lines.append(
        f"Expected {len(report.expected_topic_ids)} daily topic(s): "
        + ", ".join(f"`{tid}`" for tid in report.expected_topic_ids)
        + "."
    )
    lines.append("")

    if missing:
        lines.append("## Missing topics")
        lines.append("")
        lines.append(
            "These topics never produced a PR. Most likely the orchestrator "
            "died mid-loop before reaching them, OR the topic-researcher "
            "subagent crashed and returned no proposal."
        )
        lines.append("")
        for status in missing:
            lines.append(f"- `{status.topic_id}` — expected branch `{status.expected_branch}`")
        lines.append("")

    if open_:
        lines.append("## Open topics (PR exists but not yet merged)")
        lines.append("")
        for status in open_:
            link = status.pr_url or f"PR #{status.pr_number}" if status.pr_number else "PR ?"
            lines.append(f"- `{status.topic_id}` — {link}")
        lines.append("")

    if merged:
        lines.append("## Merged topics")
        lines.append("")
        for status in merged:
            link = status.pr_url or f"PR #{status.pr_number}" if status.pr_number else "(no link)"
            lines.append(f"- `{status.topic_id}` — {link}")
        lines.append("")

    lines.append("## Report PR")
    lines.append("")
    if report.report_pr_state == "merged":
        lines.append(
            f"Aggregate report PR merged: {report.report_pr_url or f'#{report.report_pr_number}'}"
        )
    elif report.report_pr_state == "open":
        lines.append(
            "Aggregate report PR is open but hasn't merged. Investigate via "
            f"`wikipilot recover-prs --base main` or the Conflict Resolver "
            f"routine: {report.report_pr_url or f'#{report.report_pr_number}'}"
        )
    else:
        lines.append(
            "Aggregate report PR (`claude/daily-{today}/_report`) was never created. "
            "The orchestrator never reached Step 6 of `prompts/daily_runner.md`."
        )
    lines.append("")

    lines.append("## Suggested remediation")
    lines.append("")
    step = 1
    if missing:
        lines.append(
            f"{step}. **Re-fire the missing topics** one at a time once you've "
            "confirmed the underlying failure won't recur:"
        )
        lines.append("")
        for status in missing:
            lines.append("   ```")
            lines.append(f"   uv run wikipilot research --topic {status.topic_id}")
            lines.append("   ```")
        lines.append("")
        step += 1
    if open_ or report.report_pr_state == "open":
        lines.append(f"{step}. **Unblock any open PRs** sitting on a clean+green base by running:")
        lines.append("")
        lines.append("   ```")
        lines.append("   uv run wikipilot recover-prs --base main")
        lines.append("   ```")
        lines.append("")
        step += 1
    lines.append(
        f"{step}. **Triage the underlying failure** — check the Routines UI logs for "
        f"the {today_iso} Daily Research run. Common causes: cloud session "
        "timeout, OOM, Task tool failure on one of the wiki-merger dispatches, "
        "or a topic-researcher subagent crash."
    )
    lines.append("")
    lines.append(
        "_Filed by `wikipilot daily-completeness-check` — see "
        "`docs/routines-setup.md` for the workflow that fires this check._"
    )

    return "\n".join(lines)


def find_existing_issue(
    *,
    today: date,
    label: str = DEFAULT_LABEL,
    runner: PRRunner | None = None,
) -> int | None:
    """Find an open issue tagged ``label`` whose title matches ``today``.

    Idempotency: the workflow fires once per evening but a human might
    also fire it manually. Returning an existing issue number means the
    caller can ``gh issue edit`` instead of opening a duplicate.

    Returns the issue number on hit, ``None`` on miss (including any
    ``gh`` failure — fail-closed, so worst case the caller opens a fresh
    issue rather than silently dropping the alert).
    """
    runner = runner or subprocess.run
    expected_title = render_issue_title(_empty_report(today))
    args = [
        "gh",
        "issue",
        "list",
        "--state",
        "open",
        "--label",
        label,
        "--search",
        f"in:title {today.isoformat()}",
        "--json",
        "number,title",
        "--limit",
        "50",
    ]
    try:
        result = runner(args, capture_output=True, text=True, check=False)
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0 or not (result.stdout or "").strip():
        return None
    try:
        data = _json.loads(result.stdout)
    except (ValueError, TypeError):
        return None
    if not isinstance(data, list):
        return None
    for issue in data:
        if not isinstance(issue, dict):
            continue
        if str(issue.get("title", "")) == expected_title:
            number = issue.get("number")
            if isinstance(number, int):
                return number
    return None


def ensure_label(
    label: str = DEFAULT_LABEL,
    *,
    color: str = DEFAULT_LABEL_COLOR,
    description: str = DEFAULT_LABEL_DESCRIPTION,
    runner: PRRunner | None = None,
) -> bool:
    """Idempotently create ``label`` on the current repo via ``gh label create --force``.

    ``--force`` is the GitHub CLI's "create-or-update" flag — succeeds whether
    the label already exists (with the same or different metadata) or not.
    Without this, the first sentinel fire against a freshly-cloned (or freshly
    forked) repo fails on ``gh issue create --label daily-incomplete: label
    'daily-incomplete' not found`` — exactly what happened on the 2026-05-25
    smoke-test fire.

    Returns ``True`` on success, ``False`` on any ``gh`` failure (in which
    case the caller's ``gh issue create`` will fail too, and the existing
    fail-closed handling in :func:`open_or_update_issue` will return
    ``None`` so the CLI logs and exits non-zero).
    """
    runner = runner or subprocess.run
    args = [
        "gh",
        "label",
        "create",
        label,
        "--color",
        color,
        "--description",
        description,
        "--force",
    ]
    try:
        result = runner(args, capture_output=True, text=True, check=False)
    except (OSError, subprocess.SubprocessError):
        return False
    return result.returncode == 0


def open_or_update_issue(
    report: CompletenessReport,
    *,
    label: str = DEFAULT_LABEL,
    runner: PRRunner | None = None,
) -> int | None:
    """File the completeness gap as a GitHub issue.

    If an issue already exists for ``report.today`` (matched by
    :func:`find_existing_issue`), the body is replaced via ``gh issue edit``.
    Otherwise a new issue is opened via ``gh issue create``.

    Returns the issue number on success; ``None`` on any ``gh`` failure.
    The caller (the CLI command) logs the failure but does NOT raise —
    failing to file an alert is preferable to crashing the cron job and
    masking the underlying daily-run incident.
    """
    runner = runner or subprocess.run
    if not ensure_label(label, runner=runner):
        return None
    title = render_issue_title(report)
    body = render_issue_body(report)
    existing = find_existing_issue(today=report.today, label=label, runner=runner)
    if existing is not None:
        args = [
            "gh",
            "issue",
            "edit",
            str(existing),
            "--body",
            body,
            "--add-label",
            label,
        ]
        try:
            result = runner(args, capture_output=True, text=True, check=False)
        except (OSError, subprocess.SubprocessError):
            return None
        if result.returncode != 0:
            return None
        return existing
    args = [
        "gh",
        "issue",
        "create",
        "--title",
        title,
        "--body",
        body,
        "--label",
        label,
    ]
    try:
        result = runner(args, capture_output=True, text=True, check=False)
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0:
        return None
    return _extract_issue_number(result.stdout or "")


# ---------------------------------------------------------------------------
# Internals
# ---------------------------------------------------------------------------


def _list_merged_prs_on(
    today: date,
    *,
    base: str = "main",
    runner: PRRunner | None = None,
) -> list[dict]:
    """Return PRs merged to ``base`` whose ``mergedAt`` falls on ``today`` (UTC).

    Uses ``gh pr list --search "merged:>=YYYY-MM-DD <YYYY-MM-DD+1>"``. The
    search syntax filters by GitHub's indexed merge timestamp, so the result
    set is bounded to the day window we care about — even on busy repos with
    hundreds of historical PRs.
    """
    runner = runner or subprocess.run
    start = today.isoformat()
    end = (today + timedelta(days=1)).isoformat()
    args = [
        "gh",
        "pr",
        "list",
        "--state",
        "merged",
        "--base",
        base,
        "--search",
        f"merged:{start}..{end}",
        "--json",
        "number,headRefName,mergedAt,url",
        "--limit",
        "100",
    ]
    return _gh_pr_list_json(args, runner=runner)


def _list_open_claude_prs(
    *,
    base: str = "main",
    runner: PRRunner | None = None,
) -> list[dict]:
    """Return open PRs on ``base`` with ``claude/`` head refs."""
    runner = runner or subprocess.run
    args = [
        "gh",
        "pr",
        "list",
        "--state",
        "open",
        "--base",
        base,
        "--json",
        "number,headRefName,url",
        "--limit",
        "100",
    ]
    data = _gh_pr_list_json(args, runner=runner)
    return [pr for pr in data if str(pr.get("headRefName", "")).startswith("claude/")]


def _gh_pr_list_json(args: list[str], *, runner: PRRunner) -> list[dict]:
    """Run ``gh pr list ...`` and parse the JSON output. Returns [] on failure.

    Fail-closed: a ``gh`` outage during the sentinel's run yields an empty
    list, which makes EVERY topic look ``missing``. That's actually the
    correct fail-mode — the operator sees a loud "everything missing"
    issue and investigates, rather than seeing a silently-passing check.
    """
    try:
        result = runner(args, capture_output=True, text=True, check=False)
    except (OSError, subprocess.SubprocessError):
        return []
    if result.returncode != 0 or not (result.stdout or "").strip():
        return []
    try:
        data = _json.loads(result.stdout)
    except (ValueError, TypeError):
        return []
    if not isinstance(data, list):
        return []
    return [item for item in data if isinstance(item, dict)]


def _empty_report(today: date) -> CompletenessReport:
    return CompletenessReport(
        today=today,
        expected_topic_ids=[],
        topic_results=[],
        report_pr_state="missing",
    )


def _int_or_none(value: object) -> int | None:
    return value if isinstance(value, int) else None


def _extract_issue_number(stdout: str) -> int | None:
    """Parse ``gh issue create``'s URL output to recover the issue number."""
    text = (stdout or "").strip()
    if not text:
        return None
    last = text.splitlines()[-1].rstrip("/").rsplit("/", 1)[-1]
    if last.isdigit():
        return int(last)
    return None


__all__ = [
    "DEFAULT_LABEL",
    "DEFAULT_ISSUE_TITLE_PREFIX",
    "CompletenessReport",
    "TopicStatus",
    "build_completeness_report",
    "daily_topics",
    "expected_report_branch",
    "expected_topic_branches",
    "find_existing_issue",
    "open_or_update_issue",
    "render_issue_body",
    "render_issue_title",
]
