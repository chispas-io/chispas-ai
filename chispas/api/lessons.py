from flask import Blueprint, jsonify, request
from ..utils.database import (
    initialize_database,
    store_unknown_words,
    get_unknown_words,
)
from ..utils.example_generation import (
    generate_new_examples,
    generate_progression_text_block,
)
from ..utils.explanation import generate_detailed_explanations
from ..utils.text import display_entire_text
from ..utils.theme_analysis import analyze_themes_with_chatgpt

lessons_api = Blueprint('lessons', __name__)

# TODO: add login_required to all routes
# TODO: bring in all the recent changes Ryan made to these endpoints
# TODO: https://tobiaslang.medium.com/mocking-the-openai-api-in-python-a-step-by-step-guide-4630efcb809d

@lessons_api.route('', methods=['GET'])
def list_lessons():
    raise NotImplementedError

@lessons_api.route('/difficult-words', methods=['GET', 'POST'])
def difficult_words():
    if request.method == 'POST':
        difficult_words = request.form['difficult_words']
        store_unknown_words(current_user.id, difficult_words)

    return jsonify(get_unknown_words(current_user.id))

@lessons_api.route('/difficult-words/themes', methods=['GET', 'POST'])
def analyze_themes():
    if request.method == 'POST':
        raise NotImplementedError

    difficult_words = get_unknown_words(current_user.id)
    themes = analyze_themes_with_chatgpt(difficult_words)
    return jsonify(themes)

@lessons_api.route('/difficult-words/themes/details', methods=['GET', 'POST'])
def theme_analysis_details():
    if request.method == 'POST':
        raise NotImplementedError

    difficult_words = get_unknown_words(current_user.id)
    themes = analyze_themes_with_chatgpt(difficult_words)
    explanations = generate_detailed_explanations(difficult_words, themes)
    return jsonify(explanations)

@lessons_api.route('/difficult-words/generate-example', methods=['POST'])
def generate_example():
    raise NotImplementedError
