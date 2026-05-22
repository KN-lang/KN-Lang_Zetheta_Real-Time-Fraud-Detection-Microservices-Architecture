from __future__ import annotations

import pandas as pd


class RiskScorer:
    def score(self, transactions: pd.DataFrame, rule_hits: pd.DataFrame, anomaly_alerts: pd.DataFrame, graph_alerts: pd.DataFrame) -> pd.DataFrame:
        df = transactions[["transaction_id", "customer_id"]].copy()
        rule_scores = self._max_by_transaction(rule_hits, "score")
        anomaly_scores = self._max_by_transaction(anomaly_alerts, "anomaly_score")
        graph_scores = self._graph_scores(transactions, graph_alerts)
        df["rule_score"] = df["transaction_id"].map(rule_scores).fillna(0.0)
        df["anomaly_score"] = df["transaction_id"].map(anomaly_scores).fillna(0.0)
        df["graph_score"] = df["transaction_id"].map(graph_scores).fillna(0.0)
        df["risk_score"] = (df["rule_score"] * 0.50 + df["anomaly_score"] * 0.25 + df["graph_score"] * 0.25).round(2)
        df["decision"] = df["risk_score"].apply(self.decision_for_score)
        df["reason"] = df.apply(self._reason, axis=1)
        return df

    @staticmethod
    def decision_for_score(score: float) -> str:
        if score >= 70:
            return "BLOCK"
        if score >= 40:
            return "REVIEW"
        return "APPROVE"

    @staticmethod
    def _max_by_transaction(alerts: pd.DataFrame, score_column: str) -> dict[str, float]:
        if alerts.empty:
            return {}
        return alerts.groupby("transaction_id")[score_column].max().astype(float).to_dict()

    @staticmethod
    def _graph_scores(transactions: pd.DataFrame, graph_alerts: pd.DataFrame) -> dict[str, float]:
        if graph_alerts.empty:
            return {}
        scores: dict[str, float] = {}
        severity_score = {"LOW": 25.0, "MEDIUM": 55.0, "HIGH": 85.0, "CRITICAL": 100.0}
        for alert in graph_alerts.itertuples(index=False):
            txn_ids = [item for item in str(alert.related_transactions).split(",") if item and item != "nan"]
            for txn_id in txn_ids:
                scores[txn_id] = max(scores.get(txn_id, 0.0), severity_score.get(str(alert.severity), 50.0))
        return scores

    @staticmethod
    def _reason(row: pd.Series) -> str:
        drivers = []
        if row["rule_score"] > 0:
            drivers.append("rules")
        if row["anomaly_score"] > 0:
            drivers.append("anomalies")
        if row["graph_score"] > 0:
            drivers.append("graph")
        return "Signals: " + ", ".join(drivers) if drivers else "No material fraud signals"
