# Work Modes

## Read-Only

Inspect, diagnose, research, and report. Do not edit, deploy, push, send, or alter external systems.

## Draft-Only

Create drafts and local reusable artifacts. Do not publish, push, deploy, or submit externally.

## Local-Edit

Edit relevant local files and run local verification. Do not deploy, push, or change sensitive systems.

## Live-Delivery

Use only when the user explicitly requests release, deploy, publish, or equivalent live action. Run `04-routines/live-delivery-preflight.md`, follow the project runbook, stop on failed verification, and preserve approval gates.

## Sensitive-Approval

Stop for explicit approval before secrets, credentials, auth, billing, DNS, WAF, database schema, permanent deletion, client-data deletion, paid activation, or external submissions.
