Python
from flask import Blueprint, jsonify, request
main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from Plasmo API!'})

@main_routes.route('/create', methods=['POST'])
def create():
    data = request.json
    return jsonify({'message': f'Created {data["name"]}!'})