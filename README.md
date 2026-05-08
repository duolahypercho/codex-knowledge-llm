# Codex Knowledge LLM

Codex Knowledge LLM is a Codex plugin and Obsidian vault kit for turning source material into a living knowledge system.

Install once. Open Codex in your vault. Paste any source. Get structured Obsidian notes that compound over time.

It helps Codex ingest articles, X posts, YouTube transcripts, book notes, PDFs-as-text, Readwise exports, Kindle notes, tutorials, and automation captures into clean Markdown notes.

Inspired by the workflow clarity of [Graphify](https://github.com/safishamsi/graphify): point a tool at a folder, generate useful knowledge artifacts, then let your AI assistant navigate from those artifacts instead of starting cold.

## The Workflow

```text
source material
  -> Codex classifies the source
  -> Codex creates an Obsidian note pack
  -> Home.md links the index note
  -> future Codex sessions read the vault before reasoning
```

Example output for a persuasive X post or article:

```text
notes/
  Ai Memory - Original.md
  Ai Memory - Index.md
ideas/
  Ai Memory - Structure Teardown.md
```

Example output for an implementation tutorial:

```text
notes/
  Set Up A Local Knowledge Vault - Original.md
  Set Up A Local Knowledge Vault - Index.md
ideas/
  Set Up A Local Knowledge Vault - Implementation Notes.md
```

See [`examples/`](examples/) for sample inputs and generated notes.

## One-Command Onboarding

Clone or download this repo, then run:

```bash
python scripts/onboard.py --install --vault /path/to/your/vault --owner your-name
```

On Windows:

```powershell
python scripts\onboard.py --install --vault C:\path\to\your\vault --owner your-name
```

This does two things:

- Installs and registers the local Codex plugin.
- Embeds the Obsidian-ready vault kit into your selected folder.

Your folder gets:

```text
AGENTS.md
Home.md
inbox/
notes/
ideas/
projects/
```

Restart Codex if the plugin does not appear immediately.

## How To Use It

After onboarding, open Codex in your vault folder and ask:

```text
Turn this source into Obsidian notes.
```

Then paste an article, X post, transcript, tutorial, book notes, or extracted PDF text.

Codex will:

- Read `AGENTS.md` for owner and vault context.
- Check `Home.md`, `notes/`, and `ideas/` for duplicates.
- Classify the source type.
- Create the right note pack.
- Link the source index note from `Home.md`.

Useful prompts:

```text
Turn this X post into Obsidian notes.
Turn this tutorial into implementation notes.
Turn this transcript into a concept synthesis.
Create today's session summary.
```

## Source Routes

- Persuasive articles and X posts become Original, Index, and Structure Teardown notes.
- Tutorials become Original, Index, and Implementation Notes.
- YouTube transcripts and podcasts become Original, Index, and Concept Synthesis.
- Book notes become Original, Index, and Book Notes.
- Raw captures can land in `inbox/`.

## What It Includes

- Codex plugin manifest: `.codex-plugin/plugin.json`
- Bundled skill: `skills/codex-knowledge-llm`
- Vault kit templates: `templates/vault-kit`
- One-command onboarding script: `scripts/onboard.py`
- Local plugin installer: `scripts/install-codex-plugin.py`
- Vault initializer: `scripts/init-vault-kit.py`
- Smoke test: `scripts/smoke-test.py`
- Example source-to-note packs: `examples/`
- Optional Graphify workflow docs

## Install Only

If you only want to install the Codex plugin:

```bash
python scripts/install-codex-plugin.py
```

On Windows:

```powershell
python scripts\install-codex-plugin.py
```

This installs a local plugin copy to:

```text
~/plugins/codex-knowledge-llm
```

And registers it in:

```text
~/.agents/plugins/marketplace.json
```

If you already installed it and want to replace the local copy:

```bash
python scripts/install-codex-plugin.py --force
```

## Embed The Vault Kit Only

macOS / Linux:

```bash
python scripts/init-vault-kit.py --target ~/Documents/MyVault --owner your-name
```

PowerShell:

```powershell
.\scripts\init-vault-kit.ps1 -TargetPath C:\path\to\vault -Owner your-name
```

Existing files are skipped by default.

Overwrite only when intentional:

```bash
python scripts/init-vault-kit.py --target /path/to/vault --owner your-name --force
```

```powershell
.\scripts\init-vault-kit.ps1 -TargetPath C:\path\to\vault -Owner your-name -Force
```

## Verify The Repo

Run the smoke test:

```bash
python scripts/smoke-test.py
```

It validates the plugin manifest, embeds a temporary vault kit, installs the plugin into a temporary marketplace, and checks that the expected files exist.

## Why Not Just Use Obsidian Templates?

Templates give you empty note shapes.

Codex Knowledge LLM gives Codex an operating system for deciding what kind of note to create, where it belongs, how to preserve source metadata, how to avoid duplicates, and how to make the result useful in future sessions.

The goal is not prettier notes. The goal is compounding context.

## Notes

V1 does not fetch remote content automatically. Provide the article text, transcript, book notes, or extracted PDF text to Codex.

Graphify is intentionally optional. Add it later when your vault contains enough structured notes to benefit from graph analysis.

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

## License

MIT. See [`LICENSE`](LICENSE).
