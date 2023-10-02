from flask import jsonify

def jinx_jsonify(payload, *args, **kwargs):
    new_payload = { 'data': payload }

    errors = payload.pop('errors', None)
    if errors is not None:
        new_payload['errors'] = errors

    return jsonify(new_payload, *args, **kwargs)
