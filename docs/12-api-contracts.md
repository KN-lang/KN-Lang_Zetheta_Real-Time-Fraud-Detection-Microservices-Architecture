# 12. API Contracts

## Overview
The platform exposes several APIs for ingestion, configuration, and investigation.

## Core APIs
1. **Ingestion API (`POST /v1/transactions`)**:
   - Accepts transaction data from upstream banking systems.
   - Synchronous validation; asynchronous processing.
2. **Rule Management API (`GET/POST /v1/rules`)**:
   - CRUD operations for fraud rules.
   - Enables dynamic updates without service restarts.
3. **Case Management API (`GET/PATCH /v1/cases/{case_id}`)**:
   - Used by the Investigation UI to fetch and update cases.
4. **Health & Metrics API (`GET /health`, `GET /metrics`)**:
   - Standards for Kubernetes liveness/readiness and Prometheus scraping.

## Standards
- **Format**: JSON.
- **Documentation**: OpenAPI 3.0 (refer to `api/openapi.yaml`).
- **Authentication**: OAuth2 / JWT.
- **Versioning**: URI-based (e.g., `/v1/`).
