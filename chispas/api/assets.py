from flask import Blueprint, send_from_directory

assets_api = Blueprint('assets', __name__)

@assets_api.route('/stylesheets/<path:path>')
def send_stylesheet(path):
    return send_from_directory('stylesheets', path)

@assets_api.route('/javascripts/<path:path>')
def send_js(path):
    return send_from_directory('javascripts', path)

@assets_api.route('/images/<path:path>')
def send_img(path):
    return send_from_directory('images', path)
