#!/usr/bin/env python3
"""Bind a repository to a local AI Operating Process without leaking local paths."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


MARKER_START = "<!-- ai-os-project-bootstrap:start -->"
MARKER_END = "<!-- ai-os-project-bootstrap:end -->"


def process_root_from(args: argparse.Namespace, repo: Path) -> Path:
    configured = repo / ".ai-operating-process" / "config.local.json"
    candidate = args.process_root or os.environ.get("AI_OPERATING_PROCESS_ROOT")
    if not candidate and configured.is_file():
        candidate = json.loads(configured.read_text(encoding="utf-8")).get("process_root")
    if not candidate:
        raise ValueError("Provide --process-root or set AI_OPERATING_PROCESS_ROOT.")
    root = Path(candidate).expanduser().resolve()
    required = [root / "00-CORE-INDEX.md", root / "02-operating-rules" / "work-modes.md", root / "06-approval-gates" / "approval-gates.md"]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise ValueError("AI Operating Process root is incomplete: " + ", ".join(missing))
    return root


def adapter_block(kind: str) -> str:
    return f"""{MARKER_START}
# AI Operating Process Bridge

Read `.ai-operating-process/README.md` and `.ai-operating-process/project-context.md` before non-trivial work.

Use the local process path from `.ai-operating-process/config.local.json` when it exists. If it is missing, do not invent a process path. Ask the project owner to run the AI OS project bootstrap.

Select a work mode, load only the relevant routine, run live preflight before production-impacting actions, respect approval gates, and save session state to `.ai-operating-process/handoff.md` before compaction or a cross-agent handoff.

{MARKER_END}
"""


def preflight_adapter(path: Path, integrate_existing: bool) -> None:
    if not path.exists():
        return
    content = path.read_text(encoding="utf-8")
    if MARKER_START in content and MARKER_END in content:
        return
    if not integrate_existing:
        raise ValueError(f"Existing {path.name} has no managed AI OS block. Re-run with --integrate-existing after review.")


def write_new(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def upsert_adapter(path: Path, integrate_existing: bool) -> str:
    block = adapter_block(path.name)
    if not path.exists():
        path.write_text(block, encoding="utf-8")
        return "created"
    content = path.read_text(encoding="utf-8")
    if MARKER_START in content and MARKER_END in content:
        return "already managed"
    if integrate_existing:
        suffix = "" if content.endswith("\n") else "\n"
        path.write_text(content + suffix + "\n" + block, encoding="utf-8")
        return "integrated"
    raise RuntimeError("Adapter preflight should have stopped before write.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--process-root", help="Absolute path to the personal AI Operating Process.")
    parser.add_argument("--project-name", default="")
    parser.add_argument("--integrate-existing", action="store_true")
    args = parser.parse_args()

    repo = args.repo.expanduser().resolve()
    if not repo.is_dir():
        parser.error(f"repository does not exist: {repo}")
    try:
        process_root = process_root_from(args, repo)
        for name in ("AGENTS.md", "CLAUDE.md"):
            preflight_adapter(repo / name, args.integrate_existing)
    except (ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))

    project_name = args.project_name or repo.name
    binding = repo / ".ai-operating-process"
    binding.mkdir(exist_ok=True)
    created: list[str] = []
    generated = {
        ".gitignore": "config.local.json\nhandoff.md\n",
        "README.md": """# AI Operating Process Bridge\n\nThis folder binds the repository to a personal AI Operating Process without committing machine-specific paths, secrets, or session state.\n\n- `project-context.md` is the project-specific context and delivery runbook.\n- `config.local.json` is ignored and stores the local process root.\n- `handoff.md` is ignored and stores continuity before compaction or an agent handoff.\n- `CHATGPT-PROJECT-PACKET.md` is the file to attach or paste into a ChatGPT Project.\n""",
        "project-context.md": f"""# Project Context: {project_name}\n\n## Purpose\n\n[Describe the project, audience, and current goal.]\n\n## Stack And Locations\n\n```text\nRepository: {repo.name}\nRuntime: [framework, language, version]\nPackage manager: [command]\nDeployment target: [provider and target]\nLive URL: [URL, if applicable]\n```\n\n## Protected Areas\n\n- [Auth, billing, schema, secrets, DNS, WAF, client data, or other risks.]\n\n## Verification\n\n```text\nLocal checks: [commands]\nRelease checks: [commands]\nLive proof: [health URL, smoke test, or manual confirmation]\n```\n\n## Delivery Runbook\n\n```text\n1. [test]\n2. [commit]\n3. [deploy]\n4. [verify live result]\n5. [report proof]\n```\n""",
        "CHATGPT-PROJECT-PACKET.md": """# ChatGPT Project Packet\n\nAttach this file together with the relevant files from the personal AI Operating Process.\n\n```text\nUse the AI Operating Process as controlling context.\n\nRead the attached core index, work modes, approval gates, and this project context. Load only the routine needed for the active task.\n\nDo not claim access to local files, repositories, deployments, or live systems unless they are attached, connected, or otherwise available in this ChatGPT Project.\n\nFor reusable output, create a complete artifact. For live or sensitive actions, state the required preflight or approval. For a handoff, update the attached handoff note with decisions, validation, risk, and next step.\n```\n""",
    }
    for relative, content in generated.items():
        if write_new(binding / relative, content):
            created.append(f".ai-operating-process/{relative}")

    config = binding / "config.local.json"
    config.write_text(json.dumps({"schema_version": 1, "process_root": str(process_root)}, indent=2) + "\n", encoding="utf-8")
    print(f"Local process path configured: {config}")
    for name in ("AGENTS.md", "CLAUDE.md"):
        result = upsert_adapter(repo / name, args.integrate_existing)
        print(f"{name}: {result}")
    for item in created:
        print(f"Created: {item}")
    print("Next: complete .ai-operating-process/project-context.md and run validate_project_binding.py --require-local.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
