# 11. Kafka Topic Topology

## Overview
Kafka is the backbone of the Real-Time Fraud Detection Platform. Topics are partitioned to enable parallel processing and horizontal scaling.

## Topics
| Topic Name | Purpose | Producers | Consumers |
| :--- | :--- | :--- | :--- |
| `transactions` | Raw transaction events. | Ingestor Service | Rules, Anomaly, Graph |
| `rule-hits` | Alerts from the Rule Engine. | Rule Engine Service | Risk Scorer |
| `anomaly-alerts` | Alerts from Anomaly Detector. | Anomaly Service | Risk Scorer |
| `graph-alerts` | Alerts from Graph Analyzer. | Graph Service | Risk Scorer |
| `risk-decisions` | Final fraud decisions. | Risk Scorer | Case Manager, Gateway |
| `case-updates` | Updates on fraud cases. | Case Manager | Audit Log, ML Trainer |
| `audit-log` | Immutable record of all events. | All Services | Long-term Storage (S3) |

## Partitioning Strategy
- **`transactions`**: Partitioned by `customer_id` to ensure that all transactions for a single customer are processed in order (important for velocity rules).
- **All other topics**: Partitioned by `transaction_id` for even distribution.

## Retention
- **Detection Topics**: 7 days retention for debugging and replay.
- **Audit Log**: Permanent retention in cold storage.
