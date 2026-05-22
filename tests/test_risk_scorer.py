from __future__ import annotations

import pandas as pd

from fraud_platform.cases.case_manager import CaseManager
from fraud_platform.scoring.risk_scorer import RiskScorer


def test_risk_scoring_decision_thresholds():
    assert RiskScorer.decision_for_score(39) == "APPROVE"
    assert RiskScorer.decision_for_score(40) == "REVIEW"
    assert RiskScorer.decision_for_score(70) == "BLOCK"


def test_case_generation_for_review_and_block():
    risk_scores = pd.DataFrame(
        [
            {"transaction_id": "T1", "customer_id": "C1", "risk_score": 39, "decision": "APPROVE", "reason": "none"},
            {"transaction_id": "T2", "customer_id": "C2", "risk_score": 50, "decision": "REVIEW", "reason": "rules"},
            {"transaction_id": "T3", "customer_id": "C3", "risk_score": 90, "decision": "BLOCK", "reason": "rules"},
        ]
    )
    cases = CaseManager().create_cases(risk_scores)
    assert len(cases) == 2
    assert set(cases["decision"]) == {"REVIEW", "BLOCK"}
