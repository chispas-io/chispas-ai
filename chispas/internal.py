import logging
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from .api import account_api, assets_api, base_api, feedback_api, languages_api, lessons_api, users_api
from .models.user import User
from .utils.sessions import find_or_create_secret_key

def initialize_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = find_or_create_secret_key()
    # header("Access-Control-Allow-Origin: http://localhost:8080");
    # header("Access-Control-Allow-Credentials: true");
    CORS(app, resources={ r"/api/*": { "origins": "*" } })
    logging.getLogger('flask_cors').level = logging.DEBUG
    logging.info('Chispas online!')
    return app

def initialize_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    # TODO: remove equiv in test app
    @login_manager.user_loader
    def user_loader(username):
        return User.query(username)

    # https://flask-login.readthedocs.io/en/latest/#custom-login-using-request-loader
    @login_manager.request_loader
    def request_loader(rqst):
        username = rqst.form.get('username')
        return User.query(username)

    return login_manager

def initialize_api(app):
    app.register_blueprint(base_api)
    app.register_blueprint(assets_api)

    app.register_blueprint(account_api, url_prefix='/api/account')
    app.register_blueprint(feedback_api, url_prefix='/api/feedback')
    app.register_blueprint(languages_api, url_prefix='/api/languages')
    app.register_blueprint(lessons_api, url_prefix='/api/lessons')
    app.register_blueprint(users_api, url_prefix='/api/users')
