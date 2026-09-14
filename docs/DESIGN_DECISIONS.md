# Design Decisions

This document summarizes the architecture decisions that make Go4beyond technically interesting to a senior reviewer.

## ADR-001 - Start with a modular monolith

**Decision:** keep the backend deployable as one application while separating domain responsibilities.

**Why:**

- small team / MVP delivery;
- simpler local deployment;
- easier end-to-end debugging;
- avoids early service-to-service operational overhead;
- preserves a path to later decomposition.

**Trade-off:** independent scaling is limited until specific workloads are moved behind worker queues or separate services.

## ADR-002 - Move document processing off the request path

**Decision:** use Redis/Celery-style background processing for OCR, extraction, digitization, and AI-heavy work.

**Why:**

- these jobs are long-running;
- failure/retry semantics differ from normal API requests;
- worker capacity can be scaled separately;
- users can receive immediate acknowledgement and later status updates.

**Required follow-up:** idempotency, bounded retries, queue monitoring, and eventually a dead-letter path.

## ADR-003 - Store raw files in object storage

**Decision:** use MinIO/S3-style storage for uploaded documents and keep metadata/state in PostgreSQL.

**Why:**

- files have different durability/lifecycle needs than relational records;
- direct/presigned upload reduces API bandwidth pressure;
- object storage maps naturally to future S3 deployment;
- storage encryption/access policy can be managed independently.

**Trade-off:** DB metadata and object state can diverge, so reconciliation and cleanup are required.

## ADR-004 - Localize the prototype dependencies

**Decision:** use local substitutes such as Ollama, MinIO, and SearXNG for the MVP rather than requiring the full managed-cloud architecture.

**Why:**

- lower prototype cost;
- predictable demo environment;
- ability to run core functionality without external managed-service provisioning;
- easier development for the team.

**Trade-off:** local components do not reproduce every availability, IAM, compliance, and scaling property of managed cloud services.

## ADR-005 - Reuse verified visa knowledge

**Decision:** structure and embed expensive first-query research so similar future requests can reuse it.

**Why:**

- lower repeated search/LLM cost;
- faster subsequent responses;
- creates a reusable knowledge layer instead of one-off chat responses.

**Trade-off:** stale knowledge can be more dangerous than a cache miss. Provenance, freshness, invalidation, and versioning are mandatory.

## ADR-006 - Use real-time status rather than making users poll blindly

**Decision:** the architecture includes SSE/WebSocket-style progress updates.

**Why:**

- document analysis is asynchronous;
- progress/status is part of the product experience;
- reduces aggressive client polling.

**Trade-off:** connection lifecycle, reconnect behavior, and event ordering must be handled.

## ADR-007 - Treat partner knowledge as governed content

**Decision:** agency/partner criteria are a product input, not automatically trusted truth.

**Why:**

- partners encode valuable workflow expertise;
- partner-specific checklists can make analysis more actionable;
- governance protects applicants from stale or misleading criteria.

**Production requirement:** versioned draft/review/publish/suspend workflow and audit trail.

## ADR-008 - Separate prototype evidence from enterprise roadmap

**Decision:** this portfolio explicitly labels future-state AWS components instead of blending them into MVP claims.

**Why:**

Senior reviewers care more about an accurate boundary than an impressive diagram. A clear "implemented vs proposed" distinction makes the system-design discussion more credible.

## ADR-009 - Keep provider boundaries replaceable

Logical interfaces should make infrastructure swappable where practical:

```text
ObjectStorage → MinIO | S3
LLMProvider   → Ollama | Bedrock | other provider
Search        → SearXNG | managed search API
VectorStore   → local vector DB | pgvector | managed KB
Identity      → prototype auth | Cognito/OIDC provider
```

This reduces coupling between product logic and one deployment environment.

## ADR-010 - Treat AI output as untrusted

**Decision:** model output must be schema-validated and grounded in traceable sources.

**Why:**

Visa guidance is time-sensitive and consequential. The AI layer should assist reasoning and extraction, not become an unaudited policy authority.
