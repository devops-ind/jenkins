#!/bin/bash
set -e

# Start Docker daemon
/usr/local/bin/dockerd-entrypoint.sh &

# Start Jenkins
/usr/local/bin/jenkins.sh
