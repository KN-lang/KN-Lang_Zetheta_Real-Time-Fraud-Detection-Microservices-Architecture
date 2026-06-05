# Day 04 - Dead-Letter Queue Strategy

## Failure Classes
- Schema validation failure: publish to `fraud.dlq.v1` with schema subject, version, and validation error.
- Transient dependency failure: retry with exponential backoff and jitter before DLQ handoff.
- Poison message: quarantine after max attempts and open an operational case.
- Compliance block: route to audit-compliance for evidence retention and manual approval.

## Replay Controls
Replays require change approval, signed runbook execution, bounded offsets, and a dry-run count. All replay commands emit `AuditEvent` records with operator identity, offset range, reason, and outcome.
