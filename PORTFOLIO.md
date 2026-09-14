# Portfolio Summary

## 30-second version

**Go4beyond** is a collaborative AI visa-readiness platform built for the APIE Advanced Camp Japan. The prototype combines a Next.js frontend, FastAPI backend, PostgreSQL, Redis, Celery, MinIO, local LLM inference, web-search-assisted retrieval, and a reusable knowledge cache to turn visa intent and applicant documents into structured readiness guidance.

**My role:** Group Lead / Ketua Kelompok.

I coordinated the team project, technical narrative, architecture discussion, prototype evidence, and final presentation. The project was collaborative; this personal repository is a curated case study rather than a claim of sole authorship of every source file.

## What the project demonstrates

- translating a product problem into system boundaries and data flows;
- modular-monolith API design for an MVP;
- asynchronous document processing using Redis + Celery;
- object-storage-oriented document handling;
- retrieval / RAG-oriented AI workflows;
- semantic caching / reusable knowledge records;
- real-time progress updates through SSE/event-style flows;
- privacy and security design for sensitive identity and financial documents;
- capacity planning and architecture evolution from a single-VPS prototype toward HA/cloud deployment;
- observability thinking across API, queue, database, workers, storage, and AI workloads.

## CV-ready bullet

> Led a collaborative AI visa-readiness platform project combining Next.js, FastAPI, PostgreSQL, Redis/Celery, MinIO, local LLM inference, web-search-assisted retrieval, and semantic knowledge caching; coordinated system architecture, asynchronous document-processing flows, privacy controls, scalability planning, and final prototype defense for APIE Advanced Camp Japan.

## Short website-card copy

**Go4beyond AI Visa Platform**  
AI-assisted visa readiness platform that converts fragmented requirements and applicant documents into structured checklists, automated review, readiness scoring, and contextual guidance. The localized MVP uses Next.js, FastAPI, PostgreSQL, Redis, Celery, MinIO, Ollama, SearXNG, and containerized deployment, with a documented path toward HA and managed cloud services.

**Role:** Group Lead  
**Focus:** AI platform architecture · backend/distributed workflows · security/privacy · system design

## Technical interview talking points

### Why a modular monolith?

For an MVP, a modular monolith keeps deployment and debugging simple while still enforcing domain boundaries. The project materials separate concerns such as document handling, partner/plugin rules, analysis/scoring, chat, and identity so they can be decomposed later if load or organizational ownership requires it.

### Why move OCR / AI work to background workers?

Document processing can be slow and failure-prone. Keeping it inside the synchronous request path creates long response times and poor failure isolation. Redis/Celery allows the API to acknowledge work quickly while workers perform extraction and AI tasks asynchronously.

### Why object storage instead of storing files in PostgreSQL?

Raw documents can be large and sensitive. Object storage is a better fit for file lifecycle, encryption, direct-upload patterns, and future durability/replication. PostgreSQL can keep metadata, authorization state, processing status, and relationships.

### Why a knowledge cache?

Visa-rule research is repetitive. If an expensive first query produces a structured, source-aware result, storing and embedding that record allows semantically similar future requests to reuse existing knowledge. This reduces latency and repeated search / LLM work, provided freshness and source validation are enforced.

### Where are the distributed-systems problems?

The interesting failure modes are around duplicate jobs, stale caches, worker retries, partial document processing, status synchronization, object/DB consistency, database replication lag, queue backlog, and idempotency. [SCALABILITY_RESILIENCE.md](./SCALABILITY_RESILIENCE.md) documents how the architecture should reason about them.

### What is the biggest production risk?

Sensitive applicant documents and changing official requirements. A production system must treat privacy, retention, source freshness, access control, auditability, and human review as first-class requirements. A confident AI answer is not enough.

## Evidence

See [SOURCE_EVIDENCE.md](./SOURCE_EVIDENCE.md) for the original team repository, historical implementation snapshot, test fixtures, MVP screenshots, and final-presentation evidence.
