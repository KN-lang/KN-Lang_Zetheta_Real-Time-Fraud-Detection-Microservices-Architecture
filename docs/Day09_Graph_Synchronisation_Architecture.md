# Day 09 - Graph Synchronisation Architecture

Graph-analysis consumes enriched transactions and case outcomes, upserts nodes and relationships into Neo4j, and publishes graph risk signals. Writes are idempotent by entity ID and transaction ID. Backfill jobs rebuild graph projections from Kafka offsets and validate counts against source topics.
