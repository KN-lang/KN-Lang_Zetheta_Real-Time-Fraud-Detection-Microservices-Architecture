# Day 03 - Polyglot Persistence Strategy

ShieldPay uses multiple persistence technologies because fraud detection has distinct workload shapes: transactional state, low-latency feature lookup, graph traversal, log/search analysis, time-series monitoring, and immutable evidence retention.

## Persistence Map

| Technology | Owning Services | Data Stored | Why It Fits |
| --- | --- | --- | --- |
| PostgreSQL | transaction-ingestion, rule-engine, risk-scoring, case-management | Idempotency records, rule metadata, decision policy, cases, analyst workflow | Strong consistency, relational constraints, transactions, mature operational tooling. |
| Redis | customer-profile, feature-store, risk-scoring | Online features, velocity counters, idempotency cache, short-lived risk score cache | Sub-millisecond reads, TTL support, atomic counters for velocity rules. |
| Neo4j | graph-analysis | Customers, cards, accounts, devices, IPs, phones, emails, merchants, addresses, transaction paths | Native graph traversal, shortest-path queries, centrality, fraud ring detection. |
| Elasticsearch | audit-compliance, case-management, observability projectors | Searchable case evidence, redacted logs, analyst search, investigation timelines | Full-text search, faceting, fast evidence discovery, SOC integration. |
| TimescaleDB | observability projectors, dashboard metrics | Transaction throughput, fraud rates, model drift metrics, SLA time series | SQL time-series analytics, retention policies, downsampling, operational dashboards. |
| Object Storage | feature-store, audit-compliance, ML operations | Offline feature datasets, model artifacts, immutable evidence bundles, reports | Low-cost retention, versioned artifacts, WORM policies for compliance. |

## Ownership Rules

- Services own their operational schema; no service performs direct writes into another service's database.
- Cross-service views are built from Kafka events through projectors.
- Sensitive cardholder data is tokenized before it reaches fraud analytics stores.
- All stores emit backup, restore, retention, and access evidence into `fraud.audit.events`.

## Consistency Model

Transaction decisioning is near-real-time and event-driven. `risk-scoring` tolerates eventually consistent graph and ML signals by applying timeout policies. If a non-critical signal misses the decision window, the service records the missing signal and applies a conservative `REVIEW` fallback for high-value or high-risk transactions.
