#!/usr/bin/env python3
import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "templates" / "vault-kit"


def copy_template(target: Path, owner: str, force: bool) -> tuple[int, int]:
    copied = 0
    skipped = 0

    for source in TEMPLATE_DIR.rglob("*"):
        relative = source.relative_to(TEMPLATE_DIR)
        destination = target / relative

        if source.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
            continue

        if destination.exists() and not force:
            skipped += 1
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        text = source.read_text(encoding="utf-8").replace("{{OWNER}}", owner)
        destination.write_text(text, encoding="utf-8", newline="\n")
        copied += 1

    return copied, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description="Embed the Codex Knowledge LLM vault kit into a folder.")
    parser.add_argument("--target", required=True, help="Existing folder to receive the vault kit.")
    parser.add_argument("--owner", default="ziwenxu", help="Vault owner name to write into templates.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    if not target.exists() or not target.is_dir():
        parser.error(f"Target must be an existing directory: {target}")

    copied, skipped = copy_template(target, args.owner, args.force)
    print(f"Vault kit embedded in {target}")
    print(f"Copied: {copied}")
    print(f"Skipped existing files: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

