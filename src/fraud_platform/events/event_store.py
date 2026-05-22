from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fraud_platform.events.event_models import BaseEvent


class EventStore:
    def __init__(self, log_path: str | Path | None = None):
        self.log_path = Path(log_path) if log_path else None
        if self.log_path:
            self.log_path.parent.mkdir(parents=True, exist_ok=True)
            self.log_path.write_text("", encoding="utf-8")

    def append(self, topic: str, event: BaseEvent) -> None:
        if not self.log_path:
            return
        record: dict[str, Any] = {"topic": topic, **event.model_dump(mode="json")}
        with self.log_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record) + "\n")
