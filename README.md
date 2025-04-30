This repository contains the files necessary to deploy a scalable Flask web application on a DigitalOcean Kubernetes (DOKS) cluster.

## Repository Contents

* `app/`: Contains the Flask application code (`app.py`) and its dependencies (`requirements.txt`).
* `k8s/`: Contains the Kubernetes configuration files for deploying the application:
    * `deployment.yaml`: Defines the application deployment.
    * `service.yaml`: Defines the LoadBalancer service to expose the application.
    * `hpa.yaml`: Defines the Horizontal Pod Autoscaler configuration.
* `Dockerfile`: Specifies how to build the Docker image for the Flask application.
* `README.md`: This file, providing deployment instructions.
