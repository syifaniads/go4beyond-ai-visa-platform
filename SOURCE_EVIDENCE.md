# Source Evidence

This portfolio is designed to remain traceable to the original collaborative project rather than replacing its history.

## 1. Original team repository

**Team repository**  
https://github.com/me-dangnhatminh/apie-adv-proj

The current `main` branch contains a detailed system-architecture description covering the hybrid on-premise + AWS design, actors, backend/domain responsibilities, PostgreSQL/replica strategy, Redis, object storage, managed identity, event processing, RAG, and monitoring.

## 2. Historical implementation snapshot

The team also preserved a historical working snapshot:

https://github.com/me-dangnhatminh/apie-adv-proj/tree/eb124439b6e06f64396fb23db5aa6e4c7ce71c8f

This link is important because the current branch presentation and the earlier implementation state are not identical. The portfolio therefore treats the historical commit as **implementation evidence**, not merely the current architecture README.

## 3. Prepared document fixtures

The team prepared documents specifically for testing:

https://github.com/me-dangnhatminh/apie-adv-proj/tree/main/tests/fixtures/documents

These should be treated as **test fixtures**, not as real applicant records. Real passports, IDs, financial statements, or other private applicant documents must never be committed to a public Git repository.

## 4. MVP screenshots

Original MVP screenshot evidence:

https://github.com/me-dangnhatminh/apie-adv-proj/tree/main/docs/specs/mvp/screenshots

This is the preferred source for original UI/prototype images because it preserves their collaborative-project context.

## 5. Final presentation evidence

The portfolio was curated using the team's **Group 6 Final Presentation - APIE Advanced Project** supplied by the project owner. A page-by-page technical evidence map is preserved here:

[`docs/presentation/FINAL_PRESENTATION_NOTES.md`](./docs/presentation/FINAL_PRESENTATION_NOTES.md)

The presentation supports the following portfolio claims:

| Presentation page | Evidence used in portfolio |
|---:|---|
| 2-3 | problem framing: fragmented information, document uncertainty, lack of pre-submission feedback |
| 4 | ecosystem of applicants, agency partners, admins, official sources, AI platform |
| 5 | prototype user flow: guided chat → upload → automated review → readiness score |
| 6 | localized MVP stack / containerized architecture |
| 7 | knowledge-cache flywheel |
| 8 | event-driven FastAPI/Redis/Celery architecture |
| 9 | HA/resilience design direction |
| 10-12 | defense in depth, data classification, secure document lifecycle |
| 13 | observability and operations |
| 14 | prototype → HA → enterprise-cloud deployment roadmap |
| 15 | service-ecosystem diagram |
| 16 | centralized intelligence / reusable knowledge positioning |

## 6. Architecture-source discrepancy

Two source artifacts describe different backend choices:

- **Final prototype presentation:** FastAPI backend in the localized MVP.
- **Current original-repository architecture README:** Flask modular-monolith reference design for the hybrid architecture.

This portfolio does **not** silently choose one and pretend the other never existed. The distinction is documented in [README.md](./README.md), [ARCHITECTURE.md](./ARCHITECTURE.md), and [LIMITATIONS.md](./LIMITATIONS.md).

## 7. Evidence integrity

When a claim in this portfolio is an architectural recommendation rather than a confirmed prototype implementation, it is labeled as:

- target architecture;
- roadmap;
- future-state design;
- recommended production control.

That distinction is intentional so senior reviewers can separate implemented work from system-design exploration.

## 8. Portfolio ownership vs source ownership

This repository is owned by `syifaniads` for portfolio presentation. The original implementation remains attributed to the collaborative team repository. See [TEAM_ATTRIBUTION.md](./TEAM_ATTRIBUTION.md).
