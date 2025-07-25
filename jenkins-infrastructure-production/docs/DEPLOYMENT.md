# Deployment

## Prerequisites

- Ansible 2.9+
- Docker

## Deployment Steps

1.  **Configure Inventory:** Update the `ansible/inventories/production/hosts.yml` file with your server information.

2.  **Configure Variables:** Update the variables in `ansible/group_vars/all/` to match your environment.

3.  **Deploy:** Run the deployment script:

    ```bash
    ./scripts/deploy.sh
    ```
