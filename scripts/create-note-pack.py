#!/usr/bin/env python3
import argparse
import re
import sys
from datetime import date
from pathlib import Path


ROUTE_SUFFIX = {
    "persuasive": "Structure Teardown",
    "tutorial": "Implementation Notes",
    "transcript": "Concept Synthesis",
    "book": "Book Notes",
}

ORIGINAL_TYPE = {
    "persuasive": "source article",
    "tutorial": "source article",
    "transcript": "source transcript",
    "book": "source book notes",
}

INDEX_RELATED = {
    "persuasive": "reusable breakdown for recreating this pattern",
    "tutorial": "implementation-ready breakdown",
    "transcript": "concept synthesis and reusable ideas",
    "book": "book notes and applications",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def write_text(path: Path, text: str, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    return True


def title_case(value: str) -> str:
    small_words = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "of", "on", "or", "the", "to", "vs", "with"}
    acronyms = {"ai", "api", "llm", "pdf", "ui", "ux", "url", "x"}
    words = re.split(r"\s+", value.strip())
    titled = []
    for index, word in enumerate(words):
        lowered = word.lower()
        if lowered in acronyms:
            titled.append(lowered.upper())
        elif index > 0 and lowered in small_words:
            titled.append(lowered)
        else:
            titled.append(lowered[:1].upper() + lowered[1:])
    return " ".join(titled)


def filename_safe(title: str) -> str:
    cleaned = re.sub(r"[^\w\s-]", "", title, flags=re.ASCII)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return title_case(cleaned or "Untitled Source")


def infer_title(source_text: str, fallback: str) -> str:
    for line in source_text.splitlines():
        stripped = line.strip().strip("#").strip()
        if stripped and len(stripped) <= 90:
            return filename_safe(stripped)
    return filename_safe(Path(fallback).stem)


def classify_route(route: str, source_text: str) -> str:
    if route != "auto":
        return route

    lowered = source_text.lower()
    tutorial_terms = ["step", "install", "setup", "command", "implementation", "tutorial", "configure"]
    transcript_terms = ["transcript", "speaker", "host:", "guest:", "youtube", "podcast"]
    book_terms = ["chapter", "kindle", "highlights", "book notes", "author:"]
    persuasive_terms = ["most people", "why", "shift", "problem", "opportunity", "thesis"]

    scores = {
        "tutorial": sum(term in lowered for term in tutorial_terms),
        "transcript": sum(term in lowered for term in transcript_terms),
        "book": sum(term in lowered for term in book_terms),
        "persuasive": sum(term in lowered for term in persuasive_terms),
    }
    best = max(scores, key=scores.get)
    return best if scores[best] else "persuasive"


def prose_text(source_text: str) -> str:
    lines = []
    for line in source_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        lines.append(stripped)
    return "\n".join(lines)


def first_sentences(source_text: str, limit: int = 3) -> list[str]:
    normalized = re.sub(r"\s+", " ", prose_text(source_text))
    sentences = re.split(r"(?<=[.!?])\s+", normalized)
    return [sentence.strip() for sentence in sentences if sentence.strip()][:limit]


def extract_bullets(source_text: str, limit: int = 6) -> list[str]:
    bullets = []
    for line in source_text.splitlines():
        stripped = line.strip()
        if re.match(r"^[-*]\s+", stripped) or re.match(r"^\d+[.)]\s+", stripped):
            bullets.append(re.sub(r"^([-*]|\d+[.)])\s+", "", stripped))
    if bullets:
        return bullets[:limit]
    return first_sentences(source_text, limit)


def metadata_lines(args: argparse.Namespace, route: str) -> list[str]:
    lines = [
        f"Created by: {args.owner}",
        f"Captured from: {args.source or route}",
    ]
    optional = [
        ("Original author", args.author),
        ("Original author handle", args.handle),
        ("Original publish date", args.published),
        ("Source URL", args.url),
    ]
    for label, value in optional:
        if value:
            lines.append(f"{label}: {value}")
    lines.extend(["Status: original capture", f"Type: {ORIGINAL_TYPE[route]}"])
    return lines


def original_note(title: str, args: argparse.Namespace, route: str, source_text: str) -> str:
    return "\n".join(
        [
            f"# {title} - Original",
            "",
            *metadata_lines(args, route),
            "",
            "## Original Content",
            "",
            source_text,
        ]
    )


def index_note(title: str, args: argparse.Namespace, route: str, analysis_suffix: str, source_text: str) -> str:
    summary = " ".join(first_sentences(source_text, 2))
    frame = first_sentences(source_text, 1)
    reusable_frame = frame[0] if frame else "Capture the source, extract the reusable pattern, and link it back to the vault."
    return "\n".join(
        [
            f"# {title} - Index",
            "",
            f"Created by: {args.owner}",
            "Status: captured",
            "Type: article study",
            "",
            "## Notes",
            "",
            f"- [[{title} - Original]] - original source captured for reference.",
            f"- [[{title} - {analysis_suffix}]] - {INDEX_RELATED[route]}.",
            "",
            "## Why This Matters",
            "",
            summary or "This source was captured because it may contain reusable ideas for the vault.",
            "",
            "## Reusable Frame",
            "",
            reusable_frame,
        ]
    )


def persuasive_note(title: str, args: argparse.Namespace, source_text: str) -> str:
    bullets = extract_bullets(source_text, 5)
    return "\n".join(
        [
            f"# {title} - Structure Teardown",
            "",
            f"Created by: {args.owner}",
            f"Related source: [[{title} - Original]]",
            "Status: reusable framework",
            "Type: writing teardown",
            "",
            "## One-Line Pattern",
            "",
            "Name the default behavior, reveal the hidden cost, then offer a better operating model.",
            "",
            "## High-Level Structure",
            "",
            *[f"{index}. {bullet}" for index, bullet in enumerate(bullets, start=1)],
            "",
            "## Why It Works",
            "",
            "The source works by making the reader recognize a familiar pattern, then reframing that pattern as a solvable operating problem.",
            "",
            "## Psychological Pattern",
            "",
            "### Default Versus Upgrade",
            "",
            'Pattern: "Most people do X. The leverage is Y. Here is the practical shift."',
            "",
            "Why it works: The reader sees the cost of the default behavior before being asked to adopt the new workflow.",
            "",
            "Use when: You want to turn a familiar frustration into a concrete system or product story.",
            "",
            f"## Content Needed From {args.owner}",
            "",
            "- A concrete before-and-after example.",
            "- A short demo of the workflow.",
            "- A clear next action for the reader.",
            "",
            "## Rebuild Template",
            "",
            "```text",
            "Most people use <tool> like <limited metaphor>.",
            "The missed opportunity is <better model>.",
            "The shift is simple:",
            "<step 1>",
            "<step 2>",
            "<step 3>",
            "The tool gets more useful when <new behavior>.",
            "```",
            "",
            "## Rewrite Prompt",
            "",
            "```text",
            "Rewrite this idea as a concise X article using the default-versus-upgrade pattern. Keep it practical, specific, and demo-driven.",
            "```",
        ]
    )


def tutorial_note(title: str, args: argparse.Namespace, source_text: str) -> str:
    bullets = extract_bullets(source_text, 6)
    return "\n".join(
        [
            f"# {title} - Implementation Notes",
            "",
            f"Created by: {args.owner}",
            f"Related source: [[{title} - Original]]",
            "Status: implementation-ready",
            "Type: implementation notes",
            "",
            "## Goal",
            "",
            first_sentences(source_text, 1)[0] if first_sentences(source_text, 1) else "Implement the workflow described by the source.",
            "",
            "## Prerequisites",
            "",
            "- Access to the target project or vault.",
            "- Source material with enough detail to preserve implementation context.",
            "",
            "## Setup Sequence",
            "",
            *[f"{index}. {bullet}" for index, bullet in enumerate(bullets, start=1)],
            "",
            "## Risks And Edge Cases",
            "",
            "- Missing source details may require a follow-up pass.",
            "- Existing files should be checked before overwriting generated notes.",
            "",
            "## Next Actions",
            "",
            "- Run the workflow once on a real source.",
            "- Review generated notes for missing context.",
            "- Link the output from `Home.md` or a project note.",
        ]
    )


def transcript_note(title: str, args: argparse.Namespace, source_text: str) -> str:
    ideas = extract_bullets(source_text, 6)
    return "\n".join(
        [
            f"# {title} - Concept Synthesis",
            "",
            f"Created by: {args.owner}",
            f"Related source: [[{title} - Original]]",
            "Status: synthesized",
            "Type: concept synthesis",
            "",
            "## Core Thesis",
            "",
            first_sentences(source_text, 1)[0] if first_sentences(source_text, 1) else "The source contains concepts worth turning into reusable vault context.",
            "",
            "## Key Ideas",
            "",
            *[f"- {idea}" for idea in ideas],
            "",
            "## Useful Frameworks",
            "",
            "- Convert memorable claims into reusable principles.",
            "- Separate source claims from owner applications.",
            "",
            "## Questions",
            "",
            "- What claim should be tested before relying on it?",
            "- Which project could use this idea first?",
            "",
            "## Applications",
            "",
            "- Link the strongest ideas to active projects.",
        ]
    )


def book_note(title: str, args: argparse.Namespace, source_text: str) -> str:
    ideas = extract_bullets(source_text, 6)
    return "\n".join(
        [
            f"# {title} - Book Notes",
            "",
            f"Created by: {args.owner}",
            f"Related source: [[{title} - Original]]",
            "Status: synthesized",
            "Type: book notes",
            "",
            "## Core Thesis",
            "",
            first_sentences(source_text, 1)[0] if first_sentences(source_text, 1) else "The book notes contain ideas worth preserving and applying.",
            "",
            "## Strongest Ideas",
            "",
            *[f"- {idea}" for idea in ideas],
            "",
            "## Frameworks",
            "",
            "- Turn repeated claims into named frameworks.",
            "",
            "## Quotes Or Highlights",
            "",
            "- Review the original note for exact quotes before publishing.",
            "",
            "## Applications",
            "",
            "- Connect the strongest ideas to current projects and decisions.",
        ]
    )


def quick_capture(title: str, args: argparse.Namespace, source_text: str) -> tuple[list[Path], list[str]]:
    filename = f"{date.today().isoformat()}-{filename_safe(title).lower().replace(' ', '-')}.md"
    path = Path(args.vault) / "inbox" / filename
    text = "\n".join(
        [
            f"# {title}",
            "",
            f"Created by: {args.owner}",
            f"Date: {date.today().isoformat()}",
            "Status: captured",
            "Type: quick capture",
            "",
            "## Capture",
            "",
            source_text,
        ]
    )
    return [path], [text]


def update_home(vault: Path, title: str, force_link: bool) -> None:
    home = vault / "Home.md"
    link = f"- [[{title} - Index]]"
    if not home.exists():
        home.write_text("# Home\n\n## Source Index\n\n" + link + "\n", encoding="utf-8", newline="\n")
        return

    text = home.read_text(encoding="utf-8")
    if link in text:
        return

    if "## Source Index" in text:
        text = text.rstrip() + "\n" + link + "\n"
    elif force_link:
        text = text.rstrip() + "\n\n## Source Index\n\n" + link + "\n"
    else:
        text = text.rstrip() + "\n\n## Source Index\n\n" + link + "\n"
    home.write_text(text, encoding="utf-8", newline="\n")


def build_notes(args: argparse.Namespace) -> tuple[str, list[Path], list[str]]:
    input_path = Path(args.input).expanduser().resolve()
    source_text = read_text(input_path)
    title = filename_safe(args.title) if args.title else infer_title(source_text, input_path.name)
    route = classify_route(args.route, source_text)

    if route == "raw":
        paths, texts = quick_capture(title, args, source_text)
        return route, paths, texts

    analysis_suffix = ROUTE_SUFFIX[route]
    vault = Path(args.vault).expanduser().resolve()
    paths = [
        vault / "notes" / f"{title} - Original.md",
        vault / "notes" / f"{title} - Index.md",
        vault / "ideas" / f"{title} - {analysis_suffix}.md",
    ]
    analysis_text = {
        "persuasive": persuasive_note,
        "tutorial": tutorial_note,
        "transcript": transcript_note,
        "book": book_note,
    }[route](title, args, source_text)
    texts = [
        original_note(title, args, route, source_text),
        index_note(title, args, route, analysis_suffix, source_text),
        analysis_text,
    ]
    return route, paths, texts


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create an Obsidian note pack from a local source file."
    )
    parser.add_argument("--vault", required=True, help="Vault folder that contains Home.md, notes/, and ideas/.")
    parser.add_argument("--input", required=True, help="Source Markdown or text file to ingest.")
    parser.add_argument("--title", help="Title to use for generated note filenames.")
    parser.add_argument(
        "--route",
        default="auto",
        choices=["auto", "persuasive", "tutorial", "transcript", "book", "raw"],
        help="Source route. Use auto to infer a route from the source text.",
    )
    parser.add_argument("--owner", default="ziwenxu", help="Vault owner name.")
    parser.add_argument("--source", help="Source platform or type, such as X, YouTube, PDF, or article.")
    parser.add_argument("--author", help="Original author name.")
    parser.add_argument("--handle", help="Original author handle.")
    parser.add_argument("--published", help="Original publish date as YYYY-MM-DD.")
    parser.add_argument("--url", help="Source URL.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing generated notes.")
    args = parser.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    if not vault.exists() or not vault.is_dir():
        parser.error(f"Vault must be an existing directory: {vault}")

    route, paths, texts = build_notes(args)
    written = []
    skipped = []
    for path, text in zip(paths, texts):
        if write_text(path, text, args.force):
            written.append(path)
        else:
            skipped.append(path)

    if route != "raw" and written:
        title = paths[1].name.removesuffix(" - Index.md")
        update_home(vault, title, force_link=True)

    print(f"Route: {route}")
    print(f"Written: {len(written)}")
    for path in written:
        print(f"  {path}")
    print(f"Skipped existing: {len(skipped)}")
    for path in skipped:
        print(f"  {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
