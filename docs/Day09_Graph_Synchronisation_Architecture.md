# Day 09 - Graph Synchronisation Architecture

`graph-analysis` consumes enriched transactions and case outcomes, then upserts graph entities and relationships into Neo4j. The write model is idempotent by entity key and transaction ID.

## Synchronisation Flow

1. Consume `fraud.transactions.enriched`.
2. Upsert `Customer`, `Account`, `Card`, `Device`, `IP`, `Phone`, `Email`, `Merchant`, `Address`, and `Transaction` nodes.
3. Merge relationships with first-seen, last-seen, channel, merchant, and transaction attributes.
4. Run online topology checks for shared device, shared IP, mule beneficiary, and known-fraud path proximity.
5. Publish `fraud.graph.signals`.

## Consistency and Backfill

Kafka offsets are stored with graph write batches. Backfills replay bounded offsets into a staging graph, validate node and edge counts, then promote when counts match source-topic expectations.
