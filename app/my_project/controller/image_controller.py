from flask import Flask, request, jsonify
from app.my_project.domain.dto import ImageDto
from app.my_project.service.image_service import ImageService
from app import app

image_service = ImageService()

@app.route('/images', methods=['POST'])
def create_image():
    image_dto = ImageDto(**request.get_json())
    image = image_service.create_image(image_dto)
    return jsonify(image.to_dict()), 201

@app.route('/images/<int:id>', methods=['GET'])
def get_image(id):
    image = image_service.get_image(id)
    return jsonify(image.to_dict())

@app.route('/images/<int:id>', methods=['PUT'])
def update_image(id):
    image_dto = ImageDto(**request.get_json())
    image = image_service.update_image(image_dto)
    return jsonify(image.to_dict())

@app.route('/images/<int:id>', methods=['DELETE'])
def delete_image(id):
    image_service.delete_image(id)
    return '', 204
