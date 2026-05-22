# 10. Case Management Workflow

## Overview
Flagged transactions (Decision: REVIEW) are sent to the **Case Management Service**.

## Workflow Steps
1. **Creation**: A `FraudCase` is automatically created with all related signals (Rule IDs, Anomaly Scores, Graph Findings).
2. **Assignment**: Cases are assigned to a queue or specifically to an analyst.
3. **Investigation**:
   - Analyst views the "Fraud 360" dashboard.
   - Views the entity graph (provided by Graph Analysis Service).
   - Checks historical customer behavior.
4. **Resolution**:
   - **Confirmed Fraud**: Customer is blacklisted; authorities may be notified.
   - **False Positive**: Case is closed; the signal helps tune the detection engines.
5. **Archiving**: All notes and decisions are stored for audit and regulatory compliance.

## Integration
The Case Manager provides an API for external dashboards to fetch case details and submit resolutions.
