# 13. Security and Compliance

## Data Security
- **Encryption at Rest**: All databases (PostgreSQL, MongoDB, Neo4j) and S3 buckets use AES-256 encryption.
- **Encryption in Transit**: TLS 1.2+ for all service-to-service and client-to-service communication.
- **PII Masking**: Sensitive customer data (e.g., PAN, Aadhar) is masked or tokenized before being logged or displayed to analysts.

## Access Control
- **RBAC (Role-Based Access Control)**:
  - **Analysts**: Can view and resolve cases.
  - **Managers**: Can modify rules and view reports.
  - **Admins**: Can manage system configuration and users.
- **Service Mesh (Istio)**: Enforces mTLS and service-level authorization policies.

## Compliance
- **PCI-DSS**: System follows payment card industry standards for handling transaction data.
- **GDPR/DPDP**: Supports "Right to be Forgotten" by providing tools to purge customer data from the graph and databases.
- **Auditability**: Every decision and manual intervention is logged in an immutable audit trail.
