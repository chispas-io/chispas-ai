from flask import jsonify
from chispas.utils.api import jinx_jsonify

def test_jinx_jsonify(app):
    with app.test_request_context():
        assert jinx_jsonify({ 'foot': 'bart', 'errors': [ 'foo', 'bar' ] }).json == jsonify({ 'data': { 'foot': 'bart' }, 'errors': [ 'foo', 'bar' ] }).json
