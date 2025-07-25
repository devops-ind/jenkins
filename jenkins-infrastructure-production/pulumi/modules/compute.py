import pulumi_aws as aws

class CustomCompute(pulumi.ComponentResource):
    def __init__(self, name, network_id, storage_id, opts=None):
        super().__init__("custom:compute:CustomCompute", name, {}, opts)

        ami = aws.get_ami(
            most_recent=True,
            owners=["amazon"],
            filters=[{"name":"name","values":["amzn2-ami-hvm-2.0.????????-x86_64-gp2"]}])

        instance = aws.ec2.Instance(f"{name}-instance",
            ami=ami.id,
            instance_type="t2.micro",
            subnet_id=network_id,
            tags={"Name": f"{name}-instance"})

        self.id = instance.id
        self.register_outputs({})
