#!/bin/bash
set -e

# Check if Jenkins is up and running
curl -f http://localhost:8080/login || exit 1
