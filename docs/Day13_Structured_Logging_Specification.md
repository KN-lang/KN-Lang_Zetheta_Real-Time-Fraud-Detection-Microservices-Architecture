# Day 13 - Structured Logging Specification

Logs are JSON and designed for correlation, investigation, and compliance without exposing sensitive data.

## Required Fields

| Field | Description |
| --- | --- |
| `timestamp` | RFC3339 timestamp in UTC. |
| `level` | `DEBUG`, `INFO`, `WARN`, `ERROR`. |
| `service` | Service name such as `risk-scoring`. |
| `environment` | `dev`, `staging`, or `prod`. |
| `trace_id` / `span_id` | OpenTelemetry identifiers. |
| `correlation_id` | End-to-end transaction/request identifier. |
| `transaction_id` | Transaction identifier when available. |
| `merchant_id` | Merchant tenant identifier. |
| `customer_token` | Tokenized customer reference; raw PII is prohibited. |
| `event_type` | Business or technical event. |
| `decision` | Risk decision when relevant. |
| `latency_ms` | Operation latency. |
| `error_code` | Stable application error code. |

## PII Masking

PAN, CVV, OTP, raw phone, raw email, raw address, secrets, OAuth tokens, and session cookies must never be logged. Logging libraries apply deny-list filtering and token patterns before emission.

## Retention

- Hot searchable logs in Elasticsearch: 30 days.
- Security and audit logs: 1 year searchable, 7 years archived where required.
- Debug logs in production: disabled by default and time-bounded when enabled.
