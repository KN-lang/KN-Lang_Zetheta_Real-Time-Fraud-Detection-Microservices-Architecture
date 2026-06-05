# Day 10 - Encryption Strategy

## In Transit

- External APIs use TLS 1.3 at the gateway.
- Internal service-to-service traffic uses Istio mTLS in `STRICT` mode.
- Kafka clients authenticate with mTLS/SASL depending on environment and require encrypted broker listeners.

## At Rest

- PostgreSQL, Redis snapshots, Neo4j volumes, Elasticsearch indexes, TimescaleDB metrics, Kafka broker disks, and object storage use AES-256 encryption through cloud KMS envelope encryption.
- Immutable audit and evidence objects use WORM retention and KMS customer-managed keys.

## Vault Integration

HashiCorp Vault or the cloud-native secrets manager stores database credentials, Kafka credentials, webhook secrets, signing keys, and third-party provider tokens. Kubernetes workloads receive secrets through short-lived workload identity, not static checked-in secrets.

## Tokenisation

PAN, phone, email, and address values are tokenized or hashed before events leave the payment and KYC boundary. Fraud services use `card_token`, `phone_hash`, `email_hash`, and `address_hash` for matching without storing raw sensitive values.

## Key Rotation

- KMS data encryption keys rotate at least annually and immediately after suspected compromise.
- JWT signing keys rotate quarterly with overlap windows for token validation.
- Kafka and database credentials rotate through automated secret rollout.
- Rotation evidence is emitted to `fraud.audit.events`.
