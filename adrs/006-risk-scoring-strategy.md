# ADR 005: Graph Analysis Approach

## Status
Accepted

## Context
Fraud often involves networks of related accounts, devices, and IPs. Detecting "mule accounts" or "fraud rings" requires analyzing the relationships between entities, which is difficult in traditional relational databases.

## Decision
The **Graph Analysis Service** will use a graph-based approach. While the prototype uses NetworkX (in-memory), the production design will utilize a dedicated graph database like **Neo4j** or **Amazon Neptune** to store and query entity relationships in real-time.

## Alternatives Considered
- **Relational Joins**: Extremely slow and complex for multi-hop relationship analysis (e.g., finding a customer connected to a known fraudster via a shared device).
- **In-memory Graph (Production)**: Doesn't scale beyond the memory of a single machine; lacks persistence.

## Consequences
- **Pros**:
  - Efficiently identifies complex fraud rings.
  - Visualizable relationships for investigators.
- **Cons**:
  - Graph databases are specialized and require specific expertise.
  - Synchronizing the graph state with incoming transaction streams.
