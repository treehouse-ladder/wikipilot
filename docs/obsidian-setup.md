# Obsidian setup

Wikipilot's `wiki/` directory is a plain markdown vault — Obsidian opens it as-is. The setup below makes the experience feel native: the graph view colors every node by `kind:`, source pages look distinct from synthesis pages, a single dashboard surfaces everything that needs your attention, and the daily workflow takes one or two keystrokes.

The repo ships with a working Obsidian config under `wiki/.obsidian/` — graph color groups, CSS snippet, attachment folder, and the two essential community plugins (Dataview + Front Matter Title) are already declared. After opening the vault, you'll only need to **install** the community plugins Obsidian asks for; the configuration is already in place.

## 1. Open the vault

1. File → **Open vault** → **Open folder as vault** → select **`wiki/`** (the subfolder, **not** the repo root — opening the repo root pollutes the graph with `src/`, `tests/`, etc.).
2. Obsidian uses the committed `wiki/.obsidian/` config. The `.gitignore` excludes the noisy parts (`workspace*`, `cache`, plugin internal `data.json`).
3. On first open, Obsidian will prompt you to enable community plugins listed in `wiki/.obsidian/community-plugins.json` — click "Trust author and enable plugins". This installs **Dataview** and **Front Matter Title**.

## 2. Vault settings (already pre-configured)

The `wiki/.obsidian/app.json` and the per-plugin configs commit these values; verify in Settings → Files & Links if anything looks off:

| Setting | Value | Why |
|---|---|---|
| Default location for new attachments | `In subfolder under current folder` → `assets/` | Matches the `download-source-images` skill's layout. |
| Default location for new notes | `Same folder as current note` | Concept pages stay under `concepts/`, etc. |
| New link format | `Shortest path when possible` | Matches what `wiki-merger` writes. |
| Use [[Wikilinks]] | **On** | Required by the citation discipline. |
| Strict line breaks | **Off** | Standard markdown rendering. |

## 3. Essential community plugins

### Dataview (essential — drives the dashboard)

Already listed in `community-plugins.json`. Powers the `wiki/_dashboard.md` page and any other frontmatter-based queries you write. Verify Settings → Community plugins → **Dataview** is enabled, and turn on:

- **Enable JavaScript Queries** — the dashboard uses one `dataviewjs` block to count unresolved disputes by page. Without this, the disputes block silently does nothing.
- **Enable inline JavaScript queries** — useful for ad-hoc counts in any note.

Three Dataview query patterns you'll re-use:

````markdown
```dataview
TABLE last_verified, freshness_window_days
FROM "concepts" OR "entities" OR "topics"
SORT last_verified ASC
LIMIT 20
```
````

(Most-stale pages first.)

````markdown
```dataview
LIST FROM "sources"
WHERE topic = "agentic-coding"
SORT fetched_at DESC
```
````

(All sources tagged with a given topic.)

````markdown
```dataview
TASK FROM ""
WHERE !completed
GROUP BY file.path
```
````

(Every open `## Open questions` checkbox across the wiki, grouped by host page.)

### Front Matter Title (essential — fixes the "six index files" problem)

Already listed in `community-plugins.json`. Replaces every node label that would otherwise show as `index` (six topic/catalog files all named `index.md`) with the page's frontmatter `title:`. After enabling, turn on these features in the plugin's settings:

- **Graph view** (the killer fix — the graph stops being a sea of "index" nodes)
- **Explorer**
- **Tab header**
- **Backlink panel**

### Recommended additions (install on demand)

| Plugin | Why it matters here |
|---|---|
| **Hover Editor** | Peek any source page without leaving the synthesis page you're reading — huge for the "is this claim really supported by the source?" loop. |
| **Omnisearch** | Fuzzy full-text search across the whole vault with relevance ranking. Obsidian's built-in search is exact-match; Omnisearch finds things when you forget the precise phrasing. |
| **Iconize** | Folder icons (set `topics/` = 🎯, `concepts/` = 💡, `entities/` = 👤, `sources/` = 📥, `answers/` = 💬, `comparisons/` = 📊, `reports/` = 📋). Cuts visual scan time. |
| **Bases** *(core in Obsidian 1.9.10+, no install needed)* | Native database-like views over folders with sort/filter UI. Complements Dataview — use Bases for browseable tables, Dataview for computed dashboards. |
| **Linter** | Auto-format on save. **Caveat**: turn off "format YAML frontmatter" and "format dates", or it'll fight the agents on `last_updated` / `last_verified` whenever you open an LLM-edited file. Keep it for whitespace/heading normalization only. |
| **Marp** | Required to render `wiki/decks/<topic-id>.md` (output of `uv run wikipilot deck`). Optional unless you actually share decks. |

## 4. Graph view (pre-configured)

`wiki/.obsidian/graph.json` ships with color groups that match the schema, using Obsidian's property-query syntax `[kind:value]` (single brackets, no outer quotes — see [Obsidian Search docs](https://help.obsidian.md/Plugins/Search#Search+properties)):

| Kind | Color | Query |
|---|---|---|
| `topic` | 🟡 Gold (`#FFD700`) | `[kind:topic]` |
| `concept` | 🔵 Blue (`#4A90E2`) | `[kind:concept]` |
| `entity` | 🟢 Green (`#7ED321`) | `[kind:entity]` |
| `comparison` | 🟠 Orange (`#F5A623`) | `[kind:comparison]` |
| `answer` | 🟣 Purple (`#BD10E0`) | `[kind:answer]` |
| `report` | 🔴 Coral (`#FF6B6B`) | `[kind:report]` |
| `source` | ⚫ Muted gray (`#6B7280`) | `[kind:source]` |

The intent: topics are the **landing hubs** (gold draws the eye), synthesis layers (concept / entity / comparison / answer) get distinct colors so cluster boundaries are visible, sources are muted gray because they're the raw ingest layer beneath everything else, and reports stand out coral when you want to find them.

To tweak: Settings → Core plugins → Graph view → click the **Filters → Groups** disclosure (it's the same UI editing `graph.json`).

### The killer pattern: local graph per topic

Don't navigate the full vault graph — it's a hairball. Instead:

1. Open any topic's `index.md` (e.g., click **🟡 Agentic coding tools and harnesses** in the file explorer).
2. **`Ctrl/Cmd-P`** → **Open local graph view**.
3. In the local graph's **Filters → Display**, set the depth slider to **2**.

You now see the topic plus every concept, entity, source, comparison, and answer two hops away — the topic's full neighborhood, color-coded, in one frame. This is the single most useful navigation pattern in the vault.

Optional: drag the local graph tab to the right sidebar so it follows you as you open pages — it auto-updates per current note.

### Filter recipes for the main graph

In the graph view's **Filters → Search** box:

| Goal | Query |
|---|---|
| Show only synthesis pages (hide all sources) | `-[kind:source]` |
| Show only one topic's neighborhood | open the topic's `index.md` → **Open local graph** (above) |
| Show only pages with active disputes | `"Status: unresolved"` (literal-phrase content search) |
| Show only pages tagged for one topic | `[topic:agentic-coding]` (works on source pages, which carry a `topic:` property) |
| Show only the most-recently-touched 30 pages | open the dashboard's "Recently touched synthesis pages" table instead — Dataview handles this better than graph filters |

## 5. CSS snippet (pre-configured)

`wiki/.obsidian/snippets/wikipilot.css` ships in the repo and is enabled by `wiki/.obsidian/appearance.json`. After Obsidian opens the vault, verify Settings → Appearance → **CSS snippets** → **`wikipilot`** toggle is on. It restyles:

- `## Disputes` sections → red left-border callout box (so unresolved disputes are visually unmissable)
- `## Open questions` sections → blue left-border callout box, with checkboxes dimmed (they're discussion-trackers, not GTD tasks)
- `>` blockquote evidence blocks → italicized with accent left-border (every cited claim has one underneath; this makes the evidence layer scannable)
- Inline `[[wikilinks]]` → dotted underline, solid on hover (less visual noise on heavily-cited paragraphs)
- Dataview tables → tighter padding, bolded headers (the dashboard reads better)
- Source pages → subtle background tint (visual signal that you're reading raw ingest, not synthesis)

Edit `wikipilot.css` directly to customize. After editing, Settings → Appearance → CSS snippets → click the refresh icon next to the snippet to reload without restarting Obsidian.

## 6. The personal dashboard (`wiki/_dashboard.md`)

Ships pre-built. Open it (`Ctrl/Cmd-O` → type "dashboard") to see:

- **Topics at a glance** — per-topic source counts, most recent source per topic, per-topic last-touched dates
- **Recently added sources** (last 7 days, grouped by topic)
- **Recently touched synthesis pages** (last 7 days)
- **Pages needing re-verification** (stale, with days-overdue count)
- **All open questions** (every unchecked `- [ ]` in any synthesis page)
- **Unresolved disputes** (page-level count of `Status: unresolved` bullets — computed via dvjs)
- **Recent answers** (last 30 days from the Wiki Query routine)
- **Orphan synthesis pages** (zero inbound links)
- **Quick search recipes** (paste-able Obsidian search queries)

### Bookmark it

Right-click the dashboard's tab → **Bookmark**. It now appears in the Bookmarks sidebar (enable via Settings → Core plugins → Bookmarks). One click from any view.

### The `_*.md` convention

Files starting with `_` are personal scratch: exempt from the lint, exempt from the agents' cross-page sweep, treated as **human-only** by the auto-merge gate. Use them freely for:

- `_dashboard.md` (shipped)
- `_inbox.md` (drop links here as you read; clean up weekly)
- `_reading-list.md`, `_questions-to-ask-the-wiki.md`, etc.

The schema lint and the agents will both ignore them. The auto-merge gate will **block** any LLM-authored PR that touches them, treating them with the same protection as `CLAUDE.md` and `topics.yaml`.

## 7. Bookmarks (essential workflow)

Enable Settings → Core plugins → **Bookmarks** (built-in, no install). Then bookmark, in order:

1. **`_dashboard.md`** — always one click away
2. **Each topic `index.md`** (5 topics × 1 bookmark each)
3. **`log.md`** — chronological audit trail of every routine run
4. **`index.md`** — the wiki catalog (LLM-maintained)

Drag the Bookmarks panel into the left sidebar. The frequent-access pages are now in your peripheral vision.

## 8. Workspaces (save layouts for different modes)

Enable Settings → Core plugins → **Workspaces** (built-in). Workspaces are saved tab/panel layouts. Set up these two as starters:

### "Dashboard mode"
- Center: `_dashboard.md`
- Left sidebar: Bookmarks, File explorer
- Right sidebar: Outline (of dashboard sections)

Save: `Ctrl/Cmd-P` → "Workspaces: Save and load" → name **Dashboard**.

### "Research mode"
- Center: split — left pane is a topic's `index.md`, right pane is a source page from that topic
- Right sidebar: **Local graph** (depth 2, follows current note), **Backlinks**, **Outgoing links**

Save as **Research**. Switch between them with `Ctrl/Cmd-P` → "Workspaces: Load workspace" → pick one.

A third optional workspace: **"Disputes review"** — split center with `_dashboard.md` Disputes block on the left and the page currently under review on the right. Use it after every Weekly Health PR lands.

## 9. Daily workflow

A complete loop after at least one Daily Research PR has landed:

1. **Morning** — open Obsidian, it lands on the last-used workspace. Switch to **Dashboard mode**.
2. Scan the dashboard top-to-bottom:
   - **Recently added sources** — what did the agent ingest overnight?
   - **Recently touched synthesis pages** — what did the agent rewrite? Spot-check one.
   - **Pages needing re-verification** — if anything is in your interest area, open it, re-confirm, bump `last_verified` to today (use frontmatter properties UI, not raw YAML).
   - **Unresolved disputes** — if Weekly Health filed something Sunday, resolve it per `docs/runbook.md` "Resolving a dispute".
3. **Ask the wiki a question** — either `uv run wikipilot query "..."` from a terminal, or open a GitHub issue with the `query` label. Within a minute a new answer page lands; come back to the dashboard, refresh, and the "Recent answers" block now shows it.
4. **Switch to Research mode** for any deep-dive (topic `index.md` on the left, local graph on the right).
5. **End of week** — Sunday's Weekly Health PR adds dispute candidates. Walk through them in **Disputes review** mode.

## 10. Image rendering

Source pages reference local assets under `wiki/assets/<source-slug>/<filename>`. Obsidian auto-resolves these as long as the attachment-folder setting matches (above). If an image doesn't render:

1. Check the source page's frontmatter `image_count` is non-zero.
2. Check `wiki/assets/<source-slug>/` exists and contains the image file.
3. Run `uv run wikipilot lint wiki/` — the `broken-image-ref` rule (Phase 5) flags refs that don't resolve and exits non-zero.

## 11. Troubleshooting

| Symptom | Fix |
|---|---|
| Six nodes labeled "index" in the graph | Front Matter Title plugin not installed/enabled, or its "Graph view" feature toggle is off |
| All graph nodes are gray | Either Obsidian wasn't restarted after pulling `graph.json` (close + reopen the vault), or the color-group query syntax doesn't parse. Open Graph view → cog icon → Filters → Groups → check each row's query box. Correct format is `[kind:topic]` with **single brackets, no outer quotes** (the `["kind: topic"]` double-quote form does not match anything — it tries to find a property literally named `kind: topic`). |
| Dataview blocks show raw markdown | Dataview not enabled — Settings → Community plugins → Dataview → enable. The `dataviewjs` disputes block additionally requires **Enable JavaScript Queries** in Dataview settings. |
| Dataview blocks show "0 results" | Frontmatter may use string dates (`"2026-05-11"`) instead of YAML date values. Wikipilot's writers emit proper date types, but a hand-edited page might have strings. Fix the page, or wrap with `date(last_verified)` in the query. |
| Graph view is empty | You opened the repo root instead of `wiki/`. Close the vault and re-open at `wiki/`. |
| CSS snippet doesn't apply | Settings → Appearance → CSS snippets → toggle `wikipilot` off and on. If still nothing, check the file at `wiki/.obsidian/snippets/wikipilot.css` exists. |
| New pages from the routine don't appear | `Ctrl/Cmd-P` → "Force re-index vault". Then the dashboard's Dataview blocks pick them up. |
| Marp deck won't render | Install the Marp community plugin and confirm the deck file's frontmatter has `marp: true`. |

## 12. What this does NOT replace

Obsidian is the **viewer**. The wiki itself is owned by the routines. Don't hand-edit unless:

- You're resolving a `Status: unresolved` dispute on a page (this is the canonical human-edit workflow)
- You're updating a topic's `purpose.md` (human-only) to nudge the agent
- You're adding to your own `_*.md` scratch files

Everything else (sources, synthesis, comparisons, answers, reports, index, log) is LLM-maintained. Pull from `main` to see what shipped overnight; the Dashboard makes the new state legible at a glance.
