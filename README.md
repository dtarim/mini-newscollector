# 📰 Mini News Collector  

## 📌 Project Purpose  
**Mini News Collector** is a simple but extensible **DevOps learning project**.  

- **Currently:**  
  - A small FastAPI service  
  - Fetches article titles from an external source (Hacker News API)  
  - Stores them in memory and exposes them via API endpoints  
- **In the future:**  
  - Advanced data storage (SQLite → PostgreSQL → AWS RDS)  
  - CI/CD pipelines automated with GitHub Actions, Kubernetes, and ArgoCD  
  - Infrastructure managed with Terraform on AWS (EKS, ECR, etc.)  
  - Optional frontend to display the collected articles  

---

## 🏗️ Project Structure  

```
mini-newscollector/
├── app/
│ ├── main.py # FastAPI application
| ├── __init__.py 
│ ├── requirements.txt # Python dependencies
| ├── test_main.py
├── Dockerfile # Container build file
├── k8s/
│ ├── deployment.yaml # Kubernetes Deployment
│ ├── service.yaml # Kubernetes Service
| ├── argocd-application.yaml # Kubernetes DevOps
├── .github/
│ └── workflows/
│ └── ci-cd.yaml # GitHub Actions CI/CD pipeline
└── README.md
```
# 📰 Mini News Collector

## Overview
Mini News Collector is a small, extensible DevOps learning project:
- FastAPI service that fetches headlines from a public source.
- Dockerized and CI-tested.
- Image builds are pushed to Docker Hub and Kubernetes deployments are managed through GitOps (ArgoCD).

## What we automated
- **CI**: On every push to `main`, GitHub Actions:
  - runs tests,
  - builds and pushes Docker images (tags: `latest` and `sha7`),
  - updates `k8s/deployment.yaml` with the new image tag and pushes the change back to this repo.
- **CD (GitOps)**: ArgoCD watches this repo's `k8s/` folder and automatically syncs changes to the Kubernetes cluster (minikube / EKS).

## How to see it locally
1. Start Minikube:
   ```bash
   minikube start




---

## 🚀 Current Functionality  
- The FastAPI service provides:  
  - `/` → Health check  
  - `/articles` → Returns the list of collected articles (in-memory)  
  - `/refresh` → Fetches fresh article data from Hacker News API  
- Docker image can be built and run locally  
- Kubernetes manifests available for deployment  
- GitHub Actions pipeline defined for CI/CD  

---

## 🔮 Future Roadmap  
- **Data Storage**  
  - Memory → SQLite → PostgreSQL → AWS RDS  
- **DevOps Tools**  
  - GitHub Actions CI/CD pipeline for automated Docker builds & pushes  
  - Kubernetes deployments  
  - GitOps workflow using ArgoCD  
  - Infrastructure as Code with Terraform (AWS EKS, ECR, networking)  
- **Extensions**  
  - Frontend (React/Vue or simple HTML templates) to visualize articles  
  - Monitoring with Prometheus / Grafana  
  - AWS integrations (S3, SNS/SQS, CloudWatch)  

---

## 🛠️ How to Run  

### 1. Create a virtual environment and install dependencies  
```bash
cd mini-newscollector
python3 -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt


Start the application

uvicorn app.main:app --reload



