#!/usr/bin/env sh
set -eu

root=""
while [ "$#" -gt 0 ]; do
    case "$1" in
        --root)
            [ "$#" -ge 2 ] || { printf '%s\n' "Missing value for --root" >&2; exit 2; }
            root="$2"
            shift 2
            ;;
        -h|--help)
            printf '%s\n' "Usage: sh scripts/validate-process.sh [--root /path/to/AI-Operating-Process]"
            exit 0
            ;;
        *)
            printf '%s\n' "Unknown argument: $1" >&2
            exit 2
            ;;
    esac
done

if [ -z "$root" ]; then
    script_directory=$(CDPATH= cd "$(dirname "$0")" && pwd)
    root=$(CDPATH= cd "$script_directory/.." && pwd)
fi

missing=0
for file in README.md .gitignore .gitattributes Initialize-AIOperatingProcess.ps1 00-START-HERE.md 00-CORE-INDEX.md LICENSE SECURITY.md RELEASE-NOTES.md 01-profile/voice-and-delivery.template.md 02-operating-rules/execution-standard.md 02-operating-rules/work-modes.md 02-operating-rules/runtime-guardrails.md 03-project-context/project.template.md 04-routines/ROUTINE-INDEX.md 04-routines/bug-fix.md 04-routines/writing-system.md 04-routines/live-delivery-preflight.md 04-routines/save-context.md 04-routines/public-claim-readiness.md 05-task-briefs/task.template.md 06-approval-gates/approval-gates.md 07-output-templates/completed-work.md 07-output-templates/blocker.md 07-output-templates/handoff.md 08-memory-updates/README.md 09-system-adapters/README.md 09-system-adapters/codex/AGENTS.md.template 09-system-adapters/claude/CLAUDE.md.template 09-system-adapters/chatgpt/PROJECT-INSTRUCTIONS.template.md 99-tests/release-checklist.md scripts/initialize-process.sh scripts/validate-process.sh scripts/initialize_process.py scripts/validate_process.py; do
    if [ ! -f "$root/$file" ]; then
        printf '%s\n' "FAIL: Missing required file: $file" >&2
        missing=1
    fi
done

if [ ! -f "$root/01-profile/user-profile.template.md" ] && [ ! -f "$root/01-profile/user-profile.md" ]; then
    printf '%s\n' "FAIL: Missing user profile template or configured profile." >&2
    missing=1
fi

empty=$(find "$root" -type f -name '*.md' -size 0c -print)
if [ -n "$empty" ]; then
    printf '%s\n' "FAIL: Empty Markdown files:" >&2
    printf '%s\n' "$empty" >&2
    missing=1
fi

em_dash='—'
em_dash_hits=$(find "$root" -type f -name '*.md' -exec grep -l "$em_dash" {} + || true)
if [ -n "$em_dash_hits" ]; then
    printf '%s\n' "FAIL: Em dash found:" >&2
    printf '%s\n' "$em_dash_hits" >&2
    missing=1
fi

if [ "$missing" -ne 0 ]; then
    exit 1
fi

markdown_count=$(find "$root" -type f -name '*.md' | wc -l | tr -d ' ')
printf '%s\n' "PASS: AI Operating Process Starter Kit validation passed."
printf '%s\n' "Markdown files: $markdown_count"
