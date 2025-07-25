# Security

## Hardening

The following security measures are implemented:

-   **UFW:** A simple firewall is configured to allow only necessary traffic.
-   **Fail2ban:** To protect against brute-force attacks.
-   **Auditd:** To log all security-relevant events.
-   **SELinux:** Enforcing on RedHat-based systems.

## Vault

Sensitive data, such as passwords and API keys, should be stored in an Ansible Vault. The vault file is located at `ansible/group_vars/all/vault.yml`.

To edit the vault, use the following command:

```bash
ansible-vault edit ansible/group_vars/all/vault.yml
```
