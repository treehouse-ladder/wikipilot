"""Marp deck generator from a topic page.

Phase 1 ships a working baseline that takes ``wiki/topics/<id>/index.md``
and produces a minimal Marp deck at ``wiki/decks/<id>.md`` (or a custom path)
by splitting the source on ``## ``-level headings. Phase 2 may layer on
title-slide polish, theme selection, and per-source citation footers.

Marp reads YAML frontmatter to switch into deck mode (``marp: true``); each
slide is separated by ``---``. The Obsidian Marp plugin renders these
in-place for live preview.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from wikipilot.config import TopicConfig
from wikipilot.wiki import Page, Vault


class DeckError(RuntimeError):
    """Raised when deck generation cannot proceed (missing topic page, etc.)."""


@dataclass
class DeckOptions:
    theme: str = "default"
    paginate: bool = True
    include_summary_section_only: bool = False


def generate_deck(
    vault: Vault,
    topic: TopicConfig,
    *,
    out_path: Path | None = None,
    options: DeckOptions | None = None,
) -> Path:
    """Render a Marp deck for ``topic`` and return the written file path."""
    options = options or DeckOptions()
    topic_index_path = vault.topic_index(topic.id)
    if not topic_index_path.exists():
        raise DeckError(
            f"topic {topic.id!r} has no index.md at {topic_index_path}; "
            "run a Daily Research routine first or create it manually"
        )
    page = Page.read(topic_index_path)
    deck_text = render_deck(topic, page, options=options)
    out_path = out_path or (vault.dir_for("decks") / f"{topic.id}.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(deck_text, encoding="utf-8")
    return out_path


def render_deck(topic: TopicConfig, page: Page, *, options: DeckOptions) -> str:
    sections = _split_sections(page.content)
    if options.include_summary_section_only:
        sections = [section for section in sections if section.heading.lower() == "summary"]
    title_slide = _title_slide(topic, page)
    body_slides = [_render_slide(section) for section in sections]
    slides = [title_slide] + body_slides
    deck_frontmatter = _deck_frontmatter(theme=options.theme, paginate=options.paginate)
    return deck_frontmatter + "\n\n" + "\n\n---\n\n".join(slides) + "\n"


@dataclass(frozen=True)
class _Section:
    heading: str
    body: str


_HEADING_RE = re.compile(r"^## (.+)$", re.MULTILINE)


def _split_sections(content: str) -> list[_Section]:
    matches = list(_HEADING_RE.finditer(content))
    if not matches:
        return [_Section(heading="Summary", body=content.strip())]
    sections: list[_Section] = []
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        body = content[start:end].strip()
        sections.append(_Section(heading=match.group(1).strip(), body=body))
    return sections


def _title_slide(topic: TopicConfig, page: Page) -> str:
    title = page.title or topic.display_name
    sub = topic.purpose.splitlines()[0].strip() if topic.purpose else ""
    body = f"# {title}"
    if sub:
        body += f"\n\n_{sub}_"
    return body


def _render_slide(section: _Section) -> str:
    return f"## {section.heading}\n\n{section.body}".rstrip()


def _deck_frontmatter(*, theme: str, paginate: bool) -> str:
    return f"---\nmarp: true\ntheme: {theme}\npaginate: {'true' if paginate else 'false'}\n---"
