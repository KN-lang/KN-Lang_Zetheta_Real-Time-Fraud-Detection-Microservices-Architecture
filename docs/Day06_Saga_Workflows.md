# Day 06 - Saga Workflows

## Transaction Processing Saga
The transaction-ingestion service accepts a request, publishes `transactions.validated.v1`, and waits for risk decisions asynchronously. Customer-profile enriches the event, rule-engine, anomaly-detection, and graph-analysis publish independent signals, and risk-scoring emits `risk.decisions.v1`. Compensation includes timeout-based step-up, duplicate suppression through idempotency keys, and DLQ routing for invalid events.

## Fraud Investigation Saga
A review or block decision creates a case. Case-management assigns the case, attaches evidence, records analyst action, and publishes `cases.events.v1`. Confirmed fraud triggers notification, card/account controls, and audit evidence retention. False positives feed model monitoring and rule precision metrics.

## Card Blocking Saga
Confirmed high-risk activity emits a card block request to the payment control boundary. The saga waits for card management confirmation, notifies the customer, records evidence, and opens follow-up investigation tasks if the block fails or times out.
