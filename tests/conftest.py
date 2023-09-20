import os
import pytest
from flask import Flask
from chispas.utils.sessions import find_or_create_secret_key

@pytest.fixture
@pytest.mark.usefixtures('test_env')
def app():
    test_app = Flask(__name__)
    test_app.config['SECRET_KEY'] = find_or_create_secret_key()

    @test_app.route('/')
    def index():
        pass

    return test_app

@pytest.fixture
def test_env():
    os.environ['SECRET_KEY'] = 'b33f'
