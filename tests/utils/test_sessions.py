from chispas.utils.sessions import (
    create_secret_key,
    decode_token,
    encode_token,
)

def test_create_secret_key():
    assert 86 == len(create_secret_key())

def test_encoding_and_decoding_tokens(app):
    encoded_token = encode_token(app, 'kittycat')
    decoded_payload = decode_token(app, encoded_token)
    assert decoded_payload == 'kittycat'
