from .internal import initialize_app, initialize_api, initialize_login_manager
from .utils.database import initialize_database
from .utils.open_ai import initialize_openai

def create_app():
    app = initialize_app()
    initialize_api(app)
    login_manager = initialize_login_manager(app)
    initialize_openai()
    initialize_database()
    return app
