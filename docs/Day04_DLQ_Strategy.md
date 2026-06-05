# Day 04 - DLQ Strategy

ShieldPay treats DLQ handling as an operational workflow, not a hidden consumer failure.

## Failure Classes

| Failure Class | First Action | Final Handling |
| --- | --- | --- |
| Schema validation failure | Reject and publish redacted record to `fraud.dlq`. | Fix producer/schema or create migration replay. |
| Transient dependency failure | Retry with exponential backoff and jitter. | Move through `fraud.retry.5s`, `fraud.retry.1m`, `fraud.retry.15m`. |
| Poison message | Stop repeated processing by stack hash and event ID. | Quarantine in `fraud.dlq` and open incident ticket. |
| Authorization or tenant violation | Emit security audit event. | Do not replay until security owner approves. |
| Compliance hold | Preserve payload hash and evidence metadata. | Route to audit-compliance review queue. |

## DLQ Payload Metadata

DLQ events include original topic, partition, offset, schema subject, schema version, consumer group, service version, exception class, stack hash, retry count, first failure time, last failure time, `transaction_id`, `correlation_id`, and a redacted payload.

## Replay Controls

Replays require change approval, signed runbook execution, bounded offsets, owner approval, and a dry-run count. All replay commands emit `AuditEvent` records with operator identity, offset range, reason, and outcome.
