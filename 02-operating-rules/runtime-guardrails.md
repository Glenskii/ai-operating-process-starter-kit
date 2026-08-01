# Runtime Guardrails

## Fresh Reality Check

Before production-impacting work, verify current branch and status, target environment, relevant live state, and available dry-run or health checks. Stop when live evidence conflicts with saved context.

## Reassert Approval Gates

Immediately before a sensitive action, re-check work mode, approval gates, and project context. Earlier instructions are not a sufficient approval check.

## Lean Context Loading

Use: core index -> project context -> selected routine -> output template. Do not load the entire kit by default.

## State Capture

For non-trivial work, record working directory, branch, changed files, commands, validation, and pending risk. Use `04-routines/save-context.md` before compaction or handoff.

## Concurrency Control

Treat shared operating files as single-writer unless a branch or lock strategy exists. Do not allow parallel agents to edit the same process file without coordination.

## Voice Does Not Override Syntax

Preserve technical syntax over writing style.
