# Day 02 - Service Decomposition Table

    | Service | Responsibility | Store | Consumes | Produces |
| --- | --- | --- | --- | --- |
| transaction-ingestion | Accepts external payment events, validates idempotency, and publishes canonical transaction events. | PostgreSQL | External API | transactions.validated.v1 |
| customer-profile | Maintains customer, account, device, merchant, and consent-aware profile features. | PostgreSQL + Redis | transactions.validated.v1 | transactions.enriched.v1 |
| feature-store | Serves low-latency online features and manages offline training datasets. | Redis + S3/Parquet | transactions.enriched.v1 | Feature responses |
| rule-engine | Evaluates configurable fraud rules and emits explainable rule hits. | PostgreSQL | transactions.enriched.v1 | rules.evaluated.v1 |
| anomaly-detection | Serves ML models for abnormal amount, behavior, merchant, device, and session patterns. | Model registry + Redis | transactions.enriched.v1 | ml.anomaly-scores.v1 |
| graph-analysis | Synchronizes entity relationships into Neo4j and computes fraud ring signals. | Neo4j | transactions.enriched.v1 | graph.signals.v1 |
| risk-scoring | Combines rules, ML, graph, and profile signals into final decisions. | PostgreSQL + Redis | rules/ml/graph topics | risk.decisions.v1 |
| case-management | Creates investigation cases, supports analyst workflow, and captures decisions. | PostgreSQL | risk.decisions.v1 | cases.events.v1 |
| notification | Sends customer, merchant, and operations notifications through approved channels. | PostgreSQL | risk.decisions.v1, cases.events.v1 | notifications.requests.v1 |
| audit-compliance | Stores immutable audit records, evidence bundles, and compliance reports. | WORM object store + PostgreSQL | All governed topics | audit.events.v1 |

    ## Sizing Boundary
    The design uses ten services, satisfying the Project 1C requirement for 8-12 services while keeping deployable boundaries aligned to business capabilities.
