# Day 11 - Rate Limiting Policy

Rate limiting is layered so one abusive client cannot exhaust the fraud decision path.

| Tier | Example Limit | Applied At | Purpose |
| --- | --- | --- | --- |
| Merchant | Contract-specific TPS, for example 1,000/minute for standard merchants | Kong and transaction-ingestion | Protects platform capacity and enforces commercial terms. |
| IP | 300 requests/minute, stricter for unauthenticated failures | Kong/WAF | Reduces bot and credential stuffing traffic. |
| Endpoint | `/transactions` higher throughput, `/rules` low admin throughput | Kong route plugin | Protects expensive or sensitive operations. |
| Global | Region-level platform cap with backpressure | Gateway and autoscaler policy | Preserves availability during spikes. |
| Adaptive | Dynamic reduction when fraud rate, auth failures, or 5xx errors spike | Risk-aware gateway plugin | Responds to active attacks or merchant compromise. |

## Response Behavior

429 responses include `Retry-After`, correlation ID, and a redacted policy identifier. High-risk adaptive throttles also emit `fraud.audit.events` and SOC alerts.
