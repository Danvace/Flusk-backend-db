from flask import Flask, request, jsonify
from app.my_project.domain.dto import DeliveryTypeDto
from app.my_project.service.delivery_type_service import DeliveryTypeService
from app import app

delivery_type_service = DeliveryTypeService()

@app.route('/delivery_types', methods=['POST'])
def create_delivery_type():
    delivery_type_dto = DeliveryTypeDto(**request.get_json())
    delivery_type = delivery_type_service.create_delivery_type(delivery_type_dto)
    return jsonify(delivery_type.to_dict()), 201

@app.route('/delivery_types/<string:type>', methods=['GET'])
def get_delivery_type(type):
    delivery_type = delivery_type_service.get_delivery_type(type)
    return jsonify(delivery_type.to_dict())

@app.route('/delivery_types/<string:type>', methods=['PUT'])
def update_delivery_type(type):
    delivery_type_dto = DeliveryTypeDto(**request.get_json())
    delivery_type = delivery_type_service.update_delivery_type(delivery_type_dto)
    return jsonify(delivery_type.to_dict())

@app.route('/delivery_types/<string:type>', methods=['DELETE'])
def delete_delivery_type(type):
    delivery_type_service.delete_delivery_type(type)
    return '', 204
