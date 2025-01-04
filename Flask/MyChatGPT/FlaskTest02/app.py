from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from repositories import UserRepository
from services import UserService
from serializers import UserSchema
from models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Dependency Injection (via constructor injection)
user_repository = UserRepository(db.session)
user_schema = UserSchema()
user_service = UserService(user_repository, user_schema)

@app.route("/users", methods=["GET"])
def get_users():
    users = user_service.get_all_users()
    return jsonify(users), 200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    return jsonify(user), 200

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    user = user_service.create_user(name, email)
    return jsonify(user), 201

if __name__ == "__main__":
    app.run(debug=True)
