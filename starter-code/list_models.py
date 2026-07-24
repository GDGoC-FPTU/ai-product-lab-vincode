#vincode - Ngô Đình Khánh - khanhngodinh7a@gmail.com
from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

for model in client.models.list():
    print(model.name)