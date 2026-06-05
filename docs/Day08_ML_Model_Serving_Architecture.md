# Day 08 - ML Model Serving Architecture

The anomaly-detection service hosts champion and challenger models behind a model router. It retrieves online features from feature-store, applies model-specific preprocessing, runs inference, publishes `ml.anomaly-scores.v1`, and emits monitoring samples. Models are versioned in a registry with training data lineage, approval status, explainability metadata, and rollback artifacts.
