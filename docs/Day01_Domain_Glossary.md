# Day 01 - Domain Glossary

    This glossary standardizes fintech and fraud vocabulary used across the ShieldPay fraud detection architecture.

    | Term | Definition |
| --- | --- |
| Acquirer | Financial institution that processes card transactions for merchants. |
| AML | Anti-money laundering controls used to detect suspicious financial behavior. |
| Anomaly Score | Model output describing how unusual a transaction is relative to expected behavior. |
| API Gateway | North-south entry point that authenticates, throttles, and routes external API traffic. |
| Audit Event | Immutable record proving who did what, when, why, and from where. |
| Authorization Hold | Temporary reservation of funds during payment authorization. |
| AVRO | Compact schema-based event serialization format frequently used with Kafka. |
| Behavioral Biometrics | Signals based on typing, swiping, device handling, and session behavior. |
| BIN | Bank identification number used to identify card issuer and product type. |
| Card Present | Transaction where card or device is physically present at a terminal. |
| Card Not Present | Remote transaction such as ecommerce, wallet, or app payment. |
| Case Queue | Prioritized analyst workload for suspicious transactions. |
| Chargeback | Dispute reversal initiated by a cardholder or issuer. |
| CNP Fraud | Fraud targeting online or remote card-not-present channels. |
| Correlation ID | Trace identifier linking API calls, events, logs, and decisions. |
| CQRS | Pattern separating write-side commands from optimized read-side projections. |
| Customer Due Diligence | Identity and risk verification of customers. |
| Device Fingerprint | Stable identifier assembled from device and browser signals. |
| DLQ | Dead-letter queue used for poison messages and unrecoverable processing errors. |
| Event Storming | Domain modeling workshop focused on business events and decisions. |
| Feature Store | System serving consistent ML features for training and online inference. |
| Fraud Ring | Coordinated group of related entities executing fraudulent activity. |
| GDPR | EU privacy regulation requiring lawful processing and data subject rights. |
| Graph Centrality | Measure of entity importance in a relationship network. |
| Idempotency Key | Client-provided key preventing duplicate transaction submission. |
| Issuer | Bank or financial institution that issued a card or payment instrument. |
| Kafka Partition | Ordered shard of a Kafka topic used for scale and ordering. |
| KYC | Know-your-customer identity verification process. |
| MCC | Merchant category code identifying merchant business type. |
| mTLS | Mutual TLS where both client and server authenticate certificates. |
| Mule Account | Account used to receive and move illicit funds. |
| Neo4j | Graph database used for entity relationship and path analysis. |
| OpenAPI | HTTP API contract format used for external REST APIs. |
| OTP Step-up | Additional authentication challenge for risky transactions. |
| PAN | Primary account number, protected cardholder data under PCI DSS. |
| PCI DSS | Card industry security standard for cardholder data environments. |
| PEP | Politically exposed person requiring enhanced monitoring. |
| Protobuf | Schema language for compact internal gRPC contracts. |
| Quarantine Topic | Kafka topic for events requiring manual or automated remediation. |
| Rate Limiting | Control that caps request rates by merchant, IP, endpoint, or risk level. |
| RBI | Reserve Bank of India, relevant regulator for Indian payments and banks. |
| Replay | Controlled reprocessing of retained events for recovery or backfill. |
| Risk Decision | Approve, review, block, or step-up outcome from risk scoring. |
| Rule Hit | Explainable match between transaction facts and a fraud rule. |
| Saga | Distributed workflow that coordinates multiple services through events. |
| Schema Registry | Governance service for event schema compatibility. |
| Service Mesh | Infrastructure layer providing mTLS, traffic policy, and telemetry. |
| SIEM | Security monitoring platform consuming audit and threat events. |
| Synthetic Identity | Fabricated identity assembled from real and fake attributes. |
| Tokenization | Replacement of sensitive data with non-sensitive tokens. |
| Transaction Velocity | Frequency of transactions over a time window. |
| UPI | Unified Payments Interface real-time payment rail in India. |
| Watchlist | List of sanctioned, compromised, high-risk, or blocked entities. |
