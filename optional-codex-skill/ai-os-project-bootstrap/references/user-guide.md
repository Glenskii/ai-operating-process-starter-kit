# AI OS Project Bootstrap: User Guide

## The Simple Version

Set up a project once. Then give any AI assistant one short message when you start a new session.

The project keeps its own facts, tests, safety rules, and delivery steps. Your private AI Operating Process stays outside Git. The assistant uses the same process whether you choose Codex, Claude Code, ChatGPT, Gemini, or another capable tool.

## Step 1: Set Up The Project Once

Use Codex to run the bootstrap skill. Open Codex in the project folder and send:

```text
Use $ai-os-project-bootstrap to connect this repository to my AI Operating Process.

Inspect the existing project first. Do not overwrite anything. Add the bridge only where safe, fill in project context from the repository, and stop only for details you cannot discover. Run the binding validator when complete.
```

Codex creates the project bridge:

```text
.ai-operating-process/AI-SESSION-BRIEF.md
                                        Starting point for any AI assistant
.ai-operating-process/project-context.md
                                        Project facts, tests, delivery steps, and protected areas
.ai-operating-process/handoff.md       Local continuity note, not committed to Git
AGENTS.md, CLAUDE.md                    Optional local-agent adapters
CHATGPT-PROJECT-PACKET.md               Optional ChatGPT adapter
```

For an existing project, the skill checks before changing `AGENTS.md` or `CLAUDE.md`. It does not overwrite either file.

Finish `project-context.md` with anything the repository cannot tell the assistant: live URL, deployment command, client constraints, protected systems, and the real test or live-check steps.

## Step 2: Check The First Session

Open your AI tool of choice in the project. Send this message:

```text
Read the AI Session Brief and project context before starting. Tell me what you understand about this project, its protected areas, how it is tested, and what you need before making changes.
```

This confirms that the assistant has the right context before it edits, publishes, or deploys anything.

## Step 3: Start Every Later Session

For every later session in the same project, begin with:

```text
Read the AI Session Brief and project context. Continue safely from the current project state.
```

If there is a handoff note from earlier work, the assistant should read it before continuing.

## How Each Tool Gets The Files

- Tools that automatically read repository instructions: use their normal repository-instruction file, such as `AGENTS.md` or `CLAUDE.md`. The bridge points them to the generic files.
- Tools that can open local files: ask them to read `.ai-operating-process/AI-SESSION-BRIEF.md` and `project-context.md`.
- Tools that only work with uploads or Projects: attach `AI-SESSION-BRIEF.md`, `project-context.md`, the relevant AI Operating Process files, and the tool's optional adapter packet if one exists.

## What This Does Not Do

The bridge improves consistency. It does not grant access, make deployments safe by itself, or replace tests and approval.

Before live changes, the assistant still needs to check the real environment, use the correct credentials, run the project tests, and obtain approval for sensitive actions.
