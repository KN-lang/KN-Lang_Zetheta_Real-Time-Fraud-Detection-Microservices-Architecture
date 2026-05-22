from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class TransactionType(StrEnum):
    UPI = "UPI"
    CARD = "CARD"
    NEFT = "NEFT"
    RTGS = "RTGS"
    WALLET = "WALLET"


class Channel(StrEnum):
    MOBILE = "MOBILE"
    WEB = "WEB"
    ATM = "ATM"
    POS = "POS"
    API = "API"


class Status(StrEnum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    PENDING = "PENDING"


class Decision(StrEnum):
    APPROVE = "APPROVE"
    REVIEW = "REVIEW"
    BLOCK = "BLOCK"


class Transaction(BaseModel):
    transaction_id: str
    customer_id: str
    account_id: str
    merchant_id: str
    device_id: str
    ip_address: str
    amount: float = Field(ge=0)
    currency: str = "INR"
    transaction_type: TransactionType
    channel: Channel
    country: str
    timestamp: datetime
    status: Status
