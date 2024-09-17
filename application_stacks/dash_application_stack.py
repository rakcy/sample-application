from resource_baselines.s3 import BaselineS3Bucket
from resource_baselines._lambda import BaselineLambdaFunctionPython
from aws_cdk import (
    Stack,
    Duration,
)
from constructs import Construct


class DashApplicationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        BaselineS3Bucket(self, "private-s3-bucket")
        BaselineLambdaFunctionPython(
            self,
            "sample-lambda-function",
            description=(
                "This is an example lambda function for AWS Community Day 2024"
            ),
            timeout=Duration.seconds(60),
            src_module="sample_lambda",
        )
