from dotenv import load_dotenv
from google import genai
import os
from google.genai import types
import requests

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

images = []
while True:
    path = input("at least two images or URLs (press enter to stop): ")
    if not path:
        break
    images.append(path)
 
content = ["make up a fictional story about these two images that links them together"]

for path in images:
    if path.startswith("http"):
        data = requests.get(path).content
    else:
        with open(path, "rb") as f:
            data = f.read()
    content.append(types.Part.from_bytes(data=data, mime_type="image/jpeg"))
 
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=content
)

print(response.text)
