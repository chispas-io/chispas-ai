import pytest
from flask import Flask

@pytest.fixture
def app():
    test_app = Flask(__name__)
    test_app.secret_key = 'b33f'

    @test_app.route('/')
    def index():
        pass

    return test_app
