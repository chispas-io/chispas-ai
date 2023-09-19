from openai.error import RateLimitError
from chispas.utils.open_ai import handle_openai_ratelimit_error

def test_handle_openai_ratelimit_error(app):
    with app.test_request_context():
        @handle_openai_ratelimit_error
        def to_be_decorated():
            raise RateLimitError

        assert 'Rate limited' == to_be_decorated()
