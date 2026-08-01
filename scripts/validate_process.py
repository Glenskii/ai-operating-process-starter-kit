#!/usr/bin/env python3
"""Validate a source or initialized copy of the AI Operating Process Starter Kit."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_FILES = [
    "README.md", ".gitignore", ".gitattributes", "Initialize-AIOperatingProcess.ps1",
    "00-START-HERE.md", "00-CORE-INDEX.md", "LICENSE", "SECURITY.md", "RELEASE-NOTES.md",
    "01-profile/voice-and-delivery.template.md", "02-operating-rules/execution-standard.md",
    "02-operating-rules/work-modes.md", "02-operating-rules/runtime-guardrails.md",
    "03-project-context/project.template.md", "04-routines/ROUTINE-INDEX.md",
    "04-routines/bug-fix.md", "04-routines/writing-system.md",
    "04-routines/live-delivery-preflight.md", "04-routines/save-context.md",
    "04-routines/public-claim-readiness.md", "05-task-briefs/task.template.md",
    "06-approval-gates/approval-gates.md", "07-output-templates/completed-work.md",
    "07-output-templates/blocker.md", "07-output-templates/handoff.md",
    "08-memory-updates/README.md", "09-system-adapters/README.md",
    "09-system-adapters/codex/AGENTS.md.template",
    "09-system-adapters/claude/CLAUDE.md.template",
    "09-system-adapters/chatgpt/PROJECT-INSTRUCTIONS.template.md",
    "99-tests/release-checklist.md", "scripts/initialize-process.sh",
    "scripts/validate-process.sh", "scripts/initialize_process.py", "scripts/validate_process.py",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    root = args.root.expanduser().resolve()
    failures: list[str] = []

    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            failures.append(f"Missing required file: {relative}")
    if not (root / "01-profile/user-profile.template.md").is_file() and not (root / "01-profile/user-profile.md").is_file():
        failures.append("Missing user profile template or configured profile.")

    markdown_files = list(root.rglob("*.md"))
    for path in markdown_files:
        if path.stat().st_size == 0:
            failures.append(f"Empty Markdown file: {path}")
        elif "\u2014" in path.read_text(encoding="utf-8"):
            failures.append(f"Em dash found: {path}")

    if failures:
        print("FAIL: AI Operating Process Starter Kit validation failed.")
        for failure in failures:
            print(f" - {failure}")
        return 1

    print("PASS: AI Operating Process Starter Kit validation passed.")
    print(f"Markdown files: {len(markdown_files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
