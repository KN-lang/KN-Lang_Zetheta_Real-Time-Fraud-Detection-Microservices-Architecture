# Day 01 - ShieldPay Legacy Monolith Analysis

## Legacy Context
ShieldPay currently operates a single fraud-screening monolith embedded in the payment authorization path. The monolith receives transaction requests from card, UPI, wallet, and merchant channels; reads customer and account records from shared relational tables; executes hard-coded fraud rules; writes audit records; and sends synchronous responses back to payment switches.

## Business Capabilities in the Monolith
| Capability | Current Implementation | Architecture Concern |
| --- | --- | --- |
| Transaction intake | Synchronous REST endpoints in one deployment | Scaling is tied to all other capabilities |
| Customer profile lookup | Shared SQL joins across customer/account/card tables | High coupling and broad PCI scope |
| Rule evaluation | Hard-coded Java/Python rules released with the monolith | Slow rule rollout and weak simulation controls |
| Risk scoring | Static weighted score in application code | Limited explainability and experimentation |
| Investigation cases | Basic database records and manual spreadsheets | No event trail or SLA tracking |
| Notifications | Direct SMTP/SMS integrations | Outage in provider can affect authorization path |
| Audit reporting | Append-only database tables | Hard to replay decisions and reconstruct evidence |

## Pain Points
- Peak traffic during salary days and sales campaigns causes high authorization latency because all fraud functions scale together.
- Rule changes require full application releases, creating operational risk and delaying response to emerging fraud patterns.
- The monolith depends on direct database access across payment, customer, KYC, and case tables, increasing blast radius and making schema changes slow.
- Analysts lack explainable event timelines because logs, risk decisions, and case comments are not correlated by a single trace identifier.
- PCI DSS scope is larger than necessary because sensitive card data can flow through analytical code paths.
- Batch analytics identifies some fraud rings days later, after funds have moved through mule accounts.

## External Integrations
- Payment switches and merchant acquiring platforms for authorization requests.
- Core banking, card management, wallet, and UPI systems for customer/account state.
- KYC, sanctions, PEP, and negative media screening providers.
- SMS, email, push, and webhook notification providers.
- SIEM, SOC tools, regulatory reporting systems, and data warehouse exports.

## Target Direction
The replacement architecture separates domain capabilities into Kafka-backed microservices, uses service-owned data stores, introduces schema-governed event contracts, and keeps the authorization path fast through parallel rule, ML, and graph signal generation.
