# 07. Anomaly Detection Design

## Prototype Implementation
The prototype uses a statistical approach:
- **Global Z-Score**: Identifies transactions with amounts significantly higher than the global population mean (Z > 2.5).
- **Customer Deviation**: Identifies transactions that are > 3x the specific customer's historical average amount.

## Production Design
The **Anomaly Detection Service** will evolve into a real-time ML inference pipeline.
- **Feature Store**: A real-time feature store (like Feast or Tecton) will provide customer profiles and historical aggregates (e.g., `avg_amount_30d`) with low latency.
- **Model Serving**: Models (Isolation Forest, XGBoost) will be hosted in a model server (BentoML or Seldon).
- **Online Learning**: While inference is real-time, models will be retrained offline using data from the Audit Log.

## Feedback Loop
- Analysts' "Fraud/Not Fraud" decisions from Case Management are fed back into the training pipeline to improve model precision and recall.
