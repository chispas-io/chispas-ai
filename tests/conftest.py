import os
import pytest
from flask import Flask
from chispas.utils.sessions import find_or_create_secret_key

@pytest.fixture
@pytest.mark.usefixtures('env')
def app():
    test_app = Flask(__name__)
    test_app.config['SECRET_KEY'] = find_or_create_secret_key()
    test_app.config['TESTING'] = True

    @test_app.route('/')
    def index():
        pass

    yield test_app

@pytest.fixture
def env():
    os.environ['SECRET_KEY'] = 'b33f'
