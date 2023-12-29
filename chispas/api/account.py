from flask import (
    Blueprint,
    jsonify,
    request,
)
from flask_login import login_required, login_user, logout_user
from ..models.user import User

account_api = Blueprint('account', __name__)

@account_api.route('/authenticate', methods=['POST'])
def authenticate():
    # payload = request.get_json()
    # username = payload['username']
    # password = payload['password']
    username = request.form['username']
    password = request.form['password']
    user = User.valid_login_request(username, password)
    if user:
        return jsonify({ 'authentication_token': user.authentication_token })

    return jsonify({ 'error': 'Invalid username or password' }), 401

@account_api.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.valid_login_request(username, password)
    if user:
        login_user(user)
        # TODO: pass session to FE here
        return jsonify({ 'authentication_token': user.authentication_token })

    return jsonify({ 'error': 'Invalid username or password' }), 401

@account_api.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    # TODO: support email here

    if User.query(username):
        flash('User already exists', 'error')
        return jsonify(username)

    user = User.create(username, password)
    login_user(user)

    return jsonify({ 'authentication_token': user.authentication_token })

@account_api.route('/logout', methods=['DELETE'])
@login_required
def logout():
    logout_user()
    # TODO

def verify_email():
    pass
