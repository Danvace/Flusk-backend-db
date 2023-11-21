from flask import Flask, request, jsonify
from app.my_project.domain.dto import CategoryDto
from app.my_project.service.category_service import CategoryService
from app.app_start import app,db

category_service = CategoryService(db)

@app.route('/categories', methods=['POST'])
def create_category():
    category_dto = CategoryDto(**request.get_json())
    category = category_service.create_category(category_dto)
    return jsonify(category.to_dict()), 201

@app.route('/categories/<string:name>', methods=['GET'])
def get_category(name):
    category = category_service.get_category(name)
    return jsonify(category.to_dict())

@app.route('/categories/<string:name>', methods=['PUT'])
def update_category(name):
    category_dto = CategoryDto(**request.get_json())
    category = category_service.update_category(category_dto)
    return jsonify(category.to_dict())

@app.route('/categories/<string:name>', methods=['DELETE'])
def delete_category(name):
    category_service.delete_category(name)
    return '', 204
