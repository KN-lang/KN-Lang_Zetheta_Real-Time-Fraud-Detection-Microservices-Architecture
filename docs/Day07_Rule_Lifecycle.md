# Day 07 - Rule Lifecycle

Fraud rules are operational controls. ShieldPay manages them with versioning, simulation, approval, staged rollout, monitoring, and rollback rather than direct production edits.

## Lifecycle States

| State | Entry Criteria | Exit Criteria | Controls |
| --- | --- | --- | --- |
| Draft | Rule author creates a candidate rule with category, score, condition, and expected impact. | Syntax and schema validation pass. | JSON Schema validation, owner metadata, ticket reference. |
| Simulation | Rule is replayed against historical enriched transactions. | Precision, hit rate, customer impact, and merchant impact are reviewed. | No production decisions emitted. |
| Peer Review | Fraud strategy and platform engineering review logic and blast radius. | Approval or rejection recorded. | Dual control for block-capable rules. |
| Canary | Rule evaluates a small merchant or traffic cohort. | Metrics remain within false-positive and latency thresholds. | Automatic rollback on threshold breach. |
| Active | Rule contributes to production risk score. | Rule is superseded, retired, or rolled back. | Versioned activation and audit evidence. |
| Retired | Rule no longer evaluates transactions. | Historical evidence remains queryable. | Retention follows audit policy. |

## Versioning

- Rule IDs remain stable, for example `FR-001`; versions increment as `FR-001@v3`.
- Rule versions are immutable after approval.
- A rule activation event records version, author, approver, rollout cohort, effective time, and rollback version.
- Risk decisions store matched rule IDs and versions for explainability.

## A/B Testing

A/B testing is used only for score contribution and routing behavior, not uncontrolled customer blocking. Candidate rules run in shadow mode for cohort B, while cohort A continues on the current production rule set. Evaluation compares hit rate, confirmed fraud capture, false-positive rate, case load, merchant impact, and p95 evaluation latency.
