from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


class ReportWriter:
    def write(
        self,
        output_dir: str | Path,
        risk_scores: pd.DataFrame,
        fraud_cases: pd.DataFrame,
        rule_hits: pd.DataFrame,
        anomaly_alerts: pd.DataFrame,
        graph_alerts: pd.DataFrame,
        total_transactions: int,
    ) -> dict[str, Path]:
        output = Path(output_dir)
        output.mkdir(parents=True, exist_ok=True)
        paths = {
            "risk_scores": output / "risk_scores.csv",
            "fraud_cases": output / "fraud_cases.csv",
            "rule_hits": output / "rule_hits.csv",
            "anomaly_alerts": output / "anomaly_alerts.csv",
            "graph_alerts": output / "graph_alerts.csv",
            "summary": output / "summary.json",
            "audit_log": output / "audit_log.csv",
        }
        risk_scores.to_csv(paths["risk_scores"], index=False)
        fraud_cases.to_csv(paths["fraud_cases"], index=False)
        rule_hits.to_csv(paths["rule_hits"], index=False)
        anomaly_alerts.to_csv(paths["anomaly_alerts"], index=False)
        graph_alerts.to_csv(paths["graph_alerts"], index=False)
        summary = self._summary(risk_scores, fraud_cases, rule_hits, anomaly_alerts, graph_alerts, total_transactions)
        paths["summary"].write_text(json.dumps(summary, indent=2), encoding="utf-8")
        self._audit_log(risk_scores, rule_hits, anomaly_alerts, graph_alerts).to_csv(paths["audit_log"], index=False)
        return paths

    @staticmethod
    def _summary(
        risk_scores: pd.DataFrame,
        fraud_cases: pd.DataFrame,
        rule_hits: pd.DataFrame,
        anomaly_alerts: pd.DataFrame,
        graph_alerts: pd.DataFrame,
        total_transactions: int,
    ) -> dict[str, object]:
        counts = risk_scores["decision"].value_counts().to_dict() if not risk_scores.empty else {}
        return {
            "total_transactions": int(total_transactions),
            "approved_count": int(counts.get("APPROVE", 0)),
            "review_count": int(counts.get("REVIEW", 0)),
            "blocked_count": int(counts.get("BLOCK", 0)),
            "rule_hit_count": int(len(rule_hits)),
            "anomaly_count": int(len(anomaly_alerts)),
            "graph_alert_count": int(len(graph_alerts)),
            "fraud_case_count": int(len(fraud_cases)),
            "average_risk_score": round(float(risk_scores["risk_score"].mean()), 2) if not risk_scores.empty else 0.0,
            "generated_at": datetime.now(timezone.utc).isoformat(),
        }

    @staticmethod
    def _audit_log(risk_scores: pd.DataFrame, rule_hits: pd.DataFrame, anomaly_alerts: pd.DataFrame, graph_alerts: pd.DataFrame) -> pd.DataFrame:
        rows = []
        now = datetime.now(timezone.utc).isoformat()
        for row in risk_scores.itertuples(index=False):
            rows.append({"timestamp": now, "event_type": "RISK_SCORE", "entity_id": row.transaction_id, "details": f"{row.decision} risk_score={row.risk_score}"})
        for row in rule_hits.itertuples(index=False):
            rows.append({"timestamp": now, "event_type": "RULE_HIT", "entity_id": row.transaction_id, "details": f"{row.rule_id} score={row.score}"})
        for row in anomaly_alerts.itertuples(index=False):
            rows.append({"timestamp": now, "event_type": "ANOMALY_ALERT", "entity_id": row.transaction_id, "details": f"{row.anomaly_type} score={row.anomaly_score}"})
        for row in graph_alerts.itertuples(index=False):
            rows.append({"timestamp": now, "event_type": "GRAPH_ALERT", "entity_id": row.entity_id, "details": f"{row.alert_type} severity={row.severity}"})
        return pd.DataFrame(rows, columns=["timestamp", "event_type", "entity_id", "details"])
