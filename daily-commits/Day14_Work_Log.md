# Day 14 Work Log - Deployment and DR

    ## Objectives
    Deliver the Day 14 architecture artifacts for `SWE-2C_FraudDetection_KshitijChauhan` with consistent service names, event names, and reviewable design decisions.

    ## Completed Outputs
    | Artifact | Status | Notes |
| --- | --- | --- |
| CI/CD | Completed | Aligned with Project 1C Day 14 scope. |
| GitHub Actions | Completed | Aligned with Project 1C Day 14 scope. |
| Multi-region topology | Completed | Aligned with Project 1C Day 14 scope. |
| DR plan | Completed | Aligned with Project 1C Day 14 scope. |
| Dockerfiles | Completed | Aligned with Project 1C Day 14 scope. |
| Kubernetes samples | Completed | Aligned with Project 1C Day 14 scope. |

    ## Design Notes
    - Used `correlation_id`, `transaction_id`, and immutable event envelopes across all event-driven flows.
    - Kept PCI DSS scope narrow by tokenizing PAN/card data before it reaches analytical services.
    - Applied RBI-aligned controls for Indian payment systems, auditability, customer notification, incident response, and data residency.

    ## Validation
    - File names match the requested deliverable list.
    - Cross references use the same service and topic taxonomy used in the master architecture document.
