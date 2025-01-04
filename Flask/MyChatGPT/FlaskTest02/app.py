from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from repositories import UserRepository
from services import UserService
from pydantic_models import UserCreateRequest, UserResponse
from models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Dependency Injection (via constructor injection)
user_repository = UserRepository(db.session)
user_service = UserService(user_repository)

@app.route("/users", methods=["GET"])
def get_users():
    users = user_service.get_all_users()
    return jsonify([user.dict() for user in users]), 200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    user = user_service.get_user_by_id(user_id)
    return jsonify(user.dict()), 200

@app.route("/users", methods=["POST"])
def create_user():
    try:
        # Parse and validate the input using Pydantic model
        user_data = UserCreateRequest(**request.get_json())
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    user = user_service.create_user(user_data)
    return jsonify(user.dict()), 201

if __name__ == "__main__":
    app.run(debug=True)
