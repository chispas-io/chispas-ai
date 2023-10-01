from flask import (
    flash,
    jsonify,
    redirect,
    request,
    render_template,
    send_from_directory,
    url_for,
)
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)
from .internal import initialize_app, initialize_login_manager
from .models.user import User
from .utils.database import (
    initialize_database,
    store_unknown_words,
    get_unknown_words,
)
from .utils.open_ai import initialize_openai
from .utils.example_generation import (
    generate_new_examples,
    generate_progression_text_block,
)
from .utils.explanation import generate_detailed_explanations
from .utils.text import display_entire_text
from .utils.theme_analysis import analyze_themes_with_chatgpt

# Add constants for testing (so we can test other languages too)
LEARNING_LANGUAGE='spanish'
KNOWN_LANGUAGE='english'

def create_app(): # pylint: disable=too-many-locals
    app = initialize_app()
    login_manager = initialize_login_manager(app)
    initialize_openai()
    initialize_database()

    @app.route('/', methods=['GET'])
    @login_required
    def index():
        # To display entire block of text to the user
        random_text = display_entire_text('./tests/fixtures/es_input_text.txt')

        # Get the list of difficult words from the user
        initial_difficult_words = get_unknown_words(current_user.id)
        difficult_words = ', '.join(initial_difficult_words)

        # Analyze the themes in the list of unknown words using ChatGPT
        themes = analyze_themes_with_chatgpt(
            initial_difficult_words,
            learning_language=LEARNING_LANGUAGE,
            known_language=KNOWN_LANGUAGE
        )

        # Generate detailed explanations for the unknown words
        theme_details = generate_detailed_explanations(
            initial_difficult_words,
            themes,
            learning_language=LEARNING_LANGUAGE,
            known_language=KNOWN_LANGUAGE
        )

        # Generate a new example paragraph incorporating the unknown words
        new_example = generate_new_examples(
            initial_difficult_words,
            themes,
            learning_language=LEARNING_LANGUAGE,
            known_language=KNOWN_LANGUAGE
        )

        # Generate a new text block for the next learning cycle
        progressive_text = generate_progression_text_block(
            initial_difficult_words,
            themes,
            'beginner',
            learning_language=LEARNING_LANGUAGE,
            known_language=KNOWN_LANGUAGE
        )

        return render_template(
            'index.html',
            difficult_words=difficult_words,
            new_example=new_example,
            progressive_text=progressive_text,
            random_text=random_text,
            theme_details=theme_details,
            themes=themes,
        )

    @app.route('/api/lessons', methods=['GET'])
    @login_required
    def list_lessons():
        raise NotImplementedError

    @app.route('/api/lessons/difficult-words', methods=['GET', 'POST'])
    @login_required
    def difficult_words():
        if request.method == 'POST':
            difficult_words = request.form['difficult_words']
            store_unknown_words(current_user.id, difficult_words)

        return redirect(url_for('index'))

    @app.route('/api/lessons/difficult-words/themes', methods=['GET', 'POST'])
    @login_required
    def analyze_themes():
        if request.method == 'POST':
            raise NotImplementedError

        difficult_words = get_unknown_words(current_user.id)
        themes = analyze_themes_with_chatgpt(difficult_words)
        return jsonify(themes)

    @app.route('/api/lessons/difficult-words/themes/details', methods=['GET', 'POST'])
    @login_required
    def theme_analysis_details():
        if request.method == 'POST':
            raise NotImplementedError

        difficult_words = get_unknown_words(current_user.id)
        themes = analyze_themes_with_chatgpt(difficult_words)
        explanations = generate_detailed_explanations(difficult_words, themes)
        return jsonify(explanations)

    @app.route('/api/lessons/difficult-words/generate-example', methods=['POST'])
    @login_required
    def generate_example():
        raise NotImplementedError

    @app.route('/api/languages/list', methods=['GET'])
    @login_required
    def list_supported_languages():
        raise NotImplementedError

    # curl -X POST -d "username=charlie&password=is_a_cat" http://localhost:5000/api/users/add
    @app.route('/api/users/add', methods=['POST'])
    def add_user():
        username = request.form['username']
        password = request.form['password']

        if User.query(username):
            flash('User already exists', 'error')
            return jsonify(username)

        user = User.create(username, password)

        login_user(user)

        return jsonify(username)

    # curl -X POST -d "username=charlie&password=is_a_cat" http://localhost:5000/authenticate
    @app.route('/authenticate', methods=['POST'])
    def authenticate():
        user = User.valid_login_request(request)
        if user:
            return jsonify({ 'authentication_token': user.authentication_token })

        return jsonify({ 'error': 'Invalid username or password' }), 401

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            if current_user.is_authenticated:
                flash('You are already logged in!')
                return redirect(url_for('index'))

            return render_template('login.html')

        user = User.valid_login_request(request)
        if user:
            login_user(user, remember=True)
            return redirect(url_for('index'))

        return render_template('login.html')

    @app.route('/logout', methods=['POST'])
    @login_required
    def logout():
        logout_user()
        flash('Logged out')
        return redirect(url_for('login'))

    @app.route('/stylesheets/<path:path>')
    def send_stylesheet(path):
        return send_from_directory('stylesheets', path)

    @app.route('/javascripts/<path:path>')
    def send_js(path):
        return send_from_directory('javascripts/dist', path)

    @app.route('/images/<path:path>')
    def send_img(path):
        return send_from_directory('images', path)

    @login_manager.user_loader
    def user_loader(username):
        return User.query(username)

    # https://flask-login.readthedocs.io/en/latest/#custom-login-using-request-loader
    @login_manager.request_loader
    def request_loader(rqst):
        username = rqst.form.get('username')
        return User.query(username)

    return app
