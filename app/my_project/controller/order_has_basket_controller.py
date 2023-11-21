from flask import Flask, request, jsonify
from app.my_project.domain.dto import OrderHasBasketDto
from app.my_project.service.order_has_basket_service import OrderHasBasketService
from app.app_start import app,db

order_has_basket_service = OrderHasBasketService(db)

@app.route('/order_has_basket', methods=['POST'])
def create_order_has_basket():
    order_has_basket_dto = OrderHasBasketDto(**request.get_json())
    order_has_basket = order_has_basket_service.create_order_has_basket(order_has_basket_dto)
    return jsonify(order_has_basket.to_dict()), 201

@app.route('/order_has_basket/<int:id>', methods=['GET'])
def get_order_has_basket(id):
    order_has_basket = order_has_basket_service.get_order_has_basket(id)
    return jsonify(order_has_basket.to_dict())

@app.route('/order_has_basket/<int:id>', methods=['PUT'])
def update_order_has_basket(id):
    order_has_basket_dto = OrderHasBasketDto(**request.get_json())
    order_has_basket = order_has_basket_service.update_order_has_basket(order_has_basket_dto)
    return jsonify(order_has_basket.to_dict())

@app.route('/order_has_basket/<int:id>', methods=['DELETE'])
def delete_order_has_basket(id):
    order_has_basket_service.delete_order_has_basket(id)
    return '', 204
