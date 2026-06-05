# Day 11 - Circuit Breaker Design

Circuit breakers preserve transaction flow when downstream services degrade.

## Policies

| Dependency | Breaker Trigger | Fallback |
| --- | --- | --- |
| feature-store | p95 > 25 ms or error rate > 2% | Use cached features with freshness marker; route high-risk gaps to `REVIEW`. |
| anomaly-detection | p95 > 70 ms or inference queue saturation | Use champion baseline statistical score or mark ML signal unavailable. |
| graph-analysis | p95 > 120 ms or Neo4j unavailable | Use last known graph risk; high-value unknowns go to `REVIEW`. |
| notification provider | provider 5xx > 5% | Queue notification and retry asynchronously. |
| case-management | write failure or DB unavailable | Persist decision event and replay case creation when service recovers. |

## Recovery

Breakers move from open to half-open with synthetic probes. Recovery requires stable error rate and latency for three consecutive windows. All fallback decisions include explanation fields for analyst review.
