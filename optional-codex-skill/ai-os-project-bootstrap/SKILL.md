---
name: ai-os-project-bootstrap
description: Bind a new or existing repository to a local AI Operating Process using a vendor-neutral session brief, project context, optional platform adapters, local path configuration, handoff state, and validation. Use when a user starts a project, wants any AI assistant to inherit a consistent process, needs to connect a repository to reusable routines and approval gates, or asks to validate that a project is correctly bound.
---

# AI OS Project Bootstrap

Create a project-level bridge to an existing AI Operating Process. Keep reusable rules in the process folder and repository-specific context in `.ai-operating-process/`.

Read `references/user-guide.md` when explaining the setup to a user. Use its three-message sequence instead of giving a long technical explanation.

## Workflow

1. Locate the process root from the request, `AI_OPERATING_PROCESS_ROOT`, or existing `.ai-operating-process/config.local.json`.
2. Inspect `AGENTS.md` and `CLAUDE.md` before modifying them.
3. Run `scripts/bind_project.py` with the repository and process root.
4. If an existing adapter has no managed block, stop unless the user explicitly authorizes integration.
5. Run `scripts/validate_project_binding.py --require-local` after binding.
6. Report the bridge files, local-only files, and any remaining integration decision.

## Commands

```text
python scripts/bind_project.py --repo [repository] --process-root [AI OS root]
python scripts/validate_project_binding.py --repo [repository] --require-local
```

Use `--integrate-existing` only after reviewing a pre-existing `AGENTS.md` or `CLAUDE.md`. The command appends one managed block and does not rewrite existing instructions.

## User Outcome

After one-time setup, any AI assistant can use `.ai-operating-process/AI-SESSION-BRIEF.md` and the project context. Platform-specific files such as `AGENTS.md`, `CLAUDE.md`, and `CHATGPT-PROJECT-PACKET.md` are adapters, not the source of truth. The user normally begins later work with: `Read the AI Session Brief and project context. Continue safely from the current project state.`

## Boundaries

- Never put secrets, tokens, private client data, or machine-specific paths in committed bridge files.
- Do not overwrite a project context, handoff, or adapter without explicit authorization.
- `config.local.json` and `handoff.md` are local-only by default.
- The bridge gives Codex and Claude Code an automatic entry point. ChatGPT requires the generated project packet to be attached or pasted into a ChatGPT Project.
