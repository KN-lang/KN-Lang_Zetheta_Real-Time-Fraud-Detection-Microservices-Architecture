# 17. FMEA (Failure Mode and Effects Analysis)

| Failure Mode | Impact | Severity | Mitigation |
| :--- | :--- | :--- | :--- |
| **Kafka Cluster Down** | Complete system halt. | Critical | Multi-AZ deployment; cluster replication; persistent local buffering in ingestors. |
| **Rule Engine Latency Spike** | Delayed fraud decisions. | High | Auto-scaling based on consumer lag; circuit breakers; optimized evaluation logic. |
| **Graph DB Connection Failure** | Loss of graph-based signals. | Medium | Risk Scorer uses "default safe" score; fallback to rule-only mode; retry logic. |
| **Stale Customer Baselines** | Reduced anomaly detection accuracy. | Medium | Automated daily retraining jobs; monitoring of model drift. |
| **Database Corruption** | Loss of case data / audit trail. | High | Multi-region backups; WAL-G for Postgres; Point-in-time recovery. |
| **PII Data Leak** | Regulatory fines; loss of trust. | Critical | Field-level encryption; strict RBAC; data masking in logs; regular security audits. |
| **Poisoned Rule Registry** | Legitimate transactions blocked. | High | Multi-analyst approval for rule changes; sandbox testing of new rules. |
