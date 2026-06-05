# Master Architecture Document

## Project Scope
`SWE-2C_FraudDetection_KshitijChauhan` designs ShieldPay, a real-time fraud detection platform for financial transactions. The target architecture replaces a high-coupling legacy monolith with ten independently deployable services connected by Apache Kafka, protected by service mesh controls, and operated through observable Kubernetes deployments.

## Core Architecture Decisions
| Decision | Selected Approach | Rationale |
| --- | --- | --- |
| Service style | Microservices aligned to bounded contexts | Keeps transaction intake, fraud signals, decisions, investigations, and audit independently scalable. |
| Event backbone | Apache Kafka with Protobuf schemas | Provides low-latency fan-out, replay, ordering by transaction/customer keys, and schema governance. |
| External API | OpenAPI 3.0 REST via API gateway | Fits merchant/channel integration and supports OAuth, throttling, and idempotency controls. |
| Internal API | gRPC with Protobuf | Supports low-latency service collaboration for profile, feature, rule, graph, and risk calls. |
| Persistence | PostgreSQL, Redis, Neo4j, object storage | Matches transactional, low-latency feature, graph, and immutable evidence workloads. |
| Security | OAuth/OIDC externally and Istio mTLS internally | Reduces credential sprawl and enforces workload identity and least privilege. |
| Observability | Prometheus, Grafana, OpenTelemetry, structured logs | Enables SLA monitoring, traceable decisions, and incident response. |

## Service Architecture
The platform uses ten services: `transaction-ingestion`, `customer-profile`, `feature-store`, `rule-engine`, `anomaly-detection`, `graph-analysis`, `risk-scoring`, `case-management`, `notification`, and `audit-compliance`.

The principal flow is:
1. `transaction-ingestion` accepts and validates requests from the API gateway.
2. Kafka distributes validated transactions to enrichment and fraud signal services.
3. `rule-engine`, `anomaly-detection`, and `graph-analysis` publish independent signals.
4. `risk-scoring` aggregates signals into `APPROVE`, `STEP_UP`, `REVIEW`, or `BLOCK`.
5. `case-management`, `notification`, and `audit-compliance` handle investigations, customer/merchant communication, and immutable evidence.

## Deliverable Navigation
| Area | Files |
| --- | --- |
| Domain discovery | [Day01_Domain_Glossary.md](Day01_Domain_Glossary.md), [Day01_Legacy_Monolith_Analysis.md](Day01_Legacy_Monolith_Analysis.md), [day01_event_storming_initial.mmd](../diagrams/day01_event_storming_initial.mmd) |
| Context and decomposition | [Day02_Bounded_Context_Map.md](Day02_Bounded_Context_Map.md), [Day02_Service_Decomposition_Table.md](Day02_Service_Decomposition_Table.md), [c4_level1_context.mmd](../diagrams/c4_level1_context.mmd), [c4_level2_container_draft.mmd](../diagrams/c4_level2_container_draft.mmd) |
| C4 and persistence | [c4_level2_container_final.mmd](../diagrams/c4_level2_container_final.mmd), [c4_level3_transaction_ingestion.mmd](../diagrams/c4_level3_transaction_ingestion.mmd), [c4_level3_rule_engine.mmd](../diagrams/c4_level3_rule_engine.mmd), [c4_level3_anomaly_detection.mmd](../diagrams/c4_level3_anomaly_detection.mmd), [c4_level3_risk_scoring.mmd](../diagrams/c4_level3_risk_scoring.mmd), [Day03_Service_SLA_Table.md](Day03_Service_SLA_Table.md), [Day03_Polyglot_Persistence_Strategy.md](Day03_Polyglot_Persistence_Strategy.md) |
| Events and APIs | [Day04_Kafka_Topic_Topology.md](Day04_Kafka_Topic_Topology.md), [events.proto](../api-specs/events.proto), [schema-registry-config.yml](../configs/schema-registry-config.yml), [Day04_DLQ_Strategy.md](Day04_DLQ_Strategy.md), [openapi.yml](../api-specs/openapi.yml), [internal-services.proto](../api-specs/internal-services.proto), [api-gateway-routing.yml](../configs/api-gateway-routing.yml), [Day05_Authentication_Authorization.md](Day05_Authentication_Authorization.md) |
| Workflows and CQRS | [day06_complete_event_storming_50_events.mmd](../diagrams/day06_complete_event_storming_50_events.mmd), [Day06_Saga_Workflows.md](Day06_Saga_Workflows.md), [Day06_CQRS_Read_Models.md](Day06_CQRS_Read_Models.md), [day06_cqrs_topology.mmd](../diagrams/day06_cqrs_topology.mmd) |
| Rules | [rule-schema.json](../configs/rule-schema.json), [sample-rules.yml](../configs/sample-rules.yml), [Day07_Rule_Lifecycle.md](Day07_Rule_Lifecycle.md), [day07_rule_lifecycle_state_machine.mmd](../diagrams/day07_rule_lifecycle_state_machine.mmd), [Day07_Rule_Simulation_Design.md](Day07_Rule_Simulation_Design.md), [Day07_Rule_Performance_Monitoring.md](Day07_Rule_Performance_Monitoring.md) |
| ML and graph | [Day08_ML_Model_Serving_Architecture.md](Day08_ML_Model_Serving_Architecture.md), [Day08_Feature_Store_Design.md](Day08_Feature_Store_Design.md), [day08_ml_serving_architecture.mmd](../diagrams/day08_ml_serving_architecture.mmd), [Day08_Model_Monitoring_Drift_Detection.md](Day08_Model_Monitoring_Drift_Detection.md), [Day08_Champion_Challenger_Framework.md](Day08_Champion_Challenger_Framework.md), [Day09_Graph_Database_Schema.md](Day09_Graph_Database_Schema.md), [neo4j_schema.cypher](../configs/neo4j_schema.cypher), [fraud_detection_queries.cypher](../configs/fraud_detection_queries.cypher) |
| Security and operations | [Day10_Service_Communication_Matrix.md](Day10_Service_Communication_Matrix.md), [Day10_Encryption_Strategy.md](Day10_Encryption_Strategy.md), [Day10_PCI_DSS_Compliance_Mapping.md](Day10_PCI_DSS_Compliance_Mapping.md), [Day11_API_Gateway_Design.md](Day11_API_Gateway_Design.md), [Day11_Rate_Limiting_Policy.md](Day11_Rate_Limiting_Policy.md), [Day11_Circuit_Breaker_Design.md](Day11_Circuit_Breaker_Design.md), [Day12_Grafana_Dashboard_Specifications.md](Day12_Grafana_Dashboard_Specifications.md), [prometheus-alert-rules.yml](../configs/prometheus-alert-rules.yml), [runbooks](runbooks/P1_Transaction_Pipeline_Down.md) |
| Delivery and final material | [Day14_CICD_Pipeline_Design.md](Day14_CICD_Pipeline_Design.md), [ci.yml](../.github/workflows/ci.yml), [Day14_Multi_Region_Deployment_Topology.md](Day14_Multi_Region_Deployment_Topology.md), [day14_deployment_topology.mmd](../diagrams/day14_deployment_topology.mmd), [Day14_Disaster_Recovery_Plan.md](Day14_Disaster_Recovery_Plan.md), [Board_Presentation_Outline.md](../presentation/Board_Presentation_Outline.md), [video_script.md](../presentation/video_script.md), [AI_USAGE.md](AI_USAGE.md), [ERROR_DETECTION.md](ERROR_DETECTION.md) |

## Kafka Topic Topology
The event backbone contains eleven topics, including `transactions.raw.v1`, `transactions.validated.v1`, `transactions.enriched.v1`, `rules.evaluated.v1`, `ml.anomaly-scores.v1`, `graph.signals.v1`, `risk.decisions.v1`, `cases.events.v1`, `notifications.requests.v1`, `audit.events.v1`, and `fraud.dlq.v1`.

## Compliance Position
The architecture narrows PCI DSS scope by keeping PAN and sensitive authentication data out of analytical services. It supports RBI-style operational resilience, auditability, incident response, customer notification, and data residency expectations. GDPR considerations are addressed through purpose limitation, retention control, minimization, and auditable access to personal data.

## Operational Readiness
The repository includes Prometheus alert rules, Grafana dashboard specifications, OpenTelemetry tracing, structured logging standards, P1/P2 runbooks, CI/CD design, Kubernetes samples, and multi-region disaster recovery material. These artifacts make the design reviewable as an architecture submission and give a clear path toward production implementation.
