import os
from functools import wraps

from flask_login import login_required

def admin_required(f):
    @wraps(f)
    @login_required
    def decorated_view(*args, **kwargs):
        if not current_user.is_admin:
            return current_app.login_manager.unauthorized()

        return func(*args, **kwargs)

    return decorated_view
