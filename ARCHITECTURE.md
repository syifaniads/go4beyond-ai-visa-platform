# System Architecture

This document presents the architecture as a portfolio case study and separates the **localized MVP demonstrated by the team** from the **hybrid/cloud reference architecture** described in the original architecture documentation.

## 1. Localized MVP boundary

```mermaid
flowchart TB
    USER[Applicant / Partner] --> FE[Next.js Frontend]
    FE --> API[FastAPI Modular Monolith]

    API --> DB[(PostgreSQL)]
    API --> REDIS[(Redis)]
    API --> OBJ[(MinIO / S3-compatible Storage)]
    API --> SEARCH[SearXNG / Search Layer]
    API --> LLM[Ollama / Local LLM]

    REDIS --> WORKER[Celery Workers]
    WORKER --> OBJ
    WORKER --> DB
    WORKER --> LLM

    API -->|SSE / status stream| FE
```

The final presentation frames the prototype as a localized / air-gapped stack so the core experience could run without requiring the future cloud environment.

### Responsibilities

| Component | Responsibility |
|---|---|
| Next.js | applicant/partner UI, chat, upload workflow, readiness results |
| FastAPI | synchronous API surface, business orchestration, access checks, status endpoints |
| PostgreSQL | relational state: users/projects/plugins/document metadata/results |
| Redis | cache, broker/pub-sub behavior, rate-limit state |
| Celery | asynchronous OCR/extraction/digitization/AI jobs |
| MinIO | raw document/object storage using an S3-compatible interface |
| Ollama | localized LLM inference for prototype AI workflows |
| SearXNG | localized web-search integration for newly researched visa rules |
| Vector cache | semantic retrieval of previously structured knowledge records |

## 2. Logical domains

The system is easier to reason about as a modular monolith with domain boundaries rather than a collection of unrelated endpoints.

```text
application/
├── identity/        # authentication context, roles, user/partner identity
├── projects/        # visa-readiness workspace and intent
├── documents/       # metadata, upload state, document lifecycle
├── plugins/         # partner criteria, checklists, visa-specific knowledge
├── analysis/        # readiness scoring, extraction, gap analysis
├── knowledge/       # source research, semantic cache, retrieval
├── chat/            # contextual Q&A and streaming responses
└── admin/           # governance and partner/plugin approval
```

The exact source-tree names in the original implementation may differ. The structure above is a **logical architecture view**, not a claim that the repository used these exact folder names.

## 3. Document-processing flow

```mermaid
sequenceDiagram
    actor U as Applicant
    participant FE as Next.js
    participant API as FastAPI
    participant DB as PostgreSQL
    participant OBJ as MinIO / Object Storage
    participant R as Redis
    participant W as Celery Worker

    U->>FE: Select document
    FE->>API: Request authorized upload
    API->>API: Authenticate + authorize
    API->>DB: Create document metadata/status
    API-->>FE: Upload authorization / object key
    FE->>OBJ: Direct document upload
    OBJ-->>FE: Upload complete
    FE->>API: Confirm / continue workflow
    API->>R: Enqueue processing job
    R->>W: Deliver background task
    W->>OBJ: Read document
    W->>W: OCR / extraction / validation
    W->>DB: Store structured result + status
    W->>R: Publish status update
    API-->>FE: SSE / progress update
```

The final presentation specifically highlights a presigned/direct-upload style flow to keep large files away from the API data path and to separate storage from compute.

## 4. Readiness-analysis flow

```mermaid
sequenceDiagram
    actor U as Applicant
    participant FE as Frontend
    participant API as API
    participant DB as PostgreSQL
    participant K as Knowledge Cache
    participant S as Search / Official Sources
    participant L as LLM

    U->>FE: Request readiness review
    FE->>API: Analyze project
    API->>DB: Load project, document metadata, partner criteria
    API->>K: Search reusable visa knowledge
    alt reusable knowledge exists and is fresh
        K-->>API: Structured knowledge context
    else cache miss / stale knowledge
        API->>S: Research current sources
        S-->>API: Source material
        API->>L: Structure / summarize source material
        L-->>API: Structured knowledge record
        API->>K: Store + embed record
    end
    API->>L: Evaluate documents against criteria + context
    L-->>API: Gaps / explanations / suggested actions
    API->>DB: Persist analysis result
    API-->>FE: Stream / return result
```

## 5. Event-driven decoupling

Long-running tasks are moved away from the request/response path. The architecture benefits are:

- lower user-facing latency;
- independent worker scaling;
- explicit retries;
- queue backlog visibility;
- better fault isolation;
- a path toward DLQs and durable managed messaging later.

The key production requirement is **idempotency**: a retried document-processing job should not create duplicate analysis records or corrupt document state.

## 6. Target hybrid/cloud architecture

The original team architecture README describes a broader **on-premise + AWS** design:

```mermaid
flowchart LR
    subgraph ONP[On-prem / Core]
        FE2[Web Frontend]
        API2[Modular API]
        PG[(PostgreSQL Primary)]
        REP[(Read Replica)]
        RD[(Redis)]
        MON[Zabbix]
    end

    subgraph AWS[AWS / Managed Services]
        ID[Cognito]
        S3[S3]
        Q[SNS / SQS]
        FN[Lambda]
        BR[Bedrock]
        KB[Bedrock Knowledge Base]
        CW[CloudWatch]
    end

    FE2 --> API2
    API2 --> PG
    PG --> REP
    API2 --> RD
    API2 --> S3
    API2 --> BR
    S3 --> Q --> FN --> KB
    ID --> FE2
    ONP <-->|Site-to-Site VPN| AWS
```

That reference architecture is valuable for discussing scale, managed identity, durable object storage, event-driven processing, and RAG infrastructure. It is **not presented here as fully deployed prototype infrastructure**.

## 7. Architecture discrepancy preserved intentionally

The current README in the original team repository uses **Flask** in its hybrid architecture example. The final prototype presentation identifies **FastAPI** as the localized MVP backend.

This portfolio treats them as different artifacts:

- final prototype evidence → FastAPI;
- current architecture document → Flask reference implementation language;
- product/domain architecture → framework-independent.

A senior reviewer should not have to guess which one actually ran in the prototype.

## 8. Data ownership

A production implementation should keep the following separation:

- **PostgreSQL:** metadata, relationships, roles, project state, processing status, analysis results;
- **Object storage:** raw uploaded documents;
- **Redis:** ephemeral cache/queue/rate-limit/pub-sub state;
- **Vector store:** derived embeddings and structured knowledge references;
- **LLM context:** minimum necessary excerpts, not uncontrolled copies of all applicant data.

See [SECURITY_PRIVACY.md](./SECURITY_PRIVACY.md) for the security implications.
