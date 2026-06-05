# Day 11 - API Gateway Design

Kong is the north-south control point for merchant, analyst, dashboard, and administrative API traffic.

## Responsibilities

- Terminate TLS 1.3 and enforce secure headers.
- Validate OAuth2 access tokens and JWT issuer, audience, expiry, tenant, and scope claims.
- Enforce idempotency headers on transaction submission.
- Add or propagate `correlation_id` and W3C trace context.
- Apply route-level rate limits, request size limits, schema validation, and IP allow/deny lists.
- Route accepted traffic into the Istio service mesh.

## Attack Protection

| Threat | Gateway Control |
| --- | --- |
| Credential stuffing | Per-IP and adaptive merchant throttles, WAF signatures, anomaly-based blocks. |
| Replay | Idempotency key enforcement and timestamp skew checks. |
| Token abuse | JWT validation, scope checks, tenant isolation, token revocation integration. |
| Payload abuse | JSON schema validation, max body size, suspicious field rejection. |
| Scraping dashboards | Analyst SSO, session timeout, device posture, per-user limits. |
| DDoS | Global rate limits, CDN/WAF integration, circuit breakers, autoscaling. |

## OAuth2 and JWT

Merchant machine clients use OAuth2 client credentials. Analysts use OIDC through the enterprise identity provider. JWT claims map to scopes such as `fraud:write`, `fraud:read`, `cases:write`, and `rules:admin`.
