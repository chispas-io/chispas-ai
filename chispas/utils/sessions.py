import datetime
from secrets import token_urlsafe
import jwt

def create_secret_key():
    """
    secret key for sessions.

    see http://flask.pocoo.org/docs/latest/config/#SECRET_KEY.
    """

    return token_urlsafe(64)
