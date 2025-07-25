# Monitoring

## Overview

The monitoring stack consists of:

-   **Prometheus:** For time-series data collection and alerting.
-   **Grafana:** For visualization of metrics.
-   **Alertmanager:** for handling alerts.
-   **Exporters:** For exposing metrics from various services.

## Dashboards

The following dashboards are available in Grafana:

-   **Jenkins Overview:** Overview of the Jenkins master.
-   **Jenkins Builds:** Detailed build statistics.
-   **Infrastructure Health:** Health of the underlying infrastructure.
-   **Security Metrics:** Security-related metrics.

## Alerts

Alerts are configured in `monitoring/prometheus/rules/`. They are sent to the configured receivers in `monitoring/alertmanager/alertmanager.yml`.
