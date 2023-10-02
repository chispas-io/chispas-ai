import datetime
import os
from secrets import token_urlsafe
from logging import error

from dotenv.cli import enumerate_env
from dotenv.main import set_key
from jwt import decode, encode

def create_secret_key() -> str:
    '''
    secret key for sessions.

    see http://flask.pocoo.org/docs/latest/config/#SECRET_KEY.
    '''

    return token_urlsafe(64)

def find_or_create_secret_key() -> str:
    secret_key = os.environ.get('SECRET_KEY')

    if not secret_key:
        error('SECRET_KEY not set. Add this to your .env file.')
        secret_key = create_secret_key()

    return secret_key

def encode_token(subject, days=None) -> str:
    '''
    encode subject as JWT using secret key

    claim name specs:
        https://tools.ietf.org/html/rfc7519#section-4.1
        https://www.iana.org/assignments/jwt/jwt.xhtml
    jwt encode api doc: https://python-jose.readthedocs.io/en/latest/jwt/api.html#jose.jwt.encode
    '''

    payload = {
        'iat': datetime.datetime.utcnow(),
        'sub': subject,
    }

    if days is not None:
        payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(days=days, seconds=0)

    return encode(
        payload,
        os.environ.get('SECRET_KEY'),
        algorithm='HS256',
    )

def decode_token(subject) -> str:
    '''
    decode JWT subject using secret key

    jwt decode api: https://python-jose.readthedocs.io/en/latest/jwt/api.html#jose.jwt.decode
    '''

    decoded_payload = decode(
        subject,
        os.environ.get('SECRET_KEY'),
        algorithms=['HS256'],
    )

    return decoded_payload.get('sub')

def generate_secret_key() -> str:
    new_key = create_secret_key()
    set_key(enumerate_env(), 'SECRET_KEY', new_key)
    return new_key

def encrypt_password(password) -> str:
    return encode_token(password, days=365)

def encrypt_authentication_token() -> str:
    return encode_token(token_urlsafe(8), days=30)

def create_user_token() -> str:
    return token_urlsafe(8)
