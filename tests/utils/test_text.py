from chispas.utils.text import display_random_text_block, split_text_segment

def test_display_random_text_block():
    output = display_random_text_block("./tests/fixtures/es_input_text.txt")
    assert isinstance(output, str)

def test_split_text_segment():
    input_txt = '''
        "¡Cha-chau!", "'Su cuerpo", "pa' mí", "¿Qué",
        "pa' mí", "P, viejo", "todos,"
        '''

    assert split_text_segment(input_txt) == [
        "Cha-chau", "Su cuerpo", "pa' mí", "Qué",
        "pa' mí", "P, viejo", "todos"
    ]
