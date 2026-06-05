# Day10 - Encryption - Strategy

Data in transit uses TLS 1.3 externally and Istio mTLS internally. Data at rest uses cloud KMS envelope encryption for PostgreSQL, Redis snapshots, Neo4j volumes, Kafka disks, and object storage. PAN data is tokenized before analytics services receive events.
