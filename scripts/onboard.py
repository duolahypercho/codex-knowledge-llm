#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALL_SCRIPT = ROOT / "scripts" / "install-codex-plugin.py"
VAULT_SCRIPT = ROOT / "scripts" / "init-vault-kit.py"


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install the Codex plugin and/or embed the vault kit in one step."
    )
    parser.add_argument(
        "--vault",
        help="Existing folder to turn into an Obsidian-ready knowledge vault.",
    )
    parser.add_argument(
        "--owner",
        default="ziwenxu",
        help="Vault owner name to write into generated templates.",
    )
    parser.add_argument(
        "--install",
        action="store_true",
        help="Install and register the local Codex plugin before embedding the vault kit.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace the installed plugin copy and overwrite vault kit files.",
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
    args = parser.parse_args()

    if not args.install and not args.vault:
        parser.error("Choose --install, --vault, or both.")

    if args.install:
        install_args = [
            sys.executable,
            str(INSTALL_SCRIPT),
            "--plugins-dir",
            args.plugins_dir,
            "--marketplace",
            args.marketplace,
        ]
        if args.force:
            install_args.append("--force")
        run(install_args)

    if args.vault:
        vault_args = [
            sys.executable,
            str(VAULT_SCRIPT),
            "--target",
            args.vault,
            "--owner",
            args.owner,
        ]
        if args.force:
            vault_args.append("--force")
        run(vault_args)

    print()
    print("Next, open Codex in your vault folder and try:")
    print()
    print("  Turn this source into Obsidian notes.")
    print("  Create today's session summary.")
    print()
    print("Restart Codex if the plugin was just installed and does not appear immediately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
