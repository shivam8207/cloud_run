🛒 Django E-Commerce Application
🚀 Dockerized Django App on Google Cloud Run with Cloud SQL (MySQL) & Secret Manager
📌 Project Title

Django E-Commerce Web Application using Docker & Google Cloud Run

📝 Short Description

This project is a cloud-native Django e-commerce application deployed on Google Cloud Run, using Cloud SQL (MySQL) as the backend database and Google Secret Manager for secure credential management.

The application demonstrates end-to-end deployment, secure database connectivity, and production-ready DevOps practices using Docker and GCP managed services.

✨ Key Features

✅ Add products (name, price, quantity)
✅ View product listings stored in MySQL
✅ Read & write database operations
✅ Fully Dockerized Django application
✅ Secure secret handling (no hardcoded credentials)
✅ Deployed on Google Cloud Run
✅ Uses Cloud SQL Connector (no public IP)

🧠 Use Case

This project validates:

Django ↔ MySQL connectivity in cloud

Secure secret management

Cloud-native deployment on GCP

Best practices for production workloads

🧩 Architecture Overview
User Browser
     ↓
Cloud Run (Dockerized Django App)
     ↓
Cloud SQL (MySQL) via Cloud SQL Connector
     ↓
Secrets fetched securely from Secret Manager

🔐 Step 1: Create Service Account & Assign IAM Roles

Create a Service Account and assign the following roles:

🔑 Role	📌 Purpose
Artifact Registry Writer	Push Docker images
Cloud Run Admin	Deploy Cloud Run services
Compute Admin	Required by Cloud Run backend
Editor	General permissions
Secret Manager Secret Accessor	🔴 Mandatory
Service Account User	Required for deployment

📌 Important:
This Service Account must be attached to Cloud Run.

🗄 Step 2: Create Cloud SQL (MySQL)

Go to Cloud SQL → Create Instance

Choose MySQL

Region: asia-south1

Enable Private IP

Create Database:

Database Name: teentak

🔑 Step 3: Create Secrets in Secret Manager
3.1 Enable API
gcloud services enable secretmanager.googleapis.com

3.2 Create Secrets
🔐 Secret Name	📌 Value
MYSQL_HOST	/cloudsql/devops11-479107:asia-south1:cloud-run
MYSQL_USER	teentak
MYSQL_PASSWORD	********
MYSQL_DB	teentak

📌 MYSQL_HOST Format

/cloudsql/PROJECT_ID:REGION:INSTANCE_NAME

📦 Step 4: Create Artifact Registry

Name: hdfc

Format: Docker

Region: asia-south1

🔑 Step 5: Authenticate Artifact Registry
gcloud auth login
gcloud config set project devops11-479107
gcloud auth configure-docker asia-south1-docker.pkg.dev

🐳 Step 6: Build & Push Docker Image
Build Image
docker build -t django-cloudrun-app .

Tag Image
docker tag django-cloudrun-app \
asia-south1-docker.pkg.dev/devops11-479107/hdfc/django-app:v1

Push Image
docker push asia-south1-docker.pkg.dev/devops11-479107/hdfc/django-app:v1


✔ Verify in Artifact Registry

☁️ Step 7: Deploy on Cloud Run (GUI)

Configuration

Image:

asia-south1-docker.pkg.dev/devops11-479107/hdfc/django-app:v1


Port: 8080

Authentication: Allow unauthenticated

Min Instances: 1

Max Instances: 2

Ingress: Allow all

Execution Environment: Second Generation

🌍 Step 8: Environment Variables
Name	Value
GCP_PROJECT	devops11-479107

📌 Secrets are fetched directly from Secret Manager, so no need to expose them here.

🔥 Step 9: Cloud SQL Connection (MOST IMPORTANT)

Go to:

Containers, Networking, Security → Networking


Add Cloud SQL Connection:

devops11-479107:asia-south1:cloud-run


❗ Mandatory

No public IP

No VPC connector

Fully secure socket connection

🔐 Step 10: Security Configuration

Service Account Used by Cloud Run

Default Compute Service Account


Ensure it has:

✅ Secret Manager Secret Accessor

✅ Cloud SQL Client

🚀 Step 11: Final Deployment

Click DEPLOY 🚀

✅ Expected Output

🌍 Open Cloud Run URL:

https://django-app-918955775042.asia-south1.run.app


🎉 You should see:

Django App Running on Cloud Run 🚀
Connected MySQL Database: teentak

🔐 Bonus: GitLab CI/CD (JSON Key Encoding)
base64 -w 0 key.json > key.json.b64


Use this value as:

GCP_SA_KEY

🎯 Final Notes

✔ Production-ready architecture
✔ Secure secret management
✔ No hardcoded credentials
✔ Cloud SQL best-practice integration
