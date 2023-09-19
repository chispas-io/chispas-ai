import pytest
import flask

@pytest.fixture
def app():
    test_app = flask.Flask(__name__)
    test_app.secret_key = 'b33f'

    @test_app.route('/')
    def index():
        pass

    return test_app
