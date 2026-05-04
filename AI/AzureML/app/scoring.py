import http
import json
from azureml.contrib.services.aml_response import AMLResponse


def init():
    pass


def run(raw_data: str) -> AMLResponse:
    results: dict = {
        "foo": "bar"
    }

    data = json.dumps(results)
    return AMLResponse(message=data, status_code=http.HTTPStatus.OK)