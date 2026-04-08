# SimpleTimeService DevOps Project

## Overview
A minimal FastAPI service deployed using Docker + Terraform (AWS ECS Fargate).

## Features
- Returns timestamp and client IP
- Runs as non-root container
- Fully automated infra via Terraform
- CI/CD with GitHub Actions

## Setup

### 1. Build & Push Docker Image
docker build -t <dockerhub-username>/simple-time-service ./app
docker push <dockerhub-username>/simple-time-service

### 2. AWS Setup
aws configure

### 3. Deploy
cd terraform
terraform init
terraform apply

## Output
http://<ALB-DNS>
