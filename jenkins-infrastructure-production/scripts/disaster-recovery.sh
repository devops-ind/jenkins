#!/bin/bash
set -e

ansible-playbook -i ansible/inventories/production ansible/disaster-recovery.yml --extra-vars "restore_enabled=true backup_timestamp=$1"
