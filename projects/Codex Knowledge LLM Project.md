# Codex Knowledge LLM Project

Created by: ziwenxu
Status: active
Type: project context

## Purpose

Codex Knowledge LLM is a Codex plugin and Obsidian vault kit for turning source material into durable knowledge notes. The repository should be usable as both plugin source code and a live example vault.

## Current Product Promise

Install once. Open Codex in your vault. Paste any source. Get structured Obsidian notes that compound over time.

## Core User Journey

1. Clone the repository.
2. Run `python scripts/onboard.py --install --vault <vault> --owner <name>`.
3. Restart Codex if needed.
4. Open Codex in the vault folder.
5. Ask Codex to turn a report, article, transcript, tutorial, or book note into Obsidian notes.
6. Inspect `notes/`, `ideas/`, and `Home.md`.

## Repository-as-Vault Rule

This repository should keep its own knowledge base current:

- Add raw captures and session summaries to `inbox/`.
- Add original sources and index notes to `notes/`.
- Add syntheses, implementation notes, and teardowns to `ideas/`.
- Add roadmap, launch, and product decisions to `projects/`.

## Verification

Before publishing or pushing major changes, run:

```powershell
python scripts\smoke-test.py
python -m py_compile scripts\create-note-pack.py scripts\init-vault-kit.py scripts\install-codex-plugin.py scripts\onboard.py scripts\smoke-test.py
```

## Next Improvements

- Add screenshots or rendered examples for the X article.
- Add a short launch article draft in `ideas/`.
- Keep the README demo command aligned with the smoke test.
