import datetime
import os

from dotenv.cli import enumerate_env
from dotenv.main import set_key
from jwt import decode, encode
from secrets import token_urlsafe
from logging import error
from flask import current_app

def create_secret_key():
    """
    secret key for sessions.

    see http://flask.pocoo.org/docs/latest/config/#SECRET_KEY.
    """

    return token_urlsafe(64)

def find_or_create_secret_key():
    secret_key = os.environ.get("SECRET_KEY")

    if not secret_key:
        error('SECRET_KEY not set. Add this to your .env file.')
        secret_key = create_secret_key()

    return secret_key

def encode_token(subject) -> str:
    '''
    encode subject as JWT using secret key

    spec claim name section: https://tools.ietf.org/html/rfc7519#section-4.1
    jwt encode api doc: https://python-jose.readthedocs.io/en/latest/jwt/api.html#jose.jwt.encode
    '''

    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7, seconds=0),
        'iat': datetime.datetime.utcnow(),
        'sub': subject,
    }

    return encode(
        payload,
        os.environ.get("SECRET_KEY"),
        algorithm='HS256',
    )

def decode_token(subject) -> str:
    '''
    decode JWT subject using secret key

    jwt decode api: https://python-jose.readthedocs.io/en/latest/jwt/api.html#jose.jwt.decode
    '''

    decoded_payload = decode(
        subject,
        os.environ.get("SECRET_KEY"),
        algorithms=['HS256'],
    )

    return decoded_payload.get('sub')

def generate_secret_key() -> str:
    new_key = create_secret_key()
    set_key(enumerate_env(), "SECRET_KEY", new_key)
    return new_key
