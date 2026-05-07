#!/usr/bin/env python3
import argparse
import json
import shutil
from pathlib import Path


PLUGIN_NAME = "codex-knowledge-llm"
DISPLAY_NAME = "Codex Knowledge LLM"


def copy_plugin(source_root: Path, target_root: Path, force: bool) -> Path:
    plugin_target = target_root / PLUGIN_NAME

    if plugin_target.exists():
        if not force:
            raise SystemExit(
                f"Plugin already exists at {plugin_target}. Re-run with --force to replace it."
            )
        shutil.rmtree(plugin_target)

    ignore = shutil.ignore_patterns(
        ".git",
        ".tmp-tests",
        "__pycache__",
        ".DS_Store",
        "Thumbs.db",
    )
    target_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_root, plugin_target, ignore=ignore)
    return plugin_target


def update_marketplace(marketplace_path: Path) -> None:
    marketplace_path.parent.mkdir(parents=True, exist_ok=True)

    if marketplace_path.exists():
        data = json.loads(marketplace_path.read_text(encoding="utf-8"))
    else:
        data = {
            "name": "local",
            "interface": {"displayName": "Local Plugins"},
            "plugins": [],
        }

    data.setdefault("name", "local")
    data.setdefault("interface", {}).setdefault("displayName", "Local Plugins")
    plugins = data.setdefault("plugins", [])

    entry = {
        "name": PLUGIN_NAME,
        "source": {
            "source": "local",
            "path": f"./plugins/{PLUGIN_NAME}",
        },
        "policy": {
            "installation": "AVAILABLE",
            "authentication": "ON_INSTALL",
        },
        "category": "Productivity",
    }

    for index, existing in enumerate(plugins):
        if existing.get("name") == PLUGIN_NAME:
            plugins[index] = entry
            break
    else:
        plugins.append(entry)

    marketplace_path.write_text(
        json.dumps(data, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install Codex Knowledge LLM as a local Codex plugin."
    )
    parser.add_argument(
        "--plugins-dir",
        default=str(Path.home() / "plugins"),
        help="Directory that contains local Codex plugin folders.",
    )
    parser.add_argument(
        "--marketplace",
        default=str(Path.home() / ".agents" / "plugins" / "marketplace.json"),
        help="Local Codex marketplace.json path.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing local plugin copy.",
    )
    args = parser.parse_args()

    source_root = Path(__file__).resolve().parents[1]
    plugin_target = copy_plugin(source_root, Path(args.plugins_dir).expanduser(), args.force)
    marketplace_path = Path(args.marketplace).expanduser()
    update_marketplace(marketplace_path)

    print(f"Installed {DISPLAY_NAME} to {plugin_target}")
    print(f"Updated marketplace: {marketplace_path}")
    print("Restart Codex if the plugin does not appear immediately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

