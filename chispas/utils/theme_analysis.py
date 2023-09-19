from .open_ai import get_response

def analyze_themes_with_chatgpt(unknown_words):
    # Convert the list of unknown words into a string, separated by commas
    unknown_words_str = ', '.join(unknown_words)
    learning_language = "spanish"

    # Prepare the prompt for ChatGPT
    prompt = f"Analyze the following list of unkown {learning_language} words and identify common themes from a linguistic perspective. This list is meant to eventually give some ideas for where one can focus their learning so that they can improve at {learning_language}: {unknown_words_str}."

    # Interact with ChatGPT to get its analysis
    return get_response(prompt)
