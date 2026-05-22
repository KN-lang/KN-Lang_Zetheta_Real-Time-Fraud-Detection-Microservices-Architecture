from __future__ import annotations

from collections import defaultdict
from typing import Callable

from fraud_platform.events.event_models import BaseEvent
from fraud_platform.events.event_store import EventStore

EventHandler = Callable[[str, BaseEvent], None]


class EventBus:
    def __init__(self, event_store: EventStore | None = None):
        self.event_store = event_store
        self.events: dict[str, list[BaseEvent]] = defaultdict(list)
        self.handlers: dict[str, list[EventHandler]] = defaultdict(list)

    def publish(self, topic: str, event: BaseEvent) -> None:
        self.events[topic].append(event)
        if self.event_store:
            self.event_store.append(topic, event)
        for handler in self.handlers.get(topic, []):
            handler(topic, event)

    def subscribe(self, topic: str, handler: EventHandler) -> None:
        self.handlers[topic].append(handler)

    def event_count(self) -> int:
        return sum(len(events) for events in self.events.values())

    def topics_used(self) -> list[str]:
        return sorted(topic for topic, events in self.events.items() if events)
