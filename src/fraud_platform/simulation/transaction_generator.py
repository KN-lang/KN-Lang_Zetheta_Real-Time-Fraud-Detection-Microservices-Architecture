from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd


TRANSACTION_TYPES = ["UPI", "CARD", "NEFT", "RTGS", "WALLET"]
CHANNELS = ["MOBILE", "WEB", "ATM", "POS", "API"]
STATUSES = ["SUCCESS", "FAILED", "PENDING"]
COUNTRIES = ["IN", "US", "GB", "SG", "AE"]
HIGH_RISK_COUNTRIES = ["NG", "KP", "IR", "RU", "CN"]


def generate_sample_data(records: int = 1000, output_dir: str | Path = "data/generated", seed: int = 42) -> dict[str, Path]:
    rng = np.random.default_rng(seed)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    customer_count = max(60, records // 8)
    account_count = customer_count + max(20, records // 20)
    device_count = max(customer_count * 3, records // 2)
    merchant_count = max(30, records // 18)

    customers = pd.DataFrame(
        {
            "customer_id": [f"C{i:04d}" for i in range(customer_count)],
            "name": [f"Customer {i:04d}" for i in range(customer_count)],
            "segment": rng.choice(["RETAIL", "SME", "PREMIUM"], customer_count, p=[0.72, 0.18, 0.10]),
            "home_country": "IN",
            "created_at": [(datetime(2025, 1, 1) + timedelta(days=int(i % 365))).isoformat() for i in range(customer_count)],
        }
    )
    accounts = pd.DataFrame(
        {
            "account_id": [f"A{i:04d}" for i in range(account_count)],
            "customer_id": [f"C{int(i % customer_count):04d}" for i in range(account_count)],
            "account_type": rng.choice(["SAVINGS", "CURRENT", "WALLET"], account_count, p=[0.65, 0.25, 0.10]),
            "opened_at": [(datetime(2025, 2, 1) + timedelta(days=int(i % 300))).isoformat() for i in range(account_count)],
        }
    )
    devices = pd.DataFrame(
        {
            "device_id": [f"D{i:04d}" for i in range(device_count)],
            "device_type": rng.choice(["ANDROID", "IOS", "WEB_BROWSER", "ATM_TERMINAL"], device_count),
            "first_seen_at": [(datetime(2025, 3, 1) + timedelta(days=int(i % 250))).isoformat() for i in range(device_count)],
        }
    )
    merchants = pd.DataFrame(
        {
            "merchant_id": [f"M{i:04d}" for i in range(merchant_count)],
            "merchant_category": rng.choice(["GROCERY", "TRAVEL", "GAMING", "CRYPTO", "ECOMMERCE"], merchant_count),
            "country": rng.choice(COUNTRIES, merchant_count),
        }
    )

    start = datetime(2026, 5, 1, 9, 0, 0)
    customer_profiles = {
        f"C{i:04d}": {
            "device_id": f"D{int(i % device_count):04d}",
            "ip_address": f"10.{int((i % 200) + 1)}.{int((i * 7 % 200) + 1)}.{int((i * 13 % 200) + 1)}",
        }
        for i in range(customer_count)
    }
    txns: list[dict[str, object]] = []
    for i in range(records):
        customer_id = f"C{int(rng.integers(customer_count)):04d}"
        customer_accounts = accounts.loc[accounts["customer_id"] == customer_id, "account_id"].tolist()
        amount = round(float(rng.lognormal(mean=8.3, sigma=0.85)), 2)
        profile = customer_profiles[customer_id]
        device_id = profile["device_id"] if rng.random() < 0.88 else f"D{int(rng.integers(device_count)):04d}"
        ip_address = profile["ip_address"] if rng.random() < 0.92 else f"10.{int(rng.integers(1, 255))}.{int(rng.integers(1, 255))}.{int(rng.integers(1, 255))}"
        txns.append(
            {
                "transaction_id": f"T{i:06d}",
                "customer_id": customer_id,
                "account_id": rng.choice(customer_accounts),
                "merchant_id": f"M{int(rng.integers(merchant_count)):04d}",
                "device_id": device_id,
                "ip_address": ip_address,
                "amount": amount,
                "currency": "INR",
                "transaction_type": rng.choice(TRANSACTION_TYPES, p=[0.36, 0.32, 0.12, 0.06, 0.14]),
                "channel": rng.choice(CHANNELS, p=[0.46, 0.26, 0.06, 0.16, 0.06]),
                "country": rng.choice(COUNTRIES, p=[0.86, 0.04, 0.04, 0.04, 0.02]),
                "timestamp": (start + timedelta(minutes=int(rng.integers(0, 14 * 24 * 60)))).isoformat(),
                "status": rng.choice(STATUSES, p=[0.92, 0.06, 0.02]),
            }
        )

    df = pd.DataFrame(txns)
    df = _inject_fraud_patterns(df, accounts, customer_count, seed)
    relationships = _build_relationships(df)

    outputs = {
        "transactions": output_path / "transactions.csv",
        "customers": output_path / "customers.csv",
        "accounts": output_path / "accounts.csv",
        "devices": output_path / "devices.csv",
        "merchants": output_path / "merchants.csv",
        "relationships": output_path / "relationships.csv",
    }
    df.to_csv(outputs["transactions"], index=False)
    customers.to_csv(outputs["customers"], index=False)
    accounts.to_csv(outputs["accounts"], index=False)
    devices.to_csv(outputs["devices"], index=False)
    merchants.to_csv(outputs["merchants"], index=False)
    relationships.to_csv(outputs["relationships"], index=False)
    return outputs


def _inject_fraud_patterns(df: pd.DataFrame, accounts: pd.DataFrame, customer_count: int, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed + 99)
    df = df.copy()
    if df.empty:
        return df

    indices = list(df.index[: min(len(df), 90)])
    high_amount = indices[:10]
    df.loc[high_amount, "amount"] = [75000, 125000, 91000, 64000, 180000, 54000, 68000, 99000, 150000, 72000][: len(high_amount)]

    velocity_customer = "C0001"
    velocity_time = datetime(2026, 5, 10, 10, 0, 0)
    for offset, idx in enumerate(indices[10:18]):
        df.loc[idx, ["customer_id", "timestamp", "amount", "status"]] = [
            velocity_customer,
            (velocity_time + timedelta(minutes=offset)).isoformat(),
            float(4500 + offset * 250),
            "SUCCESS",
        ]

    for idx in indices[18:24]:
        df.loc[idx, ["customer_id", "status", "timestamp"]] = ["C0002", "FAILED", datetime(2026, 5, 11, 12, int(idx % 20)).isoformat()]

    for idx, country in zip(indices[24:32], HIGH_RISK_COUNTRIES * 2):
        df.loc[idx, "country"] = country

    shared_device = "D_SHARED_FRAUD"
    shared_ip = "203.0.113.77"
    for n, idx in enumerate(indices[32:48]):
        cid = f"C{(10 + n) % customer_count:04d}"
        df.loc[idx, ["customer_id", "device_id", "ip_address", "amount"]] = [cid, shared_device, shared_ip, float(12000 + n * 1000)]

    merchant_burst = "M0001"
    burst_time = datetime(2026, 5, 12, 16, 30, 0)
    for n, idx in enumerate(indices[48:58]):
        df.loc[idx, ["merchant_id", "timestamp", "amount"]] = [merchant_burst, (burst_time + timedelta(minutes=n)).isoformat(), float(9000 + n * 400)]

    mule_account = "A_MULE_001"
    for n, idx in enumerate(indices[58:70]):
        cid = f"C{(30 + n) % customer_count:04d}"
        df.loc[idx, ["customer_id", "account_id", "transaction_type", "amount"]] = [cid, mule_account, "UPI", float(10000 + (n % 3) * 5000)]

    for idx in indices[70:82]:
        df.loc[idx, ["amount", "transaction_type"]] = [float(rng.choice([10000, 20000, 50000, 100000])), "UPI"]

    for idx in indices[82:90]:
        df.loc[idx, ["device_id", "amount", "timestamp"]] = [f"D_NEW_{idx}", float(45000 + int(idx) * 100), datetime(2026, 5, 13, 14, int(idx % 50)).isoformat()]

    account_lookup = accounts.groupby("customer_id")["account_id"].first().to_dict()
    df["account_id"] = [row.account_id if str(row.account_id).startswith("A_MULE") else account_lookup.get(row.customer_id, row.account_id) for row in df.itertuples()]
    return df


def _build_relationships(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for row in df.itertuples(index=False):
        rows.extend(
            [
                {"source_id": row.customer_id, "source_type": "customer", "target_id": row.account_id, "target_type": "account", "relationship": "OWNS"},
                {"source_id": row.customer_id, "source_type": "customer", "target_id": row.device_id, "target_type": "device", "relationship": "USES"},
                {"source_id": row.customer_id, "source_type": "customer", "target_id": row.ip_address, "target_type": "ip", "relationship": "CONNECTS_FROM"},
                {"source_id": row.customer_id, "source_type": "customer", "target_id": row.merchant_id, "target_type": "merchant", "relationship": "PAYS"},
                {"source_id": row.account_id, "source_type": "account", "target_id": row.transaction_id, "target_type": "transaction", "relationship": "HAS_TRANSACTION"},
            ]
        )
    return pd.DataFrame(rows).drop_duplicates()
