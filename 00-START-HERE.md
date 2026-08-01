# Start Here

## 10-Minute Setup

1. Rename `01-profile/user-profile.template.md` to `user-profile.md` and fill in only durable preferences.
2. Rename `01-profile/voice-and-delivery.template.md` to `voice-and-delivery.md` if writing consistency matters.
3. Copy `03-project-context/project.template.md` to a descriptive project file.
4. Copy the relevant adapter file into the project or tool you use.
5. Give the AI the routing packet below.

```text
Use the AI Operating Process at [path-to-this-folder].
Load only the relevant files.

Mode: [Read-Only, Draft-Only, Local-Edit, Live-Delivery, Sensitive-Approval]
Project: 03-project-context/[project].md
Routine: 04-routines/[routine].md
Task: [plain-language goal]
Required output: [artifact, report, local change, or approved release]
```

## First Useful Task

Create a project context file, then ask:

```text
Use the AI Operating Process. Mode: Draft-Only.
Project: 03-project-context/[project].md
Routine: 04-routines/writing-system.md
Task: Draft a README for this project.
Required output: A complete Markdown file using 07-output-templates/writing-deliverable.md.
```

## Rules That Matter

- Load the smallest relevant set of files.
- Keep durable decisions in files, not only in chat.
- Run live preflight before deployment or other production-impacting work.
- Ask before secrets, auth, billing, schema, deletion, or external submissions.
- Treat a failed or skipped check as unverified, not passed.
