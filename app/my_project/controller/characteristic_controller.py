from flask import Flask, request, jsonify
from app.my_project.domain.dto import CharacteristicDto
from app.my_project.service.characteristic_service import CharacteristicService
from app import app

characteristic_service = CharacteristicService()

@app.route('/characteristics', methods=['POST'])
def create_characteristic():
    characteristic_dto = CharacteristicDto(**request.get_json())
    characteristic = characteristic_service.create_characteristic(characteristic_dto)
    return jsonify(characteristic.to_dict()), 201

@app.route('/characteristics/<int:id>', methods=['GET'])
def get_characteristic(id):
    characteristic = characteristic_service.get_characteristic(id)
    return jsonify(characteristic.to_dict())

@app.route('/characteristics/<int:id>', methods=['PUT'])
def update_characteristic(id):
    characteristic_dto = CharacteristicDto(**request.get_json())
    characteristic = characteristic_service.update_characteristic(characteristic_dto)
    return jsonify(characteristic.to_dict())

@app.route('/characteristics/<int:id>', methods=['DELETE'])
def delete_characteristic(id):
    characteristic_service.delete_characteristic(id)
    return '', 204
