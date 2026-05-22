# 11. Kafka Topic Topology

## Overview
Kafka is the target production backbone of the Real-Time Fraud Detection Platform. In the local prototype, real Kafka is not deployed. The implementation uses an in-process `EventBus` that publishes the same logical event types to Kafka-style topic names and writes `data/output/event_log.jsonl` for audit and demonstration.

This keeps the prototype runnable without Docker or a Kafka broker while preserving a direct migration path to Kafka.

## Local EventBus Topics
| Topic Name | Purpose | Producers | Consumers |
| :--- | :--- | :--- | :--- |
| `transaction.events` | Raw transaction events. | Transaction Generator/Ingestor | Rules, Anomaly, Graph |
| `rule.hit.events` | Alerts from the Rule Engine. | Rule Engine Service | Risk Scorer |
| `anomaly.alert.events` | Alerts from Anomaly Detector. | Anomaly Service | Risk Scorer |
| `graph.alert.events` | Alerts from Graph Analyzer. | Graph Service | Risk Scorer |
| `risk.score.events` | Final scores and decisions. | Risk Scorer | Case Manager, Gateway |
| `fraud.case.events` | Fraud case creation events. | Case Manager | Audit Log, Analyst Workflow |
| `audit.events` | Immutable record of event publications. | EventBus/All Services | Long-term Storage |

## Production Kafka Mapping
The local topic names can be carried directly into Kafka. A production deployment would replace the in-process EventBus with Kafka producers and consumers while preserving the event envelope:

- `event_id`
- `event_type`
- `timestamp`
- `correlation_id`
- `source_service`
- `payload`

## Partitioning Strategy
- **`transaction.events`**: Partition by `customer_id` to keep customer transaction order for velocity rules.
- **Signal and score topics**: Partition by `transaction_id` or `correlation_id`.
- **Graph topics**: Partition by entity key when graph updates become incremental.

## Retention
- **Local prototype**: `event_log.jsonl` is overwritten per run and intended for demonstration only.
- **Production detection topics**: 7 days retention for debugging and replay.
- **Production audit events**: Permanent retention in cold storage.
