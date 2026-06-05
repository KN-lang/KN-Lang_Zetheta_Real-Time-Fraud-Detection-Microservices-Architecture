# Day10 - Service - Communication - Matrix

| From | To | Protocol | Purpose |
| --- | --- | --- | --- |
| transaction-ingestion | Kafka | Kafka | Publish validated transactions |
| customer-profile | feature-store | gRPC | Retrieve online features |
| rule-engine | Kafka | Kafka | Publish rule results |
| anomaly-detection | feature-store | gRPC | Fetch model features |
| risk-scoring | case-management | Kafka | Create review/block cases |
| audit-compliance | Kafka | Kafka | Subscribe to governed events |
