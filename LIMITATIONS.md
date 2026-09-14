# Limitations & Non-Claims

This document exists so the portfolio is technically credible to a senior reviewer.

## 1. Prototype vs enterprise design

The final presentation contains both a localized MVP and a future enterprise architecture. The following should not be read as confirmed production deployments unless source evidence explicitly proves them:

- AWS Cognito;
- Amazon Bedrock;
- Bedrock Knowledge Base;
- SNS/SQS/Lambda event processing;
- CloudFront;
- multi-AZ PostgreSQL;
- Patroni automated failover;
- Redis Sentinel / managed Redis HA;
- multi-node object storage;
- complete cloud monitoring stack.

They are architecture/roadmap elements.

## 2. Backend-framework discrepancy

The final prototype presentation identifies **FastAPI** for the localized MVP, while the current original-repository architecture README uses **Flask** in its hybrid reference architecture.

The portfolio preserves both artifacts rather than rewriting history. Product/domain architecture is treated as framework-independent where possible.

## 3. Visa-readiness score

A readiness score is a product-assistance output, not an official probability of visa approval.

A production system should expose:

- underlying criteria;
- missing evidence;
- source provenance;
- confidence/uncertainty;
- data freshness;
- explicit disclaimers.

The platform must not present itself as an immigration authority.

## 4. Problem-framing statistics

The final presentation uses figures such as time spent researching requirements and a rejection-risk framing from previous team research. This portfolio does not treat those figures as independently verified market statistics unless the supporting research is separately provided and cited.

## 5. AI reliability

An LLM can:

- hallucinate requirements;
- misread documents;
- misclassify extracted fields;
- produce outdated policy guidance;
- overstate confidence.

Production use therefore requires source provenance, freshness controls, structured validation, and human escalation.

## 6. RAG is not automatically trustworthy

Retrieval improves grounding but does not guarantee correctness. Failure modes include:

- stale source records;
- wrong document chunks;
- missing official sources;
- prompt injection inside retrieved content;
- low-quality embeddings;
- incorrectly summarized rules.

## 7. Cache correctness

A semantic cache creates operational risk when legal/administrative rules change. Cached entries need verification timestamps, source versioning, invalidation, and a stale-state policy.

## 8. Security controls

The presentation describes a defense-in-depth model and future cloud controls. This should not be interpreted as proof that every listed security mechanism was enabled in the prototype.

## 9. High-availability behavior

The roadmap discusses load balancing, replica databases, resilient queues, and failover. A production system still needs tested procedures for:

- database promotion/failback;
- split-brain avoidance;
- queue redelivery;
- idempotent workers;
- cache failure;
- storage outage;
- backup restore;
- disaster recovery.

Architecture diagrams alone do not prove those behaviors.

## 10. Test documents

Only synthetic/prepared fixtures belong in public source control. Any real applicant PII must remain outside this portfolio.

## 11. Collaborative authorship

Go4beyond is a group project. This repository documents the complete engineering story and the portfolio owner's Group Lead role, but it does not claim sole authorship of the original implementation.

## 12. Missing source-level attribution

The shared repository is hosted under a teammate account and the portfolio evidence supplied for this curation does not provide a complete per-file ownership matrix. Therefore this repository avoids assigning individual ownership to specific original modules without separate evidence.

## 13. What this portfolio adds

Some sections of this personal repository - especially explicit idempotency guidance, operational metrics, data-minimization recommendations, and production hardening checklists - are **portfolio engineering analysis derived from the team architecture**, not claims that every recommendation was already implemented.

Those additions are included to show how the prototype would be evaluated for production readiness while keeping implemented-vs-recommended boundaries explicit.
