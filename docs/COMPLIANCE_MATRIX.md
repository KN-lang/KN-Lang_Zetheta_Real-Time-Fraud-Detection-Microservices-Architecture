# Compliance Matrix

## PCI DSS

| Control Area | Services | Policies | Audit Evidence |
| --- | --- | --- | --- |
| Protect cardholder data | transaction-ingestion, audit-compliance | Tokenisation, AES-256 encryption, no raw PAN in logs | Tokenization events, KMS key evidence, log scanning reports. |
| Secure network and systems | API gateway, Istio mesh, Kubernetes | mTLS, network policies, authorization policies | Istio config, network policy manifests, access review logs. |
| Vulnerability management | CI/CD, platform engineering | Image scanning, dependency checks, SBOM | CI artifacts, scan reports, signed images. |
| Access control | gateway, case-management, rule-engine | OAuth2/OIDC, RBAC, dual control for rules | Access logs, approval records, audit events. |
| Monitoring and testing | observability, audit-compliance | Prometheus alerts, SIEM forwarding, runbooks | Alert history, runbook execution logs, incident reports. |

## RBI

| Control Area | Services | Policies | Audit Evidence |
| --- | --- | --- | --- |
| Payment system resilience | transaction-ingestion, risk-scoring, Kafka | RPO/RTO, DR, failover, multi-region | DR tests, failover logs, synthetic probe results. |
| Fraud monitoring | rule-engine, anomaly-detection, graph-analysis | Real-time rules, ML monitoring, graph analytics | Risk decisions, fraud cases, model drift reports. |
| Customer protection | notification, case-management | Step-up, customer notification, dispute workflow | Notification events, case decisions, analyst notes. |
| Incident reporting | audit-compliance, observability | Severity model, P1-P4 runbooks | Incident timeline, audit records, post-incident review. |

## GDPR

| Control Area | Services | Policies | Audit Evidence |
| --- | --- | --- | --- |
| Data minimization | all fraud services | Use tokens/hashes instead of raw PII | Data classification registry, schema PII review. |
| Purpose limitation | feature-store, graph-analysis | Fraud-only feature use and access control | Feature owner metadata, access audit logs. |
| Retention limitation | audit-compliance, graph-analysis, observability | Retention tiers and pruning | Deletion/pruning job logs, retention configs. |
| Data subject rights | customer-profile, audit-compliance | Export, correction, and deletion workflows where legally permitted | Request tickets, completion evidence. |
| Security of processing | platform services | Encryption, mTLS, secrets management | KMS, Vault, Istio, and access review evidence. |
