# Day 09 - Graph Pruning and Maintenance

Graph data must remain useful for fraud detection without becoming an unbounded retention risk.

## Retention Rules

| Data | Default Retention | Exception |
| --- | --- | --- |
| IP session relationships | 90 days | Retain if connected to confirmed fraud evidence. |
| Device/customer relationships | 365 days | Extend for active investigations. |
| Confirmed fraud topology | 7 years or policy | Immutable evidence bundle. |
| Low-value transient addresses | 180 days | Extend when used in topology matching. |

## Maintenance Jobs

- Recompute centrality metrics daily.
- Run community detection nightly for high-risk cohorts.
- Compact duplicate device fingerprints after confidence review.
- Archive stale subgraphs to object storage.
- Validate graph constraints and orphan node counts weekly.
