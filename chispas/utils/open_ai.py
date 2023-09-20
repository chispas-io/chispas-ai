import os
import openai
from flask import flash
from functools import wraps

DEFAULT_MAX_TOKENS = 100
DEFAULT_ENGINE = 'text-davinci-002'

def initialize_openai() -> None:
    openai.api_key = os.environ.get("OPENAI_API_KEY")

def handle_openai_ratelimit_error(f) -> str:
    '''Decorator to handle RateLimitError from OpenAI API

    Returns:
        AI response text or a fallback string.
    '''
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except openai.error.RateLimitError as e:
            flash('Rate limited', 'error')
            return 'Rate limited'

    return decorated

@handle_openai_ratelimit_error
def get_response(prompt, max_tokens=DEFAULT_MAX_TOKENS) -> str:
    response = openai.Completion.create(
      engine=DEFAULT_ENGINE,
      prompt=prompt,
      max_tokens=max_tokens
    )

    # Extract and return the generated text as the detailed explanations
    return response.choices[0].text.strip()
