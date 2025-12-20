#!/usr/bin/env python3



import os
import sys
import json
import http
from pathlib import Path

# Setup paths and environment
project_root = Path(__file__).parent
app_dir = project_root / "app"
sys.path.insert(0, str(app_dir))


os.environ["AZUREML_MODEL_DIR"] = str(project_root / "model")
#os.environ["PYTHONPATH"] = str(app_dir)