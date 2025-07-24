# Troubleshooting

## Jenkins Master is not starting

-   Check the logs of the jenkins-master container:

    ```bash
    docker logs jenkins-master
    ```

-   Check the systemd service status:

    ```bash
    systemctl status jenkins-master
    ```

## Jenkins agents are not connecting

-   Check the logs of the jenkins-agent container.
-   Ensure the Jenkins URL and secret are configured correctly.
-   Check network connectivity between the agent and the master.

## High Availability is not working

-   Check the status of keepalived and pacemaker.
-   Check the keepalived logs for errors.
-   Ensure the virtual IP is correctly configured.
