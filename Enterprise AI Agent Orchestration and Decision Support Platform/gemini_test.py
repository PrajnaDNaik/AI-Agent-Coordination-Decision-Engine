from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

print("API Key Loaded:", GOOGLE_API_KEY is not None)
print("First 10 characters:", GOOGLE_API_KEY[:10] if GOOGLE_API_KEY else "None")

client = genai.Client(api_key=GOOGLE_API_KEY)
response = client.models.generate_content(
  model="gemini-flash-latest",
    contents="Hello, test Gemini API"
)
print(response.text)

