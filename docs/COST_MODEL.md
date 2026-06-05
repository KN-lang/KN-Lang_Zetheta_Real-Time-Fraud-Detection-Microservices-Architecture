# Cost Model

## Scaling Assumptions

- Average traffic: 500 transactions per second.
- Peak traffic: 5,000 transactions per second.
- Monthly volume: 1.3 billion transactions.
- Production runs active-active across two regions.
- Kafka retention: 7-14 days for high-volume topics, 90 days for decisions, long-term audit export to object storage.

## Monthly Cloud Estimate

| Cost Area | Assumption | Estimated Monthly Cost |
| --- | --- | ---: |
| Kubernetes compute | 80-120 vCPU average across services and regions | USD 6,000-10,000 |
| Kafka | Managed or self-managed brokers with cross-zone replication | USD 8,000-15,000 |
| PostgreSQL | HA databases for transaction, rule, case, and scoring stores | USD 4,000-8,000 |
| Redis | HA online feature and cache clusters | USD 2,000-5,000 |
| Neo4j | Graph cluster sized for relationship traversal | USD 5,000-12,000 |
| Elasticsearch/TimescaleDB | Logs, evidence search, metrics | USD 4,000-9,000 |
| Object storage | Offline features, audit evidence, model artifacts | USD 1,000-3,000 |
| Observability and security | Prometheus/Grafana, tracing, WAF, KMS, secrets | USD 3,000-7,000 |
| Network and data transfer | Inter-region replication and egress | USD 2,000-6,000 |
| Total | Production estimate | USD 35,000-75,000 |

## Cost per Transaction

At 1.3 billion transactions/month:

- Low estimate: USD 35,000 / 1.3B = about USD 0.000027 per transaction.
- High estimate: USD 75,000 / 1.3B = about USD 0.000058 per transaction.

## Cost Controls

- Autoscale stateless services on CPU, latency, and Kafka lag.
- Keep raw high-volume topic retention short and export only required evidence.
- Use Redis TTLs for velocity windows and online features.
- Prune transient graph relationships.
- Downsample time-series metrics after hot operational windows.
- Run challenger models in shadow only for controlled cohorts.

## Build vs Buy Analysis

| Capability | Build | Buy / Managed Service | Recommendation |
| --- | --- | --- | --- |
| Fraud decision logic | Differentiated rules, scoring, graph topology, case evidence | Generic fraud SaaS may limit explainability and customization | Build core decisioning. |
| Kafka operations | Full control but high operational burden | Managed Kafka reduces toil | Prefer managed Kafka for production unless cost or residency blocks it. |
| API gateway | Custom gateway is costly | Kong or managed gateway is mature | Buy/use managed gateway. |
| Observability | Custom stack is expensive | Prometheus/Grafana/OpenTelemetry ecosystem is standard | Use standard tooling and managed storage where practical. |
| ML platform | Custom model logic needed | Managed registry/serving can reduce platform work | Build model features and governance, buy managed registry where allowed. |
