from __future__ import annotations

import pandas as pd

from fraud_platform.graph.graph_analyzer import GraphAnalyzer


def test_graph_shared_device_ip_detection():
    df = pd.DataFrame(
        [
            {
                "transaction_id": f"T{i}",
                "customer_id": f"C{i}",
                "account_id": f"A{i}",
                "merchant_id": "M1",
                "device_id": "D_SHARED",
                "ip_address": "203.0.113.8",
                "amount": 1000,
                "currency": "INR",
                "transaction_type": "UPI",
                "channel": "MOBILE",
                "country": "IN",
                "timestamp": "2026-05-01T10:00:00",
                "status": "SUCCESS",
            }
            for i in range(7)
        ]
    )
    _, alerts = GraphAnalyzer(shared_device_threshold=4, shared_ip_threshold=5).analyze(df)
    assert {"SHARED_DEVICE", "SHARED_IP"}.issubset(set(alerts["alert_type"]))
