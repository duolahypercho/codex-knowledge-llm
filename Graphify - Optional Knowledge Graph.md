# Graphify - Optional Knowledge Graph

Created by: ziwenxu

Graphify is optional. Use it after this vault contains enough notes to benefit from graph-level analysis.

## Why Use It

Obsidian stores and links notes. Graphify can generate a relationship map and report that an AI assistant can read before answering questions about the vault.

## Suggested Flow

```bash
pipx install graphifyy
graphify install --platform codex
graphify . --obsidian
```

Expected outputs:

```text
graphify-out/
  graph.html
  GRAPH_REPORT.md
  graph.json
```

## Codex Prompt

```text
Read graphify-out/GRAPH_REPORT.md first, then answer my question using the vault notes.
```

## When To Run

- After adding a batch of sources.
- Before a weekly synthesis.
- Before asking broad questions about patterns, themes, contradictions, or gaps.

