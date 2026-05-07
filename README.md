# Codex Knowledge LLM

Codex Knowledge LLM is a Codex plugin and Obsidian vault kit for turning source material into a living knowledge system.

It helps Codex ingest articles, X posts, YouTube transcripts, book notes, PDFs-as-text, Readwise exports, Kindle notes, and automation captures into clean Obsidian notes.

## What It Includes

- Codex plugin manifest: `.codex-plugin/plugin.json`
- Bundled skill: `skills/codex-knowledge-llm`
- Vault kit templates: `templates/vault-kit`
- Install scripts for embedding the vault kit into any folder
- Daily session summary workflow

## Embed The Vault Kit

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

