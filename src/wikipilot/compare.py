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

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

from wikipilot.wiki import Page, Vault, WikiError

UNKNOWN_VALUE = "_unknown_"
"""Cell rendered when an entity page omits a requested field. Markdown
italic so it stands out in Obsidian without breaking table layout."""


@dataclass(frozen=True)
class ComparisonInputs:
    """Inputs declared in a comparison page's frontmatter."""

    title: str
    entity_slugs: tuple[str, ...]
    fields: tuple[str, ...]


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
) -> str:
    """Render a deterministic markdown table from ``aggregated`` data.

    Row order follows ``entity_slugs`` (caller controls). Column order
    follows ``fields``. Cells that are missing render as :data:`UNKNOWN_VALUE`.
    The first column is always ``Entity`` (an Obsidian wikilink to the
    entity page) so the table lands as a navigation surface, not just a
    data dump.
    """
    header = ["Entity", *fields]
    sep = ["---"] * len(header)
    rows: list[list[str]] = []
    for slug in entity_slugs:
        row = [f"[[{slug}]]"]
        per_entity = aggregated.get(slug, {})
        for field in fields:
            value = per_entity.get(field)
            row.append(_render_cell(value))
        rows.append(row)
    table_lines = [
        f"| {' | '.join(header)} |",
        f"| {' | '.join(sep)} |",
    ]
    table_lines.extend(f"| {' | '.join(row)} |" for row in rows)
    body = (
        f"# {title}\n\n"
        f"## Summary\n\n"
        f"This comparison aggregates `{', '.join(fields)}` across "
        f"{len(entity_slugs)} entities. Cells marked {UNKNOWN_VALUE} are "
        f"missing on the source entity page; backfill the value there and "
        f"re-run `wikipilot compare {_slug_from_title(title)}` to refresh.\n\n"
        f"{'\n'.join(table_lines)}\n"
    )
    return body


def write_comparison_page(
    vault: Vault,
    slug: str,
    *,
    title: str,
    entity_slugs: list[str] | tuple[str, ...],
    fields: list[str] | tuple[str, ...],
    today: date | None = None,
) -> Path:
    """Create a new comparison page at ``wiki/comparisons/<slug>.md``.

    Frontmatter is fully populated so the page is lint-clean immediately:
    ``comparison_of`` and ``compare_fields`` lists drive future regeneration,
    standard freshness fields land at ``today``.
    """
    if len(entity_slugs) < 2:
        raise WikiError(f"comparison '{slug}' needs at least 2 entities (got {len(entity_slugs)})")
    if len(fields) < 1:
        raise WikiError(f"comparison '{slug}' needs at least 1 field (got 0)")
    today = today or date.today()
    aggregated = aggregate_entity_fields(vault, entity_slugs, fields)
    body = render_comparison_table(
        aggregated, entity_slugs=entity_slugs, fields=fields, title=title
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
    page = Page.from_dict(path, metadata, body)
    page.write()
    return path


def regenerate_comparison(
    vault: Vault,
    comparison_slug: str,
    *,
    today: date | None = None,
) -> Path:
    """Re-read frontmatter for an existing comparison and rewrite its body.

    Idempotent: bumps ``last_updated`` to ``today`` (so freshness reports
    surface "this comparison was regenerated today") but does NOT bump
    ``last_verified`` (the underlying entity pages may not have been
    re-checked; the comparison itself is just a derived view).
    """
    today = today or date.today()
    path = vault.page_path("comparison", comparison_slug)
    if not path.exists():
        raise WikiError(f"no comparison page at {path}")
    page = Page.read(path)
    inputs = _read_inputs(page)
    aggregated = aggregate_entity_fields(vault, inputs.entity_slugs, inputs.fields)
    page.content = render_comparison_table(
        aggregated,
        entity_slugs=inputs.entity_slugs,
        fields=inputs.fields,
        title=inputs.title,
    )
    page.metadata["last_updated"] = today
    page.write()
    return path


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
    return ComparisonInputs(
        title=title,
        entity_slugs=tuple(str(s) for s in entity_slugs),
        fields=tuple(str(f) for f in fields),
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
