from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


DEFAULT_RULES_PATH = Path("config/rules.yaml")


def load_rules_config(path: str | Path = DEFAULT_RULES_PATH) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)
