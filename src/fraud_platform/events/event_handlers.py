from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from fraud_platform.anomaly.anomaly_detector import AnomalyDetector
from fraud_platform.cases.case_manager import CaseManager
from fraud_platform.config import load_rules_config
from fraud_platform.events.event_bus import EventBus
from fraud_platform.events.event_models import (
    AnomalyAlertEvent,
    AuditEvent,
    FraudCaseEvent,
    GraphAlertEvent,
    RiskScoreEvent,
    RuleHitEvent,
    TransactionEvent,
)
from fraud_platform.events.event_store import EventStore
from fraud_platform.graph.graph_analyzer import GraphAnalyzer
from fraud_platform.reports.report_writer import ReportWriter
from fraud_platform.rules.rule_engine import RuleEngine
from fraud_platform.scoring.risk_scorer import RiskScorer

TRANSACTION_TOPIC = "transaction.events"
RULE_HIT_TOPIC = "rule.hit.events"
ANOMALY_ALERT_TOPIC = "anomaly.alert.events"
GRAPH_ALERT_TOPIC = "graph.alert.events"
RISK_SCORE_TOPIC = "risk.score.events"
FRAUD_CASE_TOPIC = "fraud.case.events"
AUDIT_TOPIC = "audit.events"


def run_event_pipeline(transactions: pd.DataFrame, output_dir: str | Path, rules_path: str | Path = "config/rules.yaml") -> dict[str, Path]:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    bus = EventBus(EventStore(output / "event_log.jsonl"))
    audit_counter = {"events": 0}

    def audit_handler(topic: str, event) -> None:
        if topic == AUDIT_TOPIC:
            return
        audit_counter["events"] += 1
        entity_id = str(event.payload.get("transaction_id") or event.payload.get("case_id") or event.payload.get("entity_id", "unknown"))
        bus.publish(
            AUDIT_TOPIC,
            AuditEvent(
                correlation_id=event.correlation_id,
                source_service="event-bus",
                payload={"action": "EVENT_PUBLISHED", "entity_id": entity_id, "details": f"{event.event_type} published to {topic}"},
            ),
        )

    for topic in [TRANSACTION_TOPIC, RULE_HIT_TOPIC, ANOMALY_ALERT_TOPIC, GRAPH_ALERT_TOPIC, RISK_SCORE_TOPIC, FRAUD_CASE_TOPIC]:
        bus.subscribe(topic, audit_handler)

    for row in transactions.itertuples(index=False):
        payload = _clean_payload(row._asdict())
        bus.publish(
            TRANSACTION_TOPIC,
            TransactionEvent(
                correlation_id=str(payload["transaction_id"]),
                source_service="transaction-generator",
                payload=payload,
            ),
        )

    config = load_rules_config(rules_path)
    rule_hits = RuleEngine(config).evaluate(transactions)
    anomaly_alerts = AnomalyDetector().detect(transactions)
    _, graph_alerts = GraphAnalyzer(
        shared_device_threshold=config["rules"]["shared_device_many_customers"]["threshold"],
        shared_ip_threshold=config["rules"]["same_ip_many_customers"]["threshold"],
    ).analyze(transactions)
    risk_scores = RiskScorer().score(transactions, rule_hits, anomaly_alerts, graph_alerts)
    fraud_cases = CaseManager().create_cases(risk_scores)

    _publish_dataframe(bus, RULE_HIT_TOPIC, RuleHitEvent, rule_hits, "rule-engine")
    _publish_dataframe(bus, ANOMALY_ALERT_TOPIC, AnomalyAlertEvent, anomaly_alerts, "anomaly-detector")
    _publish_dataframe(bus, GRAPH_ALERT_TOPIC, GraphAlertEvent, graph_alerts, "graph-analyzer", "entity_id")
    _publish_dataframe(bus, RISK_SCORE_TOPIC, RiskScoreEvent, risk_scores, "risk-scorer")
    _publish_dataframe(bus, FRAUD_CASE_TOPIC, FraudCaseEvent, fraud_cases, "case-manager")

    report_paths = ReportWriter().write(output, risk_scores, fraud_cases, rule_hits, anomaly_alerts, graph_alerts, len(transactions))
    summary = {
        "event_count": bus.event_count(),
        "topics_used": bus.topics_used(),
        "transactions_processed": int(len(transactions)),
        "risk_scores_generated": int(len(risk_scores)),
        "fraud_cases_generated": int(len(fraud_cases)),
        "rule_hit_events": int(len(rule_hits)),
        "anomaly_alert_events": int(len(anomaly_alerts)),
        "graph_alert_events": int(len(graph_alerts)),
        "audit_events": int(len(bus.events.get(AUDIT_TOPIC, []))),
        "event_log_path": str(output / "event_log.jsonl"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    summary_path = output / "event_pipeline_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    report_paths["event_log"] = output / "event_log.jsonl"
    report_paths["event_pipeline_summary"] = summary_path
    return report_paths


def _publish_dataframe(
    bus: EventBus,
    topic: str,
    event_cls: type,
    frame: pd.DataFrame,
    source_service: str,
    correlation_field: str = "transaction_id",
) -> None:
    for row in frame.itertuples(index=False):
        payload = _clean_payload(row._asdict())
        bus.publish(
            topic,
            event_cls(
                correlation_id=str(payload.get(correlation_field, payload.get("transaction_id", payload.get("case_id", "unknown")))),
                source_service=source_service,
                payload=payload,
            ),
        )


def _clean_payload(payload: dict[str, Any]) -> dict[str, Any]:
    cleaned: dict[str, Any] = {}
    for key, value in payload.items():
        if pd.isna(value):
            cleaned[key] = None
        elif hasattr(value, "isoformat"):
            cleaned[key] = value.isoformat()
        else:
            cleaned[key] = value
    return cleaned
