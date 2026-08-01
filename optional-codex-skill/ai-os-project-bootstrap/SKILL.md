---
name: ai-os-project-bootstrap
description: Bind a new or existing repository to a local AI Operating Process using a committed project bridge, project context, Codex AGENTS.md, Claude CLAUDE.md, local path configuration, handoff state, and validation. Use when a user starts a project, wants Codex or Claude Code to inherit their AI process, needs to connect a repository to reusable routines and approval gates, or asks to validate that a project is correctly bound.
---

# AI OS Project Bootstrap

Create a project-level bridge to an existing AI Operating Process. Keep reusable rules in the process folder and repository-specific context in `.ai-operating-process/`.

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

## Boundaries

- Never put secrets, tokens, private client data, or machine-specific paths in committed bridge files.
- Do not overwrite a project context, handoff, or adapter without explicit authorization.
- `config.local.json` and `handoff.md` are local-only by default.
- The bridge gives Codex and Claude Code an automatic entry point. ChatGPT requires the generated project packet to be attached or pasted into a ChatGPT Project.
