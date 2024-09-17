from requests import get


def handler(event, context):
    response = get("http://ip.jsontest.com/")
    return response.json()
