# Day 04 - Kafka Topic Topology

    | Topic | Purpose |
| --- | --- |
| transactions.raw.v1 | Raw payment attempts from API gateway and channel adapters. |
| transactions.validated.v1 | Canonical validated transaction events. |
| transactions.enriched.v1 | Events enriched with customer, account, merchant, device, and feature data. |
| rules.evaluated.v1 | Explainable rule evaluation results. |
| ml.anomaly-scores.v1 | Model inference scores and feature attribution. |
| graph.signals.v1 | Graph risk signals such as shared device and mule cluster risk. |
| risk.decisions.v1 | Final approve, review, block, or step-up decisions. |
| cases.events.v1 | Case lifecycle events and analyst decisions. |
| notifications.requests.v1 | Outbound notification requests. |
| audit.events.v1 | Immutable security, compliance, and decision audit events. |
| fraud.dlq.v1 | Poison events and schema validation failures. |

    ## Topic Standards
    - Topic names use `<domain>.<event-family>.v<major>` and major versioning for breaking schema changes.
    - Partition keys use `transaction_id` for transaction flow ordering and `customer_id` for profile/behavior aggregations.
    - Production topics use replication factor 3, minimum in-sync replicas 2, and idempotent producers.
    - Retention is 7 days for high-volume operational topics, 90 days for case topics, and policy-driven immutable retention for audit exports.
