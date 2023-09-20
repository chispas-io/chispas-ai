import datetime
from jwt import decode, encode
from secrets import token_urlsafe

def create_secret_key():
    """
    secret key for sessions.

    see http://flask.pocoo.org/docs/latest/config/#SECRET_KEY.
    """

    return token_urlsafe(64)

def encode_token(app, subject):
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
        app.config.get('SECRET_KEY'),
        algorithm='HS256',
    )

def decode_token(app, subject):
    '''
    decode JWT subject using secret key

    jwt decode api: https://python-jose.readthedocs.io/en/latest/jwt/api.html#jose.jwt.decode
    '''

    decoded_payload = decode(
        subject,
        app.config.get('SECRET_KEY'),
        algorithms=['HS256'],
    )

    return decoded_payload.get('sub')
