from flask import Flask, request, jsonify
from app.my_project.domain.dto import ReviewDto
from app.my_project.service.review_service import ReviewService
from app.app_start import app, db

review_service = ReviewService(db)

@app.route('/reviews', methods=['POST'])
def create_review():
    review_dto = ReviewDto(**request.get_json())
    review = review_service.create_review(review_dto)
    return jsonify(review.to_dict()), 201

@app.route('/reviews/<int:id>', methods=['GET'])
def get_review(id):
    review = review_service.get_review(id)
    return jsonify(review.to_dict())

@app.route('/reviews/<int:id>', methods=['PUT'])
def update_review(id):
    review_dto = ReviewDto(**request.get_json())
    review = review_service.update_review(review_dto)
    return jsonify(review.to_dict())

@app.route('/reviews/<int:id>', methods=['DELETE'])
def delete_review(id):
    review_service.delete_review(id)
    return '', 204
