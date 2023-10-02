from flask import jsonify
from chispas.utils.api import jinx_jsonify

def test_jinx_jsonify(app):
    with app.test_request_context():
        # pylint:disable-next=line-too-long
        assert jinx_jsonify({ 'foot': 'bart', 'errors': [ 'foo', 'bar' ] }).json == jsonify({ 'data': { 'foot': 'bart' }, 'errors': [ 'foo', 'bar' ] }).json
