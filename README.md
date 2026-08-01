# AI Operating Process Starter Kit

A portable, file-based operating process for using AI across Codex, Claude, ChatGPT, and similar tools.

This is not a prompt library. It is a small set of editable files that tells an assistant how to work: what context matters, which mode applies, what requires approval, how to preserve state, and what proof is required before calling work complete.

```text
Profile + Rules + Project + Routine + Task Brief + Output Template
```

## Start Here

1. Create a clean personal copy using the command for your system.
2. Read `00-START-HERE.md` in that personal copy.
3. Copy `03-project-context/project.template.md` for the first project.
4. Choose one adapter under `09-system-adapters/`.
5. Run the matching local validator.

### macOS And Linux

```sh
sh scripts/initialize-process.sh --destination "$HOME/AI-Operating-Process"
sh scripts/validate-process.sh --root "$HOME/AI-Operating-Process"
```

### Any System With Python 3

```sh
python3 scripts/initialize_process.py --destination "$HOME/AI-Operating-Process"
python3 scripts/validate_process.py --root "$HOME/AI-Operating-Process"
```

### Windows PowerShell

```powershell
.\Initialize-AIOperatingProcess.ps1 -Destination "C:\AI-Operating-Process" -OwnerName "Your Name"
powershell -NoProfile -ExecutionPolicy Bypass -File .\99-tests\validate-starter-kit.ps1 -Root "C:\AI-Operating-Process"
```

## What This Solves

- Repeatedly rebuilding context across AI tools.
- Mixing writing work, local edits, and live deployment into one unsafe instruction.
- Losing durable decisions after compaction or a cross-agent handoff.
- Calling work complete without a test, a live check, or an explicit limitation.

## Important Boundary

Markdown files govern intent. They do not enforce permissions by themselves, prove live infrastructure state, or prevent an agent from executing a command outside the process. Use the included approval gates, preflight routine, version control, least-privilege credentials, and platform controls for real enforcement.

## Folder Map

```text
01-profile/            Stable preferences and voice.
02-operating-rules/    Execution, modes, runtime guardrails.
03-project-context/    One compact context file per project.
04-routines/           Repeatable workflows.
05-task-briefs/        A reusable task packet.
06-approval-gates/     Actions that require explicit approval.
07-output-templates/   Completion, blocker, and handoff formats.
08-memory-updates/     Durable continuity notes.
09-system-adapters/    Codex, Claude, and ChatGPT setup files.
scripts/               Native shell and Python setup and validation.
99-tests/              A local validation script and release checklist.
```

## License And Security

Released under the MIT License. Do not present the kit as a security boundary or an autonomous deployment system without adding hard technical controls.
