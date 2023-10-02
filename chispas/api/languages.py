from flask import Blueprint
from ..constants.languages import SUPPORTED_LANGUAGES
from ..utils.api import jinx_jsonify

languages_api = Blueprint('languages', __name__)

@languages_api.route('/api/languages/list', methods=['GET'])
def list_supported_languages():
    return jinx_jsonify({ 'languages': SUPPORTED_LANGUAGES })
