# Day 08 - Feature Store Design

## Online Features
Redis stores transaction velocity, merchant risk aggregates, device novelty, account age, failed attempt counts, and customer baseline spend.

## Offline Features
Object storage keeps point-in-time correct Parquet datasets partitioned by event date, customer segment, and model family. Feature definitions are shared between training and serving to avoid skew.

## Governance
Features include owner, TTL, PII classification, freshness SLA, transformation code reference, and permitted model families.
