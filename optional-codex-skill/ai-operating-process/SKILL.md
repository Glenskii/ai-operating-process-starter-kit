---
name: ai-operating-process
description: Set up, route, or run work through a portable AI Operating Process folder. Use when a user asks to establish reusable AI context, choose a work mode, load project context and routines, prepare a cross-agent handoff, run a live-delivery preflight, or assess whether an AI workflow is ready for public or production claims.
---

# AI Operating Process

Use this skill to route governed AI work through an existing AI Operating Process folder. The folder is the source of truth. Do not duplicate its contents in chat or treat this skill as a security boundary.

## Locate The Process

1. Use the user-provided process path.
2. Otherwise look for `.ai-operating-process` in the repository or workspace.
3. If no process exists, direct the user to create one from the Starter Kit before claiming the workflow is configured.

## Route The Task

1. Read `00-CORE-INDEX.md`.
2. Select the narrowest work mode from `02-operating-rules/work-modes.md`.
3. Load the active project context and one routine.
4. Load voice rules only for writing or public-facing delivery.
5. Load an output template when creating a durable artifact or handoff.

## Enforce The Boundaries

- Before production-impacting work, load runtime guardrails and run live-delivery preflight.
- Before secrets, auth, billing, DNS, WAF, schema, deletion, paid services, or external submission, stop for approval.
- Before compaction or a cross-agent handoff, use the save-context routine and verify the saved note by reading it back.
- Before public technical or release claims, use public-claim readiness and calibrate language to the available evidence.

## Completion

Report the active mode, files used, verified evidence, remaining risks, and the durable artifact or state note created.
