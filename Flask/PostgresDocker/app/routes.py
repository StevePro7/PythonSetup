from flask import Blueprint, jsonify

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return "Hello, Flask with PostgreSQL!"


@bp.route("/users", methods=["GET"])
def get_users():
    from app.models import User

    # Query the database for all users
    users = User.query.all()

    # Convert the user objects to dictionaries
    user_list = [{"id": user.id, "username": user.username} for user in users]

    return jsonify(user_list)
