# Kafka Local Deployment

This local deployment supports Project 1C architecture review and contract testing. It runs Kafka, Kafka UI, Schema Registry, and Zookeeper using Docker Compose.

## Start the Stack

```bash
docker compose up -d
```

Services:

| Component | URL / Port |
| --- | --- |
| Kafka | `localhost:9092` |
| Schema Registry | `http://localhost:8081` |
| Kafka UI | `http://localhost:8080` |
| Zookeeper | `localhost:2181` |

## Create Required Topics

```bash
docker compose exec kafka kafka-topics --bootstrap-server kafka:29092 --create --if-not-exists --topic fraud.transactions.raw --partitions 12 --replication-factor 1
docker compose exec kafka kafka-topics --bootstrap-server kafka:29092 --create --if-not-exists --topic fraud.transactions.enriched --partitions 24 --replication-factor 1
docker compose exec kafka kafka-topics --bootstrap-server kafka:29092 --create --if-not-exists --topic fraud.rule.results --partitions 24 --replication-factor 1
docker compose exec kafka kafka-topics --bootstrap-server kafka:29092 --create --if-not-exists --topic fraud.anomaly.scores --partitions 24 --replication-factor 1
docker compose exec kafka kafka-topics --bootstrap-server kafka:29092 --create --if-not-exists --topic fraud.graph.signals --partitions 12 --replication-factor 1
docker compose exec kafka kafka-topics --bootstrap-server kafka:29092 --create --if-not-exists --topic fraud.risk.decisions --partitions 24 --replication-factor 1
docker compose exec kafka kafka-topics --bootstrap-server kafka:29092 --create --if-not-exists --topic fraud.notifications --partitions 6 --replication-factor 1
docker compose exec kafka kafka-topics --bootstrap-server kafka:29092 --create --if-not-exists --topic fraud.audit.events --partitions 12 --replication-factor 1
docker compose exec kafka kafka-topics --bootstrap-server kafka:29092 --create --if-not-exists --topic fraud.dlq --partitions 6 --replication-factor 1
```

Local replication factor is `1` because the compose file runs a single broker. Production uses replication factor `3` and `min.insync.replicas=2`.

## Schema Registration

The Protobuf contract is stored in `api-specs/events.proto`. Schema Registry subjects follow:

- `fraud.transactions.raw-value`
- `fraud.transactions.enriched-value`
- `fraud.rule.results-value`
- `fraud.anomaly.scores-value`
- `fraud.graph.signals-value`
- `fraud.risk.decisions-value`
- `fraud.notifications-value`
- `fraud.audit.events-value`

Compatibility is `BACKWARD_TRANSITIVE`. Breaking schema changes require a new Protobuf package version and migration plan.

## Retry and DLQ Verification

Use Kafka UI to inspect `fraud.retry.*` and `fraud.dlq` messages. Every DLQ message must include original topic, partition, offset, schema subject, service version, exception class, correlation ID, and redacted payload.
