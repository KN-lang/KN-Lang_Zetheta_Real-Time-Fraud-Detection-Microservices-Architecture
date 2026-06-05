# Day14 - Multi - Region - Deployment - Topology

Production uses active-active application regions with regional Kafka clusters, replicated schema registry, global traffic management, and regional data residency controls. Audit evidence is replicated to immutable cross-region storage.

## Data Platform Placement

| Component | Multi-Region Approach |
| --- | --- |
| Kafka | Regional clusters with controlled replication for decision, case, and audit topics. |
| PostgreSQL | Regional primary/replica topology per bounded context with tested promotion. |
| Redis | Regional online caches rebuilt from Kafka and offline feature sources. |
| Neo4j | Regional graph cluster with replayable synchronization from Kafka. |
| Elasticsearch | Regional searchable evidence indexes rebuilt from audit streams. |
| TimescaleDB | Regional metric stores with downsampled long-term retention. |

## Traffic Management

The global traffic manager routes merchants to the nearest healthy region. During failover, transaction submission can shift to the healthy region while evidence and offset reconciliation run in the background.
