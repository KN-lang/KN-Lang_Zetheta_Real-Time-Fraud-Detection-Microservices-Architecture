# 05. Data Flow Design

## Step-by-Step Flow
1. **Ingestion**: A transaction arrives via REST API in the production design, or is generated locally by the simulator.
2. **Publishing**: The Ingestor validates and publishes the `TransactionEvent` to `transaction.events`. Locally this uses the in-process EventBus; in production this maps to Kafka.
3. **Parallel Processing**:
   - **Rule Engine** evaluates the transaction against static rules.
   - **Anomaly Detector** compares the transaction against customer baselines.
   - **Graph Analyzer** updates the entity graph and searches for suspicious patterns.
4. **Signal Aggregation**:
   - Each engine publishes its findings (`RuleHitEvent`, `AnomalyAlertEvent`, `GraphAlertEvent`) to the EventBus topics.
5. **Decisioning**:
   - The **Risk Scorer** collects these signals (using a window or correlation ID).
   - It calculates the final weighted score.
   - It publishes a `RiskScoreEvent`.
6. **Outcome**:
   - If `BLOCK`, the transaction is rejected (notified via callback/webhook).
   - If `REVIEW`, a case is created in the **Case Manager**.
   - If `APPROVE`, the transaction proceeds.
7. **Audit**: Local runs write `event_log.jsonl` and `audit.events`. Production runs would retain Kafka topics and archive audit events for compliance and future model training.

## Local Event Pipeline Command

```bash
python -m fraud_platform run-event-pipeline --records 1000
```

This command generates transactions, publishes event envelopes through the in-process EventBus, writes standard fraud reports, and produces `data/output/event_pipeline_summary.json`.
