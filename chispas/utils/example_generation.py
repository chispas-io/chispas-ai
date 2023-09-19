from .open_ai import get_response

def generate_new_examples(unknown_words, themes):
    # Create a prompt for ChatGPT to generate new example sentences or paragraphs
    learning_language = "spanish"
    known_language = "english"
    prompt = f"Generate a new example paragraph in {learning_language} that incorporates the following {learning_language} words, taking into account that I'm trying to get better in the themes of {themes}. Also provide the translated version in {known_language}:\n"
    for word in unknown_words:
        prompt += f"- {word}\n"

    # Use the GPT-3 API to generate the example
    return get_response(prompt, max_tokens=150)

def generate_progression_text_block(learned_words, themes, difficulty_level):
    # Formulate the prompt for ChatGPT
    learning_language="spanish"
    prompt = f"Generate a new text block in {learning_language} aimed at a {difficulty_level} level language learner. The text should incorporate new words or concepts while only using some, but not all, of the following words that the learner has already understood:\n"
    for word in learned_words:
        prompt += f"- {word}\n"
    prompt += f"The text should be related to the themes of {', '.join(themes)}."

    # Use GPT-3 API to generate the new text block
    return get_response(prompt, max_tokens=150)
