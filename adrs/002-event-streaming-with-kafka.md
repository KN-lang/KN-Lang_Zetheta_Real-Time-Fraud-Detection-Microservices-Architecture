# ADR 002: Event Streaming with Kafka

## Status
Accepted

## Context
Real-time fraud detection requires processing transactions as they occur. Services need to communicate asynchronously to ensure that a slowdown in one service (e.g., complex graph analysis) doesn't block the entire pipeline. We need a reliable, high-throughput, and persistent messaging backbone.

## Decision
We will use **Apache Kafka** as the central event-driven backbone. Transactions will be published to a `transactions` topic, and various fraud detection services will consume these events, perform their analysis, and publish results to their respective topics (e.g., `rule-hits`, `anomaly-alerts`).

## Alternatives Considered
- **RabbitMQ**: Excellent for simple pub/sub but lacks the replayability and high-throughput partitioning of Kafka.
- **REST APIs (Synchronous)**: Would cause cascading failures and high latency if any service in the chain is slow.

## Consequences
- **Pros**:
  - Decouples services.
  - Enables event replay for debugging and model backtesting.
  - Highly scalable and fault-tolerant.
- **Cons**:
  - Requires management of a Kafka cluster.
  - Complexity in ensuring exactly-once or at-least-once delivery semantics.
  - Eventual consistency between services.
