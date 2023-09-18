import os
import openai
from dotenv import load_dotenv

def set_api_key(openai):
    #  load_dotenv
    openai.api_key = os.environ.get("OPENAI_API_KEY")
