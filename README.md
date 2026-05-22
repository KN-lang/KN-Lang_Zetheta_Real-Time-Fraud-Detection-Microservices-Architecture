# Real-Time Fraud Detection Microservices Architecture

Local Phase 1 prototype for a fintech fraud detection platform. It simulates transaction streams, applies rule checks, statistical anomaly detection, graph relationship analysis, risk scoring, and fraud case creation.

This is a lightweight Python foundation, not a production distributed system.

## Architecture

- `simulation`: deterministic synthetic transactions and relationship data
- `rules`: configurable rule engine backed by `config/rules.yaml`
- `anomaly`: statistical amount outlier detection
- `graph`: NetworkX relationship graph and entity-risk alerts
- `scoring`: weighted risk score aggregation
- `cases`: case creation for review/block decisions
- `reports`: CSV, JSON, and audit report writing
- `events`: Kafka-style in-process EventBus, event envelopes, and JSONL event logging
- `cli`: Typer command interface

The package layout is microservices-inspired so each domain can later become its own event-driven service.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Commands

```bash
python -m fraud_platform generate-data --records 1000
python -m fraud_platform score-transactions --transactions data/generated/transactions.csv --output data/output
python -m fraud_platform simulate-attack --attack-type velocity
python -m fraud_platform run-pipeline --records 1000
python -m fraud_platform run-event-pipeline --records 1000
pytest
```

## Why Kafka Is Designed But Not Deployed Locally

Kafka is the target production event backbone for the platform, but the local prototype intentionally does not require a Kafka broker, Docker, or distributed infrastructure. Instead, the project includes an in-process `EventBus` that simulates topic-based communication with the same service boundaries used in the production design.

The local EventBus publishes events to topics such as `transaction.events`, `rule.hit.events`, `anomaly.alert.events`, `graph.alert.events`, `risk.score.events`, `fraud.case.events`, and `audit.events`. It also writes `data/output/event_log.jsonl` so the event flow can be inspected and replay concepts can be discussed.

This keeps the prototype easy to run, validates the event-driven fraud detection logic, and gives a straightforward migration path to Kafka topics later. The event schemas and event envelope model define the contract that a production Kafka deployment would use.

## Generated Data

`data/generated/` contains:

- `transactions.csv`
- `customers.csv`
- `accounts.csv`
- `devices.csv`
- `merchants.csv`
- `relationships.csv`

The generator intentionally includes high-amount transactions, velocity fraud, failed attempts, unusual countries, new-device high-value transactions, merchant bursts, mule accounts, shared devices, shared IPs, and round-amount transfers.

## Output Reports

`data/output/` contains:

- `risk_scores.csv`
- `fraud_cases.csv`
- `rule_hits.csv`
- `graph_alerts.csv`
- `anomaly_alerts.csv`
- `summary.json`
- `event_log.jsonl`
- `event_pipeline_summary.json`
- `audit_log.csv`

## Sample Output

`summary.json` includes total transactions, decision counts, alert counts, case counts, average risk score, and generation timestamp.

Decisions:

- `APPROVE`: risk score 0-39
- `REVIEW`: risk score 40-69
- `BLOCK`: risk score 70-100

## Current Limitations

- Local batch and in-process event simulation only
- No deployed Kafka broker yet
- No persistent database
- No model registry or online ML serving
- Graph analysis uses in-memory NetworkX
- Rules are intentionally simple for assignment clarity

## Roadmap

1. Add Kafka topic contracts and event schemas.
2. Serve trained ML models behind a scoring API.
3. Move graph relationships into Neo4j or another graph store.
4. Split modules into deployable microservices.
5. Add observability, replay, and operational controls.
