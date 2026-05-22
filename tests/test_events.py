from __future__ import annotations

import json

import pandas as pd
import pytest
from pydantic import ValidationError

from fraud_platform.events.event_bus import EventBus
from fraud_platform.events.event_handlers import run_event_pipeline
from fraud_platform.events.event_models import TransactionEvent
from fraud_platform.events.event_store import EventStore
from fraud_platform.simulation.transaction_generator import generate_sample_data


def test_event_creation_validates_required_payload_fields():
    event = TransactionEvent(
        correlation_id="T1",
        source_service="test",
        payload={"transaction_id": "T1", "customer_id": "C1", "amount": 100.0, "timestamp": "2026-05-01T10:00:00"},
    )
    assert event.event_type == "TransactionEvent"
    assert event.payload["transaction_id"] == "T1"

    with pytest.raises(ValidationError):
        TransactionEvent(correlation_id="T2", source_service="test", payload={"transaction_id": "T2"})


def test_event_bus_publish_subscribe():
    bus = EventBus()
    received = []

    bus.subscribe("transaction.events", lambda topic, event: received.append((topic, event.event_id)))
    event = TransactionEvent(
        correlation_id="T1",
        source_service="test",
        payload={"transaction_id": "T1", "customer_id": "C1", "amount": 100.0, "timestamp": "2026-05-01T10:00:00"},
    )
    bus.publish("transaction.events", event)

    assert bus.event_count() == 1
    assert received == [("transaction.events", event.event_id)]


def test_event_log_writing(tmp_path):
    log_path = tmp_path / "event_log.jsonl"
    bus = EventBus(EventStore(log_path))
    event = TransactionEvent(
        correlation_id="T1",
        source_service="test",
        payload={"transaction_id": "T1", "customer_id": "C1", "amount": 100.0, "timestamp": "2026-05-01T10:00:00"},
    )
    bus.publish("transaction.events", event)

    lines = log_path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 1
    assert json.loads(lines[0])["topic"] == "transaction.events"


def test_run_event_pipeline_smoke(tmp_path):
    generated = tmp_path / "generated"
    output = tmp_path / "output"
    generate_sample_data(records=25, output_dir=generated, seed=7)
    transactions = pd.read_csv(generated / "transactions.csv")

    paths = run_event_pipeline(transactions, output)

    summary = json.loads(paths["event_pipeline_summary"].read_text(encoding="utf-8"))
    assert summary["transactions_processed"] == 25
    assert summary["risk_scores_generated"] == 25
    assert "transaction.events" in summary["topics_used"]
    assert paths["event_log"].exists()
