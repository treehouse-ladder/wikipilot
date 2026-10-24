"""``wikipilot tool-changes``: what moved in the tool registry since a baseline.

The benchmark scout's actual interface. Diffs the tracked fields
(``[tool_profiles].tracked_fields`` — ``status``, ``pricing``,
``commercial_use``, ``arena_rank``) of every ``profile: tool`` entity
against the same file at a baseline git revision, and lists tool entities
that appeared or disappeared. Zero LLM tokens: frontmatter + ``git show``.

Two baseline selectors:

- ``--since-rev <sha>`` — used verbatim. The natural query for the benchmark,
  which pins the wiki commit each round read.
- ``--since YYYY-MM-DD`` — resolved to ``git rev-list -1 --before=<date> HEAD``
  (the last commit on or before that date). Several PRs merge per day, so a
  date is a coarser baseline than a SHA; it's what the daily/weekly reports
  use when they don't have a pinned SHA.

Output is either markdown (the ``## Creator tooling changes`` section of the
daily and weekly reports) or the versioned JSON contract documented in
``docs/architecture.md`` (``schema_version: 1``, additive-only).
"""

from __future__ import annotations

import io
import json
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

import frontmatter

from wikipilot.config import ToolProfilesConfig
from wikipilot.tools import (
    SCHEMA_VERSION,
    GitRunner,
    ToolEntity,
    _normalize_date,
    current_head_rev,
    default_git_runner,
    find_repo_root,
    is_tool_page,
    iter_tool_entities,
    resolve_source_url,
    strip_wikilink,
    tool_record,
)
from wikipilot.wiki import Page, Vault, WikiError

EMPTY_MESSAGE = "_No creator tooling changes in this period._"


@dataclass(frozen=True)
class FieldChange:
    entity: str
    field: str
    old: Any
    new: Any
    source_slug: str | None
    source_url: str | None
    last_verified: str | None

    def to_json(self) -> dict[str, Any]:
        return {
            "entity": self.entity,
            "field": self.field,
            "old": self.old,
            "new": self.new,
            "source_slug": self.source_slug,
            "source_url": self.source_url,
            "last_verified": self.last_verified,
        }


@dataclass
class ToolChangeReport:
    baseline_rev: str | None
    head_rev: str | None
    changes: list[FieldChange] = field(default_factory=list)
    new_tools: list[dict[str, Any]] = field(default_factory=list)
    removed_tools: list[str] = field(default_factory=list)

    @property
    def is_empty(self) -> bool:
        return not (self.changes or self.new_tools or self.removed_tools)

    def to_json(self) -> dict[str, Any]:
        return {
            "schema_version": SCHEMA_VERSION,
            "baseline_rev": self.baseline_rev,
            "head_rev": self.head_rev,
            "changes": [c.to_json() for c in self.changes],
            "new_tools": list(self.new_tools),
            "removed_tools": list(self.removed_tools),
        }


def resolve_baseline_rev(
    vault: Vault,
    *,
    since: date | None = None,
    since_rev: str | None = None,
    git_runner: GitRunner | None = None,
) -> str:
    """Turn ``--since`` / ``--since-rev`` into a concrete SHA.

    Exactly one of ``since`` / ``since_rev`` must be given. Raises
    :class:`WikiError` when the vault isn't inside a git repo, the SHA
    doesn't resolve, or no commit exists on/before ``since``.
    """
    if (since is None) == (since_rev is None):
        raise WikiError("tool-changes needs exactly one of --since DATE or --since-rev SHA")
    runner = git_runner or default_git_runner
    root = find_repo_root(vault.root)
    if root is None:
        raise WikiError(f"{vault.root} is not inside a git repository")
    if since_rev is not None:
        result = runner(
            ["git", "-C", str(root), "rev-parse", "--verify", f"{since_rev}^{{commit}}"]
        )
        if result.returncode != 0 or not (result.stdout or "").strip():
            raise WikiError(f"--since-rev {since_rev!r} does not resolve to a commit")
        return result.stdout.strip()
    assert since is not None
    # `--before` is inclusive of the whole day when given a bare date; push to
    # end-of-day explicitly so "since 2026-10-01" means "state at the end of
    # 2026-10-01".
    result = runner(
        [
            "git",
            "-C",
            str(root),
            "rev-list",
            "-1",
            f"--before={since.isoformat()}T23:59:59",
            "HEAD",
        ]
    )
    sha = (result.stdout or "").strip()
    if result.returncode != 0 or not sha:
        raise WikiError(f"no commit on or before {since.isoformat()} on HEAD's history")
    return sha


def _baseline_entities(
    vault: Vault,
    baseline_rev: str,
    *,
    git_runner: GitRunner,
) -> dict[str, Page]:
    """Read every ``profile: tool`` entity as it was at ``baseline_rev``.

    Lists ``wiki/entities/`` at the baseline via ``git ls-tree`` and reads
    each file with ``git show``; pages that weren't tool entities then are
    skipped. Returns ``{slug: Page}``.
    """
    root = find_repo_root(vault.root)
    if root is None:
        return {}
    entities_rel = _repo_relative(root, vault.dir_for("entities"))
    listing = git_runner(
        ["git", "-C", str(root), "ls-tree", "--name-only", baseline_rev, f"{entities_rel}/"]
    )
    if listing.returncode != 0:
        return {}
    out: dict[str, Page] = {}
    for line in (listing.stdout or "").splitlines():
        rel = line.strip()
        if not rel.endswith(".md"):
            continue
        name = rel.rsplit("/", 1)[-1]
        if name.startswith("_"):
            continue
        shown = git_runner(["git", "-C", str(root), "show", f"{baseline_rev}:{rel}"])
        if shown.returncode != 0:
            continue
        try:
            post = frontmatter.load(io.StringIO(shown.stdout))
        except Exception:  # noqa: BLE001
            continue
        page = Page(path=root / rel, metadata=dict(post.metadata), content=post.content)
        if not is_tool_page(page):
            continue
        out[Path(rel).stem] = page
    return out


def _repo_relative(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def _comparable(value: Any) -> Any:
    """Normalize a frontmatter value so equal-meaning values compare equal."""
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, (list, tuple)):
        return [_comparable(v) for v in value]
    return value


def _source_for(page_md: dict[str, Any], field_name: str) -> str | None:
    """Pick the citation for a tracked field's current value.

    Scalar fields use ``<field>_source``. For the list-valued ``arena_rank``
    (whose ``_source`` is a parallel list) the first non-null source is used.
    """
    raw = page_md.get(f"{field_name}_source")
    if isinstance(raw, (list, tuple)):
        for item in raw:
            slug = strip_wikilink(item)
            if slug:
                return slug
        return None
    return strip_wikilink(raw)


def compute_tool_changes(
    vault: Vault,
    config: ToolProfilesConfig,
    *,
    baseline_rev: str,
    git_runner: GitRunner | None = None,
    head_rev: str | None = None,
) -> ToolChangeReport:
    """Diff current tool entities against ``baseline_rev``."""
    runner = git_runner or default_git_runner
    head = head_rev if head_rev is not None else current_head_rev(vault, runner)
    report = ToolChangeReport(baseline_rev=baseline_rev, head_rev=head)
    current: dict[str, ToolEntity] = {t.slug: t for t in iter_tool_entities(vault)}
    baseline = _baseline_entities(vault, baseline_rev, git_runner=runner)

    for slug in sorted(current):
        tool = current[slug]
        if slug not in baseline:
            report.new_tools.append(tool_record(vault, tool))
            continue
        old_md = baseline[slug].metadata
        new_md = tool.page.metadata
        for field_name in config.tracked_fields:
            old_v = _comparable(old_md.get(field_name))
            new_v = _comparable(new_md.get(field_name))
            if old_v == new_v:
                continue
            source_slug = _source_for(new_md, field_name)
            report.changes.append(
                FieldChange(
                    entity=slug,
                    field=field_name,
                    old=old_v,
                    new=new_v,
                    source_slug=source_slug,
                    source_url=resolve_source_url(vault, source_slug),
                    last_verified=_normalize_date(new_md.get("last_verified")),
                )
            )
    report.removed_tools = sorted(set(baseline) - set(current))
    return report


def render_markdown(
    report: ToolChangeReport, *, heading: str = "## Creator tooling changes"
) -> str:
    """Render the report as the report-page section."""
    lines = [heading, ""]
    if report.is_empty:
        lines.append(EMPTY_MESSAGE)
        return "\n".join(lines) + "\n"
    for change in report.changes:
        cite = f" [[{change.source_slug}]]" if change.source_slug else " _(no source recorded)_"
        lines.append(
            f"- [[{change.entity}]] `{change.field}`: {_fmt(change.old)} → {_fmt(change.new)}{cite}"
        )
    for tool in report.new_tools:
        access = ", ".join(tool.get("access") or []) or "unknown"
        lines.append(
            f"- **New tool** [[{tool['slug']}]] ({tool.get('modality') or 'unknown'}; "
            f"access: {access}; status: {tool.get('status') or 'unknown'})"
        )
    for slug in report.removed_tools:
        lines.append(f"- **Removed tool** `{slug}` (no longer a `profile: tool` entity)")
    if report.baseline_rev or report.head_rev:
        lines.append("")
        lines.append(
            f"_Baseline `{(report.baseline_rev or '?')[:12]}` → head `{(report.head_rev or '?')[:12]}`._"
        )
    return "\n".join(lines) + "\n"


def render_json(report: ToolChangeReport) -> str:
    return json.dumps(report.to_json(), indent=2, ensure_ascii=False, default=str) + "\n"


def _fmt(value: Any) -> str:
    if value is None:
        return "_missing_"
    if isinstance(value, list):
        if not value:
            return "`[]`"
        return "`" + "; ".join(str(v) for v in value) + "`"
    return f"`{value}`"


__all__ = [
    "EMPTY_MESSAGE",
    "FieldChange",
    "ToolChangeReport",
    "compute_tool_changes",
    "render_json",
    "render_markdown",
    "resolve_baseline_rev",
]
