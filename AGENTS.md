# Agent Operating Context

## Who I Am

Name: ziwenxu

Work: Building Codex Knowledge LLM, a Codex plugin and Obsidian vault kit that turns source material into durable Markdown knowledge.

Focus: Make the plugin easy to install, easy to demo, and useful as a repeatable system for compounding AI context.

Goals:
- Help users install the Codex plugin with one command.
- Turn any folder, including this repository, into an Obsidian-ready knowledge vault.
- Convert reports, articles, transcripts, tutorials, and book notes into structured note packs.
- Keep examples, smoke tests, and onboarding docs launch-ready for public sharing.

## Current Projects

Active: Productizing `codex-knowledge-llm` as a shareable Codex plugin.

Stuck on: Making the first-run experience obvious enough that someone from an X article can clone, install, demo, and understand the system quickly.

Next milestone: A clean repo that installs as a local Codex plugin, initializes a vault, ingests a source file, and documents the generated note workflow.

## Repository Map

- `.codex-plugin/plugin.json` - Codex plugin manifest.
- `skills/codex-knowledge-llm/` - Codex skill instructions and references.
- `scripts/onboard.py` - one-command install plus vault setup.
- `scripts/create-note-pack.py` - deterministic source-to-note-pack helper.
- `scripts/init-vault-kit.py` - embeds the vault kit into a folder.
- `scripts/install-codex-plugin.py` - installs the plugin into the local Codex plugin marketplace.
- `templates/vault-kit/` - reusable vault starter files.
- `examples/` - sample inputs and generated note packs.
- `inbox/`, `notes/`, `ideas/`, `projects/` - this repository's own knowledge vault.

## How This Vault Works

Owner: ziwenxu

Inbox: `/inbox` - unprocessed captures, daily briefs, and session summaries.

Notes: `/notes` - original source material and source index notes.

Ideas: `/ideas` - syntheses, teardowns, implementation notes, and original thinking.

Projects: `/projects` - active work, product decisions, launch plans, and implementation context.

## What I Want From Codex

- Read this file before making repository or vault changes.
- Preserve plugin installability and smoke-test coverage.
- Prefer small, demoable workflows over abstract documentation.
- Keep the X article reader journey in mind: clone, install, initialize, ingest, inspect notes.
- Flag contradictions between README promises, skill behavior, scripts, and examples.
- Link back to relevant vault notes when answering repository-level questions.

## Instruction

Treat this repository as both product code and its own knowledge vault. When adding important implementation or launch context, create or update notes in `notes/`, `ideas/`, or `projects/` so future Codex sessions do not start cold.
