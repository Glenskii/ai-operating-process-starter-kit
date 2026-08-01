#!/usr/bin/env sh
set -eu

usage() {
    printf '%s\n' "Usage: sh scripts/initialize-process.sh --destination /path/to/AI-Operating-Process"
}

destination=""
while [ "$#" -gt 0 ]; do
    case "$1" in
        --destination)
            [ "$#" -ge 2 ] || { usage; exit 2; }
            destination="$2"
            shift 2
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            usage
            exit 2
            ;;
    esac
done

[ -n "$destination" ] || { usage; exit 2; }

source_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
case "$destination" in
    /*) resolved_destination="$destination" ;;
    *) resolved_destination="$(pwd)/$destination" ;;
esac

if [ -e "$resolved_destination" ] && [ ! -d "$resolved_destination" ]; then
    printf '%s\n' "Destination is not a directory: $resolved_destination" >&2
    exit 1
fi

if [ -d "$resolved_destination" ] && [ -n "$(find "$resolved_destination" -mindepth 1 -maxdepth 1 -print -quit)" ]; then
    printf '%s\n' "Destination must be empty: $resolved_destination" >&2
    exit 1
fi

mkdir -p "$resolved_destination"
for item in .gitignore .gitattributes 00-CORE-INDEX.md 00-START-HERE.md 01-profile 02-operating-rules 03-project-context 04-routines 05-task-briefs 06-approval-gates 07-output-templates 08-memory-updates 09-system-adapters 99-tests Initialize-AIOperatingProcess.ps1 LICENSE README.md RELEASE-NOTES.md SECURITY.md scripts; do
    [ -e "$source_root/$item" ] && cp -R "$source_root/$item" "$resolved_destination/"
done

mv "$resolved_destination/01-profile/user-profile.template.md" "$resolved_destination/01-profile/user-profile.md"
printf '%s\n' "Created AI Operating Process at: $resolved_destination"
printf '%s\n' "Next: complete 01-profile/user-profile.md and create a project context from 03-project-context/project.template.md."
