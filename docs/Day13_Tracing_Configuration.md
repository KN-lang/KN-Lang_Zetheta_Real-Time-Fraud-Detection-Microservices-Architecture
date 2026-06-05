# Day 13 - Tracing Configuration

OpenTelemetry provides distributed traces across REST, gRPC, Kafka producers, Kafka consumers, and database calls.

## Propagation

- Gateway accepts or creates W3C `traceparent` and `tracestate`.
- Services propagate trace context over HTTP and gRPC metadata.
- Kafka producers write trace context, `correlation_id`, and schema subject into record headers.
- Kafka consumers extract headers and continue the trace when processing events.

## Sampling

Tail sampling retains all errors, high-latency traces, blocked decisions, DLQ paths, and a statistically representative sample of normal approvals. Sampling rules are configured in `configs/opentelemetry-config.yml`.

## Correlation

Every fraud decision can be reconstructed by joining trace ID, correlation ID, transaction ID, Kafka offsets, structured logs, and audit events.
