import pytest
from flask import Flask

@pytest.fixture
def app():
    test_app = Flask(__name__)
    test_app.config['SECRET_KEY'] = 'b33f'

    @test_app.route('/')
    def index():
        pass

    return test_app
