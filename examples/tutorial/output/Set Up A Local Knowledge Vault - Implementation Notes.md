# Set Up A Local Knowledge Vault - Implementation Notes

Created by: ziwenxu
Related source: [[Set Up A Local Knowledge Vault - Original]]
Status: implementation-ready
Type: implementation notes

## Goal

Create a local folder structure that Codex and Obsidian can both use as a durable knowledge vault.

## Prerequisites

- A local folder for the vault.
- Obsidian or another Markdown reader.
- A Codex session opened in the vault folder.

## Setup Sequence

1. Create `inbox`, `notes`, `ideas`, and `projects`.
2. Add `AGENTS.md` at the vault root.
3. Write owner context, current projects, and assistant instructions in `AGENTS.md`.
4. Store original source material separately from synthesis.
5. Link related notes from an index note.
6. Review `inbox` daily and promote useful captures.

## Risks And Edge Cases

- Mixing source text and synthesis makes provenance harder to track.
- Missing owner context makes generated notes feel generic.
- Letting inbox captures pile up turns the vault into another dump.

## Next Actions

- Run the Codex Knowledge LLM vault initializer.
- Add one real source.
- Ask Codex to create an index note and implementation notes.
