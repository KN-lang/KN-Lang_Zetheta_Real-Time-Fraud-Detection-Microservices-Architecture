# 02. Technology Evaluation

## Core Infrastructure
| Component | Prototype | Target Architecture | Reason |
| :--- | :--- | :--- | :--- |
| **Language** | Python | Python / Go | Python for ML/Graph, Go for high-speed rules. |
| **Backbone** | In-memory / CSV | Apache Kafka | Scalable, persistent, event-driven streaming. |
| **Orchestration** | Single Process | Kubernetes (K8s) | Scalable deployment and management. |

## Detection Components
| Component | Prototype | Target Architecture | Reason |
| :--- | :--- | :--- | :--- |
| **Rule Engine** | Pandas / Python | Custom Engine / Drools | Low latency evaluation of complex logic. |
| **Anomaly Detection** | NumPy / Statistical | Seldon Core / Scikit-learn | Supports advanced ML models in production. |
| **Graph Analysis** | NetworkX | Neo4j / AWS Neptune | Persistent, scalable graph storage and querying. |

## Data Management
| Component | Prototype | Target Architecture | Reason |
| :--- | :--- | :--- | :--- |
| **Transaction DB** | CSV | MongoDB / Cassandra | High-write throughput for transaction logs. |
| **Case DB** | CSV | PostgreSQL | ACID compliance for investigation workflows. |
| **Cache** | N/A | Redis | Fast access to rules and customer profiles. |

## Observability
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana).
- **Metrics**: Prometheus & Grafana.
- **Tracing**: Jaeger / OpenTelemetry.
