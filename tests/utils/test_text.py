from chispas.utils.text import display_random_text_block

def test_display_random_text_block():
    output = display_random_text_block('./tests/fixtures/es_input_text.txt')
    assert isinstance(output, str)
