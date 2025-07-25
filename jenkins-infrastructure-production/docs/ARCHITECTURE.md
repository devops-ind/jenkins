# Architecture

This project implements a production-grade Jenkins infrastructure with the following components:

-   **Jenkins Masters:** One or more Jenkins masters for high availability.
-   **Jenkins Agents:** A pool of dynamic agents for running builds.
-   **Harbor:** A private Docker registry for storing Jenkins images.
-   **Shared Storage:** For persisting Jenkins data and workspaces.
-   **Monitoring:** Prometheus, Grafana, and Alertmanager for monitoring and alerting.
-   **High Availability:** Keepalived and Pacemaker for high availability.
-   **Security:** UFW, Fail2ban, Auditd, and SELinux for security hardening.

## Diagram

```
[User] -> [HAProxy] -> [Jenkins Master 1]
                     -> [Jenkins Master 2]

[Jenkins Master] -> [Jenkins Agents]

[Jenkins Master] -> [Harbor]

[Jenkins Master] -> [Shared Storage]

[Prometheus] -> [Jenkins Master]
             -> [Jenkins Agents]
             -> [Node Exporter]

[Grafana] -> [Prometheus]

[Alertmanager] -> [Prometheus]
```
