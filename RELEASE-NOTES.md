# Version 1.2.0

Makes the project bootstrap vendor-neutral. The project now has `AI-SESSION-BRIEF.md` as its primary entry point for any AI assistant. Codex, Claude Code, and ChatGPT files remain optional adapters, and the user guide now explains a generic first-session and later-session workflow.

# Version 1.1.1

Adds a plain-language user guide for the project bootstrap skill. It explains the one-time setup, the first Claude Code session, later-session message, ChatGPT attachment step, and the limits of a Markdown-based process.

# Version 1.1.0

Adds the AI OS Project Bootstrap skill and standard-library Python binder. It creates a safe per-repository bridge for Codex, Claude Code, and ChatGPT, preserves existing agent instructions unless explicitly integrated, keeps local process paths and handoff state out of Git, and validates the binding before work starts.

# Version 1.0.2

Removes GNU-specific shell argument handling from the POSIX scripts for macOS BSD userland compatibility. Documents that PowerShell files included in initialized folders are optional Windows adapters and are not required on macOS or Linux.

# Version 1.0.1

Adds native POSIX shell setup and validation for macOS/Linux, standard-library Python setup and validation for cross-platform use, and GitHub Linguist configuration that treats PowerShell as an optional Windows adapter.

# Version 1.0.0

The first release includes a portable process folder, a PowerShell initializer, templates for profile and project context, reusable routines, approval gates, output templates, adapters for Codex, Claude Code, and ChatGPT, a starter-kit validator, and an optional Codex skill adapter.

It is designed to reduce repeated context setup and improve operational discipline. It does not grant permissions, enforce platform security, or replace live verification.
