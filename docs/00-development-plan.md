# Development Plan

## Phase 1: Local Simulation

Build a clean Python package that generates synthetic financial transactions, evaluates rule/anomaly/graph signals, produces risk scores, creates fraud cases, and writes auditable reports under `data/`.

## Phase 2: Kafka Event Design

Define topic names, event schemas, partition keys, retry/dead-letter handling, and replay behavior for transaction ingestion, scoring, graph alerts, and case events.

## Phase 3: ML Model Serving

Add offline feature engineering, model training experiments, model evaluation reports, and a lightweight scoring service contract for online inference.

## Phase 4: Graph Database/Neo4j Design

Move customer/account/device/IP/merchant relationships into a graph database design with Cypher queries for shared-entity, mule-account, and suspicious-cluster detection.

## Phase 5: Microservices Deployment Architecture

Split the local modules into deployable service boundaries, add API contracts, containerization, service configuration, observability, and deployment diagrams.

## Phase 6: Final Submission Package

Prepare architecture diagrams, ADRs, demo scripts, sample reports, test evidence, limitations, and a roadmap that clearly distinguishes prototype behavior from production readiness.
