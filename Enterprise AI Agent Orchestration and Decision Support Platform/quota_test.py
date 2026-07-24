from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

try:
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents="Say hello"
    )
    print(response.text)
except Exception as e:
    print(e)