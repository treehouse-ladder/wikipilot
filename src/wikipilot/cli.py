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
from wikipilot.compare import regenerate_comparison, write_comparison_page
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
    apply_weekly_health,
    make_fake_answer,
    make_fake_proposal,
    make_fake_weekly_health,
)
from wikipilot.git_ops import (
    apply_gate,
    evaluate_gate,
    infer_route_from_branch,
    view_pr,
)
from wikipilot.lint import (
    SEVERITY_ERROR,
    LintContext,
    Linter,
)
from wikipilot.qmd_index import index_vault, qmd_available
from wikipilot.sources import ingest_source_with_images
from wikipilot.wiki import (
    INDEX_SKELETON,
    WIKI_DIRS,
    ResetSummary,
    Vault,
    WikiError,
    render_log_skeleton,
    reset_vault,
)

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
        index_path.write_text(INDEX_SKELETON, encoding="utf-8")
    log_path = vault_path / "log.md"
    if force or not log_path.exists():
        log_path.write_text(render_log_skeleton(), encoding="utf-8")
    click.echo(f"Initialized vault at {vault_path}")


@main.command("reset-vault")
@click.argument(
    "vault_path",
    type=click.Path(file_okay=False, dir_okay=True, path_type=Path),
    default=DEFAULT_WIKI_PATH,
)
@click.option(
    "--yes",
    "skip_confirm",
    is_flag=True,
    default=False,
    help="Skip the typed-basename confirmation prompt (for scripted/CI use).",
)
@click.option(
    "--keep-topics",
    is_flag=True,
    default=False,
    help="Preserve wiki/topics/<id>/ folders and topics.yaml entries.",
)
@click.option(
    "--topics-file",
    "topics_path",
    type=click.Path(path_type=Path),
    default=None,
    help=(
        "Path to topics.yaml (reset to an empty stub unless --keep-topics). "
        "Defaults to the topics.yaml beside VAULT_PATH (so a tmp-vault smoke "
        "test never reaches across to the workspace topics.yaml)."
    ),
)
def reset_vault_cmd(
    vault_path: Path,
    skip_confirm: bool,
    keep_topics: bool,
    topics_path: Path | None,
) -> None:
    """Reset a forked vault back to the empty skeleton.

    Wipes the maintainer's seeded sources, concepts, entities, comparisons,
    answers, reports, decks, asset folders, topic folders, and resets
    index.md, log.md, and topics.yaml. Preserves .obsidian/ config,
    every _*.md personal scratch file, and every .gitkeep.

    Always runs a dry-run first and asks the user to confirm by typing the
    vault directory's basename (e.g. "wiki"). Pass --yes to skip the
    confirmation for scripted use.
    """
    try:
        plan = reset_vault(vault_path, keep_topics=keep_topics, dry_run=True)
    except WikiError as exc:
        click.echo(f"ERROR: {exc}", err=True)
        sys.exit(2)

    # Derive topics.yaml from the resolved vault's parent unless the user
    # passed an explicit path. This prevents `wikipilot reset-vault /tmp/foo`
    # from accidentally rewriting the workspace's topics.yaml when run from
    # a checkout root (the bug the smoke-test guard caught).
    if topics_path is None:
        topics_path = plan.root.parent / "topics.yaml"
    _print_topics_target(topics_path)
    topics_action = _plan_topics_yaml_reset(topics_path, keep_topics=keep_topics)
    _print_reset_summary(plan, topics_action=topics_action)

    if plan.is_empty() and topics_action == "skip":
        click.echo("Vault is already at the empty-skeleton state. Nothing to do.")
        return

    if not skip_confirm:
        expected = plan.root.name
        click.echo(
            f"\nType the vault directory NAME ({expected!r}) to confirm (anything else aborts): ",
            nl=False,
        )
        try:
            answer = input().strip()
        except EOFError:
            click.echo("\nNo TTY and --yes not passed. Aborting.", err=True)
            sys.exit(1)
        if answer != expected:
            click.echo("Aborted; nothing was deleted.", err=True)
            sys.exit(1)

    try:
        result = reset_vault(vault_path, keep_topics=keep_topics, dry_run=False)
    except WikiError as exc:
        click.echo(f"ERROR: {exc}", err=True)
        sys.exit(2)

    # Rewrite index.md and log.md to canonical skeletons only when the
    # helper signaled they differ from skeleton (idempotent: a second
    # reset on an already-clean vault writes nothing).
    files_to_reset_names = {p.name for p in result.files_to_reset}
    if "index.md" in files_to_reset_names:
        (result.root / "index.md").write_text(INDEX_SKELETON, encoding="utf-8")
    if "log.md" in files_to_reset_names:
        (result.root / "log.md").write_text(render_log_skeleton(), encoding="utf-8")

    # Apply the topics.yaml reset.
    if topics_action == "reset":
        try:
            _apply_topics_yaml_reset(topics_path)
            click.echo(f"Reset {topics_path} to an empty stub.")
        except OSError as exc:  # pragma: no cover - defensive
            click.echo(f"WARNING: could not rewrite {topics_path}: {exc}", err=True)

    click.echo(
        f"\nReset complete. Deleted {len(result.files_to_delete)} file(s) "
        f"and {len(result.dirs_to_delete)} director(ies). "
        f"Preserved {len(result.files_preserved)} file(s) "
        f"and {len(result.dirs_preserved)} director(ies)."
    )
    click.echo(
        "\nNext steps:\n"
        "  1. Edit topics.yaml to add your first topic.\n"
        "  2. Create wiki/topics/<id>/purpose.md and wiki/topics/<id>/index.md.\n"
        "  3. Run 'wikipilot validate-topics' and 'wikipilot lint wiki/' to confirm.\n"
    )


def _plan_topics_yaml_reset(topics_path: Path, *, keep_topics: bool) -> str:
    """Decide whether topics.yaml needs a reset.

    Returns one of: ``"reset"`` (rewrite to empty stub), ``"skip"``
    (already empty or --keep-topics), ``"missing"`` (file does not exist).
    """
    if keep_topics:
        return "skip"
    if not topics_path.exists():
        return "missing"
    text = topics_path.read_text(encoding="utf-8")
    # Already empty?
    if "topics: []" in text and "- id:" not in text:
        return "skip"
    return "reset"


def _apply_topics_yaml_reset(topics_path: Path) -> None:
    """Rewrite topics.yaml to ``topics: []``, preserving leading comments.

    Every line up to (but not including) the first non-comment, non-blank
    line is preserved verbatim. The body becomes ``topics: []`` followed
    by a single trailing newline.
    """
    text = topics_path.read_text(encoding="utf-8")
    preserved: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#") or stripped == "":
            preserved.append(line)
            continue
        break
    new_text = "\n".join(preserved).rstrip() + "\n\ntopics: []\n"
    topics_path.write_text(new_text, encoding="utf-8")


def _print_topics_target(topics_path: Path) -> None:
    """Print the resolved absolute path of the topics.yaml that will be touched.

    This is part of the safety scaffolding: every run echoes the absolute
    path so the user (and any future maintainer reading test output) can
    verify the right topics.yaml is in the blast radius.
    """
    click.echo(f"Topics file target: {topics_path.resolve()}")


def _print_reset_summary(plan: ResetSummary, *, topics_action: str) -> None:
    """Print the dry-run summary block ahead of the confirmation prompt."""
    click.echo(f"About to reset vault at: {plan.root}")
    counts: dict[str, int] = {}
    for path in plan.files_to_delete:
        try:
            rel = path.relative_to(plan.root)
            top = rel.parts[0] if rel.parts else "(root)"
        except ValueError:
            top = "(root)"
        counts[top] = counts.get(top, 0) + 1
    for top in sorted(counts):
        click.echo(f"  - delete {counts[top]:4d} file(s) in {top}/")
    if plan.dirs_to_delete:
        click.echo(f"  - delete {len(plan.dirs_to_delete)} directory(ies):")
        for d in plan.dirs_to_delete:
            try:
                click.echo(f"      {d.relative_to(plan.root)}")
            except ValueError:
                click.echo(f"      {d}")
    reset_names = sorted({p.name for p in plan.files_to_reset})
    if reset_names:
        click.echo(f"  - reset  {', '.join(reset_names)} to skeleton")
    if topics_action == "reset":
        click.echo("  - reset  topics.yaml to empty stub")
    elif topics_action == "missing":
        click.echo("  - skip   topics.yaml (not found)")
    elif topics_action == "skip":
        click.echo("  - skip   topics.yaml (--keep-topics or already empty)")
    if plan.files_preserved or plan.dirs_preserved:
        click.echo(
            f"  - preserve .obsidian/, _*.md scratch files, .gitkeep "
            f"({len(plan.files_preserved)} file(s), "
            f"{len(plan.dirs_preserved)} director(ies))"
        )


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
        click.echo(
            "qmd not importable. Install with `pip install qmd` (see docs/qmd-setup.md).",
            err=True,
        )
        sys.exit(1)
    result = index_vault(Path(vault_path), full=full)
    click.echo(result.message)
    sys.exit(0 if result.ok else 1)


@main.group("compare")
def compare_cmd() -> None:
    """Manage comparison pages (Phase 9 Pattern A).

    A comparison page aggregates frontmatter fields across N entity pages
    into one markdown table — e.g. cost-comparison reads `cost_per_mtoken`
    from each frontier-model entity. The page is regenerable from its own
    frontmatter (`comparison_of`, `compare_fields`).
    """


@compare_cmd.command("new")
@click.argument("comparison_slug", type=str)
@click.option(
    "--of",
    "entity_csv",
    required=True,
    help="Comma-separated entity slugs to include (>= 2).",
)
@click.option(
    "--fields",
    "fields_csv",
    required=True,
    help="Comma-separated frontmatter field names to aggregate (>= 1).",
)
@click.option("--title", required=True, help="Human-readable title for the comparison page.")
@click.option(
    "--vault",
    "vault_path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    default=DEFAULT_WIKI_PATH,
    show_default=True,
)
def compare_new_cmd(
    comparison_slug: str,
    entity_csv: str,
    fields_csv: str,
    title: str,
    vault_path: Path,
) -> None:
    """Create a new comparison page at wiki/comparisons/COMPARISON_SLUG.md."""
    vault = Vault.at(vault_path)
    entities = [s.strip() for s in entity_csv.split(",") if s.strip()]
    fields = [f.strip() for f in fields_csv.split(",") if f.strip()]
    try:
        path = write_comparison_page(
            vault,
            comparison_slug,
            title=title,
            entity_slugs=entities,
            fields=fields,
        )
    except WikiError as exc:
        click.echo(f"ERROR: {exc}", err=True)
        sys.exit(2)
    click.echo(f"Created comparison: {path.relative_to(vault.root.parent)}")


@compare_cmd.command("regen")
@click.argument("comparison_slug", type=str)
@click.option(
    "--vault",
    "vault_path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    default=DEFAULT_WIKI_PATH,
    show_default=True,
)
def compare_regen_cmd(comparison_slug: str, vault_path: Path) -> None:
    """Regenerate the body of an existing comparison from its frontmatter.

    Idempotent: bumps ``last_updated`` to today, leaves ``last_verified``
    untouched (the underlying entity pages may not have been re-checked).
    """
    vault = Vault.at(vault_path)
    try:
        path = regenerate_comparison(vault, comparison_slug)
    except WikiError as exc:
        click.echo(f"ERROR: {exc}", err=True)
        sys.exit(2)
    click.echo(f"Regenerated comparison: {path.relative_to(vault.root.parent)}")


@main.command("research")
@click.option(
    "--topic",
    "topic_id",
    type=str,
    default=None,
    help="Research a single topic. Omit to fire the full daily run.",
)
def research_cmd(topic_id: str | None) -> None:
    """Trigger the Daily Research routine via the /fire API."""
    try:
        response = fire_research(topic=topic_id)
    except ApiClientError as exc:
        click.echo(f"ERROR: {exc}", err=True)
        sys.exit(2)
    _render_fire_response(response, what=f"research (topic={topic_id or '*all*'})")
    sys.exit(0 if response.ok else 1)


@main.command("query")
@click.argument("question", type=str)
def query_cmd(question: str) -> None:
    """Trigger the Wiki Query routine via the /fire API."""
    try:
        response = fire_query(question)
    except ApiClientError as exc:
        click.echo(f"ERROR: {exc}", err=True)
        sys.exit(2)
    _render_fire_response(response, what=f"query: {question!r}")
    sys.exit(0 if response.ok else 1)


def _render_fire_response(response: object, *, what: str) -> None:
    click.echo(f"Fired {what} (route: {getattr(response, 'routine', '?')})")
    status = getattr(response, "status_code", 0)
    retries = getattr(response, "retries", 0)
    if getattr(response, "ok", False):
        run_id = ""
        body = getattr(response, "body", {}) or {}
        if isinstance(body, dict):
            run_id = body.get("run_id") or body.get("id") or ""
        click.echo(f"  status={status} retries={retries} run_id={run_id or '<unknown>'}")
    else:
        msg = getattr(response, "error_message", None) or "(no error message)"
        click.echo(f"  status={status} retries={retries} error={msg}", err=True)


@main.command("ingest")
@click.option("--url", required=True, help="URL of the source to ingest.")
@click.option("--topic", "topic_id", required=True, help="Topic id this source belongs to.")
@click.option("--title", required=True, help="Human-readable title for the source page.")
@click.option(
    "--body",
    default="",
    help="Optional human-readable summary for the source page body.",
)
@click.option(
    "--excerpt",
    "excerpts",
    multiple=True,
    help="Repeatable. Verbatim quote excerpt to include under '## Excerpts'.",
)
@click.option(
    "--vault",
    "vault_path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    default=DEFAULT_WIKI_PATH,
    show_default=True,
)
@click.option(
    "--config",
    "config_path",
    type=click.Path(path_type=Path),
    default=DEFAULT_CONFIG_PATH,
    show_default=True,
    help="Path to wikipilot.toml (image pipeline reads [images] from here).",
)
def ingest_cmd(
    url: str,
    topic_id: str,
    title: str,
    body: str,
    excerpts: tuple[str, ...],
    vault_path: Path,
    config_path: Path,
) -> None:
    """Write a source page for URL and localize its images.

    Idempotent: re-ingesting a known URL prints the existing slug and skips
    image work. Driven by the ``ingest-source`` skill at runtime.
    """
    vault = Vault.at(vault_path)
    config = load_wikipilot_config(config_path) if config_path.exists() else None
    images_cfg = config.images if config is not None else None
    result = ingest_source_with_images(
        vault,
        url=url,
        title=title,
        topic=topic_id,
        body=body,
        excerpts=list(excerpts) if excerpts else None,
        images=images_cfg,
    )
    rec = result.record
    if rec.created:
        click.echo(f"Created source: {rec.slug}")
        if result.download is not None:
            click.echo(
                f"Images: downloaded={result.download.downloaded} "
                f"skipped={result.download.skipped} "
                f"orphans_removed={result.download.orphans_removed}"
            )
    else:
        click.echo(f"Existing source returned: {rec.slug} (no work done)")


@main.command("dry-run")
@click.option(
    "--topic", "topic_id", type=str, default=None, help="Dry-run a research proposal for TOPIC."
)
@click.option(
    "--query", "question", type=str, default=None, help="Dry-run a query answer for QUESTION."
)
@click.option(
    "--weekly-health",
    "weekly_health",
    is_flag=True,
    default=False,
    help="Dry-run the weekly health sweep (seeds candidates, files dummy disputes).",
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
    weekly_health: bool,
    vault_path: Path,
    topics_path: Path,
) -> None:
    """Synthesize a fake proposal/answer/sweep and exercise the apply path locally.

    No Anthropic call is made. CI uses this to verify the cross-page sweep,
    image-ref handling, back-fill, and weekly-health flows end-to-end.
    """
    chosen = sum(1 for x in (topic_id, question, weekly_health) if x)
    if chosen != 1:
        click.echo(
            "ERROR: pass exactly one of --topic, --query, or --weekly-health",
            err=True,
        )
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
    elif question is not None:
        answer = make_fake_answer(question)
        result = apply_answer(vault, answer)
        click.echo(f"Wrote answer: {answer.answer_slug}.md")
        click.echo(
            f"Back-filled {len(result.pages_touched) - len(result.sources_added) - 1} related page(s)"
        )
    else:
        # --weekly-health: import the seed lazily so importing wikipilot.cli
        # doesn't drag the scripts/ tree onto sys.path unnecessarily.
        sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
        try:
            from disputes_seed import seed_candidates  # type: ignore[import-not-found]
        except ImportError as exc:
            click.echo(f"ERROR: scripts/disputes_seed.py not importable: {exc}", err=True)
            sys.exit(2)
        seed = seed_candidates(vault)
        candidates = [{"trigger": c.trigger, "pages": list(c.pages)} for c in seed.candidate_sets]
        weekly = make_fake_weekly_health(candidates)
        result = apply_weekly_health(vault, weekly)
        click.echo(
            f"Sweep dispatched over {len(candidates)} candidate set(s); "
            f"filed {len(weekly.disputes_filed)} dispute(s)"
        )
        if result.report_path:
            click.echo(f"Health report: {result.report_path.relative_to(vault.root.parent)}")


def _find_topic(topics: list[TopicConfig], topic_id: str) -> TopicConfig | None:
    for topic in topics:
        if topic.id == topic_id:
            return topic
    return None


@main.command("recover-prs")
@click.option(
    "--config",
    "config_path",
    type=click.Path(path_type=Path),
    default=DEFAULT_CONFIG_PATH,
    show_default=True,
    help="Path to wikipilot.toml (gate thresholds + branch templates).",
)
@click.option(
    "--base",
    "base_branch",
    type=str,
    default="main",
    show_default=True,
    help="Base branch to enumerate open PRs against.",
)
@click.option(
    "--dry-run/--no-dry-run",
    default=False,
    help="Print per-PR gate decisions without invoking gh pr merge/comment.",
)
@click.option(
    "--all/--claude-only",
    "include_all",
    default=False,
    help="Include non-claude/* heads (default: claude/* only). Non-claude heads are listed with route=None and skipped.",
)
def recover_prs_cmd(
    config_path: Path,
    base_branch: str,
    dry_run: bool,
    include_all: bool,
) -> None:
    """Re-run the auto-merge gate on every open ``claude/*`` PR to ``BASE``.

    Escape hatch for two recovery scenarios:

    \b
    1. A content routine crashed mid-loop and left PRs open with green CI but
       no gate decision recorded (no auto-merge queued, no checklist comment).
    2. The PR Watcher routine is itself unhealthy and needs a manual one-shot
       sweep to clear the backlog.

    Per-PR route is inferred from ``[branches]`` templates in wikipilot.toml.
    Heads that match no template are listed with ``route=None`` and skipped.
    ``--dry-run`` evaluates the gate without mutating GitHub (no merge,
    no comment).
    """
    config = load_wikipilot_config(config_path)
    pr_list = _list_recoverable_prs(base_branch=base_branch, include_all=include_all)
    if not pr_list:
        click.echo(f"0 PRs to recover (base={base_branch}).")
        return

    click.echo(f"{'PR':>5}  {'ROUTE':<16}  {'DECISION':<10}  REASONS / HEAD")
    click.echo("-" * 78)
    for entry in pr_list:
        pr_number = entry["number"]
        head_ref = entry["headRefName"]
        route = infer_route_from_branch(head_ref, config)
        if route is None:
            click.echo(f"{pr_number:>5}  {'-':<16}  {'skip':<10}  head={head_ref} (no route)")
            continue
        if dry_run:
            try:
                pr_view = view_pr(pr_number)
            except Exception as exc:  # noqa: BLE001 — surface any gh failure inline
                click.echo(f"{pr_number:>5}  {route:<16}  {'error':<10}  view_pr failed: {exc}")
                continue
            decision = evaluate_gate(pr_view, route=route, config=config)
            label = "automerge" if decision.automerge else "blocked"
            reasons = "; ".join(decision.reasons) or "all gate criteria pass"
            click.echo(f"{pr_number:>5}  {route:<16}  {label:<10}  {reasons}")
        else:
            try:
                decision = apply_gate(pr_number, route=route, config=config)
            except Exception as exc:  # noqa: BLE001
                click.echo(f"{pr_number:>5}  {route:<16}  {'error':<10}  apply_gate failed: {exc}")
                continue
            label = "merged" if decision.automerge else "comment"
            reasons = "; ".join(decision.reasons) or "all gate criteria pass"
            click.echo(f"{pr_number:>5}  {route:<16}  {label:<10}  {reasons}")


def _list_recoverable_prs(*, base_branch: str, include_all: bool) -> list[dict]:
    """Enumerate open PRs via ``gh pr list --json``, filter client-side to ``claude/*``.

    ``gh pr list --head`` doesn't accept globs, so the prefix filter happens
    here in Python after the API call. Limit is 200 PRs — way more than any
    reasonable Wikipilot backlog and below GitHub's max page size.
    """
    import json as _json
    import subprocess as _subprocess

    args = [
        "gh",
        "pr",
        "list",
        "--state",
        "open",
        "--base",
        base_branch,
        "--json",
        "number,headRefName",
        "--limit",
        "200",
    ]
    try:
        result = _subprocess.run(args, capture_output=True, text=True, check=False)
    except (OSError, _subprocess.SubprocessError) as exc:
        click.echo(f"ERROR: gh pr list failed: {exc}", err=True)
        sys.exit(2)
    if result.returncode != 0:
        click.echo(
            f"ERROR: gh pr list returned {result.returncode}: "
            f"{result.stderr.strip() or result.stdout.strip()}",
            err=True,
        )
        sys.exit(2)
    body = result.stdout.strip() or "[]"
    try:
        data = _json.loads(body)
    except (ValueError, TypeError) as exc:
        click.echo(f"ERROR: could not parse gh pr list output: {exc}", err=True)
        sys.exit(2)
    if not isinstance(data, list):
        click.echo("ERROR: gh pr list returned non-list payload", err=True)
        sys.exit(2)
    if not include_all:
        data = [pr for pr in data if str(pr.get("headRefName", "")).startswith("claude/")]
    return data


if __name__ == "__main__":  # pragma: no cover
    main()
