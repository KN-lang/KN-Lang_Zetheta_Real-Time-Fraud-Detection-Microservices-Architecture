# Day 13 Work Log - Logging and Tracing

    ## Objectives
    Deliver the Day 13 architecture artifacts for `SWE-2C_FraudDetection_KshitijChauhan` with consistent service names, event names, and reviewable design decisions.

    ## Completed Outputs
    | Artifact | Status | Notes |
| --- | --- | --- |
| Structured logging | Completed | Aligned with Project 1C Day 13 scope. |
| OpenTelemetry | Completed | Aligned with Project 1C Day 13 scope. |
| Tracing | Completed | Aligned with Project 1C Day 13 scope. |
| Formal SLA | Completed | Aligned with Project 1C Day 13 scope. |

    ## Design Notes
    - Used `correlation_id`, `transaction_id`, and immutable event envelopes across all event-driven flows.
    - Kept PCI DSS scope narrow by tokenizing PAN/card data before it reaches analytical services.
    - Applied RBI-aligned controls for Indian payment systems, auditability, customer notification, incident response, and data residency.

    ## Validation
    - File names match the requested deliverable list.
    - Cross references use the same service and topic taxonomy used in the master architecture document.
