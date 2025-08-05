import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY", "")

def load_gemini_model():
    model_client = OpenAIChatCompletionClient(model="gemini-1.5-flash", api_key=gemini_api_key)
    return model_client