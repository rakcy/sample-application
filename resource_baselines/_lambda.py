import os

from aws_cdk import aws_lambda, Duration, Tags
from constructs import Construct

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
LAMBDA_BUILDER_PATH = os.path.join(DIR_PATH, "lambda_builder.Dockerfile")


class BaselineLambdaFunctionPython(aws_lambda.Function):
    def __init__(
        self,
        scope: Construct,
        id: str,
        src_module: str,
        description: str,
        environment: dict[str, str] = None,
        layers: list[aws_lambda.ILayerVersion] = None,
        timeout=Duration.seconds(10),
        # Equivalent to ~1 vCPU
        memory_size=1769,
        **kwargs,
    ):
        app_path = scope.node.get_context("app_path")
        src_relpath = os.path.join("src", src_module)

        code = aws_lambda.Code.from_docker_build(
            path=app_path,
            file=os.path.relpath(
                LAMBDA_BUILDER_PATH,
                app_path,
            ),
            build_args={
                "SRC_PATH": src_relpath,
            }
        )

        super().__init__(
            scope=scope,
            id=id,
            code=code,
            handler="handler.handler",
            runtime=aws_lambda.Runtime.PYTHON_3_12,
            description=description,
            environment=environment,
            layers=layers,
            memory_size=memory_size,
            timeout=timeout,
            **kwargs,
        )

        Tags.of(self).add("construct_id", id)
