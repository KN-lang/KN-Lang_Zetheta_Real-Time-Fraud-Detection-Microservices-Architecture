# Day 07 - Rule Performance Monitoring

Every active rule exports operational and fraud-effectiveness metrics.

## Metrics

- `rule_evaluations_total{rule_id,version}`
- `rule_hits_total{rule_id,version}`
- `rule_hit_rate{rule_id,version}`
- `rule_latency_ms_bucket{rule_id,version}`
- `rule_score_contribution{rule_id,version}`
- `rule_confirmed_fraud_total{rule_id,version}`
- `rule_false_positive_total{rule_id,version}`
- `rule_case_load_total{rule_id,version}`

## Alerts

- Hit rate exceeds baseline by 3 standard deviations for 15 minutes.
- False-positive rate breaches rule policy after analyst feedback.
- Rule evaluation p95 latency exceeds 35 ms.
- A critical rule stops evaluating or produces zero hits for an expected high-risk cohort.

## Review Cadence

Fraud strategy reviews critical rules weekly, high-severity rules biweekly, and all other active rules monthly. Retired rules remain searchable for decision reconstruction.
