# Project Binding Layout

```text
repository/
├── AGENTS.md                         Codex entry point
├── CLAUDE.md                         Claude Code entry point
└── .ai-operating-process/
    ├── README.md                     Shared bridge contract
    ├── project-context.md            Committed project facts and runbook
    ├── CHATGPT-PROJECT-PACKET.md     Attach to a ChatGPT Project
    ├── .gitignore                    Ignores local-only state
    ├── config.local.json             Local AI OS root, ignored
    └── handoff.md                    Session continuity, ignored
```

The process root remains outside the repository. The repository only records how agents should discover and apply it on a machine where the owner has configured the local path.
