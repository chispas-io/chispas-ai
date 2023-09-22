from logging import debug
from flask import flash
from flask_login import UserMixin
from jwt import ExpiredSignatureError, InvalidTokenError

from ..constants.languages import (
    DEFAULT_BASE_LANGUAGE,
    DEFAULT_LEARNING_LANGUAGE,
    DEFAULT_LOCALE,
)
from ..utils.database import get_db_connection
from ..utils.sessions import decode_token, encrypt_password, encrypt_authentication_token

# https://flask-login.readthedocs.io/en/latest/_modules/flask_login/mixins/#UserMixin
class User(UserMixin):
    @staticmethod
    def parse_user_row(user_row):
        return {
           'id': user_row[0],
           'username': user_row[1],
           'encrypted_password': user_row[2],
           'authentication_token': user_row[3],
           'locale': user_row[4],
           'base_language': user_row[5],
           'learning_language': user_row[6]
       }

    @classmethod
    def query(cls, username):
        conn = get_db_connection()
        c = conn.cursor()

        user_row = c.execute('''
        SELECT * FROM users WHERE username = :username
        ''', { 'username': username }).fetchone()

        conn.close()

        if user_row is None:
            return None

        return cls(cls.parse_user_row(user_row))

    @classmethod
    def query_by_token(cls, authentication_token):
        conn = get_db_connection()
        c = conn.cursor()

        user_row = c.execute('''
        SELECT * FROM users WHERE authentication_token = :authentication_token
        ''', { 'authentication_token': authentication_token }).fetchone()

        conn.close()

        if user_row is None:
            return None

        return cls(cls.parse_user_row(user_row))

    @classmethod
    def create(cls, username, password):
        encrypted_password = encrypt_password(password)

        conn = get_db_connection()
        c = conn.cursor()

        authentication_token = encrypt_authentication_token()

        initial_user_info = {
            'username': username,
            'encrypted_password': encrypted_password,
            'authentication_token': authentication_token,
            'locale': DEFAULT_LOCALE,
            'base_language': DEFAULT_BASE_LANGUAGE,
            'learning_language': DEFAULT_LEARNING_LANGUAGE
        }

        c.execute('''
        INSERT INTO users (
            username,
            encrypted_password,
            authentication_token,
            locale,
            base_language,
            learning_language
        ) VALUES (
            :username,
            :encrypted_password,
            :authentication_token,
            :locale,
            :base_language,
            :learning_language
        )
        ''', initial_user_info)

        conn.commit()
        conn.close()

        debug('Created new user', initial_user_info)

        return cls(initial_user_info)

    @classmethod
    def refresh_authentication_token(cls, user_id):
        conn = get_db_connection()
        c = conn.cursor()

        authentication_token = encrypt_authentication_token()

        c.execute('UPDATE users (authentication_token) VALUES (?) WHERE user_id = (?)', (authentication_token, user_id))

        flash('Refreshed authentication token')

        conn.commit()
        conn.close()

    @classmethod
    def valid_login_request(cls, request):
        username = request.form['username']
        password = request.form['password']

        user = cls.query(username)

        if user is None:
            flash('User not found', 'error')
            return False

        try:
            decoded_password = decode_token(user.encrypted_password)
            if password == decoded_password:
                flash(f'Hello, {user.username}!')
                return user

            flash('Bad login', 'error')
            return False
        except ExpiredSignatureError:
            flash('Expired token', 'error')
            return False
        except InvalidTokenError:
            flash('Invalid token', 'error')
            return False

    def __init__(self, user_info):
        self.id = user_info['username']
        self.username = user_info['username']
        self.encrypted_password = user_info['encrypted_password']
        self.authentication_token = user_info['authentication_token']

        self.locale = user_info['locale']
        self.base_language = user_info['base_language']
        self.learning_language = user_info['learning_language']
