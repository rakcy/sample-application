from aws_cdk import aws_s3, RemovalPolicy, Tags, aws_kms
from constructs import Construct


class BaselineS3Bucket(aws_s3.Bucket):
    def __init__(
        self,
        scope: Construct,
        id: str,
        access_control=aws_s3.BucketAccessControl.PRIVATE,
        block_public_access=aws_s3.BlockPublicAccess.BLOCK_ALL,
        public_read_access=False,
        encryption_key: aws_kms.IKey = None,
        versioned=True,
        **kwargs,
    ):
        super().__init__(
            scope=scope,
            id=id,
            access_control=access_control,
            block_public_access=block_public_access,
            public_read_access=public_read_access,
            versioned=versioned,
            encryption_key=encryption_key,
            # Strict defaults
            encryption=aws_s3.BucketEncryption.KMS,
            auto_delete_objects=False,
            enforce_ssl=True,
            minimum_tls_version=1.2,
            # Easier re-deployment during stack creation
            removal_policy=RemovalPolicy.RETAIN_ON_UPDATE_OR_DELETE,
            **kwargs,
        )

        Tags.of(self).add("construct_id", id)
