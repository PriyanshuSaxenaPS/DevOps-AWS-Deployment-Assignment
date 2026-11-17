# AWS Deployment Assignment

This repository contains my completed practical assignment for the **TuteDude DevOps** module.

## Project
**Flask Backend + Express Frontend**

A full-stack web application deployed across three progressive AWS cloud architectures, demonstrating virtual machine hosting, private VPC networking, and managed container orchestration.

---

## Technologies
- Python
- Flask (with Flask-CORS & Gunicorn)
- Node.js
- Express.js
- AWS EC2
- Docker & Docker Compose
- Amazon ECR
- Amazon ECS
- Amazon VPC & Application Load Balancer (ALB)

---

## Deployment Configurations

1. **Single EC2 instance** — Hosted both the Flask API (Gunicorn on port `5000`) and Express frontend (port `3000`) on a single Ubuntu `t3.micro` EC2 instance communicating over `localhost`.
2. **Separate EC2 instances** — Decoupled the frontend and backend onto two dedicated EC2 instances within the same VPC, routing API requests securely via private IPv4 addresses and custom Security Groups.
3. **Docker containers using ECR and ECS** — Built and pushed Docker images to **Amazon ECR**, configured a custom **VPC** (`myapp-vpc`) with public/private subnets and an Internet Gateway, and orchestrated containers on **Amazon ECS** behind an internet-facing **Application Load Balancer (ALB)**.

---

## Service Ports & Endpoints

### Frontend
* **Port:** `3000`
* **Local URL:** `http://localhost:3000`

### Backend
* **Port:** `5000`
* **Local API Endpoint:** `http://localhost:5000/api/hello`

---

## Docker (Local Setup)

### 1. Clone the Repository
```bash
git clone https://github.com
cd AWS-Deployment-Assignment
```

### 2. Run with Docker Compose
```bash
docker compose up --build
```

### 3. Access the Application
* **Open Frontend:** [http://localhost:3000](http://localhost:3000)
* **Backend API:** [http://localhost:5000/api/hello](http://localhost:5000/api/hello)

---

## AWS Deployment Summary

| Deployment Stage | Architecture Details | Endpoints / Ports |
| :--- | :--- | :--- |
| **1. Single EC2** | Ubuntu 24.04 (`t3.micro`), Gunicorn + Node running via `nohup` | Frontend `:3000`, Backend `:5000` |
| **2. Separate EC2** | Dedicated Frontend EC2 & Backend EC2 communicating over Private IP | Frontend `:3000` → Backend Private IP `:5000` |
| **3. ECR, ECS & VPC** | Docker images hosted in Amazon ECR, deployed via ECS cluster inside `myapp-vpc` | Public ALB DNS (`HTTP:80` → Target Group `:3000`) |

---

## Repository Structure
```text
AWS-Deployment-Assignment/
├── backend/
│   ├── app.py              # Flask REST API (/ and /api/hello endpoints)
│   ├── Dockerfile          # Backend container build configuration
│   └── requirements.txt    # Flask, flask-cors, and gunicorn dependencies
├── frontend/
│   ├── public/
│   │   └── index.html      # Frontend UI to test Flask backend connectivity
│   ├── app.js              # Express server forwarding requests via BACKEND_URL
│   ├── Dockerfile          # Frontend container build configuration
│   └── package.json        # Node.js dependencies
├── .gitignore              # Excludes virtual environments and node_modules
├── docker-compose.yml      # Local multi-container test configuration
└── README.md               # Project documentation
```
