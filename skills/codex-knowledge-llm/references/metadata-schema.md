# Metadata Schema

Use simple Markdown metadata lines at the top of generated notes.

## Required Fields

```markdown
Created by: <owner>
Status: captured
Type: <type>
```

Default owner: `ziwenxu`.

## Source Metadata

Use only when known:

```markdown
Captured from: <platform or source>
Original author: <name>
Original author handle: <handle>
Original publish date: YYYY-MM-DD
Source URL: <url>
Related source: [[Source Note]]
```

## Types

Recommended values:

- `source article`
- `source transcript`
- `source book notes`
- `article study`
- `writing teardown`
- `concept synthesis`
- `implementation notes`
- `book notes`
- `daily session summary`
- `quick capture`

## Ownership Rule

Generated vault notes are created by the vault owner. External creators belong in source metadata only. Do not write a note in a way that suggests the external author created the vault.

## Filename Rule

Use title case, ASCII-safe filenames, and the suffix pattern:

- `<Title> - Original.md`
- `<Title> - Index.md`
- `<Title> - Structure Teardown.md`
- `<Title> - Concept Synthesis.md`
- `<Title> - Implementation Notes.md`
- `<Title> - Book Notes.md`

