from flask import Blueprint
from ..utils.admin import admin_required

users_api = Blueprint('users', __name__)
