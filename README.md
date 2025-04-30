# Scalable Web Application on DigitalOcean Kubernetes (DOKS)

This repository contains the files necessary to deploy a scalable Flask web application on a DigitalOcean Kubernetes (DOKS) cluster. For detailed explanations and context, please refer to the **Setup Guide** document.

## Repository Contents

* `app/`: Contains the Flask application code (`app.py`) and its dependencies (`requirements.txt`).
* `k8s/`: Contains the Kubernetes configuration files for deploying the application:
    * `deployment.yaml`: Defines the application deployment.
    * `service.yaml`: Defines the LoadBalancer service to expose the application.
    * `hpa.yaml`: Defines the Horizontal Pod Autoscaler configuration.
* `Dockerfile`: Specifies how to build the Docker image for the Flask application.
* `README.md`: This file, providing quick deployment instructions.

## Prerequisites

* **DigitalOcean Account:** Required.
* **DigitalOcean CLI (`doctl`):** Installed and authenticated.
* **Kubernetes CLI (`kubectl`):** Installed and configured to connect to your DOKS cluster.
* **Docker:** Installed (if building the image locally).
* **Helm v3:** Installed (for optional Metrics Server installation).

For detailed installation instructions for these prerequisites, please see the **Setup Guide**.

## Quick Deployment Instructions

Follow these steps to quickly deploy the application on your DigitalOcean Kubernetes cluster:

1.  **DOKS Cluster and DOCR Setup:**
    * Ensure you have a DOKS cluster running in your DigitalOcean account.
    * Create a DigitalOcean Container Registry (DOCR) in the same region.
    * Authenticate Docker to your DOCR using `docker login`.
    * **(Refer to Step 1 and Step 2 of the Setup Guide for detailed instructions.)**

2.  **Build and Push Docker Image:**
    * Navigate to the root of this repository and build the Docker image:
        ```bash
        docker build -t <your-registry>/<your-registry-name>/flask-app:latest .
        ```
        *(Replace placeholders as needed.)*
    * Push the image to DOCR:
        ```bash
        docker push <your-registry>/<your-registry-name>/flask-app:latest
        ```

3.  **Apply Kubernetes Configurations:**
    * Ensure `kubectl` is connected to your DOKS cluster.
    * Navigate to the `k8s/` directory:
        ```bash
        cd k8s
        ```
    * Apply the Deployment, Service, and HPA:
        ```bash
        kubectl apply -f deployment.yaml
        kubectl apply -f service.yaml
        kubectl apply -f hpa.yaml
        ```
        *(Ensure `imagePullSecrets` in `deployment.yaml` is configured if your registry is private. See the **Setup Guide** for details.)*

4.  **Access the Application:**
    * Get the external IP of the LoadBalancer:
        ```bash
        kubectl get svc my-app-loadbalancer -n default
        ```
    * Open the `EXTERNAL-IP` in your web browser.

5.  ** Metrics Server:**
    * Install Metrics Server using Helm as described in the **Setup Guide (Step 5)** to enable HPA based on CPU utilization.

## Scaling

The application will automatically scale based on CPU utilization as configured in `hpa.yaml`. See the **Setup Guide (Step 4)** for details.
