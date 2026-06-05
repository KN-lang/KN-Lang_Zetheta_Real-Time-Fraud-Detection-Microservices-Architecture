# Day 08 - ML Model Serving Architecture

The `anomaly-detection` service serves low-latency fraud anomaly models without owning transaction decisions. It publishes model signals to Kafka, and `risk-scoring` remains the decision authority.

## Runtime Flow

1. Consume `fraud.transactions.enriched`.
2. Fetch online features from `feature-store` over gRPC.
3. Select the champion model and eligible challenger models from the model registry.
4. Run inference with request-level timeout and model-specific preprocessing.
5. Publish champion score to `fraud.anomaly.scores`.
6. Send challenger, feature, latency, and drift samples to model monitoring.

## Components

| Component | Responsibility |
| --- | --- |
| Model router | Selects champion, challenger, canary, or rollback model version by policy. |
| Feature client | Reads online features and validates freshness. |
| Inference runtime | Executes Isolation Forest, gradient boosted anomaly model, or deep autoencoder artifacts. |
| Explainer | Produces top feature contributions for analyst evidence. |
| Monitor publisher | Emits PSI, KS, latency, error, and score distribution samples. |

## Canary Deployment

New models start in shadow mode, move to 1% canary, then 10%, then 50%, then champion. Promotion gates require stable p95 latency, no material drift regression, acceptable fraud capture, and model risk approval. Rollback returns all traffic to the previous champion without changing event schemas.
