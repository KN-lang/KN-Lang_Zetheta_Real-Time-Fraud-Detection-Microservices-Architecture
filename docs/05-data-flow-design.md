# 05. Data Flow Design

## Step-by-Step Flow
1. **Ingestion**: A transaction arrives via REST API.
2. **Publishing**: The Ingestor validates and publishes the `TransactionEvent` to the Kafka `transactions` topic.
3. **Parallel Processing**:
   - **Rule Engine** evaluates the transaction against static rules.
   - **Anomaly Detector** compares the transaction against customer baselines.
   - **Graph Analyzer** updates the entity graph and searches for suspicious patterns.
4. **Signal Aggregation**:
   - Each engine publishes its findings (`RuleHitEvent`, `AnomalyAlertEvent`, `GraphAlertEvent`) to Kafka.
5. **Decisioning**:
   - The **Risk Scorer** collects these signals (using a window or correlation ID).
   - It calculates the final weighted score.
   - It publishes a `RiskDecisionEvent`.
6. **Outcome**:
   - If `BLOCK`, the transaction is rejected (notified via callback/webhook).
   - If `REVIEW`, a case is created in the **Case Manager**.
   - If `APPROVE`, the transaction proceeds.
7. **Audit**: All events are archived for compliance and future model training.
