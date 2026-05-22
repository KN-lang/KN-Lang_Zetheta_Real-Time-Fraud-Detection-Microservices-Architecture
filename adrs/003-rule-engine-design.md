# ADR 003: Rule Engine Design

## Status
Accepted

## Context
The system needs to evaluate transactions against a set of business rules (velocity, thresholds, blacklists) with extremely low latency. These rules change frequently based on emerging fraud patterns.

## Decision
The **Rule Engine Service** will be designed as a stateless service that loads rules from a dynamic configuration store (e.g., Redis or a dedicated Rule Registry). It will use a fast evaluation library (like `json-logic` or a custom optimized Python/Go engine) to process incoming transaction events.

## Alternatives Considered
- **Hard-coded Rules**: Too rigid; requires redeployment for every rule change.
- **SQL-based Rules**: Latency might be too high for real-time evaluation if queries are complex.

## Consequences
- **Pros**:
  - Sub-millisecond evaluation.
  - Rules can be updated without service restarts.
  - Clear separation between business logic and engine implementation.
- **Cons**:
  - Managing rule versioning and conflicts.
  - Complexity in implementing complex stateful rules (e.g., long-window velocity).
