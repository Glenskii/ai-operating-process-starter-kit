#!/usr/bin/env python3
"""Create a clean personal copy of the AI Operating Process Starter Kit."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


ROOT_FILES = [
    ".gitignore",
    ".gitattributes",
    "00-CORE-INDEX.md",
    "00-START-HERE.md",
    "Initialize-AIOperatingProcess.ps1",
    "LICENSE",
    "README.md",
    "RELEASE-NOTES.md",
    "SECURITY.md",
]
ROOT_DIRECTORIES = [
    "01-profile", "02-operating-rules", "03-project-context", "04-routines",
    "05-task-briefs", "06-approval-gates", "07-output-templates",
    "08-memory-updates", "09-system-adapters", "99-tests", "scripts",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()

    source = Path(__file__).resolve().parent.parent
    destination = args.destination.expanduser().resolve()
    if destination.exists() and not destination.is_dir():
        parser.error(f"destination is not a directory: {destination}")
    if destination.exists() and any(destination.iterdir()):
        parser.error(f"destination must be empty: {destination}")

    destination.mkdir(parents=True, exist_ok=True)
    for name in ROOT_FILES:
        shutil.copy2(source / name, destination / name)
    for name in ROOT_DIRECTORIES:
        shutil.copytree(source / name, destination / name)

    (destination / "01-profile" / "user-profile.template.md").rename(
        destination / "01-profile" / "user-profile.md"
    )
    print(f"Created AI Operating Process at: {destination}")
    print("Next: complete 01-profile/user-profile.md and create a project context from 03-project-context/project.template.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
