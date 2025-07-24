import yaml

def test_inventory():
    with open('ansible/inventories/production/hosts.yml', 'r') as f:
        inventory = yaml.safe_load(f)

    assert 'all' in inventory
    assert 'children' in inventory['all']
    assert 'jenkins_masters' in inventory['all']['children']
    assert 'jenkins_agents' in inventory['all']['children']
    assert 'monitoring' in inventory['all']['children']
