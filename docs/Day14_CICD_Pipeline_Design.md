# Day 14 - CI/CD Pipeline Design

CI/CD validates architecture artifacts and provides a production path for implementation teams.

## CI Stages

1. Checkout and dependency setup.
2. Markdown link validation.
3. JSON validation for rule schemas.
4. YAML validation for OpenAPI, Kubernetes, Istio, Kong, Prometheus, and Docker Compose.
5. Protobuf syntax validation when `protoc` is available.
6. Unit tests for the local Python prototype.
7. Container image build, SBOM generation, and vulnerability scanning.
8. Kubernetes manifest linting and policy checks.

## CD Stages

Images move from dev to staging to production through signed artifacts. Production deployment uses canary rollout, automated metrics gates, and rollback on error budget burn, latency breach, or fraud decision anomalies.

## Governance Gates

Rule changes, model promotions, gateway policy changes, and schema changes require approval evidence. High-impact production changes emit audit events and retain CI artifacts.
