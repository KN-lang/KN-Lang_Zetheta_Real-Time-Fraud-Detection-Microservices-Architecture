from __future__ import annotations

import pandas as pd

from fraud_platform.config import load_rules_config
from fraud_platform.rules.rule_engine import RuleEngine


def test_rule_engine_detects_high_amount():
    df = pd.DataFrame(
        [
            {
                "transaction_id": "T1",
                "customer_id": "C1",
                "account_id": "A1",
                "merchant_id": "M1",
                "device_id": "D1",
                "ip_address": "10.0.0.1",
                "amount": 75000,
                "currency": "INR",
                "transaction_type": "UPI",
                "channel": "MOBILE",
                "country": "IN",
                "timestamp": "2026-05-01T10:00:00",
                "status": "SUCCESS",
            }
        ]
    )
    hits = RuleEngine(load_rules_config()).evaluate(df)
    assert "amount_greater_than_50000" in set(hits["rule_id"])


def test_velocity_rule_detection():
    rows = []
    for i in range(6):
        rows.append(
            {
                "transaction_id": f"T{i}",
                "customer_id": "C1",
                "account_id": "A1",
                "merchant_id": "M1",
                "device_id": f"D{i}",
                "ip_address": f"10.0.0.{i}",
                "amount": 1000,
                "currency": "INR",
                "transaction_type": "UPI",
                "channel": "MOBILE",
                "country": "IN",
                "timestamp": f"2026-05-01T10:0{i}:00",
                "status": "SUCCESS",
            }
        )
    hits = RuleEngine(load_rules_config()).evaluate(pd.DataFrame(rows))
    assert "velocity_more_than_5_txn_10_min" in set(hits["rule_id"])
