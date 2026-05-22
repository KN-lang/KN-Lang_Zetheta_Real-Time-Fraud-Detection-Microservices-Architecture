# 09. Risk Scoring and Decisioning

## Logic
The **Risk Scorer** is the brain of the system. It uses a weighted formula to combine signals:
- `Final Score = (Rule Score * 0.50) + (Anomaly Score * 0.25) + (Graph Score * 0.25)`

## Decisions
- **APPROVE (Score < 40)**: Transaction is considered safe.
- **REVIEW (Score 40-69)**: Transaction is suspicious; proceeds but a Case is created for analyst review.
- **BLOCK (Score >= 70)**: Transaction is high-risk and is stopped immediately.

## Correlation
In a distributed environment, the Risk Scorer must wait for signals from the three detection engines. It uses the `transaction_id` as a correlation key and a short-lived state (in Redis) to aggregate scores. If a service times out, a default "safe" score is used or the transaction is moved to REVIEW based on fail-safe policies.
