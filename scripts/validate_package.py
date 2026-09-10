#!/usr/bin/env python3
"""Validate the skill package without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "SKILL.md",
    "agents/openai.yaml",
    "assets/profile-template.md",
    "assets/review-checklist-template.md",
    "assets/workspace-config-template.md",
    "references/accumulation.md",
    "references/legal-research.md",
    "references/management-deck.md",
    "references/profile-setup.md",
    "references/quality-gates.md",
    "references/runtime-adaptation.md",
    "references/upfront-briefing.md",
)
LOCAL_MD_LINK = re.compile(r"\]\((?!https?://|#)([^)]+\.md)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            fail(f"missing required file: {relative}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = re.match(r"^---\n(.*?)\n---\n", skill, re.DOTALL)
    if not frontmatter:
        fail("SKILL.md has no valid YAML frontmatter block")
    header = frontmatter.group(1)
    if not re.search(r"^name:\s*foreign-legal-ppt\s*$", header, re.MULTILINE):
        fail("SKILL.md has an unexpected skill name")
    if not re.search(r"^description:\s*\S.+$", header, re.MULTILINE):
        fail("SKILL.md has no non-empty description")

    broken: list[str] = []
    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for match in LOCAL_MD_LINK.finditer(text):
            target = (markdown.parent / match.group(1)).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                broken.append(f"{markdown.relative_to(ROOT)} -> outside package")
                continue
            if not target.is_file():
                broken.append(
                    f"{markdown.relative_to(ROOT)} -> {match.group(1)}"
                )
    if broken:
        fail("broken local Markdown links:\n" + "\n".join(broken))

    print(f"OK: {len(REQUIRED)} required files and local Markdown links validated")


if __name__ == "__main__":
    main()
