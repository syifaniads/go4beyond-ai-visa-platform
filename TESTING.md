# Testing Strategy

The original team repository includes **prepared document fixtures for testing**. This document turns that evidence into a reviewer-friendly test strategy while distinguishing observed project artifacts from additional production-readiness recommendations.

## Original fixture evidence

Prepared documents:

https://github.com/me-dangnhatminh/apie-adv-proj/tree/main/tests/fixtures/documents

These fixtures should remain synthetic/prepared. Real applicant PII must not be used in public tests.

## Core workflow test matrix

| Workflow | What to validate |
|---|---|
| Guided intake | country/visa/nationality intent becomes valid structured state |
| Upload authorization | unauthenticated/unauthorized requests are rejected |
| Document upload | supported fixture accepted; invalid size/type rejected |
| Background processing | upload produces a queued job and reaches a terminal status |
| Extraction | expected fixture fields are extracted with traceable errors |
| Readiness analysis | criteria can identify present/missing evidence |
| Knowledge lookup | cache hit and cache miss both produce valid source-aware context |
| Streaming/status | frontend can observe progress without polling-only dependency |
| Retry | transient worker failure does not create duplicate final results |
| Deletion | document deletion removes or schedules removal of derived private artifacts |

## Document-state tests

A state-machine test is more useful than checking only individual endpoints.

```text
uploaded
  ↓
queued
  ↓
processing
  ├──→ ready
  ├──→ retryable_error → queued
  └──→ failed
```

Validate that illegal transitions are rejected, for example:

```text
failed → ready       # without a new processing attempt
uploaded → ready     # without processing
ready → processing   # without explicit re-analysis/versioning
```

## Idempotency tests

Recommended test cases:

- deliver the same job twice;
- retry after worker timeout;
- retry after DB write but before acknowledgement;
- upload the same object/checksum twice;
- request the same readiness analysis concurrently.

The assertion should be that business state remains correct even when execution is repeated.

## Knowledge-cache tests

### Hit

A semantically similar request with a fresh record should reuse the verified structured context.

### Miss

A materially different or absent record should trigger new research/structuring.

### Stale

A record beyond freshness policy should not silently behave like a valid hit.

### Source change

When a source changes, old records should be superseded or marked stale.

## Security tests

Recommended cases for synthetic fixtures:

- unsupported MIME disguised by extension;
- oversized document;
- malicious HTML/SVG content;
- path/object-key manipulation;
- access to another user's document ID;
- expired upload authorization;
- replay of an upload request;
- prompt-injection text inside an uploaded document;
- accidental PII exposure in logs/errors;
- deletion followed by retrieval attempt.

## AI-output validation

LLM output should be treated as untrusted structured data.

Tests should verify:

- schema validation;
- required fields;
- unknown/unsupported result handling;
- confidence/uncertainty behavior;
- source references where required;
- no fabricated approval guarantees;
- no raw sensitive document content copied into unrelated outputs.

## Load tests by workload class

Do not model every request as equal.

Suggested separate tests:

- concurrent dashboard/API reads;
- concurrent uploads;
- OCR worker throughput;
- LLM analysis concurrency;
- queue backlog recovery;
- vector-search latency;
- large-file object-store throughput.

## Failure-injection tests

For production readiness, intentionally test:

- Redis unavailable;
- PostgreSQL unavailable;
- object storage timeout;
- LLM unavailable;
- search provider unavailable;
- worker process killed mid-job;
- replica lag;
- stale knowledge record;
- network delay between services.

## What is source-derived vs added analysis

**Source-derived:** the team prepared document fixtures and the final presentation demonstrates upload, automated review, event-driven workers, readiness output, caching, and resilience concepts.

**Portfolio engineering analysis:** the detailed idempotency, failure-injection, state-machine, and security-test matrix above is a recommended production-readiness extension; it is not presented as proof that every test was already implemented by the team.
