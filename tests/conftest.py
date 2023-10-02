# import os
# import pytest
# from flask import Flask
# from flask_login import LoginManager
# from chispas.models.user import User
# from chispas.internal import initialize_api
#
# @pytest.fixture
# @pytest.mark.usefixtures('env')
# def app():
#     test_app = Flask(__name__)
#     test_app.config['SECRET_KEY'] = 'jinx'
#     test_app.config['TESTING'] = True
#     initialize_api(test_app)
#     # login_manager = LoginManager()
#     # login_manager.init_app(test_app)
#
#     @test_app.route('/')
#     def index():
#         pass
#
#     @login_manager.user_loader
#     def user_loader(username):
#         return User.query(username)
#
#     yield test_app
#
# @pytest.fixture
# def env():
#     os.environ['SECRET_KEY'] = 'b33f'
