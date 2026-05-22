# ADR 007: Case Management Design

## Status
Accepted

## Context
Transactions flagged for "REVIEW" need to be investigated by human analysts. We need a system to track these investigations, store analyst notes, and capture final outcomes.

## Decision
The **Case Management Service** will be a separate microservice with its own database (PostgreSQL) to store fraud cases. It will provide a UI (or API for a UI) for analysts to view transaction details, fraud signals, and entity relationship graphs.

## Alternatives Considered
- **Email/Ticketing System**: Lacks the specific context (graph views, rule hits) needed for fraud investigation.
- **Manual Spreadsheet**: Not scalable, lacks audit trail and security.

## Consequences
- **Pros**:
  - Dedicated workflow for analysts.
  - Rich context provided to the investigator.
  - Audit trail for regulatory compliance.
- **Cons**:
  - Requires building/integrating a UI.
  - Need to keep case data synchronized with transaction outcomes.
