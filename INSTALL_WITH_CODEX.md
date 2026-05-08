# Install With Codex

This guide is for users who want their own Codex agent to install Codex Knowledge LLM from a GitHub link.

## Copy-Paste Prompt

Paste this into Codex and replace the placeholders:

```text
Install this Codex plugin from GitHub:

https://github.com/duolahypercho/codex-knowledge-llm

Set it up for my local knowledge vault at:

<absolute path to my vault>

Use this owner name in generated vault files:

<my name>

Please:
1. Clone or update the repository locally.
2. Run the onboarding script with --install and --vault.
3. Verify the plugin manifest and run the smoke test.
4. Confirm the plugin was registered in my local Codex marketplace.
5. Tell me whether I need to restart Codex.
```

## What Codex Should Run

After cloning the repo, Codex should run:

```bash
python scripts/onboard.py --install --vault /path/to/your/vault --owner your-name
python scripts/smoke-test.py
```

On Windows:

```powershell
python scripts\onboard.py --install --vault C:\path\to\your\vault --owner your-name
python scripts\smoke-test.py
```

## What This Does

The onboarding script:

- Installs the plugin into the local Codex plugin folder.
- Registers it in the local Codex marketplace file.
- Embeds the vault kit into the selected folder.
- Creates `AGENTS.md`, `Home.md`, `inbox/`, `notes/`, `ideas/`, and `projects/`.

## After Install

Restart Codex if the plugin does not appear immediately.

Then open Codex in your vault folder and ask:

```text
Turn this source into Obsidian notes.
```

For a local file, ask:

```text
Use Codex Knowledge LLM to ingest this file into my vault: /path/to/source.md
```
