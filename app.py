#!/usr/bin/env python3
import os

from aws_cdk import App, Tags  # , Aspects

from application_stacks.sample_application_stack import SampleApplicationStack
from application_stacks.dash_application_stack import DashApplicationStack
# from cdk_nag import PCIDSS321Checks
from aws_pdk.cdk_graph import CdkGraph
from aws_pdk.cdk_graph_plugin_diagram import (
    CdkGraphDiagramPlugin,
)


app = App()

# Aspects.of(app).add(PCIDSS321Checks(verbose=True))

app_path = app.node.try_get_context("app_path")
if not app_path:
    app_path = os.path.dirname(os.path.realpath(__file__))
    app.node.set_context("app_path", app_path)

deployment_environment: str = app.node.try_get_context("deployment_environment")
if deployment_environment:
    assert deployment_environment in ("production", "qa")
    deployment_environment = deployment_environment.capitalize()
else:
    deployment_environment = ""

Tags.of(app).add(
    "deployment_environment",
    deployment_environment.lower(),
)

SampleApplicationStack(
    app,
    f"{deployment_environment}SampleApplicationStack",
)

if deployment_environment:
    DashApplicationStack(
        app,
        f"{deployment_environment.lower()}-dash-application-stack",
    )

cdk_graph = CdkGraph(
    app,
    plugins=[CdkGraphDiagramPlugin()],
)

app.synth()

cdk_graph.report()
