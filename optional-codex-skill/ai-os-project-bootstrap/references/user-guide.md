# AI OS Project Bootstrap: User Guide

## What This Does

This connects one project to your AI Operating Process.

You set it up once. After that, Codex and Claude Code can read the project instructions and context whenever you open a new session in that project.

It does not copy your private operating process into Git. It stores only the project instructions in the repository. Your local process location and unfinished-session notes stay on your computer and are ignored by Git.

## Before You Start

You need two folders:

1. Your personal AI Operating Process folder.
2. The new or existing project folder you want an AI to work on.

For an existing project, the bootstrap checks its current instructions first. It does not overwrite them. If it finds an existing `AGENTS.md` or `CLAUDE.md`, it stops and asks before adding its bridge.

## Step 1: Set Up The Project Once

Open Codex in the project folder and send this message:

```text
Use $ai-os-project-bootstrap to connect this repository to my AI Operating Process.

Inspect the existing project first. Do not overwrite anything. Add the bridge only where safe, fill in project context from the repository, and stop only for details you cannot discover. Run the binding validator when complete.
```

The skill creates:

```text
AGENTS.md                              Instructions for Codex
CLAUDE.md                              Instructions for Claude Code
.ai-operating-process/project-context.md
                                        Project facts, tests, delivery steps, and protected areas
.ai-operating-process/CHATGPT-PROJECT-PACKET.md
                                        File to use with a ChatGPT Project
```

Before calling setup complete, fill in anything the repository cannot reveal: live URL, deployment command, client constraints, protected systems, and the real test or live-check steps.

## Step 2: Start The First Claude Code Session

Open Claude Code in the same project folder. Then send this message:

```text
Read the project instructions and context before starting. Tell me what you understand about this project, its protected areas, how it is tested, and what you need before making changes.
```

This is a short check that Claude Code found the project instructions and understands the project before it starts editing.

## Step 3: Start Later Sessions

For later Codex or Claude Code sessions in that project, begin with:

```text
Read the project instructions and context. Continue safely from the current project state.
```

The assistant should read `AGENTS.md` or `CLAUDE.md`, then the project context. If the previous session left a handoff note, it should use that too.

## Using ChatGPT

ChatGPT cannot automatically read files from a local repository. Create a ChatGPT Project, attach `.ai-operating-process/CHATGPT-PROJECT-PACKET.md`, and attach the relevant process files and project context. Start the chat with:

```text
Read the attached operating process and project context. Work only from the information and tools available in this Project.
```

## What This Does Not Do

The bridge improves consistency. It does not grant access, make deployments safe by itself, or replace tests and approval.

Before live changes, the assistant still needs to check the real environment, use the correct credentials, run the project tests, and obtain approval for sensitive actions.
