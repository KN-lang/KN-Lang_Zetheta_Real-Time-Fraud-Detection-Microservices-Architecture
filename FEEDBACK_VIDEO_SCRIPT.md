# Feedback Video Script: Real-Time Fraud Detection Platform

**Duration**: ~5-7 Minutes

---

## 1. Introduction (0:00 - 0:45)
- **Visual**: Show the project title and a high-level architecture diagram.
- **Script**: "Hello, I'm the lead architect for the Real-Time Fraud Detection Platform. Today, I'll walk you through our hybrid approach to identifying financial fraud using microservices, event streaming, and multi-dimensional analysis."

## 2. The Problem & Solution (0:45 - 1:30)
- **Visual**: Show the `01-scenario-analysis.md` or a slide on fraud rings.
- **Script**: "Traditional systems are too slow. Our solution combines static business rules, statistical anomaly detection, and graph-based relationship analysis to catch everything from simple velocity attacks to complex organized fraud rings."

## 3. Prototype Demonstration (1:30 - 3:00)
- **Visual**: Screen recording of running the CLI simulation and showing the summary statistics.
- **Script**: "We've built a Python-based simulation. As you can see, we generated 1,000 transactions. Our engines flagged 109 rule hits and 86 anomalies, resulting in 62 fraud cases for review. All 6 internal unit tests are passing, validating our core logic."

## 4. Target Architecture (3:00 - 4:30)
- **Visual**: Show the C4 Container diagram (`diagrams/c4-container.puml`).
- **Script**: "While the prototype is local, the target design is a fully distributed microservices architecture. We use Apache Kafka as the event backbone, allowing our Rule, Anomaly, and Graph services to process transactions in parallel. Decisions are aggregated by a weighted Risk Scorer."

## 5. Deep Dive: Graph Analysis (4:30 - 5:30)
- **Visual**: Show the Graph Analysis Flow diagram (`diagrams/graph-analysis-flow.puml`).
- **Script**: "One of our key differentiators is graph analysis. We don't just look at a transaction in isolation; we analyze how customers, devices, and IPs are connected. This allows us to detect mule accounts and suspicious clusters that rules would miss."

## 6. Conclusion & Roadmap (5:30 - 6:00)
- **Visual**: Show the Final Submission Report.
- **Script**: "We have a clear roadmap to move this into production on Kubernetes, with a target throughput of 5,000 transactions per second. Thank you for your time."
