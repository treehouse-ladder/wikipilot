"""Tool entity profiles: enumerate ``profile: tool`` entity pages.

Generative tools (image / video / 3D / rig / motion / music / SFX / voice /
sprite generators) are ordinary ``kind: entity`` pages that additionally
carry a machine-readable profile block (see CLAUDE.md "Tool entity
profile"). This module is the single enumerator every consumer shares:

- the ``tool-profile`` lint rule (field presence + enum membership),
- ``wikipilot tools`` (the benchmark scout's registry dump),
- ``wikipilot tool-changes`` (the per-period delta, :mod:`wikipilot.tool_changes`),
- the ``topic-researcher`` roster sweep (``tools_for_topic``), which
  derives its roster from ``[tool_profiles.modality_topics]`` instead of a
  static list so a tool proposed via ``page_diffs`` is swept on the next
  run with no edit to the human-owned ``wikipilot.toml``.

Design notes
------------
- The JSON shape emitted by :func:`tool_record` is a versioned contract
  (``SCHEMA_VERSION``). Additive changes only: new keys may appear, existing
  keys never change meaning or disappear within a major version.
- ``*_source`` fields are normalized to bare source slugs (the ``[[...]]``
  wrapper is stripped) and each gets a ``*_source_url`` sibling resolved
  from the source page's ``url`` frontmatter — so the scout never has to
  do a second lookup or parse wikilinks.
- Nothing here guesses. A missing field is reported as missing (the lint
  flags it); a field whose value is the literal ``unknown`` is passed
  through verbatim.
"""

from __future__ import annotations

import re
import subprocess
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

from wikipilot.config import ToolProfilesConfig
from wikipilot.wiki import Page, Vault, parse_wikilinks

SCHEMA_VERSION = 1
"""Version of the JSON records emitted by ``wikipilot tools`` and
``wikipilot tool-changes``. Bump only on a breaking change."""

TOOL_PROFILE_MARKER = "tool"
"""Value of the ``profile`` frontmatter key that marks a tool entity."""

UNKNOWN = "unknown"
"""Literal string used for any profile field no source substantiates."""

PROFILE_SCALAR_FIELDS: tuple[str, ...] = (
    "modality",
    "vendor",
    "open_weights_license",
    "hardware_floor",
    "pricing",
    "commercial_use",
    "status",
    "last_release",
)
PROFILE_LIST_FIELDS: tuple[str, ...] = ("tasks", "model_ids", "access", "arena_rank")
PROFILE_SCALAR_SOURCE_FIELDS: tuple[str, ...] = (
    "pricing_source",
    "commercial_use_source",
    "status_source",
)
PROFILE_LIST_SOURCE_FIELDS: tuple[str, ...] = ("arena_rank_source",)

PROFILE_FIELDS: tuple[str, ...] = (
    "modality",
    "tasks",
    "vendor",
    "model_ids",
    "access",
    "open_weights_license",
    "hardware_floor",
    "pricing",
    "pricing_source",
    "commercial_use",
    "commercial_use_source",
    "status",
    "status_source",
    "last_release",
    "arena_rank",
    "arena_rank_source",
)
"""Every key a ``profile: tool`` page must carry, in canonical order."""

_WIKILINK_WRAP_RE = re.compile(r"^\[\[([^\[\]|#\n]+?)(?:#[^\]]*)?(?:\|[^\]]*)?\]\]$")


def is_tool_page(page: Page) -> bool:
    """True when ``page`` is an entity carrying ``profile: tool``."""
    return page.kind == "entity" and str(page.metadata.get("profile", "")) == TOOL_PROFILE_MARKER


def strip_wikilink(value: Any) -> str | None:
    """Return the bare slug of a ``[[slug]]`` string (or the string itself).

    ``None`` stays ``None`` so callers can tell "no source" from a slug.
    """
    if value is None:
        return None
    text = str(value).strip()
    match = _WIKILINK_WRAP_RE.match(text)
    if match:
        return match.group(1).strip()
    links = parse_wikilinks(text)
    if len(links) == 1 and text.startswith("[["):
        return links[0]
    return text or None


def resolve_source_url(vault: Vault, source_slug: str | None) -> str | None:
    """Return the ``url`` frontmatter of ``wiki/sources/<slug>.md`` or ``None``."""
    if not source_slug:
        return None
    path = vault.dir_for("sources") / f"{source_slug}.md"
    if not path.exists():
        return None
    try:
        page = Page.read(path)
    except Exception:  # noqa: BLE001 — a corrupt source page must not kill the dump
        return None
    url = page.metadata.get("url")
    return str(url) if url else None


@dataclass(frozen=True)
class ToolEntity:
    """One ``profile: tool`` entity page, parsed."""

    slug: str
    path: Path
    page: Page

    @property
    def modality(self) -> str | None:
        value = self.page.metadata.get("modality")
        return str(value) if value is not None else None

    @property
    def tracked_values(self) -> dict[str, Any]:
        """Convenience accessor used by the delta diff."""
        return {k: self.page.metadata.get(k) for k in PROFILE_FIELDS}


def iter_tool_entities(vault: Vault) -> Iterable[ToolEntity]:
    """Yield every ``profile: tool`` entity under ``wiki/entities/`` (sorted by slug)."""
    entities_dir = vault.dir_for("entities")
    if not entities_dir.is_dir():
        return
    for path in sorted(entities_dir.glob("*.md")):
        if path.name.startswith("_"):
            continue  # personal scratch convention
        try:
            page = Page.read(path)
        except Exception:  # noqa: BLE001 — unparseable page is the lint's problem, not ours
            continue
        if not is_tool_page(page):
            continue
        yield ToolEntity(slug=path.stem, path=path, page=page)


def tools_for_topic(
    vault: Vault,
    config: ToolProfilesConfig,
    topic_id: str,
) -> list[ToolEntity]:
    """Return the derived roster for ``topic_id``.

    A tool belongs to the topic that owns its ``modality`` per
    ``[tool_profiles.modality_topics]``. Tools with an unknown or unmapped
    modality belong to no topic (the lint flags them).
    """
    owned = set(config.modalities_for_topic(topic_id))
    if not owned:
        return []
    return [t for t in iter_tool_entities(vault) if t.modality in owned]


def tools_for_modality(vault: Vault, modality: str) -> list[ToolEntity]:
    return [t for t in iter_tool_entities(vault) if t.modality == modality]


def _normalize_date(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, date):
        return value.isoformat()
    return str(value)


def _normalize_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return list(value)
    return [value]


def tool_record(vault: Vault, tool: ToolEntity) -> dict[str, Any]:
    """Render one tool entity as the versioned JSON record.

    Keys are stable (see module docstring). ``*_source`` values are bare
    slugs; ``*_source_url`` is resolved from the source page. ``sources``
    is the entity's full citation list, also as bare slugs.
    """
    md = tool.page.metadata
    rel_path = _vault_relative(vault, tool.path)
    record: dict[str, Any] = {
        "slug": tool.slug,
        "path": rel_path,
        "title": tool.page.title,
        "modality": md.get("modality"),
        "tasks": _normalize_list(md.get("tasks")),
        "vendor": md.get("vendor"),
        "model_ids": _normalize_list(md.get("model_ids")),
        "access": _normalize_list(md.get("access")),
        "open_weights_license": md.get("open_weights_license"),
        "hardware_floor": md.get("hardware_floor"),
    }
    for field_name in ("pricing", "commercial_use", "status"):
        record[field_name] = md.get(field_name)
        slug = strip_wikilink(md.get(f"{field_name}_source"))
        record[f"{field_name}_source"] = slug
        record[f"{field_name}_source_url"] = resolve_source_url(vault, slug)
    record["last_release"] = _normalize_date(md.get("last_release"))
    record["arena_rank"] = [str(x) for x in _normalize_list(md.get("arena_rank"))]
    rank_sources = [strip_wikilink(x) for x in _normalize_list(md.get("arena_rank_source"))]
    record["arena_rank_source"] = rank_sources
    record["arena_rank_source_url"] = [resolve_source_url(vault, s) for s in rank_sources]
    record["last_verified"] = _normalize_date(md.get("last_verified"))
    record["last_updated"] = _normalize_date(md.get("last_updated"))
    record["aliases"] = [str(a) for a in _normalize_list(md.get("aliases"))]
    record["sources"] = [strip_wikilink(s) for s in _normalize_list(md.get("sources"))]
    return record


def _vault_relative(vault: Vault, path: Path) -> str:
    """``wiki/entities/<slug>.md`` style path (vault dir name + relative)."""
    try:
        rel = path.resolve().relative_to(vault.root)
    except ValueError:
        return path.as_posix()
    return (Path(vault.root.name) / rel).as_posix()


def build_registry(
    vault: Vault,
    *,
    tools: Iterable[ToolEntity] | None = None,
    head_rev: str | None = None,
) -> dict[str, Any]:
    """Assemble the ``wikipilot tools --format json`` payload."""
    selected = list(tools) if tools is not None else list(iter_tool_entities(vault))
    return {
        "schema_version": SCHEMA_VERSION,
        "head_rev": head_rev,
        "tools": [tool_record(vault, t) for t in selected],
    }


def render_registry_markdown(registry: dict[str, Any]) -> str:
    """Compact markdown table of the registry (one row per tool)."""
    tools = registry.get("tools", [])
    if not tools:
        return "_No tool entities (profile: tool) found._\n"
    header = [
        "slug",
        "modality",
        "vendor",
        "access",
        "status",
        "pricing",
        "commercial_use",
        "arena_rank",
        "last_verified",
    ]
    lines = [
        f"| {' | '.join(header)} |",
        f"| {' | '.join(['---'] * len(header))} |",
    ]
    for t in tools:
        row = [
            f"[[{t['slug']}]]",
            _cell(t.get("modality")),
            _cell(t.get("vendor")),
            _cell(t.get("access")),
            _cell(t.get("status")),
            _cell(t.get("pricing")),
            _cell(t.get("commercial_use")),
            _cell(t.get("arena_rank")),
            _cell(t.get("last_verified")),
        ]
        lines.append(f"| {' | '.join(row)} |")
    return "\n".join(lines) + "\n"


def _cell(value: Any) -> str:
    if value is None:
        return "_missing_"
    if isinstance(value, list):
        return ", ".join(str(v) for v in value) if value else "_none_"
    return str(value).replace("|", "\\|")


GitRunner = Any
"""``Callable[[list[str]], subprocess.CompletedProcess[str]]`` — injectable for tests."""


def default_git_runner(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, capture_output=True, text=True, check=False)


def find_repo_root(start: Path) -> Path | None:
    cur = start.resolve()
    for candidate in (cur, *cur.parents):
        if (candidate / ".git").exists():
            return candidate
    return None


def current_head_rev(vault: Vault, git_runner: GitRunner | None = None) -> str | None:
    """Return ``HEAD``'s SHA for the repo containing ``vault``, or ``None``."""
    runner = git_runner or default_git_runner
    root = find_repo_root(vault.root)
    if root is None:
        return None
    result = runner(["git", "-C", str(root), "rev-parse", "HEAD"])
    if result.returncode != 0:
        return None
    sha = (result.stdout or "").strip()
    return sha or None
