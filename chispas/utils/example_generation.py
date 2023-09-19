import openai

def generate_new_examples(unknown_words, themes, learning_language="spanish", known_language="english"):
    # Create a prompt for ChatGPT to generate new example sentences or paragraphs
    prompt = f"""
        I am a native {known_language} speaker who is learning {learning_language}.

        I was given a block of text and identified the following common themes {themes} in the words that I didn't understand: {unknown_words}. 
        I have now learned more about what these words mean and would like to test my
        knowledge. 
        
        Generate a new example paragraph in {learning_language} so that I can test if I have improved in learning the words. 
        Then add a newline and a translated version of the {learning_language} paragraph in {known_language}:
    """
    for word in unknown_words:
        prompt += f"- {word}\n"

    # Use the GPT-3 API to generate the example
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )

    # Extract and return the generated text as the new example
    new_example = response.choices[0].text.strip()

    return new_example


def generate_progression_text_block(learned_words, themes, difficulty_level):
    # Formulate the prompt for ChatGPT
    learning_language="spanish"
    prompt = f"Generate a new text block in {learning_language} aimed at a {difficulty_level} level language learner. The text should incorporate new words or concepts while only using some, but not all, of the following words that the learner has already understood:\n"
    for word in learned_words:
        prompt += f"- {word}\n"
    prompt += f"The text should be related to the themes of {', '.join(themes)}."

    # Use GPT-3 API to generate the new text block
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )

    # Extract and return the generated text as the new text block
    new_text_block = response.choices[0].text.strip()

    return new_text_block
