from __future__ import annotations

import pandas as pd

from fraud_platform.anomaly.anomaly_detector import AnomalyDetector


def test_anomaly_score_generation():
    amounts = [1000] * 30 + [100000]
    df = pd.DataFrame(
        [
            {
                "transaction_id": f"T{i}",
                "customer_id": "C1" if i < 30 else "C2",
                "account_id": "A1",
                "merchant_id": "M1",
                "device_id": "D1",
                "ip_address": "10.0.0.1",
                "amount": amount,
                "currency": "INR",
                "transaction_type": "UPI",
                "channel": "MOBILE",
                "country": "IN",
                "timestamp": "2026-05-01T10:00:00",
                "status": "SUCCESS",
            }
            for i, amount in enumerate(amounts)
        ]
    )
    alerts = AnomalyDetector().detect(df)
    assert not alerts.empty
    assert alerts["anomaly_score"].max() > 0
