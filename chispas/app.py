import os
import requests
from flask import (
    Flask,
    flash,
    jsonify,
    redirect,
    request,
    render_template,
    send_from_directory,
    session,
    url_for,
)
from flask_cors import CORS
from .utils.database import (
    initialize_database,
    store_unknown_words,
    get_unknown_words,
)
from .utils.open_ai import set_api_key
from .utils.example_generation import (
    generate_new_examples,
    generate_progression_text_block,
)
from .utils.explanation import generate_detailed_explanations
from .utils.sessions import create_secret_key
from .utils.text import (
    display_entire_text,
    display_random_text_block,
)
from .utils.theme_analysis import analyze_themes_with_chatgpt

def create_app():
    print('Chispas online!')

    app = Flask(__name__)
    app.config['SECRET_KEY'] = create_secret_key()
    CORS(app)

    set_api_key()

    initialize_database()

    # Hardcoded user_id for demonstration; in a real application, you'll
    # dynamically determine this
    user_id = 1

    @app.route('/', methods=['GET'])
    def index():
        #  if 'username' not in session:
        #      return redirect(url_for('login'))

        #  flash(f'Hello {session["username"]}')

        # To display entire block of text to the user
        random_text = display_entire_text("./tests/fixtures/es_input_text.txt")

        # Get the list of difficult words from the user
        initial_difficult_words = get_unknown_words(user_id)
        difficult_words = " ".join(initial_difficult_words)

        # Add constants for testing (so we can test other languages too)
        LEARNING_LANGUAGE="spanish"
        KNOWN_LANGUAGE="english"

        # Analyze the themes in the list of unknown words using ChatGPT
        themes = analyze_themes_with_chatgpt(initial_difficult_words, learning_language=LEARNING_LANGUAGE, known_language=KNOWN_LANGUAGE)

        # Generate detailed explanations for the unknown words
        theme_details = generate_detailed_explanations(initial_difficult_words, themes, learning_language=LEARNING_LANGUAGE, known_language=KNOWN_LANGUAGE)

        # Generate a new example paragraph incorporating the unknown words
        new_example = generate_new_examples(initial_difficult_words, themes, learning_language=LEARNING_LANGUAGE, known_language=KNOWN_LANGUAGE)

        # Generate a new text block for the next learning cycle
        progressive_text = generate_progression_text_block(initial_difficult_words, themes, "beginner", learning_language=LEARNING_LANGUAGE, known_language=KNOWN_LANGUAGE)

        return render_template('index.html', random_text=random_text, difficult_words=difficult_words, themes=themes, theme_details=theme_details, new_example=new_example, progressive_text=progressive_text)

    @app.route("/api/v1/lessons", methods=['GET'])
    def list_lessons():
        raise NotImplementedError

    @app.route("/api/v1/lessons/difficult-words", methods=['GET', 'POST'])
    def difficult_words():
        if request.method == 'POST':
            difficult_words = request.form['difficult_words']
            store_unknown_words(user_id, difficult_words)
            return redirect(url_for('index'))

        return jsonify(get_unknown_words(user_id))

    @app.route("/api/v1/lessons/difficult-words/themes", methods=['GET', 'POST'])
    def analyze_themes():
        if request.method == 'POST':
            raise NotImplementedError

        difficult_words = get_unknown_words(user_id)
        themes = analyze_themes_with_chatgpt(difficult_words)
        return jsonify(themes)

    @app.route("/api/v1/lessons/difficult-words/themes/details", methods=['GET', 'POST'])
    def theme_analysis_details():
        if request.method == 'POST':
            raise NotImplementedError

        difficult_words = get_unknown_words(user_id)
        themes = analyze_themes_with_chatgpt(difficult_words)
        explanations = generate_detailed_explanations(difficult_words, themes)
        return jsonify(explanations)

    @app.route("/api/v1/lessons/difficult-words/generate-example", methods=['POST'])
    def generate_example():
        raise NotImplementedError

    @app.route("/api/v1/languages/list", methods=['GET'])
    def list_supported_languages():
        raise NotImplementedError

    @app.route("/api/v1/users/create", methods=['POST'])
    def create_user():
        session['username'] = 'Tomas'
        return jsonify(success=True)

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return render_template('login.html')

    @app.route("/logout")
    def logout():
        session.clear()
        flash("Logged out.")
        return redirect(url_for('index'))

    @app.route('/stylesheets/<path:path>')
    def send_stylesheet(path):
        return send_from_directory('stylesheets', path)

    @app.route('/javascripts/<path:path>')
    def send_js(path):
        return send_from_directory('javascripts', path)

    @app.route('/images/<path:path>')
    def send_img(path):
        return send_from_directory('images', path)

    return app
