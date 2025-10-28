"""Scoring script for Azure ML - loads model and returns predictions."""

import http
import json
import logging
import time
import os
from typing import Any, Dict

import joblib
import numpy as np
from azureml.contrib.services.aml_response import AMLResponse

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# container for loaded model objects
model_runner: Dict[str, Any] = {"model": None, "scaler": None, "info": None}


def _features_from_name(name: str):
    """Convert a name string into the feature vector expected by the model."""
    name_length = len(name)
    vowel_count = sum(1 for c in name.lower() if c in "aeiou")
    consonant_count = name_length - vowel_count
    return [name_length, vowel_count, consonant_count]


def init():
    """Azure ML init hook - load model and preprocessing artifacts into memory."""
    logger.info("Initiating scoring script")

    try:
        base_dir = os.path.dirname(os.path.dirname(__file__))
        model_dir = os.environ.get("MODEL_DIR", os.path.join(base_dir, "model"))

        model_path = os.path.join(model_dir, "greeting_model.pkl")
        scaler_path = os.path.join(model_dir, "scaler.pkl")
        info_path = os.path.join(model_dir, "model_info.json")

        logger.info("Loading model from %s", model_path)
        model = joblib.load(model_path)
        logger.info("Loading scaler from %s", scaler_path)
        scaler = joblib.load(scaler_path)

        model_info = None
        if os.path.exists(info_path):
            with open(info_path, "r", encoding="utf-8") as f:
                model_info = json.load(f)

        model_runner["model"] = model
        model_runner["scaler"] = scaler
        model_runner["info"] = model_info

        logger.info("Model loaded: %s", model_info.get("model_name") if model_info else str(model))

    except (FileNotFoundError, OSError, ValueError) as exc:
        logger.exception("Failed to initialize model runner: %s", exc)
        # keep model_runner in a safe, empty state
        model_runner["model"] = None
        model_runner["scaler"] = None
        model_runner["info"] = None


def run(data: str):
    """Azure ML run hook - accept JSON string, return prediction(s) wrapped in AMLResponse.

    Supported input examples:
      {"name": "Alice"}
      {"features": [[5,2,3], [4,1,3]]}
      {"instances": [[5,2,3]]}
    """

    logger.info("Running scoring script")
    logger.debug("Raw input: %s", data)

    if model_runner.get("model") is None or model_runner.get("scaler") is None:
        logger.error("Model or scaler not loaded")
        body = json.dumps({"error": "Model not loaded"})
        return AMLResponse(body, status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR)

    try:
        payload = json.loads(data)
    except json.JSONDecodeError as exc:
        logger.exception("Failed to parse input JSON: %s", exc)
        body = json.dumps({"error": "Invalid JSON payload"})
        return AMLResponse(body, status_code=http.HTTPStatus.BAD_REQUEST)

    # Allow optional sleep behavior for testing/backwards compatibility
    try:
        sleep = payload.get("sleep", 0)
        if sleep:
            logger.info("Sleeping for %s seconds", sleep)
            time.sleep(sleep)
    except (TypeError, ValueError):
        # ignore malformed sleep values
        pass

    # Build feature matrix
    features_arr = None
    if isinstance(payload, dict) and "name" in payload:
        features_arr = np.array([_features_from_name(payload["name"])])
    elif "features" in payload:
        features_arr = np.array(payload["features"])
    elif "instances" in payload:
        features_arr = np.array(payload["instances"])
    else:
        # unsupported payload
        logger.error("Unsupported payload format - expected 'name' or 'features' or 'instances'")
        body = json.dumps({"error": "Unsupported payload format"})
        return AMLResponse(body, status_code=http.HTTPStatus.BAD_REQUEST)

    try:
        scaler = model_runner["scaler"]
        model = model_runner["model"]

        features_scaled = scaler.transform(features_arr)
        preds = model.predict(features_scaled)

        # Ensure JSON serializable
        predictions = [float(p) for p in preds]

        result = {"predictions": predictions, "model": model_runner.get("info")}
        logger.info("Complete scoring script")
        body = json.dumps(result)
        return AMLResponse(body, status_code=http.HTTPStatus.OK)

    except (AttributeError, ValueError) as exc:
        logger.exception("Failed during prediction: %s", exc)
        body = json.dumps({"error": "Prediction failed"})
        return AMLResponse(body, status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR)
