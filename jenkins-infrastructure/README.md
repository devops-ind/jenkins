# Production-Grade Jenkins Infrastructure with Ansible

This project automates the deployment and management of a High-Availability (HA), scalable, and observable Jenkins environment using Ansible.

## Features

- **HA Jenkins Masters**: Deploys multiple Jenkins master containers, fronted by HAProxy.
- **Shared `JENKINS_HOME`**: Uses NFS for a shared `JENKINS_HOME` directory.
- **Configuration as Code (JCasC)**: Jenkins is configured entirely via YAML files.
- **Decoupled Image Building**: A separate Ansible role manages building custom Jenkins images.
- **Ansible-Managed Containers**: Deploys all services (Jenkins, Prometheus, Grafana) as containers managed by Ansible.
- **Monitoring Stack**: Deploys Prometheus and Grafana for monitoring.
- **Automated Backups**: Includes a Jenkins pipeline for daily backups.

## Deployment Steps

1.  **Configure Inventory & Variables**
    -   Update `ansible/inventories/production/hosts.yml`.
    -   Update `ansible/inventories/production/group_vars/all/main.yml`.
    -   Encrypt secrets in `ansible/inventories/production/group_vars/all/vault.yml` with `make vault-encrypt`.

2.  **Install Ansible Dependencies**
    ```bash
    make setup
    ```

3.  **Run the Main Deployment**
    ```bash
    make deploy
    ```
