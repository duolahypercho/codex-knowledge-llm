#!/usr/bin/env python3
import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / ".tmp-tests" / "smoke"


def run(args: list[str]) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def assert_exists(path: Path) -> None:
    if not path.exists():
        raise AssertionError(f"Expected path to exist: {path}")


def main() -> int:
    if TMP.exists():
        shutil.rmtree(TMP)
    TMP.mkdir(parents=True)

    plugin_json = ROOT / ".codex-plugin" / "plugin.json"
    with plugin_json.open("r", encoding="utf-8") as handle:
        manifest = json.load(handle)

    assert manifest["name"] == "codex-knowledge-llm"
    assert manifest["skills"] == "./skills/"

    vault = TMP / "vault"
    vault.mkdir()
    run(
        [
            sys.executable,
            "scripts/init-vault-kit.py",
            "--target",
            str(vault),
            "--owner",
            "test-owner",
        ]
    )
    assert_exists(vault / "AGENTS.md")
    assert_exists(vault / "Home.md")
    assert_exists(vault / "notes" / "Notes.md")
    assert "test-owner" in (vault / "AGENTS.md").read_text(encoding="utf-8")

    plugins_dir = TMP / "plugins"
    marketplace = TMP / ".agents" / "plugins" / "marketplace.json"
    run(
        [
            sys.executable,
            "scripts/install-codex-plugin.py",
            "--plugins-dir",
            str(plugins_dir),
            "--marketplace",
            str(marketplace),
        ]
    )
    assert_exists(plugins_dir / "codex-knowledge-llm" / ".codex-plugin" / "plugin.json")

    data = json.loads(marketplace.read_text(encoding="utf-8"))
    plugin_names = [plugin["name"] for plugin in data["plugins"]]
    assert "codex-knowledge-llm" in plugin_names

    source = ROOT / "examples" / "report" / "input.md"
    run(
        [
            sys.executable,
            "scripts/create-note-pack.py",
            "--vault",
            str(vault),
            "--input",
            str(source),
            "--owner",
            "test-owner",
            "--route",
            "persuasive",
            "--source",
            "X article",
        ]
    )
    assert_exists(vault / "notes" / "Compounding AI Context - Original.md")
    assert_exists(vault / "notes" / "Compounding AI Context - Index.md")
    assert_exists(vault / "ideas" / "Compounding AI Context - Structure Teardown.md")
    assert "[[Compounding AI Context - Index]]" in (vault / "Home.md").read_text(
        encoding="utf-8"
    )

    print("Smoke test passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
