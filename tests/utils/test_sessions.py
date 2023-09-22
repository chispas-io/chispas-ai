import pytest
from chispas.utils.sessions import (
    create_secret_key,
    decode_token,
    encode_token,
)

def test_create_secret_key():
    assert 86 == len(create_secret_key())

@pytest.mark.usefixtures('env')
def test_encoding_and_decoding_tokens():
    encoded_token = encode_token('kittycat')
    decoded_payload = decode_token(encoded_token)
    assert decoded_payload == 'kittycat'
