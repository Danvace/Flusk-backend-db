from flask import Flask, request, jsonify
from app.my_project.domain.dto import DeliveryDto
from app.my_project.service.delivery_service import DeliveryService
from app import app

delivery_service = DeliveryService()

@app.route('/deliveries', methods=['POST'])
def create_delivery():
    delivery_dto = DeliveryDto(**request.get_json())
    delivery = delivery_service.create_delivery(delivery_dto)
    return jsonify(delivery.to_dict()), 201

@app.route('/deliveries/<int:id>', methods=['GET'])
def get_delivery(id):
    delivery = delivery_service.get_delivery(id)
    return jsonify(delivery.to_dict())

@app.route('/deliveries/<int:id>', methods=['PUT'])
def update_delivery(id):
    delivery_dto = DeliveryDto(**request.get_json())
    delivery = delivery_service.update_delivery(delivery_dto)
    return jsonify(delivery.to_dict())

@app.route('/deliveries/<int:id>', methods=['DELETE'])
def delete_delivery(id):
    delivery_service.delete_delivery(id)
    return '', 204
