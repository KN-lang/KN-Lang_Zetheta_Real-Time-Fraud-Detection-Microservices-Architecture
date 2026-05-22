# ADR 001: Microservices Architecture

## Status
Accepted

## Context
The current fraud detection system is implemented as a local Python prototype. While functional for small-scale simulations, it lacks the scalability, fault tolerance, and modularity required for a high-volume, real-time financial environment. To handle thousands of transactions per second with low latency, the system needs a more robust architecture.

## Decision
We will transition the local prototype to a **Microservices Architecture**. Each core fraud detection capability (Rule Engine, Anomaly Detection, Graph Analysis, Risk Scoring, Case Management) will be developed and deployed as an independent service.

## Alternatives Considered
- **Monolithic Architecture**: Easier to develop initially but difficult to scale individual components (e.g., Graph Analysis requires more memory/CPU than Rule Engine).
- **Serverless (Functions-as-a-Service)**: Good for intermittent loads, but might introduce cold-start latencies and complexity in managing state for graph/anomaly detection.

## Consequences
- **Pros**:
  - Independent scaling of services.
  - Technology flexibility (e.g., Python for ML/Graph, Go for high-throughput rules).
  - Improved fault isolation.
- **Cons**:
  - Increased operational complexity (deployment, service discovery, monitoring).
  - Network latency between services (mitigated by event-driven approach).
  - Distributed data management challenges.
