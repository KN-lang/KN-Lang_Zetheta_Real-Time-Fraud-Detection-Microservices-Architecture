from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd


class CaseManager:
    def create_cases(self, risk_scores: pd.DataFrame) -> pd.DataFrame:
        candidates = risk_scores[risk_scores["decision"].isin(["REVIEW", "BLOCK"])].copy()
        rows = []
        created_at = datetime.now(timezone.utc).isoformat()
        for n, row in enumerate(candidates.sort_values("risk_score", ascending=False).itertuples(index=False), start=1):
            rows.append(
                {
                    "case_id": f"CASE-{n:06d}",
                    "transaction_id": row.transaction_id,
                    "customer_id": row.customer_id,
                    "risk_score": row.risk_score,
                    "decision": row.decision,
                    "reason": row.reason,
                    "priority": self.priority_for(row.risk_score),
                    "created_at": created_at,
                    "status": "OPEN",
                }
            )
        return pd.DataFrame(rows, columns=["case_id", "transaction_id", "customer_id", "risk_score", "decision", "reason", "priority", "created_at", "status"])

    @staticmethod
    def priority_for(score: float) -> str:
        if score >= 90:
            return "CRITICAL"
        if score >= 70:
            return "HIGH"
        if score >= 50:
            return "MEDIUM"
        return "LOW"
