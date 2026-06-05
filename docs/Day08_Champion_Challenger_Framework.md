# Day 08 - Champion Challenger Framework

The champion-challenger framework lets ShieldPay improve fraud models without destabilizing real-time decisioning.

## Roles

- Champion: approved model whose score contributes to production risk decisions.
- Challenger: candidate model scored in shadow or controlled canary mode.
- Baseline: simple statistical model retained for sanity checks and disaster fallback.

## Evaluation

| Dimension | Measurement |
| --- | --- |
| Fraud effectiveness | Confirmed fraud recall, precision, value at risk detected. |
| Customer impact | False-positive rate, step-up rate, merchant escalation count. |
| Operations | Added case load, analyst overturn rate, review queue age. |
| Platform | p95/p99 inference latency, error rate, CPU/memory usage. |
| Governance | Feature lineage, approval status, explainability, data retention compliance. |

## Promotion and Rollback

Challengers must pass offline backtesting, shadow comparison, canary monitoring, model risk approval, and rollback simulation. Rollback is a model-router configuration change and does not require redeploying `risk-scoring`.
