# Day 04 - Kafka Topic Topology

Kafka is the backbone of ShieldPay. All material fraud decisions, enrichment results, investigation events, notifications, and audit records flow through schema-governed Kafka topics. The topic names below are the canonical Project 1C names; schema subjects use Protobuf package versions for compatibility governance.

## Canonical Topics

| Topic | Partitions | Replication Factor | Retention | Key Strategy | Producer Services | Consumer Groups |
| --- | ---: | ---: | --- | --- | --- | --- |
| `fraud.transactions.raw` | 12 | 3 | 24 hours | `transaction_id` | API gateway, transaction-ingestion | `transaction-validator`, `audit-raw-sink` |
| `fraud.transactions.enriched` | 24 | 3 | 7 days | `transaction_id` | customer-profile, feature-store | `rule-engine`, `anomaly-detection`, `graph-analysis`, `audit-enriched-sink` |
| `fraud.rule.results` | 24 | 3 | 14 days | `transaction_id` | rule-engine | `risk-scoring`, `rule-metrics-projector`, `audit-rule-sink` |
| `fraud.anomaly.scores` | 24 | 3 | 14 days | `transaction_id` | anomaly-detection | `risk-scoring`, `model-monitoring`, `audit-ml-sink` |
| `fraud.graph.signals` | 12 | 3 | 30 days | `customer_id` then `transaction_id` | graph-analysis | `risk-scoring`, `graph-monitoring`, `audit-graph-sink` |
| `fraud.risk.decisions` | 24 | 3 | 90 days | `transaction_id` | risk-scoring | `case-management`, `notification`, `dashboard-projector`, `audit-decision-sink` |
| `fraud.notifications` | 6 | 3 | 7 days | `recipient_id` | notification, case-management, risk-scoring | `sms-dispatcher`, `email-dispatcher`, `push-dispatcher`, `webhook-dispatcher` |
| `fraud.audit.events` | 12 | 3 | 7 years or regulatory policy | `correlation_id` | all services | `audit-compliance-worm-sink`, `siem-forwarder`, `regulatory-report-projector` |

## Supporting Topics

| Topic | Purpose | Retention | Consumer Groups |
| --- | --- | --- | --- |
| `fraud.transactions.validated` | Canonical valid transaction event before enrichment. | 7 days | `profile-enricher`, `feature-enricher`, `audit-validated-sink` |
| `fraud.cases.events` | Case lifecycle, assignment, evidence, and analyst outcomes. | 365 days | `case-dashboard-projector`, `notification`, `audit-case-sink` |
| `fraud.retry.5s` | First retry lane for transient dependency failures. | 24 hours | `retry-dispatcher` |
| `fraud.retry.1m` | Second retry lane for repeated transient failures. | 24 hours | `retry-dispatcher` |
| `fraud.retry.15m` | Final retry lane before DLQ. | 72 hours | `retry-dispatcher` |
| `fraud.dlq` | Poison events, schema failures, exhausted retries, and unrecoverable processing failures. | 30 days | `dlq-triage`, `audit-dlq-sink` |

## Versioning and Compatibility

- Protobuf message versions live in package names such as `shieldpay.events.v1`.
- Breaking changes create a new message/package version and, when required, a new topic suffix such as `fraud.risk.decisions.v2`.
- Schema Registry compatibility is `BACKWARD_TRANSITIVE` for production subjects.
- Producers must register schemas in CI before deployment.
- Consumers must tolerate unknown Protobuf fields and must not assume field order.

## Retry, DLQ, and Poison Message Handling

1. Consumers retry in memory for short transient errors with exponential backoff and jitter.
2. Events that still fail are republished to `fraud.retry.5s`, then `fraud.retry.1m`, then `fraud.retry.15m`.
3. Events are sent to `fraud.dlq` after retry exhaustion, schema rejection, invalid idempotency state, or unrecoverable business validation failure.
4. DLQ records include original topic, partition, offset, schema subject, exception class, stack hash, service version, `correlation_id`, and redacted payload.
5. Poison messages require an incident ticket, owner approval, replay offset range, and audit event before reprocessing.

## Operational Standards

- Production topics use replication factor 3 and `min.insync.replicas=2`.
- Producers use idempotence and `acks=all`.
- Consumers commit offsets only after successful side effects or idempotent write confirmation.
- Topic creation is managed as infrastructure-as-code; manual console topic creation is prohibited outside emergency break-glass procedures.
