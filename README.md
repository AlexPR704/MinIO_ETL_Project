# MinIO ETL Project

A data engineering pipeline using MinIO, Apache Airflow, and Docker to simulate an end-to-end ETL workflow. Raw data is stored in MinIO (an S3-compatible object store), processed via Python scripts, and orchestrated using Airflow.


# Features

- Upload raw data to MinIO buckets
- ETL scripts to clean and transform data
- Task scheduling & orchestration via Apache Airflow
- Containerized with Docker for easy setup
- Modular and easy to extend


# Requirements

Make sure you have the following installed:

- Docker Desktop
- Docker Compose
- (Optional) Git, VS Code, PowerShell or Terminal


# Folder Structure

MinIO_ETL_Project/
├── airflow/           # Airflow configs and DAGs
├── data/              # Raw & processed data
├── scripts/           # ETL Python scripts
├── README.md          # Project documentation

# Project Overview
This project demonstrates how to build a basic but functional ETL pipeline from scratch using modern tools. It's perfect for practicing data engineering workflows like:

- Moving data into object storage
- Cleaning and transforming with Python
- Automating workflows with Airflow

# How to Run

 1. Start Airflow (from the `airflow/` folder)

Run:
docker-compose up airflow-init
docker-compose up

 2.  Access Airflow UI

Once running, open your browser and go to:

http://localhost:8080

Default credentials:
Username: airflow
Password: airflow

 3. Stop the Containers
To stop all services; Go to the bash and paste this in:

docker-compose down

# Future Improvements
- Add MinIO monitoring with Prometheus/Grafana
- Add automated data refreshes
- Secure credentials using .env best practices
- Add unit tests for ETL logic
- Deploy pipeline to the cloud

# Built By
Alex G.
[GitHub](https://github.com/AlexPR704)  
[LinkedIn](https://www.linkedin.com/in/alexanderggarcia/)