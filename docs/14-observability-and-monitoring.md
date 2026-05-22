# 14. Observability and Monitoring

## Logging
- **Centralized Logging**: All services send logs to an ELK stack.
- **Structured Logs**: Use JSON format for easy parsing and searching.
- **Audit Trails**: Specialized logs for high-sensitivity actions (e.g., rule changes, case overrides).

## Metrics (Prometheus/Grafana)
- **Golden Signals**: Latency, Traffic, Errors, and Saturation for each microservice.
- **Business Metrics**:
  - Number of transactions processed.
  - Fraud detection rate (DR).
  - False positive rate (FPR).
  - Average risk score.
  - Queue depth (Kafka lag).

## Tracing (Jaeger)
- Distributed tracing is used to follow a transaction's journey through the various detection engines and the risk scorer.
- Crucial for identifying latency bottlenecks in the event-driven pipeline.

## Alerting
- PagerDuty/Slack alerts for:
  - High error rates (> 1%).
  - Kafka consumer lag exceeding thresholds.
  - Service downtime.
  - Detection rate dropping below baseline.
