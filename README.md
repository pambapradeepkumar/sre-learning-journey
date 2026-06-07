# SRE Learning Journey

My hands-on learning path from SDET to SRE.

## Goals
- Deploy and manage applications on Kubernetes
- Run Selenium E2E tests inside Kubernetes pods
- Build full CI/CD pipelines with GitHub Actions
- Infrastructure as Code with Terraform + AWS

## Stack
- **Backend:** Django (Python)
- **Frontend:** React (Node.js)
- **Tests:** Selenium (Python + Node.js)
- **Container:** Docker
- **Orchestration:** Kubernetes (minikube locally, EKS on AWS)
- **CI/CD:** GitHub Actions
- **IaC:** Terraform

## Progress
- [x] Local Kubernetes cluster with minikube
- [x] YAML-based deployments
- [x] Namespaces
- [x] Scaling deployments
- [ ] Dockerize Django app
- [ ] Dockerize React app
- [ ] Selenium tests in K8s pods
- [ ] GitHub Actions pipeline
- [ ] AWS EKS deployment
- [ ] Terraform infrastructure

## Structure
├── k8s/              # Kubernetes YAML files
├── docker/           # Dockerfiles
├── app/              # Application code
│   ├── backend/      # Django
│   ├── frontend/     # React
│   └── tests/        # Selenium tests
├── ci-cd/            # GitHub Actions workflows
├── terraform/        # Infrastructure as Code
└── docs/             # Notes and learnings
