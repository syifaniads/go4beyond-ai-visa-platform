# Final Presentation Evidence Notes

This document records the technical evidence from the team's **Group 6 Final Presentation - APIE Advanced Project** so a portfolio reviewer can understand what was actually presented even without opening the slide deck.

## Page-by-page evidence

### Page 1 - Go4beyond

Project framing: **Go4beyond - Distilling Global Mobility from Chaos to Clarity**.

### Pages 2-3 - Problem framing

The presentation frames three product problems:

- official visa information is fragmented and difficult to interpret consistently;
- document readiness depends on validity, completeness, and format;
- applicants lack a structured pre-submission feedback loop.

It proposes a visa assistant that converts rules into checklists, validates documents, and connects users to trusted partner knowledge.

### Page 4 - ecosystem

The platform connects:

- Applicants;
- Official Sources;
- Agency Partners;
- Admin Governance;
- Go4beyond AI Visa Platform as the intelligence/workflow layer.

### Page 5 - prototype user experience

Four-stage prototype flow:

1. AI-guided chat;
2. document upload;
3. automated review;
4. readiness score / actionable dashboard.

### Page 6 - localized MVP architecture

The slide explicitly presents a **localized / air-gapped prototype** with:

- Traefik/Nginx + Next.js gateway/UI;
- FastAPI backend;
- Redis + PostgreSQL;
- MinIO local S3-compatible object storage;
- Ollama local LLM instead of AWS Bedrock;
- SearXNG local web search instead of SerpAPI;
- Dockerized services on the prototype host.

### Page 7 - knowledge-cache flywheel

The presentation describes:

1. first query: higher-cost real-time search + LLM synthesis;
2. ingestion/embedding: cache the structured record and embed it in ChromaDB / pgvector-style storage;
3. subsequent queries: semantic similarity retrieves reusable knowledge at much lower cost.

### Page 8 - event-driven decoupling

Implemented architecture view:

- Next.js frontend;
- FastAPI modular monolith;
- main/replica database pattern in the design;
- Redis as pub/sub & broker;
- Celery background workers for OCR, AI extraction, and digitization;
- real-time frontend synchronization through SSE/WebSocket-style notifications.

### Page 9 - availability & resilience

Scale/HA direction includes:

- stateless FastAPI instances behind Nginx/Traefik;
- retry/DLQ-oriented queue resilience;
- PostgreSQL main + streaming replica and future failover planning;
- durable S3-compatible object storage.

This is a **resilience design direction**, not proof that the complete HA stack was deployed in the prototype.

### Page 10 - defense in depth

Security layers shown:

1. network boundary / TLS / VPN concept;
2. identity and access / OIDC-style managed identity direction;
3. role-based application controls;
4. data protection / object and database encryption.

### Page 11 - data classification

Examples shown in the presentation:

- Critical: passport scans, national IDs;
- High: bank statements, pay slips;
- Medium: invitation letters, study plans;
- Low: plugin metadata, public visa rules.

### Page 12 - secure passport upload flow

The slide separates:

- browser;
- FastAPI API;
- MinIO/S3 storage;
- Celery/LLM worker.

The flow uses authenticated authorization, a time-limited/presigned upload approach, direct object upload, and background/ephemeral worker processing.

### Page 13 - operations

Operational concerns shown:

- infrastructure health monitoring;
- queue/cache health;
- automated knowledge-cache invalidation;
- Redis-backed rate limiting.

### Page 14 - deployment roadmap

Three stages:

1. APIE prototype - Docker Compose on a single VPS with local dependencies;
2. scale & HA - reverse proxy/load balancing, multiple API instances, Redis/database resilience;
3. enterprise cloud-native - managed AWS-style identity, storage, queues, database, CDN, and RAG services.

### Page 15 - service ecosystem diagram

The platform coordinates applicants, partner expertise, official-source information, admin governance, storage/identity/AI infrastructure, readiness output, and partner value.

### Page 16 - centralized intelligence / moat

The closing design thesis is that reusable structured visa knowledge becomes a compounding platform asset: infrastructure and product workflows can repeatedly consume the same verified knowledge instead of rebuilding it for each applicant.

## Interpretation rule

These notes preserve the distinction between:

- **prototype evidence** (what the final presentation says ran locally), and
- **future architecture** (what the presentation proposes for scale/enterprise deployment).

See [`../../LIMITATIONS.md`](../../LIMITATIONS.md) for non-claims and architecture discrepancies.
