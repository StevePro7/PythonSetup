#!/usr/bin/env python3
"""


"""
import http
import os
import sys
import json
from flask import Flask, request, jsonify
import importlib.util
# Add app dir
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "app"))

def load_scoring_module():
    """Load scoring.py module dynamically (like Azure ML does)"""
    scoring_path = os.path.join(os.path.dirname(__file__), "app", "scoring.py")

    spec = importlib.util.spec_from_file_location("scoring", scoring_path)
    scoring_module = importlib.util.module_from_spec(spec)

    # Set env var
    os.environ["AZUREML_MODEL_DIR"] = os.path.join(os.path.dirname(__file__), "model")

    spec.loader.exec_module(scoring_module)
    return scoring_module

# Create Flask app (similar to what Azure ML does)
app = Flask(__name__)

print("Load score mod")
scoring = load_scoring_module()

print("Call init")
try:
    scoring.init()
    print("Init complete")
except Exception as e:
    print(f"{e}")
    sys.exit(1)

@app.route("/score", methods=["POST"])
def score():
    """
    This endpoint simulates Azure ML /score endpoint
    It shows how run() gets called in Production
    """
    print()
    print("NEW REQ")
    print()

    try:
        # Get raw request data (like Azure ML does)
        raw_data = request.get_data(as_text=True)
        print(f"Raw req='{raw_data}'")
        print(f"Content='{request.content_type}'")
        print("Call scoring.run()")

        # Cal run function (like Azure ML does)
        aml_response = scoring.run(raw_data)

        print("NEW RES")
        print(f"Code:'{aml_response.status_code}'")
        print(f"Type:'{type(aml_response.data)}")
        print(f"Data:'{str(aml_response.data)[:200]}...")

        # Convert AML Response to Flask response (like Azure ML does)
        response_data = aml_response.data
        if isinstance(response_data, bytes):
            response_data = response_data.decode('utf-8')
        return response_data, aml_response.status_code, {"Content-Type": "application/json"}

    except Exception as e:
        print(f"Error {e}")
        import traceback
        traceback.print_exc()

        error_response = {
            "error": "Server error",
            "message": str(e)
        }
        return json.dumps(error_response), http.HTTPStatus.INTERNAL_SERVER_ERROR, {"Content-Type": "application/json"}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)