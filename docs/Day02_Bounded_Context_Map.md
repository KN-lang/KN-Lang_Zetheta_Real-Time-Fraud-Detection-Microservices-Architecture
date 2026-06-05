# Day 02 - Bounded Context Map

    ## Contexts
    | Bounded Context | Owned Services | Primary Data | Integration Style |
| --- | --- | --- | --- |
| Transaction Processing | transaction-ingestion | Transaction envelope, idempotency records | REST ingress and Kafka publish |
| Customer Intelligence | customer-profile, feature-store | Customer, account, device, merchant, derived features | gRPC lookup and Kafka enrichment |
| Fraud Signal Generation | rule-engine, anomaly-detection, graph-analysis | Rule hits, anomaly scores, graph signals | Kafka consumers/producers and gRPC model calls |
| Decisioning | risk-scoring | Decision policy, score weights, outcome history | Kafka aggregation and decision events |
| Investigation | case-management | Cases, evidence, analyst decisions | Kafka event subscription and REST API |
| Engagement | notification | Message templates and delivery state | Kafka command events |
| Governance | audit-compliance | Audit log, evidence bundles, retention policies | Kafka sink and compliance APIs |

    ## Integration Rules
    - Contexts communicate through Kafka events for state changes and gRPC for low-latency query-style collaboration.
    - Each service owns its operational store; shared databases are prohibited.
    - Cardholder data is tokenized before analytical contexts consume events.
    - Audit-compliance subscribes to all material decision and administrative events.
