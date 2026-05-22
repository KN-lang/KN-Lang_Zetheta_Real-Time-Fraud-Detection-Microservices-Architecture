# 03. Domain Model and Bounded Contexts

## Domain Model
The core entities in the Fraud Detection domain include:
- **Transaction**: The primary event being analyzed.
- **Customer**: The entity initiating the transaction.
- **Account**: The financial source/destination.
- **Device**: The hardware used (Mobile, Web, ATM).
- **Merchant**: The recipient of the transaction.
- **Fraud Signal**: An alert from rules, anomalies, or graph analysis.
- **Risk Score**: The synthesized result of all signals.
- **Fraud Case**: A record for human investigation.

## Bounded Contexts
1. **Ingestion Context**: Handles incoming transactions and normalizes data.
2. **Detection Context**: Contains the specialized detection engines (Rules, Anomaly, Graph).
3. **Scoring Context**: Aggregates signals and makes final decisions.
4. **Investigation Context**: Manages cases and analyst workflows.
5. **Configuration Context**: Manages rules, thresholds, and system settings.
