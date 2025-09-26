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

'''
mini-newscollector/
├── app/
│ ├── main.py # FastAPI application
│ ├── requirements.txt # Python dependencies
├── Dockerfile # Container build file
├── k8s/
│ ├── deployment.yaml # Kubernetes Deployment
│ ├── service.yaml # Kubernetes Service
├── .github/
│ └── workflows/
│ └── ci-cd.yaml # GitHub Actions CI/CD pipeline
└── README.md

'''

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

