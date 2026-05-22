from __future__ import annotations

import numpy as np
import pandas as pd


class AnomalyDetector:
    def detect(self, transactions: pd.DataFrame) -> pd.DataFrame:
        if transactions.empty:
            return self._empty()
        df = transactions.copy()
        alerts: list[dict[str, object]] = []
        global_mean = float(df["amount"].mean())
        global_std = float(df["amount"].std(ddof=0)) or 1.0
        customer_avg = df.groupby("customer_id")["amount"].transform("mean").replace(0, np.nan)
        df["global_z"] = (df["amount"] - global_mean) / global_std
        df["customer_ratio"] = (df["amount"] / customer_avg).fillna(0)

        for row in df[df["global_z"] >= 2.5].itertuples():
            score = min(100.0, max(0.0, float(row.global_z) * 20.0))
            alerts.append(
                {
                    "transaction_id": row.transaction_id,
                    "anomaly_type": "GLOBAL_AMOUNT_ZSCORE",
                    "anomaly_score": round(score, 2),
                    "reason": f"Amount z-score {row.global_z:.2f} is unusually high",
                }
            )

        for row in df[(df["customer_ratio"] >= 3.0) & (df["amount"] >= 10000)].itertuples():
            score = min(100.0, float(row.customer_ratio) * 18.0)
            alerts.append(
                {
                    "transaction_id": row.transaction_id,
                    "anomaly_type": "CUSTOMER_AMOUNT_DEVIATION",
                    "anomaly_score": round(score, 2),
                    "reason": f"Amount is {row.customer_ratio:.1f}x customer average",
                }
            )

        return pd.DataFrame(alerts).drop_duplicates() if alerts else self._empty()

    @staticmethod
    def _empty() -> pd.DataFrame:
        return pd.DataFrame(columns=["transaction_id", "anomaly_type", "anomaly_score", "reason"])
