from flask import request, jsonify
from http import HTTPStatus

def require_api_key(func):
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("x-api-key")
        if api_key != "mysecurekey123":
            return jsonify({"error": "Unauthorized"}, HTTPStatus.UNAUTHORIZED)
        return func(args, kwargs)
    return wrapper()
