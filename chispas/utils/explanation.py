from .open_ai import get_response


def generate_detailed_explanations(
    unknown_words, themes, learning_language="spanish", known_language="english"
):
    # Create a prompt for ChatGPT that asks for explanations and examples for each unknown word

    prompt = f"""
      I am a language learner with {known_language} as my native language, and I'm currently learning {learning_language}. 
      I've identified the following words and themes as challenging:

      Words: {', '.join(unknown_words)}
      Themes: {', '.join(themes)}

      Could you provide structured explanations and examples for each word in a format that's easy to understand? 
      For each word, please:

      1. Give its definition in both {known_language} and {learning_language}.
      2. Provide an example sentence in both {known_language} and {learning_language}.
      3. If it is a verb, provide its conjugation in the present tense.

      Here is the list of words: {', '.join(unknown_words)}
    """

    # Call ChatGPT to generate the explanations
    return get_response(prompt, max_tokens=500)
