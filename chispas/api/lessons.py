from flask import Blueprint, jsonify, request, redirect, url_for
from flask_login import current_user
from ..utils.explanation  import generate_detailed_explanations
from ..utils.theme_analysis import analyze_themes_with_chatgpt
from ..utils.database import get_unknown_words, store_unknown_words

lessons_api = Blueprint('lessons', __name__)

@lessons_api.route('/api/lessons', methods=['GET'])
def list_lessons():
    raise NotImplementedError

@lessons_api.route('/api/lessons/difficult-words', methods=['GET', 'POST'])
def difficult_words():
    if request.method == 'POST':
        store_unknown_words(current_user.id, request.form['difficult_words'])

    return redirect(url_for('index'))

@lessons_api.route('/api/lessons/difficult-words/themes', methods=['GET', 'POST'])
def analyze_themes():
    if request.method == 'POST':
        raise NotImplementedError

    unknown_words = get_unknown_words(current_user.id)
    themes = analyze_themes_with_chatgpt(unknown_words)
    return jsonify(themes)

@lessons_api.route('/api/lessons/difficult-words/themes/details', methods=['GET', 'POST'])
def theme_analysis_details():
    if request.method == 'POST':
        raise NotImplementedError

    unknown_words = get_unknown_words(current_user.id)
    themes = analyze_themes_with_chatgpt(unknown_words)
    explanations = generate_detailed_explanations(unknown_words, themes)
    return jsonify(explanations)

@lessons_api.route('/api/lessons/difficult-words/generate-example', methods=['POST'])
def generate_example():
    raise NotImplementedError
