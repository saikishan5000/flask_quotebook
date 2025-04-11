from flask import Blueprint, request, jsonify
from app.services import quote_service
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.decorators.role_required import roles_required
quote_bp = Blueprint('quote_bp', __name__, url_prefix='/quotes')

@quote_bp.route('/', methods=['POST'])
@jwt_required()
@roles_required(0, 1)
def add_quote():
    data = request.get_json()
    if not data or 'author' not in data or 'quote' not in data:
        return jsonify({'error': 'Both author and quote are required.'}), 400
    quote = quote_service.create_quote(data)
    return jsonify(quote.to_dict()), 201

@quote_bp.route('/', methods=['GET'])
@jwt_required()
@roles_required(0, 1)
def get_quotes():
    quotes = quote_service.get_all_quotes()
    return jsonify([q.to_dict() for q in quotes])

@quote_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
@roles_required(0, 1)
def get_quote(id):
    quote = quote_service.get_quote_by_id(id)
    if not quote:
        return jsonify({'error': 'Quote not found'}), 404
    return jsonify(quote.to_dict())

@quote_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
@roles_required(1)
def update(id):
    data = request.get_json()
    quote = quote_service.get_quote_by_id(id)
    if not quote:
        return jsonify({'error': 'Quote not found'}), 404
    updated = quote_service.update_quote(quote, data)
    return jsonify({'message': 'Updated', 'quote': updated.to_dict()})

@quote_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@roles_required(1)
def delete(id):
    quote = quote_service.get_quote_by_id(id)
    if not quote:
        return jsonify({'error': 'Quote not found'}), 404
    quote_service.delete_quote(quote)
    return jsonify({'message': 'Deleted successfully'})
