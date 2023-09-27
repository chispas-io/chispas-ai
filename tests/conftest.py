import os
import pytest
from flask import Flask
from flask_login import LoginManager
from chispas.models.user import User
from chispas.utils.admin import admin_required
from chispas.utils.database import initialize_database
from chispas.internal import initialize_api, initialize_login_manager

@pytest.fixture
@pytest.mark.usefixtures('env')
def app():
    test_app = Flask(__name__)
    test_app.config['SECRET_KEY'] = 'jinx'
    test_app.config['TESTING'] = True
    initialize_api(test_app)
    login_manager = LoginManager()
    login_manager.init_app(test_app)

    @test_app.route('/')
    def index():
        pass

    @test_app.route("/admin-protected")
    @admin_required
    def protected():
        pass

    @login_manager.user_loader
    def user_loader(username):
        return User.query(username)

    # TODO: db.create_all()

    yield test_app

    # TODO: db.drop_all()

@pytest.fixture
def env():
    os.environ['SECRET_KEY'] = 'b33f'

@pytest.fixture
@pytest.mark.usefixtures('env')
def test_user():
    initialize_database()
    return User.create('charlie', 'is_a_cat')

@pytest.fixture
@pytest.mark.usefixtures('env')
def test_admin():
    initialize_database()
    user = User.create('sif', 'is_a_cat')
    user.is_admin = True
    return user
