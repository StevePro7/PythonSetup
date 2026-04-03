import http
import json
import traceback
import numpy as np
from azureml.contrib.services.aml_response import AMLResponse

from app.container import build_controller
from app.models.dto import InferenceRequest
from app.models.dto import InferenceResponse


controller = None


def init() -> None:
    build_controller()


def run(raw_data) -> AMLResponse:
    import torch, os
    print("Worker PID:", os.getpid())
    print("CUDA available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("CUDA device:", torch.cuda.get_device_name(0))

    build_controller()
    try:
        controller = build_controller()

        data = json.loads(raw_data)
        points = np.array(data["points"], dtype=np.float32)

        request: InferenceRequest = InferenceRequest(points=points)
        response: InferenceResponse = controller.handle(request)

        data = json.dumps(response.__dict__)
        return AMLResponse(message=data, status_code=http.HTTPStatus.OK)

    except Exception as e:
        return json.dumps({
            "error": str(e),
            "trace": traceback.format_exc()
        })
