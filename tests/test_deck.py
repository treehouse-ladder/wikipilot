"""Tests for ``wikipilot.deck`` (Marp deck generation)."""

from __future__ import annotations

import pytest

from wikipilot.config import TopicConfig
from wikipilot.deck import DeckError, DeckOptions, generate_deck, render_deck
from wikipilot.wiki import Page, Vault


def _topic() -> TopicConfig:
    return TopicConfig(
        id="ai-agents",
        display_name="AI agents and agentic systems",
        purpose="In-scope: research and engineering on autonomous LLM agents.\nOut-of-scope: general LLM research.",
    )


def test_render_deck_includes_marp_frontmatter(sample_vault: Vault) -> None:
    page = Page.read(sample_vault.topic_index("ai-agents"))
    deck = render_deck(_topic(), page, options=DeckOptions())
    assert deck.startswith("---\nmarp: true")
    assert "theme: default" in deck


def test_render_deck_splits_on_h2(sample_vault: Vault) -> None:
    page = Page.read(sample_vault.topic_index("ai-agents"))
    deck = render_deck(_topic(), page, options=DeckOptions())
    assert deck.count("\n---\n") >= 2
    assert "## Summary" in deck
    assert "## See also" in deck


def test_render_deck_title_slide_first(sample_vault: Vault) -> None:
    page = Page.read(sample_vault.topic_index("ai-agents"))
    deck = render_deck(_topic(), page, options=DeckOptions())
    body = deck.split("---\n", 2)[2] if deck.count("---\n") >= 2 else deck
    assert "# AI agents and agentic systems" in body


def test_generate_deck_writes_to_default_path(sample_vault: Vault) -> None:
    out = generate_deck(sample_vault, _topic())
    assert out == sample_vault.dir_for("decks") / "ai-agents.md"
    assert out.exists()
    text = out.read_text(encoding="utf-8")
    assert "marp: true" in text


def test_generate_deck_missing_topic_raises(sample_vault: Vault) -> None:
    missing_topic = TopicConfig(
        id="does-not-exist",
        display_name="x",
        purpose="x",
    )
    with pytest.raises(DeckError, match="has no index.md"):
        generate_deck(sample_vault, missing_topic)


def test_render_deck_summary_only(sample_vault: Vault) -> None:
    page = Page.read(sample_vault.topic_index("ai-agents"))
    deck = render_deck(_topic(), page, options=DeckOptions(include_summary_section_only=True))
    assert "## Summary" in deck
    assert "## See also" not in deck
