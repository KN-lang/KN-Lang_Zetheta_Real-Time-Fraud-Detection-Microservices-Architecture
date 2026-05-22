# 15. Deployment and CI/CD

## Infrastructure as Code (IaC)
- **Terraform**: Manages cloud infrastructure (EKS, MSK for Kafka, RDS, S3).
- **Helm**: Manages Kubernetes manifests and service deployments.

## CI/CD Pipeline (GitHub Actions)
1. **Commit**: Developer pushes code to a feature branch.
2. **CI**: 
   - Linting (Ruff/ESLint).
   - Unit Tests (Pytest/Jest).
   - Integration Tests (with Testcontainers).
   - Docker Image Build and Push to ECR.
3. **CD (Staging)**: 
   - Automated deployment to the staging cluster.
   - Smoke tests and Performance tests.
4. **CD (Production)**: 
   - Manual approval or automated canary/blue-green deployment.
   - Rollback capability if metrics degrade.

## Deployment Strategy
- **Canary Deployments**: New models or rule engine versions are rolled out to a small percentage of traffic first.
- **Feature Flags**: Enable/disable specific rules or detection logic without code changes.
