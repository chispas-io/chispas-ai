from flask import (
    Blueprint,
    flash,
    jsonify,
    request,
)
from flask_login import login_user
from ..models.user import User

users_api = Blueprint('users', __name__)

# curl -X POST -d "username=charlie&password=is_a_cat" http://localhost:5000/api/users/add
@users_api.route('/add', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']

    if User.query(username):
        flash('User already exists', 'error')
        return jsonify(username)

    user = User.create(username, password)

    login_user(user)

    return jsonify(username)
