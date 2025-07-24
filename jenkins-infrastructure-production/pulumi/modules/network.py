import pulumi_aws as aws

class CustomNetwork(pulumi.ComponentResource):
    def __init__(self, name, opts=None):
        super().__init__("custom:network:CustomNetwork", name, {}, opts)

        vpc = aws.ec2.Vpc(f"{name}-vpc",
            cidr_block="10.0.0.0/16",
            tags={"Name": f"{name}-vpc"})

        subnet = aws.ec2.Subnet(f"{name}-subnet",
            vpc_id=vpc.id,
            cidr_block="10.0.1.0/24",
            tags={"Name": f"{name}-subnet"})

        self.id = vpc.id
        self.subnet_id = subnet.id
        self.register_outputs({})
