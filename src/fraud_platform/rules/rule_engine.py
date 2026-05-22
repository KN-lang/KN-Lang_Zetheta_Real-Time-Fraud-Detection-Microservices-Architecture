from __future__ import annotations

import pandas as pd


class RuleEngine:
    def __init__(self, config: dict):
        self.config = config
        self.rules = config.get("rules", {})
        self.high_risk_countries = set(config.get("high_risk_countries", []))

    def evaluate(self, transactions: pd.DataFrame) -> pd.DataFrame:
        if transactions.empty:
            return self._empty()
        df = transactions.copy()
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        hits: list[dict[str, object]] = []
        self._amount_rule(df, hits)
        self._failed_attempts_rule(df, hits)
        self._velocity_rule(df, hits)
        self._country_rule(df, hits)
        self._new_device_rule(df, hits)
        self._round_amount_rule(df, hits)
        self._same_ip_rule(df, hits)
        self._shared_device_rule(df, hits)
        return pd.DataFrame(hits) if hits else self._empty()

    def _add(self, hits: list[dict[str, object]], row, rule_id: str, reason: str) -> None:
        rule = self.rules[rule_id]
        hits.append(
            {
                "transaction_id": row.transaction_id,
                "rule_id": rule_id,
                "severity": rule["severity"],
                "reason": reason,
                "score": int(rule["score"]),
            }
        )

    def _amount_rule(self, df: pd.DataFrame, hits: list[dict[str, object]]) -> None:
        rule_id = "amount_greater_than_50000"
        threshold = self.rules[rule_id]["threshold"]
        for row in df[df["amount"] > threshold].itertuples():
            self._add(hits, row, rule_id, f"Amount {row.amount:.2f} exceeds {threshold}")

    def _failed_attempts_rule(self, df: pd.DataFrame, hits: list[dict[str, object]]) -> None:
        rule_id = "failed_attempts_more_than_3"
        rule = self.rules[rule_id]
        failed = df[df["status"] == "FAILED"].sort_values("timestamp")
        for _, group in failed.groupby("customer_id"):
            rolling = group.set_index("timestamp").rolling(f"{rule['window_minutes']}min")["transaction_id"].count()
            flagged_ids = group.loc[rolling.to_numpy() > rule["threshold"], "transaction_id"]
            for row in group[group["transaction_id"].isin(flagged_ids)].itertuples():
                self._add(hits, row, rule_id, f"More than {rule['threshold']} failed attempts in {rule['window_minutes']} minutes")

    def _velocity_rule(self, df: pd.DataFrame, hits: list[dict[str, object]]) -> None:
        rule_id = "velocity_more_than_5_txn_10_min"
        rule = self.rules[rule_id]
        for _, group in df.sort_values("timestamp").groupby("customer_id"):
            rolling = group.set_index("timestamp").rolling(f"{rule['window_minutes']}min")["transaction_id"].count()
            flagged_ids = group.loc[rolling.to_numpy() > rule["threshold"], "transaction_id"]
            for row in group[group["transaction_id"].isin(flagged_ids)].itertuples():
                self._add(hits, row, rule_id, f"More than {rule['threshold']} transactions in {rule['window_minutes']} minutes")

    def _country_rule(self, df: pd.DataFrame, hits: list[dict[str, object]]) -> None:
        rule_id = "high_risk_country"
        for row in df[df["country"].isin(self.high_risk_countries)].itertuples():
            self._add(hits, row, rule_id, f"Transaction originated from high-risk country {row.country}")

    def _new_device_rule(self, df: pd.DataFrame, hits: list[dict[str, object]]) -> None:
        rule_id = "new_device_high_amount"
        threshold = self.rules[rule_id]["amount_threshold"]
        first_seen = df.groupby(["customer_id", "device_id"])["timestamp"].transform("min")
        mask = (df["timestamp"] == first_seen) & (df["amount"] > threshold)
        for row in df[mask].itertuples():
            self._add(hits, row, rule_id, f"First observed device used for amount above {threshold}")

    def _round_amount_rule(self, df: pd.DataFrame, hits: list[dict[str, object]]) -> None:
        rule_id = "round_amount_transfer"
        rule = self.rules[rule_id]
        mask = (df["amount"] >= rule["min_amount"]) & (df["amount"] % rule["modulo"] == 0) & df["transaction_type"].isin(["UPI", "NEFT", "RTGS"])
        for row in df[mask].itertuples():
            self._add(hits, row, rule_id, f"Round amount transfer divisible by {rule['modulo']}")

    def _same_ip_rule(self, df: pd.DataFrame, hits: list[dict[str, object]]) -> None:
        rule_id = "same_ip_many_customers"
        threshold = self.rules[rule_id]["threshold"]
        risky_ips = df.groupby("ip_address")["customer_id"].nunique()
        risky_ips = set(risky_ips[risky_ips > threshold].index)
        for row in df[df["ip_address"].isin(risky_ips)].itertuples():
            self._add(hits, row, rule_id, f"IP used by more than {threshold} customers")

    def _shared_device_rule(self, df: pd.DataFrame, hits: list[dict[str, object]]) -> None:
        rule_id = "shared_device_many_customers"
        threshold = self.rules[rule_id]["threshold"]
        risky_devices = df.groupby("device_id")["customer_id"].nunique()
        risky_devices = set(risky_devices[risky_devices > threshold].index)
        for row in df[df["device_id"].isin(risky_devices)].itertuples():
            self._add(hits, row, rule_id, f"Device used by more than {threshold} customers")

    @staticmethod
    def _empty() -> pd.DataFrame:
        return pd.DataFrame(columns=["transaction_id", "rule_id", "severity", "reason", "score"])
