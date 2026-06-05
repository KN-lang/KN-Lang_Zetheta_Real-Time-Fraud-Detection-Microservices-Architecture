# Day 07 - Rule Simulation Design

Rule simulation prevents high-impact false positives before production rollout.

## Inputs

- Historical `fraud.transactions.enriched` events.
- Confirmed fraud and false-positive labels from `fraud.cases.events`.
- Merchant risk segments and transaction channel metadata.
- Existing production rule results for overlap analysis.

## Outputs

| Metric | Purpose |
| --- | --- |
| Hit rate | Measures customer and merchant impact. |
| Confirmed fraud recall | Estimates fraud capture. |
| False-positive rate | Protects customer experience and analyst capacity. |
| Blocked amount | Quantifies financial exposure. |
| Rule overlap | Identifies duplicate or redundant rules. |
| Added case load | Shows operational impact on analysts. |
| Latency impact | Ensures p95 rule evaluation stays within SLA. |

## Promotion Gate

A rule can move to canary only when schema validation passes, simulation evidence is attached, expected score impact is documented, false-positive threshold is acceptable, and rollback criteria are defined.
