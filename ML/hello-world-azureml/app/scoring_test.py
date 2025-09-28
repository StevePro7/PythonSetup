import http
import json
import logging
import time

from azureml.contrib.services.aml_response import AMLResponse
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


model_runner = None


def init():
    logger.info("Initiating scoring script")
    logger.info(f"OS items '{os.environ.items()}'")

    global model_runner
    model_runner = ...  # Load your model here


def run(data: str):
    logger.info("Running scoring script")
    logger.info(f"Data: {data}")

    try:
        deserialized_input = json.loads(data)
        sleep = deserialized_input.get("sleep", 0)
        if sleep:
            logger.info(f"Sleeping for {sleep} seconds")
            time.sleep(sleep)

    except Exception as _:
        pass

    logger.info("Complete scoring script")
    return AMLResponse(message=data, status_code=http.HTTPStatus.OK)
