#!/bin/bash
set -e

ansible-playbook -i ansible/inventories/production ansible/site.yml
