"""Comparison pages: aggregate frontmatter across N entities into a table.

Phase 9 introduces ``comparison`` as a first-class wiki kind alongside
``concept``/``entity``. A comparison page surfaces N-way disagreement (or
plain side-by-side data) for a set of related entities — e.g.
``cost-comparison`` reads cost/Mtoken from each frontier-model entity page
and renders one row per model, one column per field.

Design notes
------------
- The page declares its inputs in frontmatter (``comparison_of``,
  ``compare_fields``); the body is a generated markdown table that can
  always be regenerated idempotently from those inputs.
- Missing values render as ``_unknown_`` so blank cells are visible (rather
  than silently empty); that's the explicit lint signal that a field needs
  to be backfilled on the source entity page.
- Renders are deterministic: alphabetical column order matches
  ``compare_fields`` ordering preserved as authored, alphabetical row order
  matches ``comparison_of`` ordering preserved as authored. Authors control
  presentation order; nothing is sorted behind their backs.
- Citations for the values themselves live on the entity pages, not the
  comparison page — so the lint's ``citation-density`` rule does NOT apply
  to ``kind: comparison`` (see ``lint._is_synthesis_page``).
"""

from __future__ import annotations

import re
import subprocess
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

from wikipilot.wiki import Page, Vault, WikiError

UNKNOWN_VALUE = "_unknown_"
"""Cell rendered when an entity page omits a requested field. Markdown
italic so it stands out in Obsidian without breaking table layout."""

NO_GLOSS_PLACEHOLDER = "_no gloss configured_"
"""Placeholder for the legend block when a column has no matching entry in
``[frontier_models.benchmark_glosses]`` / ``[frontier_models.cost_glosses]``.
Not an error — the comparison renderer is also used for comparisons outside
the frontier-models domain that may not register glosses at all."""

GitRunner = Callable[[list[str]], "subprocess.CompletedProcess[str]"]
"""Subprocess runner type used for `git show`-based diffs.

Default value (``_default_git_runner``) shells out to the real `git`.
Tests inject a fake to avoid touching the filesystem-level repo state."""


@dataclass(frozen=True)
class ComparisonInputs:
    """Inputs declared in a comparison page's frontmatter."""

    title: str
    entity_slugs: tuple[str, ...]
    fields: tuple[str, ...]
    highlight_leaders: bool = False
    show_glosses: bool = False
    cost_fields: tuple[str, ...] = ()
    glosses: dict[str, str] = field(default_factory=dict)


def aggregate_entity_fields(
    vault: Vault,
    entity_slugs: list[str] | tuple[str, ...],
    fields: list[str] | tuple[str, ...],
) -> dict[str, dict[str, Any]]:
    """Read ``fields`` from each entity page in ``entity_slugs``.

    Returns ``{entity_slug: {field: value}}``. Missing entity pages are
    represented as empty dicts (so the caller can decide whether to skip
    them or render ``_unknown_``); missing fields on a present entity are
    simply absent from the returned per-entity dict.
    """
    out: dict[str, dict[str, Any]] = {}
    entities_dir = vault.dir_for("entities")
    for slug in entity_slugs:
        page_path = entities_dir / f"{slug}.md"
        if not page_path.exists():
            out[slug] = {}
            continue
        page = Page.read(page_path)
        out[slug] = {field: page.metadata.get(field) for field in fields if field in page.metadata}
    return out


def render_comparison_table(
    aggregated: dict[str, dict[str, Any]],
    *,
    entity_slugs: list[str] | tuple[str, ...],
    fields: list[str] | tuple[str, ...],
    title: str,
    highlight_leaders: bool = False,
    cost_fields: list[str] | tuple[str, ...] = (),
    show_glosses: bool = False,
    glosses: dict[str, str] | None = None,
    leader_changes: str | None = None,
) -> str:
    """Render a deterministic markdown table from ``aggregated`` data.

    Row order follows ``entity_slugs`` (caller controls). Column order
    follows ``fields``. Cells that are missing render as :data:`UNKNOWN_VALUE`.
    The first column is always ``Entity`` (an Obsidian wikilink to the
    entity page) so the table lands as a navigation surface, not just a
    data dump.

    When ``highlight_leaders`` is true, the per-column #1 cell renders
    ``**bold**`` and the #2 cell renders ``_italic_``. Columns whose name
    appears in ``cost_fields`` are inverted (lower-is-better). Missing
    values are excluded from the ranking; numeric coercion best-efforts
    against ``float()`` and silently ignores non-numeric values.

    When ``show_glosses`` is true, a ``## What each column means for me``
    legend block is rendered immediately above the table. ``glosses`` is
    a ``{column_name: gloss_text}`` mapping (typically merged from
    ``[frontier_models.benchmark_glosses]`` + ``[frontier_models.cost_glosses]``);
    columns without an entry render :data:`NO_GLOSS_PLACEHOLDER`.

    ``leader_changes`` is an optional already-rendered markdown paragraph
    (see :func:`compute_leader_changes`) appended below the table as a
    ``## Leader changes since last regen`` section.
    """
    glosses = glosses or {}
    cost_fields_set = set(cost_fields)
    numeric_by_field = _coerce_numeric_columns(
        aggregated, entity_slugs=entity_slugs, fields=fields
    )
    leaders_by_field: dict[str, tuple[str | None, str | None]] = {}
    if highlight_leaders:
        for col in fields:
            lower_is_better = col in cost_fields_set
            leaders_by_field[col] = _rank_top_two(
                numeric_by_field.get(col, {}), lower_is_better=lower_is_better
            )

    header = ["Entity", *fields]
    sep = ["---"] * len(header)
    rows: list[list[str]] = []
    for slug in entity_slugs:
        row = [f"[[{slug}]]"]
        per_entity = aggregated.get(slug, {})
        for col in fields:
            value = per_entity.get(col)
            cell = _render_cell(value)
            if highlight_leaders and cell != UNKNOWN_VALUE:
                first, second = leaders_by_field.get(col, (None, None))
                if first == slug:
                    cell = f"**{cell}**"
                elif second == slug:
                    cell = f"_{cell}_"
            row.append(cell)
        rows.append(row)
    table_lines = [
        f"| {' | '.join(header)} |",
        f"| {' | '.join(sep)} |",
    ]
    table_lines.extend(f"| {' | '.join(row)} |" for row in rows)

    sections = [
        f"# {title}",
        "",
        "## Summary",
        "",
        (
            f"This comparison aggregates `{', '.join(fields)}` across "
            f"{len(entity_slugs)} entities. Cells marked {UNKNOWN_VALUE} are "
            f"missing on the source entity page; backfill the value there and "
            f"re-run `wikipilot compare regen {_slug_from_title(title)}` to refresh."
        ),
    ]
    if show_glosses:
        sections.extend(["", "## What each column means for me", ""])
        for col in fields:
            gloss = glosses.get(col, NO_GLOSS_PLACEHOLDER)
            sections.append(f"- **`{col}`** — {gloss}")
    sections.extend(["", *table_lines])
    if leader_changes:
        sections.extend(["", "## Leader changes since last regen", "", leader_changes.strip()])
    return "\n".join(sections) + "\n"


def _coerce_numeric_columns(
    aggregated: dict[str, dict[str, Any]],
    *,
    entity_slugs: list[str] | tuple[str, ...],
    fields: list[str] | tuple[str, ...],
) -> dict[str, dict[str, float]]:
    """Best-effort coerce each entity's value per field into a float.

    Returns ``{field: {entity_slug: float}}`` with non-coercible / missing
    values omitted (so callers can do simple max/min over the resulting
    mapping). Booleans are skipped — leader highlighting on a boolean
    column is rarely what you want, and there's no obvious "best" ordering.
    """
    out: dict[str, dict[str, float]] = {col: {} for col in fields}
    for slug in entity_slugs:
        per_entity = aggregated.get(slug, {})
        for col in fields:
            value = per_entity.get(col)
            if value is None or isinstance(value, bool):
                continue
            try:
                out[col][slug] = float(value)
            except (TypeError, ValueError):
                continue
    return out


def _rank_top_two(
    column: dict[str, float],
    *,
    lower_is_better: bool,
) -> tuple[str | None, str | None]:
    """Return ``(first_slug, second_slug)`` from ``{slug: float}``.

    Tie-break by entity slug (stable, alphabetical). Either or both may
    be ``None`` when the column has fewer than 2 numeric values — e.g.
    a brand-new benchmark with one entry shouldn't claim a runner-up.
    """
    if not column:
        return (None, None)
    items = sorted(column.items(), key=lambda kv: (kv[1], kv[0]))
    if not lower_is_better:
        items.reverse()
    first = items[0][0] if items else None
    second = items[1][0] if len(items) > 1 else None
    return (first, second)


def write_comparison_page(
    vault: Vault,
    slug: str,
    *,
    title: str,
    entity_slugs: list[str] | tuple[str, ...],
    fields: list[str] | tuple[str, ...],
    today: date | None = None,
    highlight_leaders: bool = False,
    show_glosses: bool = False,
    cost_fields: list[str] | tuple[str, ...] = (),
    glosses: dict[str, str] | None = None,
) -> Path:
    """Create a new comparison page at ``wiki/comparisons/<slug>.md``.

    Frontmatter is fully populated so the page is lint-clean immediately:
    ``comparison_of`` and ``compare_fields`` lists drive future regeneration,
    standard freshness fields land at ``today``. Optional ``highlight_leaders``
    and ``show_glosses`` are recorded in the frontmatter so subsequent
    ``regenerate_comparison`` calls produce the same rendering.
    """
    if len(entity_slugs) < 2:
        raise WikiError(f"comparison '{slug}' needs at least 2 entities (got {len(entity_slugs)})")
    if len(fields) < 1:
        raise WikiError(f"comparison '{slug}' needs at least 1 field (got 0)")
    today = today or date.today()
    aggregated = aggregate_entity_fields(vault, entity_slugs, fields)
    body = render_comparison_table(
        aggregated,
        entity_slugs=entity_slugs,
        fields=fields,
        title=title,
        highlight_leaders=highlight_leaders,
        cost_fields=cost_fields,
        show_glosses=show_glosses,
        glosses=glosses,
    )
    path = vault.page_path("comparison", slug)
    metadata: dict[str, Any] = {
        "title": title,
        "kind": "comparison",
        "comparison_of": list(entity_slugs),
        "compare_fields": list(fields),
        "sources": [],
        "last_updated": today,
        "last_verified": today,
        "freshness_window_days": 30,
    }
    if highlight_leaders:
        metadata["highlight_leaders"] = True
    if show_glosses:
        metadata["show_glosses"] = True
    page = Page.from_dict(path, metadata, body)
    page.write()
    return path


def regenerate_comparison(
    vault: Vault,
    comparison_slug: str,
    *,
    today: date | None = None,
    cost_fields: list[str] | tuple[str, ...] = (),
    glosses: dict[str, str] | None = None,
    git_runner: GitRunner | None = None,
) -> Path:
    """Re-read frontmatter for an existing comparison and rewrite its body.

    Idempotent: bumps ``last_updated`` to ``today`` (so freshness reports
    surface "this comparison was regenerated today") but does NOT bump
    ``last_verified`` (the underlying entity pages may not have been
    re-checked; the comparison itself is just a derived view).

    When the page's frontmatter declares ``highlight_leaders: true``, the
    caller may pass ``cost_fields`` (defaults to empty) to invert the
    leader ordering for lower-is-better columns. When the page declares
    ``show_glosses: true``, the caller passes ``glosses`` (typically
    merged from ``[frontier_models.benchmark_glosses]`` +
    ``[frontier_models.cost_glosses]``) to populate the legend block.

    Leader-change diffing reads the previous on-disk revision of the
    same file via ``git show HEAD:<path>``; non-git environments (or
    a brand-new page) silently skip the section. ``git_runner`` is
    injectable for tests.
    """
    today = today or date.today()
    path = vault.page_path("comparison", comparison_slug)
    if not path.exists():
        raise WikiError(f"no comparison page at {path}")
    page = Page.read(path)
    inputs = _read_inputs(page)
    aggregated = aggregate_entity_fields(vault, inputs.entity_slugs, inputs.fields)
    leader_changes_text: str | None = None
    if inputs.highlight_leaders:
        leader_changes_text = compute_leader_changes(
            vault,
            path,
            aggregated=aggregated,
            entity_slugs=inputs.entity_slugs,
            fields=inputs.fields,
            cost_fields=cost_fields,
            git_runner=git_runner,
        )
    page.content = render_comparison_table(
        aggregated,
        entity_slugs=inputs.entity_slugs,
        fields=inputs.fields,
        title=inputs.title,
        highlight_leaders=inputs.highlight_leaders,
        cost_fields=cost_fields,
        show_glosses=inputs.show_glosses,
        glosses=glosses,
        leader_changes=leader_changes_text,
    )
    page.metadata["last_updated"] = today
    page.write()
    return path


def compute_leader_changes(
    vault: Vault,
    path: Path,
    *,
    aggregated: dict[str, dict[str, Any]],
    entity_slugs: list[str] | tuple[str, ...],
    fields: list[str] | tuple[str, ...],
    cost_fields: list[str] | tuple[str, ...] = (),
    git_runner: GitRunner | None = None,
) -> str | None:
    """Diff today's column leaders against the prior on-disk revision.

    Returns a one-paragraph markdown summary (one bullet per column whose
    #1 changed), or ``None`` when the page isn't tracked in git or there's
    no movement to report. The previous leaders are reconstructed by
    parsing the prior revision's table for ``**bold**`` cells — no
    parallel state file needed.
    """
    cost_fields_set = set(cost_fields)
    numeric = _coerce_numeric_columns(
        aggregated, entity_slugs=entity_slugs, fields=fields
    )
    current_leaders: dict[str, str | None] = {}
    for col in fields:
        first, _second = _rank_top_two(
            numeric.get(col, {}), lower_is_better=col in cost_fields_set
        )
        current_leaders[col] = first
    prior_leaders = _read_prior_leaders(
        vault, path, fields=fields, git_runner=git_runner
    )
    if prior_leaders is None:
        return None
    bullets: list[str] = []
    for col in fields:
        was = prior_leaders.get(col)
        now = current_leaders.get(col)
        if was != now and now is not None:
            if was is None:
                bullets.append(
                    f"- **`{col}`**: first leader recorded — [[{now}]]."
                )
            else:
                bullets.append(
                    f"- **`{col}`**: [[{now}]] took #1 from [[{was}]]."
                )
    if not bullets:
        return None
    return "\n".join(bullets)


_PRIOR_LEADER_PATTERN = re.compile(r"\*\*([^*|]+)\*\*")


def _read_prior_leaders(
    vault: Vault,
    path: Path,
    *,
    fields: list[str] | tuple[str, ...],
    git_runner: GitRunner | None,
) -> dict[str, str | None] | None:
    """Reconstruct prior #1 per column from the previous git revision.

    Returns ``None`` when git can't reach the prior revision (untracked
    file, no parent commit, runner failure). When present, the returned
    mapping has one entry per column in ``fields`` — value is the slug
    that was bolded in that column, or ``None`` if no cell was bolded.
    """
    runner = git_runner or _default_git_runner
    repo_root = _find_repo_root(vault.root)
    if repo_root is None:
        return None
    try:
        rel = path.resolve().relative_to(repo_root)
    except ValueError:
        return None
    result = runner(
        ["git", "-C", str(repo_root), "show", f"HEAD:{rel.as_posix()}"]
    )
    if result.returncode != 0:
        return None
    return _parse_leaders_from_markdown(result.stdout, fields=fields)


def _parse_leaders_from_markdown(
    text: str, *, fields: list[str] | tuple[str, ...]
) -> dict[str, str | None]:
    """Pick the slug in the ``**bold**`` cell per column from a rendered table."""
    lines = text.splitlines()
    header_idx = next(
        (
            i
            for i, line in enumerate(lines)
            if line.startswith("| Entity ") and all(f in line for f in fields)
        ),
        None,
    )
    out: dict[str, str | None] = dict.fromkeys(fields, None)
    if header_idx is None:
        return out
    header_cells = [c.strip() for c in lines[header_idx].strip("|").split("|")]
    # Build column-index lookup so we don't depend on field order in the body.
    col_idx_by_field: dict[str, int] = {}
    for i, cell in enumerate(header_cells):
        if cell in fields:
            col_idx_by_field[cell] = i
    for line in lines[header_idx + 2 :]:
        if not line.startswith("|"):
            break
        row_cells = [c.strip() for c in line.strip("|").split("|")]
        if not row_cells:
            continue
        entity_cell = row_cells[0]
        match = re.match(r"\[\[([^\]]+)\]\]", entity_cell)
        if not match:
            continue
        slug = match.group(1)
        for fname, idx in col_idx_by_field.items():
            if idx >= len(row_cells):
                continue
            cell = row_cells[idx]
            if _PRIOR_LEADER_PATTERN.search(cell):
                out[fname] = slug
    return out


def _find_repo_root(start: Path) -> Path | None:
    cur = start.resolve()
    for candidate in (cur, *cur.parents):
        if (candidate / ".git").exists():
            return candidate
    return None


def _default_git_runner(args: list[str]) -> "subprocess.CompletedProcess[str]":
    return subprocess.run(args, capture_output=True, text=True, check=False)


def _read_inputs(page: Page) -> ComparisonInputs:
    title = page.metadata.get("title")
    if not isinstance(title, str) or not title:
        raise WikiError(f"{page.path}: comparison page has no title")
    entity_slugs = page.metadata.get("comparison_of")
    if not isinstance(entity_slugs, list) or len(entity_slugs) < 2:
        raise WikiError(
            f"{page.path}: comparison page has invalid 'comparison_of' "
            "(must be a list of at least 2 entity slugs)"
        )
    fields = page.metadata.get("compare_fields")
    if not isinstance(fields, list) or len(fields) < 1:
        raise WikiError(
            f"{page.path}: comparison page has invalid 'compare_fields' "
            "(must be a list of at least 1 field name)"
        )
    highlight_leaders = bool(page.metadata.get("highlight_leaders", False))
    show_glosses = bool(page.metadata.get("show_glosses", False))
    return ComparisonInputs(
        title=title,
        entity_slugs=tuple(str(s) for s in entity_slugs),
        fields=tuple(str(f) for f in fields),
        highlight_leaders=highlight_leaders,
        show_glosses=show_glosses,
    )


def _render_cell(value: Any) -> str:
    if value is None:
        return UNKNOWN_VALUE
    if isinstance(value, (list, tuple)):
        if not value:
            return UNKNOWN_VALUE
        return ", ".join(str(item) for item in value)
    if isinstance(value, bool):
        return "yes" if value else "no"
    return str(value)


def _slug_from_title(title: str) -> str:
    from wikipilot.wiki import slugify

    return slugify(title)
