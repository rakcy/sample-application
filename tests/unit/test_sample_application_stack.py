import aws_cdk as core
import aws_cdk.assertions as assertions

from sample_application.sample_application_stack import SampleApplicationStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sample_application/sample_application_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SampleApplicationStack(app, "sample-application")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
