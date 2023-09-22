from logging import info
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from .utils.sessions import find_or_create_secret_key

def initialize_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = find_or_create_secret_key()
    CORS(app)
    info('Chispas online!')
    return app

def initialize_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    return login_manager
