from resource_baselines.s3 import BaselineS3Bucket
from resource_baselines._lambda import BaselineLambdaFunctionPython
from aws_cdk import (
    Stack,
    Duration,
)
from constructs import Construct


class SampleApplicationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        private_s3_bucket = BaselineS3Bucket(self, "PrivateS3Bucket")
        sample_lambda_function = BaselineLambdaFunctionPython(
            self,
            "SampleLambdaFunction",
            description=(
                "This is an example lambda function for AWS Community Day 2024"
            ),
            timeout=Duration.seconds(60),
            src_module="sample_lambda",
        )

        private_s3_bucket.grant_read(sample_lambda_function)
