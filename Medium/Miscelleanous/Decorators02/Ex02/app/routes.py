from flask import Flask, jsonify
from app.decorators import require_api_key

app = Flask(__name__)

@app.route('secure-data', methods=["GET"])
@require_api_key
def secure_data():
    return jsonify({"data": "This is secure data!"})

if __name__ == "__main__":
    app.run(debug=True)