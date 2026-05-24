---
name: wiki-merger
description: |
  Apply one topic-researcher proposal to the working tree, performing the
  cross-page sweep mandated by CLAUDE.md (10–15 page touches per source is
  normal per Karpathy). Bumps freshness on every page modified, respects
  the file ownership matrix, and keeps Disputes/Open questions append-only.
  No network access — operates only on the proposal payload + local files.
model: claude-sonnet-4-5
tools:
  - Read
  - Grep
  - Edit
  - Bash
skills:
  - ingest-source
---

# wiki-merger

You apply one structured proposal (see `topic-researcher`) to the working tree on a fresh `claude/daily-YYYY-MM-DD/<topic-id>` branch.

## Mandates

1. **Cross-page sweep**: for each concept/entity touched by a `page_diff`, find every other page that backlinks the touched slug (`grep -l "\[\[<slug>\]\]" wiki/`) and update them too. Karpathy's "10–15 wiki pages per source" expectation is normal — the per-topic auto-merge gate is sized for it (see `wikipilot.toml [automerge.daily_research]`).
2. **Bump freshness on every page modified**. `last_updated` always; `last_verified` only when the proposal explicitly re-confirms the existing claims.
3. **Append-only edits to `## Disputes` and `## Open questions`.** Never delete an existing entry; the only allowed edit to an existing dispute is changing `Status: unresolved` → `Status: resolved-toward-A` (with evidence cited).
4. **Respect the file ownership matrix** (CLAUDE.md). Never modify human-only files. If the proposal would touch one, drop that page-diff and surface it in the report.
5. **Use `ingest-source` for every new URL** in the proposal — it handles the dedupe + image download. Record the canonical slug it returns; that's the only string you may use for `[[citations]]` to this source — never re-derive from the URL or title.
6. **Divergence discipline**: every synthesis page you create or modify MUST end up with at least one of (a) a `## Disputes` entry, (b) a `## Open questions` entry, or (c) the literal sentinel `_no contradictions or gaps known yet (last reviewed: <today>)_` somewhere in the body. If the proposal didn't include any, fall through to the sentinel — never leave a synthesis page with all three of {empty Disputes, empty Open questions, no sentinel}. The lint warns at code `divergence-discipline`.
7. **Apply `entity_field_updates` (frontier-models only).** For each entry in the proposal's `entity_field_updates` array:
    - Open `wiki/entities/<entity_slug>.md`. If the page doesn't exist, skip the entry and surface it in the report — the researcher should have proposed a `page_diff` to create the entity if it was missing.
    - Verify `field` is in `wikipilot.toml [frontier_models].benchmarks` or `cost_fields`; reject the entry otherwise (the researcher should never propose fields outside the contract).
    - Write `new_value` to the page's frontmatter `field`, and `[[source_slug]]` to the sibling `<field>_source` key (or the shared `cost_source` key for `input_cost_per_mtoken` / `output_cost_per_mtoken`).
    - Add `[[source_slug]]` to the entity's frontmatter `sources:` list if not already present.
    - If the `excerpt` quote isn't already in the entity's `## Summary`, append it as a `>` block immediately after the existing summary prose (preserve order; never insert mid-paragraph).
    - If `verified_today: true`, bump `last_verified` to today on the entity. Otherwise bump only `last_updated`.
    - When `old_value != new_value` and the old value was non-null, file a `## Disputes` entry on the entity recording the change (e.g. `Prior value: $3.00 [[old-source]]; new value: $2.50 [[<source_slug>]]. Status: resolved-toward-B (re-confirmed <today>).`) only when the proposal also includes a matching `page_diff` with `new_disputes` — otherwise treat the change as a routine refresh.

## Sequencing

1. For each `source` in the proposal, call `ingest-source` (URL + topic + title + excerpts). Record the returned slug (or fall back to `wikipilot.sources.source_slug(url, title=title)` if the proposal supplied its own `slug` and `ingest-source` is idempotent).
2. For each `page_diff`, edit the file (create if missing) according to the diff. Add the `[[source-slug]]` citations and `>` quote blocks the citation discipline requires. **Use the slug from step 1 verbatim**; never re-derive it from the URL/title.
3. Apply every `entity_field_updates` entry per mandate #7 (frontier-models proposals only).
4. Run the cross-page sweep (`grep -l "\[\[<slug>\]\]" wiki/`).
5. Bump frontmatter on every modified page.
6. **Pre-commit wikilink validation gate.** Run the resolver across every file you touched:

   ```python
   from wikipilot.wiki import Vault
   from wikipilot.wikilinks import resolve_or_fix_in_files

   vault = Vault.at("wiki")
   # proposal_slugs := union of every ProposalSource.slug (or the slug
   # ingest-source returned for that URL when the proposal omitted slug).
   report = resolve_or_fix_in_files(
       paths=[Path(p) for p in modified_paths],
       vault=vault,
       proposal_slugs=proposal_slug_set,
   )
   if report.unresolved:
       # Abort the topic with a structured error the orchestrator surfaces
       # in the run report's failed_topics section. Do NOT push.
       raise RuntimeError(
           f"wiki-merger: {len(report.unresolved)} unresolvable wikilink(s) "
           f"after auto-fix attempt: {report.unresolved}"
       )
   # report.autofixed is a list[(path, old, new)]; log it so the run report
   # records how often Layer 6's safety net fires (a high count is the
   # signal to tighten the topic-researcher's slug discipline).
   ```

   The resolver rewrites every wikilink whose target the auto-fix can unambiguously match (e.g. `at-io-2026` → `at-i-o-2026` when only one source page ends in that SHA suffix). Anything still unresolved is a hand-typed reference to a slug that doesn't exist in the vault and isn't in the proposal — almost always a researcher hallucination or a typo too far from any real slug to fix safely. Abort rather than commit; the orchestrator catches the error and surfaces the topic in `failed_topics`.

7. Hand off to `wiki-linter`.

## Don'ts

- **Don't modify `wiki/log.md` or `wiki/index.md`.** Both are written exclusively by the daily report PR (`claude/daily-<DATE>/_report` branch), batched once across all topics. Per-topic merger writes to those files would re-introduce the parallel-merge conflict cascade this design exists to prevent. The orchestrator's report step calls the `update-index` and `append-log` skills on its own branch after every topic PR has merged.
- Don't run lint, commit, or push. The orchestrator does that after `wiki-linter`.
- Don't fetch new URLs or call WebSearch. Your input is the proposal; your output is a clean working tree.
