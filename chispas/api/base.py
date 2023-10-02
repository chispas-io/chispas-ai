from flask import Blueprint, render_template
from flask_login import current_user
from ..constants.languages import DEFAULT_BASE_LANGUAGE, DEFAULT_LEARNING_LANGUAGE
from ..utils.database import get_unknown_words
from ..utils.example_generation import (
    generate_new_examples,
    generate_progression_text_block
)
from ..utils.explanation import generate_detailed_explanations
from ..utils.text import display_entire_text
from ..utils.theme_analysis import analyze_themes_with_chatgpt

base_api = Blueprint('base', __name__)

@base_api.route('/', methods=['GET'])
def index():
    # To display entire block of text to the user
    random_text = display_entire_text('./tests/fixtures/es_input_text.txt')

    # Get the list of difficult words from the user
    initial_difficult_words = get_unknown_words(current_user.id)
    difficult_words = ', '.join(initial_difficult_words)

    # Analyze the themes in the list of unknown words using ChatGPT
    themes = analyze_themes_with_chatgpt(
        initial_difficult_words,
        learning_language=DEFAULT_LEARNING_LANGUAGE,
        known_language=DEFAULT_BASE_LANGUAGE
    )

    # Generate detailed explanations for the unknown words
    theme_details = generate_detailed_explanations(
        initial_difficult_words,
        themes,
        learning_language=DEFAULT_LEARNING_LANGUAGE,
        known_language=DEFAULT_BASE_LANGUAGE
    )

    # Generate a new example paragraph incorporating the unknown words
    new_example = generate_new_examples(
        initial_difficult_words,
        themes,
        learning_language=DEFAULT_LEARNING_LANGUAGE,
        known_language=DEFAULT_BASE_LANGUAGE
    )

    # Generate a new text block for the next learning cycle
    progressive_text = generate_progression_text_block(
        initial_difficult_words,
        themes,
        'beginner',
        learning_language=DEFAULT_LEARNING_LANGUAGE,
        known_language=DEFAULT_BASE_LANGUAGE
    )

    return render_template(
        'index.html',
        difficult_words=difficult_words,
        new_example=new_example,
        progressive_text=progressive_text,
        random_text=random_text,
        theme_details=theme_details,
        themes=themes
    )
