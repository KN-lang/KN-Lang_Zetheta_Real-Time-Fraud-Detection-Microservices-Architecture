# SWE-2C_FraudDetection_KshitijChauhan

    ## Executive Summary
    This repository presents a GitHub-ready architecture submission for Project 1C: Real-Time Fraud Detection Microservices Architecture. It designs ShieldPay, an event-driven fraud detection platform for financial transactions using Apache Kafka, microservices, rule evaluation, ML anomaly detection, Neo4j graph analysis, risk scoring, case management, audit, observability, security, and Kubernetes deployment patterns.

    ## Problem Statement
    Legacy fraud systems are often monolithic, batch-oriented, difficult to tune, and slow to react to fraud rings, mule accounts, account takeover, and high-velocity digital payment abuse. ShieldPay replaces that model with real-time decisioning and explainable fraud evidence.

    ## Repository Structure
    - `docs/` - daily architecture documents, runbooks, compliance mappings, and final master document.
    - `diagrams/` - Mermaid C4, event storming, CQRS, ML, auth, and deployment diagrams.
    - `api-specs/` - OpenAPI external REST contract and Protobuf internal/event contracts.
    - `configs/` - Kafka schema registry, rules, Neo4j Cypher, Istio, gateway, observability, and alert configs.
    - `samples/` - Docker and Kubernetes deployment examples.
    - `presentation/` - board presentation outline and walkthrough script.
    - `daily-commits/` - daily work logs for Day 01 through Day 15.

    ## Architecture Overview
    The architecture uses ten services: transaction-ingestion, customer-profile, feature-store, rule-engine, anomaly-detection, graph-analysis, risk-scoring, case-management, notification, audit-compliance. Kafka topics connect ingestion, enrichment, rule evaluation, ML scoring, graph analysis, risk decisions, cases, notifications, and audit events. Istio provides mTLS and authorization policy. Kong/API gateway provides external routing, OAuth enforcement, and rate limiting.

    ## Key Deliverables
    | Day | Primary Work Log | Status |
| --- | --- | --- |
| Day 01 | `daily-commits/Day01_Work_Log.md` | Complete |
| Day 02 | `daily-commits/Day02_Work_Log.md` | Complete |
| Day 03 | `daily-commits/Day03_Work_Log.md` | Complete |
| Day 04 | `daily-commits/Day04_Work_Log.md` | Complete |
| Day 05 | `daily-commits/Day05_Work_Log.md` | Complete |
| Day 06 | `daily-commits/Day06_Work_Log.md` | Complete |
| Day 07 | `daily-commits/Day07_Work_Log.md` | Complete |
| Day 08 | `daily-commits/Day08_Work_Log.md` | Complete |
| Day 09 | `daily-commits/Day09_Work_Log.md` | Complete |
| Day 10 | `daily-commits/Day10_Work_Log.md` | Complete |
| Day 11 | `daily-commits/Day11_Work_Log.md` | Complete |
| Day 12 | `daily-commits/Day12_Work_Log.md` | Complete |
| Day 13 | `daily-commits/Day13_Work_Log.md` | Complete |
| Day 14 | `daily-commits/Day14_Work_Log.md` | Complete |
| Day 15 | `daily-commits/Day15_Work_Log.md` | Complete |

    ## How to Review the Project
    1. Start with `docs/Master_Architecture_Document.md`.
    2. Review `diagrams/c4_level1_context.mmd`, `diagrams/c4_level2_container_final.mmd`, and the Level 3 service diagrams.
    3. Inspect `api-specs/openapi.yml`, `api-specs/internal-services.proto`, and `api-specs/events.proto`.
    4. Review `configs/sample-rules.yml`, `configs/fraud_detection_queries.cypher`, Istio configs, Prometheus alerts, and Kubernetes samples.
    5. Use `presentation/video_script.md` for the 5-8 minute walkthrough.

    ## Technology Stack
    Apache Kafka, Protobuf, OpenAPI 3.0, PostgreSQL, Redis, Neo4j, Python, Kubernetes, Docker, Istio, Kong, Prometheus, Grafana, OpenTelemetry, and GitHub Actions.

    ## Submission Checklist
    - [x] 8-12 microservices defined.
    - [x] Kafka event backbone with 8+ topics.
    - [x] C4 Level 1, Level 2, and four Level 3 diagrams.
    - [x] External OpenAPI and internal gRPC contracts.
    - [x] Rule schema and 20 sample fraud rules.
    - [x] ML serving and feature store design.
    - [x] Neo4j schema and 5+ Cypher fraud queries.
    - [x] Service mesh, security, observability, runbooks, CI/CD, Kubernetes, DR, and presentation material.

    ## Contact / Author
    Kshitij Chauhan  
    Repository name: `KN-Lang_Zetheta_Real-Time-Fraud-Detection-Microservices-Architecture`
    Repository link: `https://github.com/KN-lang/KN-Lang_Zetheta_Real-Time-Fraud-Detection-Microservices-Architecture`
 