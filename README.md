# SRE Learning Journey

My hands-on learning path from SDET to SRE.

## Goals
- Deploy and manage applications on Kubernetes ✅
- Run Selenium E2E tests inside Kubernetes pods ✅
- Build full CI/CD pipelines with GitHub Actions ✅
- Infrastructure as Code with Terraform + AWS (next)

## Stack
- **Backend:** Django (Python)
- **Frontend:** React (Node.js)
- **Tests:** Selenium with Allure Reports
- **Container:** Docker
- **Orchestration:** Kubernetes (minikube locally, EKS on AWS)
- **CI/CD:** GitHub Actions
- **Notifications:** Slack
- **IaC:** Terraform (next)

## Progress
- [x] Local Kubernetes cluster with minikube
- [x] YAML-based deployments
- [x] Namespaces
- [x] Scaling deployments
- [x] Dockerize Django app
- [x] Dockerize React app
- [x] Docker Compose multi-container setup
- [x] Full stack deployed on Kubernetes
- [x] Selenium E2E tests running in K8s pods
- [x] Allure reports for test results
- [x] GitHub Actions CI/CD pipeline
- [x] Docker images pushed to DockerHub
- [x] Slack notifications on pipeline success/failure
- [ ] Terraform + AWS infrastructure
- [ ] AWS EKS deployment
- [ ] Prometheus + Grafana monitoring
- [ ] SLOs and error budgets

## Structure
├── k8s/              # Kubernetes YAML files
├── docker/           # Dockerfiles
├── app/              # Application code
│   ├── backend/      # Django REST API
│   ├── frontend/     # React Task Manager
│   └── tests/        # Selenium E2E tests
├── ci-cd/            # GitHub Actions workflows
├── terraform/        # Infrastructure as Code (coming soon)
└── docs/             # Notes and learnings

## Live Pipeline
https://github.com/pambapradeepkumar/sre-learning-journey/actions
