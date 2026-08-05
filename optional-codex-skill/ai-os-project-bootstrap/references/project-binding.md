# Project Binding Layout

```text
repository/
├── AGENTS.md                         Codex entry point
├── CLAUDE.md                         Claude Code entry point
└── .ai-operating-process/
    ├── README.md                     Shared bridge contract
    ├── AI-SESSION-BRIEF.md           Starting point for any AI assistant
    ├── project-context.md            Committed project facts and runbook
    ├── CHATGPT-PROJECT-PACKET.md     Attach to a ChatGPT Project
    ├── .gitignore                    Ignores local-only state
    ├── config.local.json             Local AI OS root, ignored
    └── handoff.md                    Session continuity, ignored
```

The process root remains outside the repository. `AI-SESSION-BRIEF.md` is the source of truth for any AI assistant. The named files at repository root and the ChatGPT packet are optional platform adapters.
