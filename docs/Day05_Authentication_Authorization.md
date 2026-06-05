# Day 05 - Authentication and Authorization

## External Authentication
External API access uses OAuth 2.0 client credentials for merchants and OIDC authorization code flow for analyst users. API gateway validates JWT issuer, audience, expiry, scopes, and tenant claims before routing.

## Internal Authentication
All service-to-service communication uses Istio mTLS with SPIFFE identities. Workload identity, not static shared secrets, is the primary trust primitive.

## Authorization Model
- Merchants can submit transactions and read only their own transaction decisions.
- Analysts can view and decide cases assigned to their queue.
- Rule administrators require dual control for activating high-impact rules.
- Compliance users can export evidence bundles but cannot alter case decisions.

## Sensitive Data Controls
PAN and authentication data are tokenized or excluded. Access to customer identifiers is logged as an audit event and protected through least privilege RBAC.
