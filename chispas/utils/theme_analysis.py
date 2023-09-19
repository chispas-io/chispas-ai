from .open_ai import get_response


def analyze_themes_with_chatgpt(
    unknown_words, learning_language="spanish", known_language="english"
):
    # Check if the list of unknown words is empty
    if not unknown_words:
        return "No unknown words found. You're doing great!"

    # Convert the list of unknown words into a string, separated by commas
    unknown_words_str = ", ".join(unknown_words)

    # Prepare the prompt for ChatGPT
    prompt = f"""
      I am a native {known_language} speaker who is learning {learning_language}.

      I have identified the following {learning_language} words as being difficult for me to understand: {unknown_words_str} 

      Analyze the that list of {learning_language} words and identify common themes
      from a linguistic perspective. Some exmamples include, but are not limited to:
      - common tenses
      - common subject matter
      - common parts of speech
      - common prefixes or suffixes
      - common roots
      - common conjugations

      This list is meant to eventually give some ideas for where I can focus my learning.
      Write the themese in {known_language} in a clear and simple bulleted format with short descriptions. 
      If no reasonable theme can be found then say "no theme found".
    """
    # Interact with ChatGPT to get its analysis
    return get_response(prompt)
