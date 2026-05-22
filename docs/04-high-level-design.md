# 04. High-Level Design

## Overview
The platform follows an **Event-Driven Microservices Architecture**. All communications between detection services are handled via **Apache Kafka**.

## Components
1. **API Gateway**: Entry point for transaction ingestion.
2. **Transaction Ingestor**: Publishes transactions to the `transactions` topic.
3. **Rule Engine Service**: Consumes from `transactions`, publishes to `rule-hits`.
4. **Anomaly Detection Service**: Consumes from `transactions`, publishes to `anomaly-alerts`.
5. **Graph Analysis Service**: Consumes from `transactions`, maintains a graph database, publishes to `graph-alerts`.
6. **Risk Scorer**: Consumes from all signal topics, correlates alerts, and publishes `risk-decisions`.
7. **Case Manager**: Consumes `risk-decisions` (for REVIEW status) and creates cases for analysts.
8. **Audit Logger**: Consumes all topics for a complete immutable audit trail.

## Visual Representation
*(Refer to diagrams/c4-container.puml for the full visual design)*
