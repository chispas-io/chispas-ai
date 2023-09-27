from flask import Blueprint, jsonify

base_api = Blueprint('base', __name__)

@base_api.route('/', methods=['GET'])
def index():
    return jsonify('✨ Chispas')
