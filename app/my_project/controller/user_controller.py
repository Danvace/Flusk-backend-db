from flask import Flask, request, jsonify
from app.my_project.domain.dto import UserDto
from app.my_project.service.user_service import UserService
from app import app

user_service = UserService()

@app.route('/users', methods=['POST'])
def create_user():
    user_dto = UserDto(**request.get_json())
    user = user_service.create_user(user_dto)
    return jsonify(user.to_dict()), 201

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = user_service.get_user(id)
    return jsonify(user.to_dict())

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user_dto = UserDto(**request.get_json())
    user = user_service.update_user(user_dto)
    return jsonify(user.to_dict())

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user_service.delete_user(id)
    return '', 204
