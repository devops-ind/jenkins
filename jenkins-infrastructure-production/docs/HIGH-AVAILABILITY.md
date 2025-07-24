# High Availability

High availability is provided by a combination of:

-   **Keepalived:** For VRRP and managing a virtual IP (VIP).
-   **Pacemaker:** For cluster resource management.
-   **HAProxy:** For load balancing traffic to the Jenkins masters.

## Configuration

-   **Keepalived:** The configuration is located at `ansible/roles/high-availability/templates/keepalived.conf.j2`.
-   **Pacemaker:** The configuration is complex and environment-specific. It is recommended to configure it manually.
-   **HAProxy:** The configuration is located at `ansible/roles/jenkins-infrastructure/templates/haproxy.cfg.j2`.
