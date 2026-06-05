# Day 06 - CQRS Read Models

## Command Side
Commands are accepted by transaction-ingestion, rule-engine administration APIs, and case-management analyst APIs. Command handlers validate intent and publish events.

## Read Models
| Read Model | Source Events | Consumers |
| --- | --- | --- |
| Transaction risk timeline | transaction, rule, ML, graph, decision events | Analyst dashboard |
| Open case queue | risk decisions and case events | Fraud operations |
| Merchant fraud metrics | transaction and decision events | Merchant risk managers |
| Rule performance view | rule evaluations and analyst outcomes | Rule administrators |
| Model drift view | anomaly scores and confirmed outcomes | ML operations |

Read models are rebuildable from Kafka and stored in PostgreSQL, Redis, or analytical stores depending on latency and query pattern.

## Event Modeling Taxonomy

| Type | Examples | Owner |
| --- | --- | --- |
| Commands | `SubmitTransaction`, `EvaluateRules`, `ScoreAnomaly`, `AnalyzeGraph`, `RecordCaseDecision`, `BlockCard`, `SendNotification` | API or workflow service receiving intent. |
| Events | `TransactionAccepted`, `TransactionEnriched`, `RuleEvaluationCompleted`, `AnomalyScoreCalculated`, `GraphSignalsPublished`, `RiskScoreCalculated`, `CaseCreated`, `CardBlocked`, `AuditRecordWritten` | Service that owns the resulting fact. |
| Policies | Route high-risk uncertainty to review; create case on `BLOCK` or high-confidence `REVIEW`; notify customer on card block; write audit event for every decision. | Domain policy owner and service implementation owner. |
| Aggregates | `Transaction`, `CustomerProfile`, `RuleSet`, `ModelVersion`, `GraphEntity`, `RiskDecision`, `FraudCase`, `AuditRecord` | Owning bounded context. |
| Read Models | Risk timeline, case queue, merchant fraud metrics, rule performance, model drift, infrastructure SLA view | Projection services and dashboard APIs. |

## Command Handling Rules

Commands validate authorization, tenant ownership, idempotency, and schema before emitting events. Events are immutable facts and are never edited in place; corrections are represented by compensating events.
