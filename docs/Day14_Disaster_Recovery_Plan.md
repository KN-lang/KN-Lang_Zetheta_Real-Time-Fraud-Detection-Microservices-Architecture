# Day 14 - Disaster Recovery Plan

## Objectives

| Capability | RPO | RTO |
| --- | ---: | ---: |
| Transaction ingestion and Kafka decision path | 0-1 minute | 15 minutes |
| Risk-scoring and audit-compliance | 0-1 minute | 15 minutes |
| Case-management | 15 minutes | 60 minutes |
| Feature-store online cache | 15 minutes | 30 minutes |
| Graph-analysis | 30 minutes | 2 hours |
| Dashboards and analytics | 60 minutes | 4 hours |

## Architecture

Production uses multi-region Kubernetes clusters, replicated Kafka, replicated schema registry, database replicas, object storage replication, and global traffic management. Audit evidence is written to immutable object storage with cross-region replication.

## Recovery Sequence

1. Freeze rule and model changes.
2. Confirm incident scope and affected region.
3. Shift gateway traffic to healthy region.
4. Validate Kafka topic health and consumer group offsets.
5. Promote database replicas if required.
6. Replay bounded offsets for affected projectors.
7. Run synthetic transaction, decision, case, notification, and audit probes.
8. Record actions and evidence in audit-compliance.

## Chaos Engineering

Minimum quarterly chaos experiments:

1. Kill `transaction-ingestion` pods during peak synthetic load.
2. Inject Kafka broker failure and validate replication and consumer recovery.
3. Add 500 ms latency to `feature-store` and verify risk-scoring fallback.
4. Make Neo4j unavailable and verify graph-signal degradation to review policy.
5. Fail notification provider and verify queued retry without decision-path impact.
6. Expire a service certificate in staging and verify Istio mTLS alerting.
