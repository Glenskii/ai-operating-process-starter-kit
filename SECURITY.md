# Security Boundary

The AI Operating Process is an organizational and instruction layer. It is not an authentication system, a permission system, a sandbox, or a replacement for platform security controls.

Before using this kit for production work:

- enforce least-privilege credentials outside the AI process;
- keep secrets in approved secret storage, never in Markdown files;
- use version control, protected branches, reviews, and deployment controls;
- require explicit approval for sensitive or irreversible actions;
- verify current live state before making production claims or changes.

Report a security issue privately to the repository owner. Do not include credentials, private data, or exploit details in public issues.
