# ADR 006: Risk Scoring Strategy

## Status
Accepted

## Context
Multiple signals (rules, anomalies, graph alerts) need to be synthesized into a single actionable decision (Approve, Review, Block).

## Decision
The **Risk Scoring Service** will implement a **Weighted Risk Scoring** model.
- Rule Hits: 50% weight
- Anomaly Alerts: 25% weight
- Graph Alerts: 25% weight
The final score (0-100) determines the decision:
- < 40: APPROVE
- 40-70: REVIEW (Create Case)
- \>= 70: BLOCK

## Alternatives Considered
- **Boolean Logic (OR)**: If any signal triggers, block the transaction. (Too many false positives).
- **Consensus Voting**: Each service votes. (Hard to weigh the importance of different signal types).

## Consequences
- **Pros**:
  - Balanced decision-making.
  - Weights can be tuned based on historical performance.
  - Transparent and explainable.
- **Cons**:
  - Requires careful calibration of weights.
  - Dependent on all upstream services providing timely results.
