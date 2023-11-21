from flask import Flask, request, jsonify
from app.my_project.domain.dto import BasketDto
from app.my_project.service.basket_service import BasketService
from app.app_start import app, db

basket_service = BasketService(db)

@app.route('/baskets', methods=['POST'])
def create_basket():
    basket_dto = BasketDto(**request.get_json())
    basket = basket_service.create_basket(basket_dto)
    return jsonify(basket.to_dict()), 201

@app.route('/baskets/<int:id>', methods=['GET'])
def get_basket(id):
    basket = basket_service.get_basket(id)
    return jsonify(basket.to_dict())

@app.route('/baskets/<int:id>', methods=['PUT'])
def update_basket(id):
    basket_dto = BasketDto(**request.get_json())
    basket = basket_service.update_basket(id, basket_dto)
    return jsonify(basket.to_dict())

@app.route('/baskets/<int:id>', methods=['DELETE'])
def delete_basket(id):
    basket_service.delete_basket(id)
    return '', 204
