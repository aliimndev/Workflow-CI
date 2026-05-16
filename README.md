# Workflow CI - Telco Customer Churn

![CI](https://github.com/aliimndev/Workflow-CI/actions/workflows/ci.yml/badge.svg)

Repository CI/CD untuk otomatisasi training model Telco Customer Churn. Workflow akan melatih ulang model dan push Docker image ke Docker Hub setiap push ke main.

## Struktur
Workflow-CI/  
├── .github/workflows/ci.yml  
├── MLProject/  
│   ├── MLProject  
│   ├── modelling.py  
│   └── telco_customer_churn_preprocessing/  
└── README.md  

## Workflow
Trigger: Push ke main atau manual dispatch  
Steps: Checkout → Setup Python 3.12.7 → Install dependencies → Training → Build Docker image → Push ke Docker Hub

## Docker
docker pull aliimndev/telco-churn-model:latest  
docker run -p 8080:8080 aliimndev/telco-churn-model:latest

## Author
Ali Imannudin - Dicoding MSML Submission Kriteria 3
