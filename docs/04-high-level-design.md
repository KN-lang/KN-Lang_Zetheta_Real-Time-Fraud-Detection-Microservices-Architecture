# 04. High-Level Design

## Overview
The platform follows an **Event-Driven Microservices Architecture**. Apache Kafka is the target production event backbone, but the local prototype does not deploy Kafka. Instead, it uses an in-process `EventBus` to simulate topic-based communication and validate service boundaries without Docker or broker infrastructure.

## Components
1. **API Gateway**: Target production entry point for transaction ingestion.
2. **Transaction Ingestor / Generator**: Publishes `TransactionEvent` records to `transaction.events`.
3. **Rule Engine Service**: Evaluates rules and publishes `RuleHitEvent` records to `rule.hit.events`.
4. **Anomaly Detection Service**: Evaluates statistical anomalies and publishes `AnomalyAlertEvent` records to `anomaly.alert.events`.
5. **Graph Analysis Service**: Builds relationship risk signals and publishes `GraphAlertEvent` records to `graph.alert.events`.
6. **Risk Scorer**: Correlates signals and publishes `RiskScoreEvent` records to `risk.score.events`.
7. **Case Manager**: Creates fraud cases from REVIEW/BLOCK decisions and publishes `FraudCaseEvent` records to `fraud.case.events`.
8. **Audit Logger**: Records event publications to `audit.events` and the local `event_log.jsonl`.

## Local vs Production Runtime
- **Local prototype**: Python modules plus in-process EventBus, deterministic generated data, CSV/JSON/JSONL reports.
- **Production target**: Independent services connected through Kafka producers/consumers, persistent stores, observability, and deployment automation.

## Visual Representation
*(Refer to diagrams/c4-container.puml for the full visual design)*
