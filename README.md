# Codex Knowledge LLM

Codex Knowledge LLM is a Codex plugin and Obsidian vault kit for turning source material into a living knowledge system.

It helps Codex ingest articles, X posts, YouTube transcripts, book notes, PDFs-as-text, Readwise exports, Kindle notes, and automation captures into clean Obsidian notes.

Inspired by the workflow clarity of [Graphify](https://github.com/safishamsi/graphify): point a tool at a folder, generate useful knowledge artifacts, then let your AI assistant navigate from those artifacts instead of starting cold.

```bash
python scripts/init-vault-kit.py --target /path/to/your/folder --owner your-name
```

That's it. Your folder gets an Obsidian-ready vault kit:

```text
AGENTS.md
Home.md
inbox/
notes/
ideas/
projects/
```

## What It Includes

- Codex plugin manifest: `.codex-plugin/plugin.json`
- Bundled skill: `skills/codex-knowledge-llm`
- Vault kit templates: `templates/vault-kit`
- Install scripts for embedding the vault kit into any folder
- Daily session summary workflow
- Optional Graphify workflow docs for turning the vault into a queryable graph

## Embed The Vault Kit

macOS / Linux:

```bash
python3 scripts/init-vault-kit.py --target ~/Documents/MyVault --owner ziwenxu
```

PowerShell:

```powershell
.\scripts\init-vault-kit.ps1 -TargetPath C:\path\to\vault -Owner ziwenxu
```

Python:

```bash
python scripts/init-vault-kit.py --target /path/to/vault --owner ziwenxu
```

Existing files are skipped by default.

Overwrite only when intentional:

```powershell
.\scripts\init-vault-kit.ps1 -TargetPath C:\path\to\vault -Owner ziwenxu -Force
```

```bash
python scripts/init-vault-kit.py --target /path/to/vault --owner ziwenxu --force
```

## Use The Skill

After installing the plugin or copying the skill into Codex, ask:

```text
Turn this source into Obsidian notes.
```

The skill routes sources by type:

- Persuasive articles and X posts become Original, Index, and Structure Teardown notes.
- Tutorials become Original, Index, and Implementation Notes.
- YouTube transcripts become Original, Index, and Concept Synthesis.
- Book notes become Original, Index, and Book Notes.
- Raw captures can land in `inbox`.

## Daily Session Summary

Ask Codex:

```text
Create today's session summary.
```

Codex writes:

```text
inbox/session-summary-YYYY-MM-DD.md
```

The summary includes what changed, decisions, open questions, next actions, and related notes.

## Notes

V1 does not fetch remote content automatically. Provide the article text, transcript, book notes, or extracted PDF text to Codex.

Graphify is intentionally deferred. Add it later when your vault contains enough structured notes to benefit from graph analysis.

## Optional: Add Graphify

Codex Knowledge LLM creates structured notes. Graphify can then map those notes into a graph.

After your vault has useful material:

```bash
pipx install graphifyy
graphify install --platform codex
graphify . --obsidian
```

Useful Graphify outputs include:

```text
graphify-out/
  graph.html
  GRAPH_REPORT.md
  graph.json
```

Recommended flow:

1. Use Codex Knowledge LLM to ingest and structure sources.
2. Run Graphify on the vault when you want a relationship map.
3. Ask Codex to read `GRAPH_REPORT.md` before answering vault-level questions.

Graphify is an optional analysis layer, not required for basic vault use.
