import unittest

from reference.document_job_state import (
    DocumentJob,
    InvalidTransition,
    JobEvent,
    JobState,
    apply_event,
)


class DocumentJobStateTests(unittest.TestCase):
    def test_happy_path_reaches_succeeded(self) -> None:
        job = DocumentJob(document_id="doc-001")
        job = apply_event(job, JobEvent.ENQUEUE, "evt-1")
        job = apply_event(job, JobEvent.START, "evt-2")
        job = apply_event(job, JobEvent.COMPLETE, "evt-3")

        self.assertEqual(job.state, JobState.SUCCEEDED)
        self.assertEqual(job.attempt, 1)

    def test_duplicate_event_is_idempotent(self) -> None:
        job = DocumentJob(document_id="doc-002")
        queued = apply_event(job, JobEvent.ENQUEUE, "evt-1")
        duplicate = apply_event(queued, JobEvent.ENQUEUE, "evt-1")

        self.assertEqual(duplicate, queued)

    def test_failed_job_can_retry(self) -> None:
        job = DocumentJob(document_id="doc-003")
        job = apply_event(job, JobEvent.ENQUEUE, "evt-1")
        job = apply_event(job, JobEvent.START, "evt-2")
        job = apply_event(job, JobEvent.FAIL, "evt-3")
        job = apply_event(job, JobEvent.RETRY, "evt-4")
        job = apply_event(job, JobEvent.START, "evt-5")

        self.assertEqual(job.state, JobState.PROCESSING)
        self.assertEqual(job.attempt, 2)

    def test_invalid_transition_is_rejected(self) -> None:
        job = DocumentJob(document_id="doc-004")
        with self.assertRaises(InvalidTransition):
            apply_event(job, JobEvent.COMPLETE, "evt-invalid")

    def test_empty_event_id_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            apply_event(DocumentJob(document_id="doc-005"), JobEvent.ENQUEUE, "  ")


if __name__ == "__main__":
    unittest.main()
