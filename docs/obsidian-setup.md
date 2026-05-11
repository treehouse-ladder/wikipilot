# Obsidian setup

Wikipilot's `wiki/` directory is a plain markdown vault — Obsidian opens it as-is. The setup below makes the experience feel native: graph view shows backlinks correctly, image references resolve to local assets, and Dataview queries surface the wiki's structure.

## Open the vault

1. File → Open vault → Open folder as vault → select `wiki/`.
2. Obsidian creates `.obsidian/` inside the vault. The `.gitignore` already excludes the noisy parts (`.obsidian/workspace*`, `.obsidian/cache`).

## Vault settings

Settings → Files & Links:

| Setting | Value | Why |
|---|---|---|
| Default location for new attachments | `In subfolder under current folder` → `assets/` | Obsidian's "paste image" places under `wiki/assets/<page>/`, matching the `download-source-images` skill's layout. |
| Default location for new notes | `Same folder as current note` | Concept pages stay under `concepts/`, etc. |
| New link format | `Shortest path when possible` | Matches what the wiki-merger writes. |
| Use [[Wikilinks]] | On | Required by the citation discipline. |
| Strict line breaks | Off | Standard markdown rendering. |

## Recommended plugins

### Dataview (essential)

Installs from Settings → Community plugins → Browse → "Dataview". Lets you query the wiki's frontmatter as a database. Three example queries to drop into a personal scratch note:

````markdown
```dataview
TABLE last_verified, freshness_window_days
FROM "concepts" OR "entities" OR "topics"
WHERE !contains(file.path, "purpose.md")
SORT last_verified ASC
LIMIT 20
```
````

(Most-stale pages first.)

````markdown
```dataview
LIST
FROM "concepts" OR "entities" OR "topics"
WHERE !contains(file.path, "purpose.md")
WHERE date(today) - date(last_updated) <= dur(7 days)
SORT last_updated DESC
```
````

(Pages touched in the last week — Daily Research output.)

````markdown
```dataview
TASK
FROM ""
WHERE !completed
GROUP BY file.path
```
````

(Every `## Open questions` checkbox across the wiki, grouped by page.)

### Marp (optional, for `wikipilot deck` output)

Installs from Community plugins → "Marp". When you run `uv run wikipilot deck <topic-id>`, the resulting `wiki/decks/<topic-id>.md` opens directly in Marp's preview pane. Useful for sharing a topic's state with stakeholders without copy-pasting markdown.

### Backlink panel (built-in)

Right sidebar → enable Backlinks. The cross-page sweep is the most important quality-of-life feature for an LLM-maintained wiki — the backlink panel makes that visible at a glance.

## Image rendering

Source pages reference local assets under `wiki/assets/<source-slug>/<filename>`. Obsidian auto-resolves these as long as the attachment-folder setting matches (above). If an image doesn't render:

1. Check the source page's frontmatter `image_count` is non-zero.
2. Check `wiki/assets/<source-slug>/` exists and contains the image file.
3. Run `uv run wikipilot lint wiki/` — the broken-local-image-link rule (Phase 5) flags refs that don't resolve.

## Graph view

Settings → Core plugins → Graph view → enable. The graph view is the wiki's most powerful navigation aid:

- Concept clusters appear as densely-connected blobs.
- Disputes between sources become visible as cross-cluster edges.
- Orphan pages float at the periphery — easy to spot.
- Answer pages (filed by `query-answerer`) appear linked from every concept they touch via the back-fill.

Filter the graph to `kind: concept` or `kind: answer` to focus on one layer at a time.
