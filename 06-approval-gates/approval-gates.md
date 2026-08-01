# Approval Gates

## Allowed Without Asking

- Read files and inspect repositories.
- Run non-destructive discovery, tests, and builds.
- Make narrow local fixes when Local-Edit is active.
- Create drafts, reports, templates, and backup copies.

## Ask Before

- Pushing to remote repositories, deploying, publishing, or sending external messages.
- Deleting files permanently or restructuring a project.
- Changing secrets, auth, billing, DNS, WAF, database schema, payment logic, or customer data.
- Installing paid services or making external submissions.

Default rule: inspect and draft first, then ask before the final external action.
