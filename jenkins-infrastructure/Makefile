# Makefile
.PHONY: help setup deploy deploy-ha update-images vault-edit vault-encrypt vault-decrypt clean

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  setup             Install Ansible dependencies from requirements.yml"
	@echo "  deploy            Run the main site.yml playbook to deploy/update everything"
	@echo "  deploy-ha         Run only the Jenkins HA deployment tasks"
	@echo "  update-images     Build and push new Jenkins Docker images"
	@echo "  vault-edit        Edit the encrypted vault.yml file"
	@echo "  vault-encrypt     Encrypt the vault.yml file"
	@echo "  vault-decrypt     Decrypt the vault.yml file for viewing"
	@echo "  clean             Remove Ansible log files"

setup:
	@echo "Installing Ansible collections and roles..."
	ansible-galaxy install -r ansible/requirements.yml

deploy: setup
	@echo "Running the main deployment playbook..."
	ansible-playbook ansible/site.yml --vault-ask-pass

deploy-ha: setup
	@echo "Deploying/updating Jenkins HA masters..."
	ansible-playbook ansible/site.yml --tags "jenkins-master" --vault-ask-pass

update-images: setup
	@echo "Building and pushing Jenkins images..."
	ansible-playbook ansible/playbooks/update-images.yml --vault-ask-pass

VAULT_FILE = ansible/inventories/production/group_vars/all/vault.yml
vault-edit:
	@echo "Editing vault file: $(VAULT_FILE)"
	ansible-vault edit $(VAULT_FILE)

vault-encrypt:
	@echo "Encrypting vault file: $(VAULT_FILE)"
	ansible-vault encrypt $(VAULT_FILE)

vault-decrypt:
	@echo "Decrypting vault file: $(VAULT_FILE)"
	ansible-vault decrypt $(VAULT_FILE)

clean:
	@echo "Cleaning up log files..."
	rm -f ansible/ansible.log
