from flask import Flask, request, jsonify
from app.my_project.domain.dto import OrderDto
from app.my_project.service.order_service import OrderService
from app import app

order_service = OrderService()

@app.route('/orders', methods=['POST'])
def create_order():
    order_dto = OrderDto(**request.get_json())
    order = order_service.create_order(order_dto)
    return jsonify(order.to_dict()), 201

@app.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = order_service.get_order(id)
    return jsonify(order.to_dict())

@app.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    order_dto = OrderDto(**request.get_json())
    order = order_service.update_order(order_dto)
    return jsonify(order.to_dict())

@app.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    order_service.delete_order(id)
    return '', 204
