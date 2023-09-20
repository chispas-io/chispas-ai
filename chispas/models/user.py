from flask import flash
from flask_login import UserMixin
from jwt import ExpiredSignatureError, InvalidTokenError

from ..utils.database import get_db_connection
from ..utils.sessions import decode_token

# https://flask-login.readthedocs.io/en/latest/_modules/flask_login/mixins/#UserMixin
class User(UserMixin):
    @classmethod
    def query(cls, username):
        conn = get_db_connection()
        c = conn.cursor()

        user = c.execute('SELECT * FROM users WHERE username = :username', { 'username': username }).fetchone()

        conn.close()

        if user is None:
            return None

        return cls(user[1], user[2], user[3])

    @classmethod
    def valid_login_request(cls, app, request):
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
            else:
                flash('Bad login', 'error')
                return False
        except ExpiredSignatureError:
            flash('Expired token', 'error')
            return False
        except InvalidTokenError:
            flash('Invalid token', 'error')
            return False

    def __init__(self, username, encrypted_password, native_language):
        self.id = username
        self.username = username
        self.encrypted_password = encrypted_password
        self.native_language = native_language

    def save(self):
        conn = get_db_connection()
        c = conn.cursor()

        c.execute('INSERT INTO users (username, encrypted_password, native_language) VALUES (?, ?, ?)', (self.username, self.encrypted_password, self.native_language))

        conn.commit()
        conn.close()
