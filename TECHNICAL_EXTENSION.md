# Executable Technical Extension

This repository is primarily an evidence-backed architecture case study of the collaborative Go4beyond project. To make one core distributed-systems idea directly reviewable, the portfolio adds a small **2026 engineering extension** under `reference/`.

It is not presented as recovered historical source code.

## Why this extension exists

The documented architecture uses Redis/Celery-style asynchronous processing for OCR, extraction, and AI document review. Queue delivery can be retried or duplicated, so workers must not assume every message arrives exactly once.

`reference/document_job_state.py` models that boundary with:

- explicit document-job states;
- valid state transitions;
- retry semantics;
- attempt counting;
- duplicate-event idempotency through a stable event identifier;
- rejection of invalid transitions.

## State model

```text
uploaded
   |
 enqueue
   v
 queued ---- start ----> processing ---- complete ----> succeeded
                         |
                         +---- fail ----> failed ---- retry ----> queued
```

The model deliberately keeps persistence, Redis, Celery, OCR, and LLM calls out of the pure transition function. In a production implementation, the state update and idempotency record would need durable transactional storage so a process crash cannot acknowledge a message without persisting the corresponding state.

## Run locally

```bash
python -m unittest discover -s tests -v
```

The tests cover the happy path, duplicate delivery, retry after failure, invalid transitions, and invalid event identifiers.

## What this does not claim

This extension does not claim that the original prototype used this exact Python module or state schema. It exists to turn the repository's documented resilience discussion into executable, reviewable engineering logic while preserving historical attribution boundaries.
