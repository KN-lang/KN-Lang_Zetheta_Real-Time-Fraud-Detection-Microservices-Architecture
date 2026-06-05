# Day 03 - Service SLA Table

    | Service | Availability | P95 Latency | RPO/RTO | Scaling Trigger |
| --- | --- | --- | --- | --- |
| transaction-ingestion | 99.99% | < 80 ms | 0 min / 15 min | CPU > 65% or request rate |
| customer-profile | 99.95% | < 40 ms | 5 min / 30 min | Redis miss rate and gRPC latency |
| feature-store | 99.95% | < 25 ms | 5 min / 30 min | Online feature QPS |
| rule-engine | 99.95% | < 35 ms | 0 min / 30 min | Kafka lag and eval latency |
| anomaly-detection | 99.9% | < 70 ms | 15 min / 60 min | GPU/CPU inference queue |
| graph-analysis | 99.9% | < 120 ms | 15 min / 60 min | Neo4j query latency |
| risk-scoring | 99.99% | < 50 ms | 0 min / 15 min | Signal aggregation lag |
| case-management | 99.9% | < 200 ms | 15 min / 60 min | Analyst API latency |
| notification | 99.5% | < 2 s | 30 min / 4 hr | Delivery queue backlog |
| audit-compliance | 99.99% | < 100 ms | 0 min / 30 min | Audit sink lag |
