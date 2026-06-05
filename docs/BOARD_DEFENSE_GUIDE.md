# Board Defense Guide

## CTO Questions

| Question | Model Answer |
| --- | --- |
| Why Kafka instead of direct synchronous calls? | Fraud signals need fan-out, replay, backpressure handling, and independent scaling. Kafka lets rule, ML, graph, audit, and case services evolve without coupling the authorization path to every downstream dependency. |
| How do you prevent inconsistent decisions if ML or graph is late? | `risk-scoring` owns the decision window. Late or unavailable non-critical signals are marked in the explanation and high-risk uncertainty falls back to `REVIEW`. |
| How does the design evolve without breaking consumers? | Protobuf schemas use backward-transitive compatibility, unknown-field tolerance, and versioned packages. Breaking changes require new versions and migration plans. |

## CRO Questions

| Question | Model Answer |
| --- | --- |
| How does this reduce fraud loss? | It combines known-pattern rules, anomaly detection, and graph relationship signals in real time, improving coverage against account takeover, mule accounts, synthetic identity, and merchant abuse. |
| How do analysts trust decisions? | Risk decisions include matched rule versions, ML model version, top features, graph paths, and evidence event IDs. |
| How are false positives controlled? | Rule simulation, model champion-challenger testing, canary rollout, analyst feedback loops, and false-positive alerting are built into the lifecycle. |

## VP Engineering Questions

| Question | Model Answer |
| --- | --- |
| Why ten services? | The ten services map to bounded contexts: ingestion, profile, feature store, rules, ML, graph, scoring, cases, notifications, and audit. This is inside the required 8-12 range and avoids splitting by technical layer only. |
| What is the operational risk? | The main risks are Kafka operations, schema governance, model drift, and case queue overload. The repo includes runbooks, alerts, retry/DLQ, schema registry, and dashboard specifications to manage them. |
| How do we deploy safely? | GitHub Actions validates contracts and manifests, CD uses canaries, and service mesh policies provide mTLS, traffic controls, and circuit breaking. |

## Compliance Questions

| Question | Model Answer |
| --- | --- |
| How is PCI DSS scope controlled? | PAN and sensitive authentication data are tokenized before analytics services. Fraud services operate on tokens and hashes, and audit evidence is immutable. |
| How is GDPR handled? | The design applies minimization, purpose limitation, retention policies, PII masking, auditable access, and deletion workflows for non-regulatory data. |
| How is RBI operational resilience addressed? | The design includes audit trails, incident runbooks, notification flows, RPO/RTO targets, DR, failover, and multi-region operations. |

## CFO Questions

| Question | Model Answer |
| --- | --- |
| What drives cost? | Kafka throughput, model inference capacity, Neo4j graph size, observability retention, and multi-region replication are the largest drivers. |
| Why build instead of buy? | Build is justified when fraud signals, rule strategy, regulatory evidence, and merchant-specific controls are differentiators. Commodity pieces such as gateway, observability, and managed databases can be bought or managed services. |
| How is cost controlled? | Autoscaling, retention tiers, online/offline feature separation, topic retention policies, downsampling, and right-sized graph pruning reduce waste. |
