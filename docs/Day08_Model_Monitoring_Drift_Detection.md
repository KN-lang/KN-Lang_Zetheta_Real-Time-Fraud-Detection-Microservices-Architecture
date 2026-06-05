# Day 08 - Model Monitoring and Drift Detection

Model monitoring protects fraud detection quality after deployment.

## Drift Metrics

| Metric | Applied To | Alert Threshold |
| --- | --- | --- |
| Population Stability Index (PSI) | Numeric feature buckets and model scores | PSI > 0.20 warning, PSI > 0.30 critical |
| Kolmogorov-Smirnov (KS) statistic | Numeric live vs training distributions | KS p-value < 0.01 for two windows |
| Missing value rate | All model features | 2x training baseline or > 5% absolute |
| Categorical cardinality | MCC, merchant, country, device segment | 25% increase vs baseline |
| Score distribution shift | Model output | Median or tail shift outside control limits |

## Retraining Strategy

Retraining is triggered by sustained drift, confirmed-fraud recall degradation, false-positive increases, new fraud typologies, or scheduled monthly refresh. Training uses point-in-time correct offline features and case labels. Promotion requires backtest evidence, bias review, explainability review, and rollback artifacts.

## Evidence

Monitoring samples are retained in TimescaleDB for dashboarding and object storage for model governance. Model decisions include model name, version, feature freshness, and top explanatory features.
