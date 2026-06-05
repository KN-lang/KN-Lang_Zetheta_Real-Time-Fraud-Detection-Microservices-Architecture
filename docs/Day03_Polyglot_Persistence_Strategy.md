# Day 03 - Polyglot Persistence Strategy

## Store Selection
- PostgreSQL stores transactional service-owned data such as idempotency records, cases, rule definitions, and decision policies.
- Redis stores online features, idempotency cache, risk score cache, and short-lived read models requiring sub-25 ms access.
- Neo4j stores customer, account, device, merchant, IP, beneficiary, and transaction relationships for fraud ring analysis.
- Object storage stores offline features, model training datasets, evidence bundles, dashboard exports, and immutable audit attachments.
- Kafka remains the source of event propagation, replay, and recovery for downstream projections.

## Data Ownership Principles
Each service owns its schema and publishes facts through versioned events. Cross-service joins are implemented through read models, feature materialization, or graph synchronization rather than shared relational tables.

## Compliance Considerations
Sensitive PAN values are tokenized before persistence outside the payment boundary. Retention policies apply GDPR purpose limitation, RBI audit expectations, and PCI DSS evidence requirements.
