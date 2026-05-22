# 16. Capacity Planning

## Traffic Targets
- **Peak Transactions**: 5,000 TPS (Transactions Per Second).
- **Average Transactions**: 1,200 TPS.
- **Payload Size**: ~1.5 KB per transaction event.

## Compute Resources (Estimated for Peak)
| Service | Instances | CPU/Instance | RAM/Instance |
| :--- | :--- | :--- | :--- |
| **Ingestor** | 5 | 2 vCPU | 4 GB |
| **Rule Engine** | 10 | 4 vCPU | 8 GB |
| **Anomaly Detection** | 8 | 4 vCPU | 16 GB |
| **Graph Analysis** | 4 | 8 vCPU | 64 GB |
| **Risk Scorer** | 4 | 2 vCPU | 4 GB |
| **Case Manager** | 2 | 2 vCPU | 4 GB |

## Storage Requirements
- **Transaction Logs (S3)**: ~15 TB per month (compressed).
- **Graph Database (Neo4j)**: ~1 TB (with high-speed NVMe drives).
- **Relational DB (Postgres)**: ~500 GB (for cases and configuration).

## Network Bandwidth
- **Kafka Throughput**: ~10 MB/s incoming; ~50 MB/s aggregate (including inter-service streaming).
