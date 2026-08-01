#!/usr/bin/env python3
"""Validate a repository binding to a local AI Operating Process."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


MARKER_START = "<!-- ai-os-project-bootstrap:start -->"
MARKER_END = "<!-- ai-os-project-bootstrap:end -->"
REQUIRED = [
    ".ai-operating-process/.gitignore",
    ".ai-operating-process/README.md",
    ".ai-operating-process/project-context.md",
    ".ai-operating-process/CHATGPT-PROJECT-PACKET.md",
    "AGENTS.md",
    "CLAUDE.md",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--require-local", action="store_true")
    args = parser.parse_args()
    repo = args.repo.expanduser().resolve()
    failures: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED:
        if not (repo / relative).is_file():
            failures.append(f"Missing required file: {relative}")
    bridge_ignore = repo / ".ai-operating-process/.gitignore"
    if bridge_ignore.is_file():
        ignored_entries = bridge_ignore.read_text(encoding="utf-8")
        for entry in ("config.local.json", "handoff.md"):
            if entry not in ignored_entries:
                failures.append(f"Bridge .gitignore does not exclude {entry}")
    for name in ("AGENTS.md", "CLAUDE.md"):
        path = repo / name
        if path.is_file():
            content = path.read_text(encoding="utf-8")
            if MARKER_START not in content or MARKER_END not in content:
                failures.append(f"Missing managed AI OS block: {name}")

    config = repo / ".ai-operating-process/config.local.json"
    if not config.is_file():
        message = "Local process configuration is absent. This is expected for a fresh clone, but the repository is not bound on this machine."
        (failures if args.require_local else warnings).append(message)
    else:
        try:
            root = Path(json.loads(config.read_text(encoding="utf-8"))["process_root"]).expanduser()
            if not (root / "00-CORE-INDEX.md").is_file():
                failures.append(f"Configured AI Operating Process root is invalid: {root}")
        except (KeyError, json.JSONDecodeError) as error:
            failures.append(f"Invalid local process configuration: {error}")

    if failures:
        print("FAIL: AI OS project binding validation failed.")
        for failure in failures:
            print(f" - {failure}")
        return 1
    for warning in warnings:
        print(f"WARN: {warning}")
    print("PASS: AI OS project binding validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
