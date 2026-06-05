# Day 14 - Failover Runbook

## Trigger

Use this runbook for regional outage, Kafka unavailability, database primary failure, or sustained P1 transaction decision outage.

## Steps

1. Declare incident and assign incident commander, communications lead, and technical leads.
2. Freeze rule, model, and deployment changes.
3. Confirm affected services, region, Kafka clusters, databases, and gateway health.
4. Shift global traffic manager weights to the healthy region.
5. Verify Kafka replication, schema registry, and consumer group lag.
6. Promote database replicas only after confirming replication position and data loss window.
7. Restart or scale critical consumers: `risk-scoring`, `case-management`, and `audit-compliance`.
8. Run synthetic checks for `/transactions`, risk score retrieval, case creation, notification queueing, and audit evidence.
9. Communicate status every 15 minutes for P1 incidents.
10. After recovery, perform offset reconciliation, case queue reconciliation, and post-incident review.

## Rollback

If failover increases error rate or data inconsistency risk, route traffic to conservative review mode and pause non-critical consumers until the incident commander approves the next action.
