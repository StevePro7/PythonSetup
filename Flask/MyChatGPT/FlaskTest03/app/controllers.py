from flask import Blueprint, request, jsonify
from app.repositories import UserRepository
from app.services import UserService
from app.serializers import UserSchema
from app.database import db

user_bp = Blueprint('users', __name__)
user_repository = UserRepository(db.session)
user_service = UserService(user_repository)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify(users_schema.dump(users)), 200

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user_schema.dump(user)), 200
    return jsonify({'message': 'User not found'}), 404

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = user_service.create_user(data['name'], data['email'])
    return jsonify(user_schema.dump(user)), 201

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_service.delete_user(user_id):
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'message': 'User not found'}), 404

def register_blueprints(app):
    app.register_blueprint(user_bp)
