# 06. Rule Engine Design

## Prototype Implementation
The prototype implements a `RuleEngine` class using Pandas for batch processing. Key rules include:
- **Velocity**: > 5 transactions in 10 minutes.
- **Threshold**: Amount > 50,000.
- **Geography**: Transactions from high-risk countries.
- **Technical**: New device with high amount, shared devices/IPs.
- **Patterns**: Round amount transfers (e.g., multiples of 10,000).

## Production Design
The production **Rule Engine Service** will be a stateless evaluator.
- **Rule Registry**: A centralized database (PostgreSQL) where rules are defined, versioned, and tested.
- **Distribution**: Rules are pushed to service instances (via Kafka or sidecar) and cached in-memory for zero-latency lookups.
- **Language**: Evaluated using a high-performance engine like `JsonLogic` or `Expr` (Go).

## Scalability
- **Horizontal Scaling**: Multiple instances of the service can process the Kafka `transactions` partition.
- **Stateful Rules**: Velocity and frequency rules use **Redis** to maintain counters and sliding windows across distributed instances.
