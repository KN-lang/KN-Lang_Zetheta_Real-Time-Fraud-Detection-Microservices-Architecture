# ADR 004: Anomaly Detection Approach

## Status
Accepted

## Context
Rules can only catch known patterns. To detect "unknown unknowns" or emerging fraud, we need a statistical or machine-learning-based approach to identify outliers in transaction behavior.

## Decision
The **Anomaly Detection Service** will initially use the statistical prototype's approach (Z-Score and Customer Deviation) for baseline detection. The architecture will be designed to support a pluggable ML model serving layer (e.g., using Seldon Core or BentoML) to host models like Isolation Forest or Autoencoders in the future.

## Alternatives Considered
- **Rule-only system**: Fails to catch sophisticated, novel fraud.
- **Full ML-only system**: ML models can be "black boxes" and hard to explain; statistical baselines are more transparent.

## Consequences
- **Pros**:
  - Detects novel fraud patterns.
  - Scalable approach to handling "big data" behavioral analysis.
  - Path to advanced ML is built-in.
- **Cons**:
  - Potential for high false-positive rates if not tuned correctly.
  - Requires feature engineering and state management for customer baselines.
