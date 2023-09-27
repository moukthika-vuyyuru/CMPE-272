# Assignment 2: Microservices Deployment on Kubernetes

## Overview

This repository showcases the transformation of a Monolith application into a Microservices-based architecture and its deployment on a Kubernetes cluster. The project is divided into two main components:

1. **Monolith Application**: The original single-unit application.
2. **Microservice-Based Application**: The refactored application, divided into microservices and deployed on Kubernetes.

## Monolith Application

### Description

The Monolith Application is a Flask-based API rate limiter designed to manage client requests while enforcing a rate limit policy.

### Components

- **app.py**: The primary application file containing the Flask app and rate-limiting logic.
- **Dockerfile**: Instructions for building a Docker image of the Monolith application.
- **startup.sh**: A script to launch the application and the Redis server.
- **web-app.yaml**: Kubernetes YAML file for deploying the web application microservice.
- **script.py**: Python script for testing rate limiting functionality.

### Deployment (Docker)

To deploy the Monolith Application using Docker:

1. Build the Docker image: `docker build -t moukthikavuyyuru/web-app:latest .`
2. Run the Docker container: `docker run -p 2000:5000 moukthikavuyyuru/web-app:latest`
3. Access the application at `http://localhost:2000/endpoint`

**Note**: In the Monolith Application, a single container runs both the application and the Redis server. Testing is performed using a curl script.

## Microservice-Based Application

### Microservices Transformation

To achieve a more scalable and maintainable architecture, we broke down the Monolith Application into smaller, independent microservices. Each microservice handles a specific aspect of the original application's functionality, resulting in a more flexible and easily extensible system.

The key components of the Microservice-Based Application include:

- **Web Application (web-app)**: A Flask application managing rate limiting.
- **Redis (redis)**: A dedicated Redis server for data storage and retrieval.
- **Testing (test)**: A testing microservice to ensure rate limiting functionality.

### Microservices

#### Web Application (web-app)

- **app.py**: Flask application managing rate limiting.
- **Dockerfile**: Docker image build instructions.
- **web-app.yaml**: Kubernetes YAML file for deploying the web application microservice.

#### Redis (redis)

- **Dockerfile**: Docker image build for the Redis server.
- **redis.yaml**: Kubernetes deployment and service configuration for Redis.

#### Testing (test)

- **Dockerfile**: Docker image build for testing.
- **script.py**: Python script for testing rate limiting functionality.
- **test_job.yaml**: Kubernetes Job configuration for running tests.

### Deployment (Kubernetes)

To deploy the Microservice-Based Application on Kubernetes:

1. Deploy Redis: Apply `redis.yaml` to create the Redis service and deployment.
2. Deploy the Web Application: Apply `web-appt.yaml` to create the web application service and deployment.
3. Run Tests: Utilize the Kubernetes Job defined in `test_job.yaml` to test the application.

**Note**: In the Microservices-Based Application, multiple pods are deployed, including pods for Redis, the web application, and a separate Job to run tests. This architecture enhances scalability and maintainability.

## Architecture Diagram

### Monolith Architecture Diagram

![Monolith Architecture Diagram](https://drive.google.com/uc?export=view&id=1XHZG9LWb8UoTxd-K8hpi3VUtEg2QGYaI)

### Microservice Based Architecture Diagram

![Microservice Based Architecture Diagram](https://drive.google.com/uc?export=view&id=1EDqlEKxz28KeOe5z9NAaKlVM3vYNAcfZ)

## Screenshots

### Monolith Cluster State
![Monolith Kubernetes Cluster State](https://drive.google.com/uc?export=view&id=1eOZFX36AxJUecpjFWdSWsGrwXPGQMTrp)

### Monolith Application in Action
![Monolith Application in Action](https://drive.google.com/uc?export=view&id=1CRHKfHmYa7bq_yAmw8OjtslKtp-WFcLw)
![Monolith Application in Action](https://drive.google.com/uc?export=view&id=1KhUoEawWNftGAUkk76b0401c0BIMi3s-)

### Monolith Test Script
![Monolith Test Script](https://drive.google.com/uc?export=view&id=1O1Y69-j-X5G8RE3_6pH8wSe6-N672XRl)


### Microservices Kubernetes Cluster State
![Microservices Kubernetes Cluster State](https://drive.google.com/uc?export=view&id=1rR0GBh2gQF6ypXg8Rry3BC7nd6QgETAn)
![Microservices Kubernetes Cluster State](https://drive.google.com/uc?export=view&id=1lOCtotHOq1lJeP6HV0PWGItt-UVkNEPI)

### Microservices Application in Action
![Microservices Application in Action](https://drive.google.com/uc?export=view&id=1rS_2TEqjkfNLbcuVytBvmSOCSITW5UOs)
![Microservices Application in Action](https://drive.google.com/uc?export=view&id=1lOCtotHOq1lJeP6HV0PWGItt-UVkNEPI)

### Microservices Test Job
![Microservices Test Job](https://drive.google.com/uc?export=view&id=1cSkj-1wRCsx2lqpSvP0Raioa-YK157eS)
![Microservices Test Job](https://drive.google.com/uc?export=view&id=1nMIln_NsWHVrfUPg4paQYPE1MweNGl7V)



