"""Wikipilot command-line interface.

Phase 1 ships the full subcommand surface called out in the plan:
``lint``, ``init-vault``, ``validate-topics``, ``freshness-report``, ``deck``,
``index-wiki``, ``research``, ``query``. Some subcommands (``research``,
``query``) currently surface a "wired in Phase 6" error from
``api_client.py``; this is intentional so the CLI shape is stable for users
following the docs from day one.
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import click

from wikipilot import __version__
from wikipilot.api_client import (
    ApiClientError,
    fire_query,
    fire_research,
)
from wikipilot.config import (
    ConfigError,
    TopicConfig,
    load_topics,
    load_wikipilot_config,
)
from wikipilot.deck import DeckError, DeckOptions, generate_deck
from wikipilot.dryrun import (
    apply_answer,
    apply_proposal,
    make_fake_answer,
    make_fake_proposal,
)
from wikipilot.lint import (
    SEVERITY_ERROR,
    LintContext,
    Linter,
)
from wikipilot.qmd_index import index_vault, qmd_available
from wikipilot.wiki import WIKI_DIRS, Vault

DEFAULT_WIKI_PATH = Path("wiki")
DEFAULT_TOPICS_PATH = Path("topics.yaml")
DEFAULT_CONFIG_PATH = Path("wikipilot.toml")


@click.group(help="Wikipilot: autonomous-research wiki maintained by Claude Code Cloud Routines.")
@click.version_option(__version__, prog_name="wikipilot")
def main() -> None:
    """Top-level entry point."""


@main.command("lint")
@click.argument(
    "vault_path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    default=DEFAULT_WIKI_PATH,
)
@click.option(
    "--config",
    "config_path",
    type=click.Path(path_type=Path),
    default=DEFAULT_CONFIG_PATH,
    show_default=True,
    help="Path to wikipilot.toml (lint reads thresholds + branch info).",
)
@click.option(
    "--branch",
    "branch_name",
    type=str,
    default=None,
    help="Current git branch (enables ownership-violation rule when prefixed claude/...).",
)
@click.option(
    "--changed-path",
    "changed_paths",
    multiple=True,
    help="Repeatable. File path changed on this branch (relative to repo root).",
)
@click.option(
    "--no-warnings",
    is_flag=True,
    default=False,
    help="Suppress non-error severities in output (errors still cause exit 1).",
)
def lint_cmd(
    vault_path: Path,
    config_path: Path,
    branch_name: str | None,
    changed_paths: tuple[str, ...],
    no_warnings: bool,
) -> None:
    """Lint the wiki vault at VAULT_PATH (default: wiki/)."""
    vault = Vault.at(vault_path)
    config = load_wikipilot_config(config_path) if config_path.exists() else None
    ctx = LintContext.collect(
        vault,
        config=config,
        branch_name=branch_name,
        changed_paths=changed_paths,
    )
    issues = Linter().run(ctx)
    visible = [i for i in issues if not no_warnings or i.severity == SEVERITY_ERROR]
    for issue in visible:
        click.echo(issue.render())
    errors = sum(1 for i in issues if i.severity == SEVERITY_ERROR)
    warnings = sum(1 for i in issues if i.severity == "warning")
    click.echo(f"\n{errors} error(s), {warnings} warning(s).")
    sys.exit(1 if Linter.has_errors(issues) else 0)


@main.command("init-vault")
@click.argument(
    "vault_path",
    type=click.Path(file_okay=False, dir_okay=True, path_type=Path),
    default=DEFAULT_WIKI_PATH,
)
@click.option(
    "--force/--no-force",
    default=False,
    help="Overwrite existing index.md/log.md if present (default: skip).",
)
def init_vault_cmd(vault_path: Path, force: bool) -> None:
    """Create the standard wiki/ skeleton at VAULT_PATH if it doesn't exist."""
    vault_path.mkdir(parents=True, exist_ok=True)
    for sub in WIKI_DIRS:
        sub_dir = vault_path / sub
        sub_dir.mkdir(parents=True, exist_ok=True)
        gitkeep = sub_dir / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.write_text("", encoding="utf-8")
    index_path = vault_path / "index.md"
    if force or not index_path.exists():
        index_path.write_text(_INDEX_SKELETON, encoding="utf-8")
    log_path = vault_path / "log.md"
    if force or not log_path.exists():
        log_path.write_text(_LOG_SKELETON.format(date=date.today().isoformat()), encoding="utf-8")
    click.echo(f"Initialized vault at {vault_path}")


@main.command("validate-topics")
@click.argument(
    "topics_path",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    default=DEFAULT_TOPICS_PATH,
)
def validate_topics_cmd(topics_path: Path) -> None:
    """Validate TOPICS_PATH (default: topics.yaml) against the documented schema."""
    try:
        topics = load_topics(topics_path)
    except ConfigError as exc:
        click.echo(f"ERROR: {exc}", err=True)
        sys.exit(2)
    if not topics:
        click.echo(f"{topics_path}: 0 topics defined (valid; no work to do).")
        return
    for topic in topics:
        click.echo(
            f"  - {topic.id} ({topic.frequency}): "
            f"{topic.display_name} | "
            f"max_sources_per_run={topic.max_sources_per_run} "
            f"freshness_window_days={topic.freshness_window_days}"
        )
    click.echo(f"\n{topics_path}: {len(topics)} topic(s), all valid.")


@main.command("freshness-report")
@click.argument(
    "vault_path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    default=DEFAULT_WIKI_PATH,
)
@click.option(
    "--default-window",
    type=int,
    default=30,
    show_default=True,
    help="Fallback freshness window when a page lacks freshness_window_days.",
)
def freshness_report_cmd(vault_path: Path, default_window: int) -> None:
    """List wiki pages by ascending freshness (most stale first)."""
    vault = Vault.at(vault_path)
    today = date.today()
    rows: list[tuple[int, str, str, int]] = []
    for path in sorted(vault.iter_markdown_files()):
        if path.name in {"index.md", "log.md"}:
            continue
        from wikipilot.wiki import Page  # local import keeps top-level imports tidy

        page = Page.read(path)
        verified = page.last_verified
        if verified is None:
            rows.append((10**6, str(path.relative_to(vault.root)), "never", default_window))
            continue
        age = (today - verified).days
        window = page.freshness_window_days or default_window
        rows.append((age, str(path.relative_to(vault.root)), verified.isoformat(), window))
    rows.sort(reverse=True)
    if not rows:
        click.echo("No wiki pages found.")
        return
    click.echo(f"{'AGE':>5}  {'WINDOW':>6}  {'LAST VERIFIED':<14}  PAGE")
    for age, rel, verified_str, window in rows:
        marker = "!" if age > window else " "
        age_str = "----" if age >= 10**6 else str(age)
        click.echo(f"{age_str:>5}{marker} {window:>6}  {verified_str:<14}  {rel}")


@main.command("deck")
@click.argument("topic_id", type=str)
@click.option(
    "--vault",
    "vault_path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    default=DEFAULT_WIKI_PATH,
    show_default=True,
)
@click.option(
    "--topics",
    "topics_path",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    default=DEFAULT_TOPICS_PATH,
    show_default=True,
)
@click.option(
    "--out",
    "out_path",
    type=click.Path(path_type=Path),
    default=None,
    help="Output path (default: <vault>/decks/<topic-id>.md).",
)
@click.option("--theme", default="default", show_default=True, help="Marp theme name.")
def deck_cmd(
    topic_id: str,
    vault_path: Path,
    topics_path: Path,
    out_path: Path | None,
    theme: str,
) -> None:
    """Generate a Marp deck for TOPIC_ID from the topic's index.md."""
    vault = Vault.at(vault_path)
    try:
        topics = load_topics(topics_path)
    except ConfigError as exc:
        click.echo(f"ERROR: {exc}", err=True)
        sys.exit(2)
    topic = _find_topic(topics, topic_id)
    if topic is None:
        click.echo(f"ERROR: topic {topic_id!r} not found in {topics_path}", err=True)
        sys.exit(2)
    try:
        written = generate_deck(vault, topic, out_path=out_path, options=DeckOptions(theme=theme))
    except DeckError as exc:
        click.echo(f"ERROR: {exc}", err=True)
        sys.exit(1)
    click.echo(f"Wrote deck: {written}")


@main.command("index-wiki")
@click.argument(
    "vault_path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    default=DEFAULT_WIKI_PATH,
)
@click.option(
    "--full/--incremental",
    default=False,
    help="Force full reindex instead of incremental (default).",
)
def index_wiki_cmd(vault_path: Path, full: bool) -> None:
    """Refresh the qmd index over the wiki/ vault."""
    if not qmd_available():
        click.echo("qmd not found on PATH. Install with `pip install qmd` (see docs/qmd-setup.md).")
        sys.exit(0)
    result = index_vault(Path(vault_path), full=full)
    click.echo(result.message)
    sys.exit(0 if result.ok else 1)


@main.command("research")
@click.option(
    "--topic",
    "topic_id",
    type=str,
    default=None,
    help="Research a single topic. Omit to fire the full daily run.",
)
def research_cmd(topic_id: str | None) -> None:
    """Trigger the Daily Research routine via the /fire API (wired in Phase 6)."""
    try:
        fire_research(topic=topic_id)
    except ApiClientError as exc:
        click.echo(f"ERROR: {exc}", err=True)
        sys.exit(2)


@main.command("query")
@click.argument("question", type=str)
def query_cmd(question: str) -> None:
    """Trigger the Wiki Query routine via the /fire API (wired in Phase 6)."""
    try:
        fire_query(question)
    except ApiClientError as exc:
        click.echo(f"ERROR: {exc}", err=True)
        sys.exit(2)


@main.command("dry-run")
@click.option(
    "--topic", "topic_id", type=str, default=None, help="Dry-run a research proposal for TOPIC."
)
@click.option(
    "--query", "question", type=str, default=None, help="Dry-run a query answer for QUESTION."
)
@click.option(
    "--vault",
    "vault_path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    default=DEFAULT_WIKI_PATH,
    show_default=True,
)
@click.option(
    "--topics",
    "topics_path",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    default=DEFAULT_TOPICS_PATH,
    show_default=True,
)
def dry_run_cmd(
    topic_id: str | None,
    question: str | None,
    vault_path: Path,
    topics_path: Path,
) -> None:
    """Synthesize a fake proposal/answer and exercise the apply path locally.

    No Anthropic call is made. CI uses this to verify the cross-page sweep,
    image-ref handling, and back-fill flows end-to-end.
    """
    if (topic_id is None) == (question is None):
        click.echo("ERROR: pass exactly one of --topic or --query", err=True)
        sys.exit(2)
    vault = Vault.at(vault_path)
    if topic_id is not None:
        try:
            topics = load_topics(topics_path)
        except ConfigError as exc:
            click.echo(f"ERROR: {exc}", err=True)
            sys.exit(2)
        topic = _find_topic(topics, topic_id)
        if topic is None:
            click.echo(f"ERROR: topic {topic_id!r} not found in {topics_path}", err=True)
            sys.exit(2)
        proposal = make_fake_proposal(topic)
        result = apply_proposal(vault, proposal)
        click.echo(f"Wrote {len(result.sources_added)} new source(s)")
        click.echo(f"Touched {len(set(result.pages_touched))} page(s)")
        if result.report_path:
            click.echo(f"Run report: {result.report_path.relative_to(vault.root.parent)}")
    else:
        assert question is not None
        answer = make_fake_answer(question)
        result = apply_answer(vault, answer)
        click.echo(f"Wrote answer: {answer.answer_slug}.md")
        click.echo(
            f"Back-filled {len(result.pages_touched) - len(result.sources_added) - 1} related page(s)"
        )


def _find_topic(topics: list[TopicConfig], topic_id: str) -> TopicConfig | None:
    for topic in topics:
        if topic.id == topic_id:
            return topic
    return None


_INDEX_SKELETON = """# Index

The catalog of every page in this wiki.

This file is **LLM-write, human-read**.

## Topics

_(none yet)_

## Concepts

_(none yet)_

## Entities

_(none yet)_

## Sources

_(none yet)_

## Answers

_(none yet)_

## Reports

_(none yet)_
"""

_LOG_SKELETON = """# Log

Chronological, append-only record of every routine run. Parseable with `grep "^## \\[" wiki/log.md`.

This file is **LLM-write, human-read**.

---

## [{date}] manual | bootstrap

Empty wiki initialized.
"""


if __name__ == "__main__":  # pragma: no cover
    main()
