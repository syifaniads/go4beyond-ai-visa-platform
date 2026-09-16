"""Deterministic reference model for asynchronous document-processing jobs.

This module is a 2026 portfolio engineering extension derived from the
architecture documented in this repository. It is intentionally small and
framework-agnostic: the original team implementation is not replaced or
retroactively claimed here.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum


class JobState(str, Enum):
    UPLOADED = "uploaded"
    QUEUED = "queued"
    PROCESSING = "processing"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


class JobEvent(str, Enum):
    ENQUEUE = "enqueue"
    START = "start"
    COMPLETE = "complete"
    FAIL = "fail"
    RETRY = "retry"


class InvalidTransition(ValueError):
    """Raised when an event is invalid for the current job state."""


_TRANSITIONS: dict[tuple[JobState, JobEvent], JobState] = {
    (JobState.UPLOADED, JobEvent.ENQUEUE): JobState.QUEUED,
    (JobState.QUEUED, JobEvent.START): JobState.PROCESSING,
    (JobState.PROCESSING, JobEvent.COMPLETE): JobState.SUCCEEDED,
    (JobState.PROCESSING, JobEvent.FAIL): JobState.FAILED,
    (JobState.FAILED, JobEvent.RETRY): JobState.QUEUED,
}


@dataclass(frozen=True, slots=True)
class DocumentJob:
    document_id: str
    state: JobState = JobState.UPLOADED
    attempt: int = 0
    last_event_id: str | None = None


def apply_event(job: DocumentJob, event: JobEvent, event_id: str) -> DocumentJob:
    """Apply one state transition with duplicate-event idempotency.

    The same ``event_id`` can be delivered more than once by an at-least-once
    queue. Re-delivery returns the current value unchanged instead of applying
    the transition twice.
    """

    if not event_id.strip():
        raise ValueError("event_id must be non-empty")

    if job.last_event_id == event_id:
        return job

    target = _TRANSITIONS.get((job.state, event))
    if target is None:
        raise InvalidTransition(f"cannot apply {event.value!r} from {job.state.value!r}")

    next_attempt = job.attempt + 1 if event is JobEvent.START else job.attempt
    return replace(
        job,
        state=target,
        attempt=next_attempt,
        last_event_id=event_id,
    )
