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
    path = input("image or URL (press enter to stop): ")
    if not path:
        break
    images.append(path)
 

for path in images:
    if path.startswith("http"):
        data = requests.get(path).content
    else:
        with open(path, "rb") as f:
            data = f.read()
    contents.append(types.Part.from_bytes(data=data, mime_type="image/jpeg"))
 
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["make up a creative and fantastical story that links these pictures together"]
)
 
print(response.text)
