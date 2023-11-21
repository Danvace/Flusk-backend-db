from flask import Flask, request, jsonify
from app.my_project.auth.domain.i_dto import BasketHasProductService, BasketHasProductDto
from app import app

basket_has_product_service = BasketHasProductService()

@app.route('/basket_has_products', methods=['POST'])
def create_basket_has_product():
    basket_has_product_dto = BasketHasProductDto(**request.get_json())
    basket_has_product = basket_has_product_service.create_basket_has_product(basket_has_product_dto)
    return jsonify(basket_has_product.to_dict()), 201

@app.route('/basket_has_products/<int:id>', methods=['GET'])
def get_basket_has_product(id):
    basket_has_product = basket_has_product_service.get_basket_has_product(id)
    return jsonify(basket_has_product.to_dict())

@app.route('/basket_has_products/<int:id>', methods=['PUT'])
def update_basket_has_product(id):
    basket_has_product_dto = BasketHasProductDto(**request.get_json())
    basket_has_product = basket_has_product_service.update_basket_has_product(id, basket_has_product_dto)
    return jsonify(basket_has_product.to_dict())

@app.route('/basket_has_products/<int:id>', methods=['DELETE'])
def delete_basket_has_product(id):
    basket_has_product_service.delete_basket_has_product(id)
    return '', 204
