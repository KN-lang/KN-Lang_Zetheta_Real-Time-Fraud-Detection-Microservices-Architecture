# Project Submission: Real-Time Fraud Detection Microservices Architecture

## Executive Summary
This project delivers a comprehensive design and a functional local prototype for a Real-Time Fraud Detection Platform. By combining rule-based heuristics, statistical anomaly detection, and graph-based relationship analysis, the system identifies suspicious financial activities in a controlled simulation. The design transitions from a local Python prototype to a scalable, event-driven microservices architecture using Apache Kafka and Kubernetes as target production technologies.

## Problem Statement
Financial institutions face billions in losses due to sophisticated fraud. Existing systems are often slow, siloed, and unable to detect complex fraud rings. There is a critical need for a real-time, integrated platform that can analyze transactions from multiple dimensions simultaneously.

## What Was Implemented (Local Prototype)
- **Data Generation**: Simulated 1,000 realistic transactions with associated customers, accounts, devices, and merchants.
- **Rule Engine**: Heuristic-based detection (Velocity, Amount, Geo, Device).
- **Anomaly Detection**: Statistical Z-score and deviation analysis.
- **Graph Analysis**: NetworkX-based entity relationship mapping and fraud ring detection.
- **Risk Scoring**: Weighted aggregation of signals for final decisioning.
- **Case Management**: Automated generation of fraud cases for review.
- **EventBus Simulation**: Kafka-style in-process topics, event envelopes, and JSONL event logging.
- **CLI & Reporting**: Tools for running simulations and viewing summary results.

## Local Prototype Architecture
The prototype is implemented in Python, using:
- **Pandas**: For high-performance data manipulation.
- **NetworkX**: For graph-based entity analysis.
- **Pydantic**: For data validation and modeling.
- **In-process EventBus**: For local event-driven flow without Kafka runtime.
- **Pytest**: For ensuring logic correctness.

## Target Microservices Architecture
The production design (documented in `docs/`) moves to:
- **Apache Kafka**: For low-latency event streaming.
- **Microservices**: Decoupled services for Rules, Anomalies, Graph, and Scoring.
- **Neo4j**: For persistent and scalable graph analysis.
- **Kubernetes**: For container orchestration and scaling.

## Key Approaches
- **Rule Engine**: Dynamic registry of rules for instant updates.
- **Anomaly Detection**: Transitions from statistical prototypes to ML-based inference.
- **Graph Analysis**: Detects "mule accounts" and "fraud rings" through multi-hop relationship queries.
- **Risk Scoring**: Weighted model (50% Rules, 25% Anomalies, 25% Graph).
- **Event Contracts**: Events use `event_id`, `event_type`, `timestamp`, `correlation_id`, `source_service`, and `payload` fields so local EventBus topics can map to production Kafka topics.

## Kafka Deployment Status
Kafka is designed as the production event backbone but is not deployed in the local prototype. The current implementation uses a lightweight EventBus that simulates topics such as `transaction.events`, `rule.hit.events`, `anomaly.alert.events`, `graph.alert.events`, `risk.score.events`, `fraud.case.events`, and `audit.events`.

This is intentional: it avoids unnecessary local infrastructure, keeps the assignment runnable without Docker, validates event-driven service boundaries, and provides a clear path to replacing the EventBus with Kafka producers and consumers later.

## Validation Results (Phase 1)
The simulation produced the following metrics:
- **Total Transactions**: 1,000
- **Approved**: 938
- **Review**: 56
- **Blocked**: 6
- **Rule Hits**: 109
- **Anomaly Alerts**: 86
- **Graph Alerts**: 3
- **Fraud Cases**: 62
- **Average Risk Score**: 4.42
- **Unit Tests**: pytest suite passes.

## Limitations
- **Prototype Scale**: Currently limited to in-memory processing.
- **Kafka Runtime**: Kafka is not deployed locally; the EventBus is a simulation layer.
- **Statistical Simplicity**: Anomaly detection uses basic statistics; production requires ML.
- **Simulation Fidelity**: Real-world data may contain more noise and missing fields.

## Future Roadmap
- **ML Integration**: Implement Isolation Forest models for better anomaly detection.
- **Graph Neural Networks**: Automate suspicious cluster detection using GNNs.
- **Real-Time UI**: Build a React-based investigation dashboard.
- **Load Testing**: Validate 5,000 TPS targets on Kubernetes.

## GitHub Repository
INSERT_GITHUB_REPO_LINK_HERE
