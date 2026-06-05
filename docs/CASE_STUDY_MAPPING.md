# Case Study Mapping

## Target Breach

| Failure Pattern | ShieldPay Mitigation |
| --- | --- |
| Third-party access and weak network segmentation | Istio authorization policies, mTLS, gateway authentication, network policies, least-privilege service identities. |
| Insufficient monitoring of suspicious activity | Structured logs, OpenTelemetry traces, Prometheus alerts, SIEM-forwarded `fraud.audit.events`. |
| Broad data exposure | Tokenisation, PII masking, AES-256 storage encryption, narrow PCI scope. |

## Cosmos Bank Attack

| Failure Pattern | ShieldPay Mitigation |
| --- | --- |
| Coordinated high-velocity ATM/payment abuse | Velocity rules, anomaly detection, graph relationship analysis, risk-scoring block/review decisions. |
| Delayed detection of coordinated withdrawals | Kafka real-time signal fan-out and fraud dashboards. |
| Weak transaction monitoring | Rule lifecycle, ML drift monitoring, case workflows, audit trail. |

## Netflix Resilience Patterns

| Pattern | ShieldPay Adoption |
| --- | --- |
| Failure injection and chaos testing | Six chaos experiments in the DR plan. |
| Graceful degradation | Circuit breakers and conservative review fallback when feature, ML, or graph services degrade. |
| Observability-first operations | Dashboards, traces, structured logs, P1-P4 alerts, runbooks. |

## Wirecard Audit Failure

| Failure Pattern | ShieldPay Mitigation |
| --- | --- |
| Weak evidence and reconciliation | Immutable audit events, evidence bundles, Kafka replay, case decision records. |
| Poor governance and opaque reporting | Compliance matrix, board defense guide, traceability matrix, audit-compliance service. |
| Inadequate independent verification | Schema registry, CI validation, explicit controls and evidence mapping. |
