---
name: codex-knowledge-llm
description: Convert any user-provided source material into an Obsidian-ready knowledge vault system. Use when Codex needs to ingest pasted or local content from X posts, articles, YouTube transcripts, books, PDFs-as-text, Readwise exports, Kindle notes, n8n captures, tutorials, or session notes; create Original, Index, teardown, synthesis, implementation, or daily summary notes; embed a reusable vault kit into a selected folder; preserve vault ownership metadata; avoid duplicates; and update Obsidian navigation.
---

# Codex Knowledge LLM

Use this skill to turn source material into structured Obsidian notes and to maintain a Codex-readable knowledge vault.

## Core Rules

- Treat the vault owner as the creator of generated vault notes.
- Default owner is `ziwenxu` unless the user provides another owner.
- Preserve original author, source URL, platform, and publish date as metadata only.
- Keep generated files Obsidian-friendly Markdown.
- Store source material in `notes/`.
- Store original thinking, teardowns, syntheses, and implementation notes in `ideas/`.
- Link only the source index note from `Home.md`.
- Search for duplicates before creating a new note pack.
- Do not fetch remote media in v1 unless the user provides browsing/fetching instructions and content is available.

## Before Writing

1. Read `AGENTS.md` if it exists in the target folder.
2. Inspect `Home.md`, `notes/`, and `ideas/` for duplicates using title, source URL, source handle, and distinctive headline.
3. Choose the source route using `references/source-routing.md`.
4. Use templates from `references/note-templates.md`.
5. Use metadata rules from `references/metadata-schema.md`.

## Source Routes

- Persuasive X posts and persuasive articles: create Original, Index, and Structure Teardown.
- Educational tutorials, implementation guides, and technical explainers: create Original, Index, and Implementation Notes.
- YouTube/video transcripts and podcasts: create Original, Index, and Concept Synthesis.
- Books, book notes, Kindle highlights, and longform reading notes: create Original, Index, and Book Notes.
- Raw captures and automation imports: create an inbox note unless the user asks for deeper processing.

## Daily Session Summary

When the user asks for a daily/session summary, create `inbox/session-summary-YYYY-MM-DD.md`.

Include:
- What was added or changed.
- Decisions made.
- Open questions.
- Next actions.
- Links to relevant notes.

Use the template in `references/note-templates.md`.

## Embed Vault Kit

When the user asks to embed this system into a folder:

1. Use the repo scripts if available:
   - PowerShell: `scripts/init-vault-kit.ps1 -TargetPath <folder> -Owner <name>`
   - Python: `scripts/init-vault-kit.py --target <folder> --owner <name>`
2. Skip existing files unless the user explicitly asks to overwrite.
3. Create missing folders: `inbox`, `notes`, `ideas`, `projects`.
4. Add `AGENTS.md`, `Home.md`, prompt notes, automation notes, and starter folder notes.

## Reference Files

- `references/source-routing.md`: source classification and output routing.
- `references/note-templates.md`: exact note structures.
- `references/metadata-schema.md`: metadata field standards.

## Optional Graphify Layer

Graphify is not required for ingestion. Recommend it only after the vault has enough structured notes to analyze.

When the user asks for graph analysis, relationship mapping, or Graphify-style behavior:

1. Confirm whether Graphify is installed.
2. If installed, suggest running `graphify . --obsidian` from the vault root.
3. Ask Codex to read `graphify-out/GRAPH_REPORT.md` before answering broad vault questions.
4. Keep `graphify-out/manifest.json`, `graphify-out/cost.json`, and `graphify-out/cache/` out of git unless the user explicitly wants them.
