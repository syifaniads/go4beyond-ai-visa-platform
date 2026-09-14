# Security Policy

This is a **portfolio mirror of a collaborative prototype**, not a production visa-processing service.

## Sensitive data

Do not commit or open issues containing:

- real passport scans;
- national IDs;
- bank statements or pay slips;
- applicant names combined with private visa documents;
- passwords, API keys, tokens, cookies, presigned URLs, or private keys;
- production/internal credentials.

Use synthetic fixtures only.

## Architecture security

The security and privacy design is documented in [SECURITY_PRIVACY.md](./SECURITY_PRIVACY.md), covering:

- data classification;
- identity and authorization;
- document-upload boundaries;
- encryption;
- AI/PII minimization;
- RAG prompt-injection concerns;
- logging;
- retention/deletion.

## Reporting a problem

If you find a secret, real personal document, or other sensitive artifact in this portfolio repository, do not reproduce it in a public issue. Contact the repository owner privately and identify only the affected path.

## Original project

Issues concerning the original collaborative codebase should be evaluated against the original team repository linked in [SOURCE_EVIDENCE.md](./SOURCE_EVIDENCE.md). This portfolio does not automatically represent the current deployment state of that project.
