# Day 09 - Graph Database Schema

Neo4j supports relationship-first fraud detection where fraud rings are visible through shared devices, contact details, IP addresses, beneficiaries, merchants, and transaction paths.

## Required Node Types

| Node | Key | Purpose |
| --- | --- | --- |
| `Card` | `card_token` | Tokenized payment card or instrument. |
| `Customer` | `customer_id` | KYC customer entity. |
| `Device` | `device_id` | Device fingerprint used during sessions. |
| `IP` | `ip_address` | Network source and proxy/VPN indicator. |
| `Phone` | `phone_hash` | Tokenized phone identity signal. |
| `Email` | `email_hash` | Tokenized email identity signal. |
| `Merchant` | `merchant_id` | Acquiring merchant or payee. |
| `Account` | `account_id` | Bank, wallet, or card account. |
| `Address` | `address_hash` | Tokenized shipping, billing, or KYC address. |
| `Transaction` | `transaction_id` | Payment or transfer event for temporal analysis. |

## Relationship Types

`OWNS`, `USES`, `PAID`, `INITIATED`, `LOGGED_IN_FROM`, `HAS_PHONE`, `HAS_EMAIL`, `HAS_ADDRESS`, `BILLED_TO`, `SHIPPED_TO`, `FUNDED`, `TRANSFERRED_TO`, and `SHARES_SIGNAL_WITH`.

## Analysis Patterns

- Community detection finds dense mule clusters and synthetic identity groups.
- Centrality analysis identifies high-influence devices, IPs, merchants, and beneficiary accounts.
- Path analysis finds short paths from a new transaction to known fraud.
- Temporal analysis detects rapid account/device/IP churn.
- Fraud topology matching detects known patterns such as many customers sharing one device and cashing out through the same merchant.
