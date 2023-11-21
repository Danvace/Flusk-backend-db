from flask import Flask, request, jsonify
from app.my_project.domain.dto import ProductDto
from app.my_project.service.product_service import ProductService
from app.app_start import app, db

product_service = ProductService(db )

@app.route('/products', methods=['POST'])
def create_product():
    product_dto = ProductDto(**request.get_json())
    product = product_service.create_product(product_dto)
    return jsonify(product.to_dict()), 201

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = product_service.get_product(id)
    return jsonify(product.to_dict())

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product_dto = ProductDto(**request.get_json())
    product = product_service.update_product(product_dto)
    return jsonify(product.to_dict())

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product_service.delete_product(id)
    return '', 204
