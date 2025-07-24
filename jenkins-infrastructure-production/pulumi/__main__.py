import pulumi
from modules import network, storage, compute

# Create a network
net = network.CustomNetwork("jenkins-net")

# Create storage
store = storage.CustomStorage("jenkins-storage", net.id)

# Create compute instances
compute.CustomCompute("jenkins-master", net.id, store.id)
