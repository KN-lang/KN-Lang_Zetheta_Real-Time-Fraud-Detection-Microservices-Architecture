from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, ClassVar
from uuid import uuid4

from pydantic import BaseModel, Field, model_validator


class BaseEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid4()))
    event_type: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    correlation_id: str
    source_service: str
    payload: dict[str, Any]

    required_payload_fields: ClassVar[set[str]] = set()

    @model_validator(mode="after")
    def validate_payload_shape(self) -> "BaseEvent":
        missing = self.required_payload_fields.difference(self.payload)
        if missing:
            missing_list = ", ".join(sorted(missing))
            raise ValueError(f"{self.event_type} payload missing required fields: {missing_list}")
        return self


class TransactionEvent(BaseEvent):
    event_type: str = "TransactionEvent"
    required_payload_fields: ClassVar[set[str]] = {"transaction_id", "customer_id", "amount", "timestamp"}


class RuleHitEvent(BaseEvent):
    event_type: str = "RuleHitEvent"
    required_payload_fields: ClassVar[set[str]] = {"transaction_id", "rule_id", "severity", "score"}


class AnomalyAlertEvent(BaseEvent):
    event_type: str = "AnomalyAlertEvent"
    required_payload_fields: ClassVar[set[str]] = {"transaction_id", "anomaly_type", "anomaly_score"}


class GraphAlertEvent(BaseEvent):
    event_type: str = "GraphAlertEvent"
    required_payload_fields: ClassVar[set[str]] = {"entity_id", "alert_type", "severity", "related_transactions"}


class RiskScoreEvent(BaseEvent):
    event_type: str = "RiskScoreEvent"
    required_payload_fields: ClassVar[set[str]] = {"transaction_id", "customer_id", "risk_score", "decision"}


class FraudCaseEvent(BaseEvent):
    event_type: str = "FraudCaseEvent"
    required_payload_fields: ClassVar[set[str]] = {"case_id", "transaction_id", "customer_id", "risk_score", "decision"}


class AuditEvent(BaseEvent):
    event_type: str = "AuditEvent"
    required_payload_fields: ClassVar[set[str]] = {"action", "entity_id", "details"}
