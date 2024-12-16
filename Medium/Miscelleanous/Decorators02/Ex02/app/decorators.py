from flask import request, jsonify
import http

def require_api_key(func):
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("x-api-key")
        if api_key != "mysecurekey123":
            return jsonify({"error": "Unauthorized"}), http.HTTPStatus.UNAUTHORIZED
        return func(*args, **kwargs)
    return wrapper