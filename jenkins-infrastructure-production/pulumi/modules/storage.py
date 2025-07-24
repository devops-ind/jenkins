import pulumi_aws as aws

class CustomStorage(pulumi.ComponentResource):
    def __init__(self, name, network_id, opts=None):
        super().__init__("custom:storage:CustomStorage", name, {}, opts)

        efs = aws.efs.FileSystem(f"{name}-efs",
            tags={"Name": f"{name}-efs"})

        mount_target = aws.efs.MountTarget(f"{name}-mount-target",
            file_system_id=efs.id,
            subnet_id=network_id)

        self.id = efs.id
        self.register_outputs({})
