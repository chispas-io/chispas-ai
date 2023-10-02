from flask import Blueprint, render_template, jsonify, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from ..models.user import User

account_api = Blueprint('account', __name__)

# curl -X POST -d "username=charlie&password=is_a_cat" http://localhost:5000/authenticate
@account_api.route('/authenticate', methods=['POST'])
def authenticate():
    user = User.valid_login_request(request)
    if user:
        return jsonify({ 'authentication_token': user.authentication_token })

    return jsonify({ 'error': 'Invalid username or password' }), 401

@account_api.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            flash('You are already logged in!')
            return redirect(url_for('index'))

        return render_template('login.html')

    user = User.valid_login_request(request)
    if user:
        login_user(user, remember=True)
        return redirect(url_for('index'))

    return render_template('login.html')

@account_api.route('/logout', methods=['POST'])
def logout():
    logout_user()
    flash('Logged out')
    return redirect(url_for('login'))
