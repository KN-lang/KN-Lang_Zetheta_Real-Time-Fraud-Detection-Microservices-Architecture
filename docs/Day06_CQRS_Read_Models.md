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
