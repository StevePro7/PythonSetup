import os
from dataclasses import dataclass
from pathlib import Path

from joblib import load


@dataclass(frozen=True)
class AppContext:
    model: object
    model_name: str
    model_version: str


def build_app_context() -> AppContext:
    # TODO
#    model_path = Path(os.getenv("AZUREML_MODEL_DIR")) / "model.joblib"
#    model = load(model_path)

    model = None
    return AppContext(
        model=model,
        model_name=os.getenv("MODEL_NAME", "unknown"),
        model_version=os.getenv("MODEL_VERSION", "unknown"),
    )
