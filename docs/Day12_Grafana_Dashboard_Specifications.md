# Day 12 - Grafana Dashboard Specifications

ShieldPay requires four primary Grafana dashboards for operational and fraud-risk review.

## Transaction Processing Dashboard

- Transactions per second by merchant, channel, country, and region.
- API p50/p95/p99 latency for gateway and `transaction-ingestion`.
- Kafka produce latency and broker health.
- Idempotency duplicate rate and schema rejection rate.
- Decision outcome distribution: approve, step-up, review, block.

## Fraud Detection Dashboard

- Rule hit rate by rule ID, version, category, and merchant.
- ML anomaly score distribution, PSI, KS, model version, and drift state.
- Graph signal volume, shared device/IP detections, mule cluster counts.
- Confirmed fraud rate, false-positive rate, and value at risk detected.
- Top reasons contributing to `BLOCK` and `REVIEW`.

## Case Management Dashboard

- Open cases by priority, queue, SLA age, and analyst.
- Case creation rate from risk decisions.
- Analyst decision distribution and overturn rate.
- Average time to first action and time to closure.
- Evidence attachment and audit completeness rate.

## Infrastructure Dashboard

- Kubernetes pod readiness, restart count, CPU, memory, and HPA state.
- Kafka broker health, partitions under replicated, consumer lag, and disk usage.
- PostgreSQL, Redis, Neo4j, Elasticsearch, and TimescaleDB health.
- Istio request rate, mTLS policy state, 4xx/5xx rates, and circuit breaker ejections.
- OpenTelemetry collector throughput and dropped spans.
