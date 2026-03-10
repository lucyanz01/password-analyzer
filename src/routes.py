from flask import Blueprint, request, jsonify
from analyzer import password_analyzer  

api = Blueprint('api', __name__)

@api.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    password = data.get('password', '')

    result = password_analyzer(password)

    return jsonify(result)